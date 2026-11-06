#!/usr/bin/env python3
"""Convertit un .docx du miroir en Markdown, sans rien écrire dans le coffre.

    python3 .outils/convertir.py "Raw/Year 2/Probability/Cours 6 - T-Test.docx"

affiche le texte converti, avec la transcription de chaque image : c'est ainsi qu'on
relit un document de cours. maj.py se sert des mêmes fonctions pour préparer le lot
d'une mise à jour. Les noms de dossiers sont dans chemins.py.
"""
import argparse
import csv
import hashlib
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import chemins

ICI = Path(__file__).resolve().parent
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


def charger_transcriptions(coffre):
    """Renvoie {empreinte: texte} pour toutes les transcriptions du coffre."""
    dossier = Path(coffre) / chemins.TRANSCRIPTIONS
    if not dossier.is_dir():
        return {}
    return {f.stem: f.read_text(encoding="utf-8") for f in dossier.glob("*.md")}


def concepts_presents(corps, concepts, chemin):
    """Noms des concepts existants repérés dans un texte, avec les règles des anciens liens
    automatiques : variantes de aliases, limitées par matieres au chemin du document."""
    lien = re.compile(r"\[\[([^\]|\\]+)")
    deja = set(lien.findall(corps))
    noms = {nom for nom, _, _ in concepts}
    return sorted((set(lien.findall(lier(corps, concepts, chemin))) - deja) & noms)


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


def convertir_docx(source, base):
    """Convertit un .docx. Renvoie (corps, images) : images = {nom: octets}, et le corps
    désigne chaque image par ![[<base>/<nom>]]. Lève CalledProcessError si pandoc échoue."""
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pandoc", str(docx_pour_pandoc(source, tmp)), "-f", "docx", "-t", "gfm+tex_math_dollars",
             "--wrap=none", f"--lua-filter={ICI / 'boites.lua'}",
             "--extract-media=m", "-o", "n.md"],
            cwd=tmp, check=True, capture_output=True, text=True,
        )
        corps = (Path(tmp) / "n.md").read_text(encoding="utf-8")
        nouveaux = contenu_dossier(Path(tmp) / "m" / "media")

    def image(m):
        return f"![[{base}/{m[1]}]]"

    corps = re.sub(r"!\[[^\]\n]*\]\(m/media/([^)\s]+)[^)\n]*\)", image, corps)
    corps = re.sub(r'<img src="m/media/([^"]+)"[^>]*>', image, corps)
    return corps.strip() + "\n", nouveaux


def empreintes_images(images, base):
    """{référence de l'image dans le corps: empreinte de son contenu}."""
    return {f"{base}/{nom}": hashlib.sha256(octets).hexdigest() for nom, octets in images.items()}


def lire(source, coffre):
    """Texte d'un .docx avec la transcription de chaque image, comme on le relit."""
    corps, images = convertir_docx(source, "images")
    return inserer_transcriptions(corps, empreintes_images(images, "images"),
                                  charger_transcriptions(coffre))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("document", type=Path, help="fichier .docx à lire")
    parser.add_argument("--coffre", type=Path, default=ICI.parent)
    args = parser.parse_args(argv)
    if args.document.suffix.lower() != ".docx" or not args.document.is_file():
        print(f"erreur : {args.document} n'est pas un .docx existant", file=sys.stderr)
        return 2
    try:
        texte = lire(args.document, args.coffre.resolve())
    except subprocess.CalledProcessError as erreur:
        print(f"erreur : pandoc a échoué : {erreur.stderr.strip()}", file=sys.stderr)
        return 1
    sys.stdout.write(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
