#!/usr/bin/env python3
"""Convertit le miroir Drive en notes Obsidian et y insère les liens vers les concepts.

Les notes sont entièrement recalculées à partir du miroir, des concepts et des
transcriptions : relancer le script redonne le même résultat. Les noms de ces
dossiers sont dans chemins.py.
"""
import argparse
import csv
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import chemins

ICI = Path(__file__).resolve().parent
MIROIR_DEFAUT = ICI.parent / chemins.MIROIR
URI_IMAGE = "http://schemas.openxmlformats.org/drawingml/2006/picture"
GROUPE_DESSIN = re.compile(r"<mc:AlternateContent\b.*?</mc:AlternateContent>", re.S)

PROTEGE = (
    r"```.*?```|~~~.*?~~~"  # blocs de code
    r"|\$\$.*?\$\$|(?<!\\)\$[^$\n]+?\$"  # formules
    r"|`[^`\n]+`"  # code en ligne
    r"|!?\[\[[^\]\n]*\]\]"  # liens et images Obsidian
    r"|!?\[[^\]\n]*\]\([^)\n]*\)"  # liens et images Markdown
    r"|<[^>\n]+>"  # balises HTML
    r"|https?://[^\s)]+"  # URL
    r"|^[ \t]*(?:>[ \t]*)*#{1,6}[ \t][^\n]*$"  # titres
    r"|\[![^\]\n]*\][^\n]*$"  # en-têtes de callout
)
LIGNE_DE_TABLEAU = re.compile(r"[ \t]*(?:>[ \t]*)*\|")
PREFIXE_CITATION = re.compile(r"[ \t]*(?:>[ \t]?)*")
IMAGE_OBSIDIAN = re.compile(r"!\[\[([^\]\n]+)\]\]")


def nom_sur(nom):
    """Retire les caractères qu'Obsidian refuse ou comprend mal dans un nom de note."""
    une_ligne = re.sub(r"\s+", " ", nom)  # tabulations et sauts de ligne venus de Drive
    propre = re.sub(r" ?[:#^\[\]|\\]+ ?", " - ", une_ligne).strip(" -")
    return propre or "sans titre"


def lire_frontmatter(texte):
    """Lit l'en-tête YAML limité dont on a besoin : chaque valeur devient une liste."""
    bloc = re.match(r"---\n(.*?)\n---(?:\n|$)", texte, re.S)
    if not bloc:
        return {}
    champs, cle = {}, None
    for ligne in bloc[1].splitlines():
        element = re.match(r"\s*-\s+(.*)", ligne)
        paire = re.match(r"([\w-]+):\s*(.*)", ligne)
        if element and cle:
            champs.setdefault(cle, []).append(element[1].strip().strip("\"'"))
        elif paire:
            cle = paire[1]
            # Entre guillemets, un # fait partie de la valeur : ce n'est pas un commentaire.
            citee = re.match(r"""(["'])(.*)\1""", paire[2].strip())
            if citee:
                champs[cle] = [citee[2]]
                continue
            valeur = re.sub(r"\s+#.*$", "", paire[2]).strip()
            if valeur.startswith("[") and valeur.endswith("]"):
                lu = next(csv.reader([valeur[1:-1]], skipinitialspace=True), [])
                champs[cle] = [v.strip() for v in lu if v.strip()]
            elif valeur:
                champs[cle] = [valeur.strip("\"'")]
    return champs


def charger_concepts(dossier):
    """Renvoie [(nom, variantes, matières)] trié, pour un résultat reproductible."""
    concepts = []
    for note in sorted(Path(dossier).rglob("*.md")):
        champs = lire_frontmatter(note.read_text(encoding="utf-8"))
        variantes = [note.stem, *champs.get("aliases", [])]
        concepts.append((note.stem, variantes, champs.get("matieres", [])))
    return concepts


def lier(corps, concepts, chemin):
    """Lie la première occurrence de chaque concept dans le corps d'une note."""
    dossiers = {p.casefold() for p in Path(chemin).parts}
    index = {}
    for nom, variantes, matieres in concepts:
        if matieres and not dossiers & {m.casefold() for m in matieres}:
            continue
        for variante in variantes:
            cle = variante.casefold()
            if index.setdefault(cle, nom) != nom:
                print(f"attention : « {variante} » désigne {index[cle]} et {nom}", file=sys.stderr)
    if not index:
        return corps

    termes = "|".join(re.escape(v) for v in sorted(index, key=len, reverse=True))
    motif = re.compile(
        rf"(?P<protege>{PROTEGE})|(?<![\w-])(?P<terme>{termes})(?![\w-])",
        re.S | re.M | re.I,
    )
    deja_lies = set()

    def remplacer(m):
        terme = m["terme"]
        if terme is None:
            cible = re.match(r"\[\[([^\]|\\]+)", m[0])
            if cible:
                deja_lies.add(cible[1])
            return m[0]
        nom = index.get(terme.casefold())
        if nom is None or nom in deja_lies:
            return m[0]
        deja_lies.add(nom)
        if terme == nom:
            return f"[[{nom}]]"
        debut = m.string.rfind("\n", 0, m.start()) + 1
        barre = r"\|" if LIGNE_DE_TABLEAU.match(m.string, debut) else "|"
        return f"[[{nom}{barre}{terme}]]"

    return motif.sub(remplacer, corps)


def inserer_transcriptions(corps, empreintes, textes):
    """Ajoute une transcription repliable sous chaque image qui en a une."""

    def bloc(prefixe, texte):
        vide = prefixe.rstrip()
        lignes = [f"{prefixe}> [!info]- Transcription (automatique, l'image fait foi)"]
        lignes += [f"{prefixe}> {l}".rstrip() for l in texte.strip().splitlines()]
        return [vide, *lignes, vide]

    sortie, en_attente = [], []
    for ligne in corps.split("\n"):
        prefixe = PREFIXE_CITATION.match(ligne)[0]
        dans_tableau = ligne[len(prefixe):].startswith("|")
        if en_attente and not dans_tableau:
            sortie += en_attente
            en_attente = []
        sortie.append(ligne)
        for image in IMAGE_OBSIDIAN.findall(ligne):
            texte = textes.get(empreintes.get(image, ""), "")
            if texte.strip():
                # Un callout ne peut pas vivre dans une cellule : il suit le tableau.
                ajout = bloc(prefixe, texte)
                if dans_tableau:
                    en_attente += ajout
                else:
                    sortie += ajout
    return "\n".join(sortie + en_attente)


def contenu_dossier(dossier):
    if not dossier.is_dir():
        return {}
    return {f.name: f.read_bytes() for f in dossier.iterdir() if f.is_file()}


def chemin_note(coffre, relatif):
    """Emplacement attendu de la note d'un document du miroir."""
    dossiers = [nom_sur(p) for p in relatif.parent.parts]
    return coffre.joinpath(chemins.NOTES, *dossiers, f"{nom_sur(relatif.stem)}.md")


def source_lisible(relatif):
    """Chemin de la source tel qu'il est écrit dans l'en-tête de la note."""
    return re.sub(r"\s+", " ", relatif.as_posix()).replace('"', "")


def notes_deplacees(coffre, miroir):
    """Trouve les notes générées hors de leur place alors que leur source existe encore."""
    attendues = {}
    for source in miroir.rglob("*.docx"):
        relatif = source.relative_to(miroir)
        attendues[source_lisible(relatif)] = chemin_note(coffre, relatif)
    deplacees = []
    for note in sorted((coffre / chemins.NOTES).rglob("*.md")):
        champs = lire_frontmatter(note.read_text(encoding="utf-8"))
        if champs.get("genere") != ["true"]:
            continue
        attendue = attendues.get(next(iter(champs.get("source", [])), None))
        if attendue is not None and attendue != note:
            deplacees.append((note, attendue))
    return deplacees


def runs_du_groupe(choix):
    """Traduit un dessin Google en images simples, suivies de son texte."""
    runs = []
    for numero, pic in enumerate(re.findall(r"<pic:pic\b.*?</pic:pic>", choix, re.S)):
        taille = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic)
        cx, cy = taille.groups() if taille else ("5000000", "3000000")
        runs.append(
            f'<w:r><w:drawing><wp:inline distB="0" distT="0" distL="0" distR="0">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{900000 + numero}" name=""/>'
            f'<a:graphic><a:graphicData uri="{URI_IMAGE}">{pic}</a:graphicData></a:graphic>'
            f"</wp:inline></w:drawing></w:r>"
        )

    morceaux = []
    for boite in re.findall(r"<w:txbxContent>(.*?)</w:txbxContent>", choix, re.S):
        for paragraphe in re.findall(r"<w:p\b.*?</w:p>", boite, re.S):
            ecrits = [
                r for r in re.findall(r"<w:r\b.*?</w:r>", paragraphe, re.S)
                if re.search(r"<w:t\b[^>]*>\s*[^<\s]", r)
            ]
            if ecrits:
                morceaux.append("".join(ecrits))
    if morceaux:
        runs.append("<w:r><w:br/></w:r>")
        separateur = '<w:r><w:t xml:space="preserve"> ; </w:t></w:r>'
        runs.append('<w:r><w:t xml:space="preserve">Texte du dessin : </w:t></w:r>')
        runs.append(separateur.join(morceaux))
    return "".join(runs)


def aplatir_groupes(xml):
    """Remplace les dessins groupés, que pandoc ignore, par leurs images et leur texte.

    L'image de repli de ces groupes est une image vide : seul le contenu du groupe compte.
    """
    sortie, position = [], 0
    for groupe in GROUPE_DESSIN.finditer(xml):
        debut = max(xml.rfind("<w:r>", position, groupe.start()),
                    xml.rfind("<w:r ", position, groupe.start()))
        fin = xml.find("</w:r>", groupe.end())
        if debut < 0 or fin < 0:
            continue
        choix = groupe[0].split("<mc:Fallback", 1)[0]
        sortie += [xml[position:debut], runs_du_groupe(choix)]
        position = fin + len("</w:r>")
    sortie.append(xml[position:])
    return "".join(sortie)


def docx_pour_pandoc(source, dossier):
    """Renvoie le chemin à donner à pandoc : une copie corrigée si le docx a des groupes."""
    try:
        entree = zipfile.ZipFile(source)
    except zipfile.BadZipFile:
        return source.resolve()  # pandoc signalera le fichier illisible
    with entree:
        xml = entree.read("word/document.xml").decode("utf-8")
        if not GROUPE_DESSIN.search(xml):
            return source.resolve()
        copie = Path(dossier) / "source.docx"
        with zipfile.ZipFile(copie, "w", zipfile.ZIP_DEFLATED) as sortie:
            for element in entree.infolist():
                if element.filename == "word/document.xml":
                    sortie.writestr(element, aplatir_groupes(xml).encode("utf-8"))
                else:
                    sortie.writestr(element, entree.read(element.filename))
    return copie


def convertir_doc(source, relatif, coffre, concepts, textes):
    """Produit la note d'un .docx. Renvoie son chemin et ses empreintes d'images."""
    note = chemin_note(coffre, relatif)
    medias = note.parent / "medias" / note.stem
    base = medias.relative_to(coffre).as_posix()

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pandoc", str(docx_pour_pandoc(source, tmp)), "-f", "docx", "-t", "gfm+tex_math_dollars",
             "--wrap=none", f"--lua-filter={ICI / 'boites.lua'}",
             "--extract-media=m", "-o", "n.md"],
            cwd=tmp, check=True, capture_output=True, text=True,
        )
        corps = (Path(tmp) / "n.md").read_text(encoding="utf-8")
        nouveaux = contenu_dossier(Path(tmp) / "m" / "media")

    corps = re.sub(r"!\[[^\]\n]*\]\(m/media/([^)\s]+)[^)\n]*\)", rf"![[{base}/\1]]", corps)
    corps = re.sub(r'<img src="m/media/([^"]+)"[^>]*>', rf"![[{base}/\1]]", corps)
    empreintes = {f"{base}/{n}": hashlib.sha256(o).hexdigest() for n, o in nouveaux.items()}

    corps = inserer_transcriptions(corps, empreintes, textes)
    corps = lier(corps, concepts, relatif)
    entete = f'---\ngenere: true\nsource: "{source_lisible(relatif)}"\n---\n\n'
    texte = entete + corps.strip() + "\n"

    note.parent.mkdir(parents=True, exist_ok=True)
    etat = None
    if not note.exists():
        etat = "nouvelle"
    elif note.read_text(encoding="utf-8") != texte:
        etat = "modifiée"
    if etat:
        note.write_text(texte, encoding="utf-8")
    if contenu_dossier(medias) != nouveaux:
        shutil.rmtree(medias, ignore_errors=True)
        if nouveaux:
            medias.mkdir(parents=True)
            for nom, octets in nouveaux.items():
                (medias / nom).write_bytes(octets)
    return note, empreintes, etat


def retirer_dossiers_vides(dossier, limite):
    while dossier != limite and dossier.is_dir() and not any(dossier.iterdir()):
        dossier.rmdir()
        dossier = dossier.parent


def retirer_orphelines(coffre, gardees):
    """Supprime les notes générées dont la source a disparu, jamais les autres."""
    cours = coffre / chemins.NOTES
    retirees = []
    for note in sorted(cours.rglob("*.md")):
        if note in gardees:
            continue
        if lire_frontmatter(note.read_text(encoding="utf-8")).get("genere") == ["true"]:
            note.unlink()
            shutil.rmtree(note.parent / "medias" / note.stem, ignore_errors=True)
            retirer_dossiers_vides(note.parent / "medias", cours)
            retirer_dossiers_vides(note.parent, cours)
            retirees.append(note)
    return retirees


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--miroir", type=Path, default=MIROIR_DEFAUT)
    parser.add_argument("--coffre", type=Path, default=ICI.parent)
    parser.add_argument("--matiere", help="ne traiter que ce sous-dossier du miroir")
    args = parser.parse_args(argv)
    coffre = args.coffre.resolve()

    racine = args.miroir / args.matiere if args.matiere else args.miroir
    sources = sorted(racine.rglob("*.docx")) if racine.is_dir() else []
    if not sources:
        print(f"erreur : aucun .docx dans {racine}, rien n'est modifié", file=sys.stderr)
        return 2

    deplacees = notes_deplacees(coffre, args.miroir)
    if deplacees:
        print("erreur : des notes générées ont été déplacées dans le coffre, rien n'est modifié.\n"
              f"{chemins.NOTES}/ suit l'arborescence de Drive : "
              "range-les sur Drive, ou remets-les en place.",
              file=sys.stderr)
        for note, attendue in deplacees:
            print(f"  {note.relative_to(coffre)}  (attendue : {attendue.relative_to(coffre)})",
                  file=sys.stderr)
        return 3

    dossier_tr = coffre / chemins.TRANSCRIPTIONS
    dossier_tr.mkdir(parents=True, exist_ok=True)
    textes = {f.stem: f.read_text(encoding="utf-8") for f in dossier_tr.glob("*.md")}
    dossier_concepts = coffre / chemins.CONCEPTS
    concepts = charger_concepts(dossier_concepts) if dossier_concepts.is_dir() else []

    notes, a_transcrire, echecs, changees = {}, {}, [], []
    reussies = 0
    for source in sources:
        relatif = source.relative_to(args.miroir)
        cible = chemin_note(coffre, relatif)
        if cible in notes:
            echecs.append(f"{relatif} : même note que {notes[cible]}")
            continue
        notes[cible] = relatif
        try:
            note, empreintes, etat = convertir_doc(source, relatif, coffre, concepts, textes)
            if etat:
                changees.append((etat, note))
        except subprocess.CalledProcessError as erreur:
            echecs.append(f"{relatif} : {erreur.stderr.strip()}")
            continue
        reussies += 1
        for image, empreinte in empreintes.items():
            if empreinte not in textes:
                a_transcrire.setdefault(empreinte, image)

    (dossier_tr / chemins.A_FAIRE).write_text(
        "".join(f"{e}\t{i}\n" for e, i in a_transcrire.items()), encoding="utf-8")

    retirees = [] if args.matiere else retirer_orphelines(coffre, set(notes))
    html = [n for n in notes if n.exists() and "<table" in n.read_text(encoding="utf-8")]

    print(f"{reussies} notes à jour, {len(retirees)} retirées, "
          f"{len(a_transcrire)} images à transcrire, {len(concepts)} concepts")
    for etat, note in changees:
        print(f"{etat} : {note.relative_to(coffre)}")
    for note in retirees:
        print(f"retirée : {note.relative_to(coffre)}")
    for note in html:
        print(f"tableau resté en HTML (liens inactifs dedans) : {note.relative_to(coffre)}")
    for echec in echecs:
        print(f"échec : {echec}", file=sys.stderr)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
