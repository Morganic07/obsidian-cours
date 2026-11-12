#!/usr/bin/env python3
"""Mise à jour depuis Drive : récupérer, comparer, convertir, transcrire, préparer le lot.

    bash .outils/maj.sh                rclone Drive → miroir, puis préparation du lot
    bash .outils/maj.sh --reprendre    refait la préparation sans contacter Drive
    bash .outils/maj.sh --clore        vide le dossier de travail, une fois le wiki à jour

Rien n'est écrit dans le wiki. Tout le travail se fait dans un dossier hors du coffre
(chemins.travail()) :

- avant.json : empreinte de chaque fichier du miroir avant la synchronisation ;
- ancien/ : versions remplacées ou supprimées, gardées par rclone (--backup-dir) ;
- conversions/NN/{nouveau,ancien}/ : texte converti et images de chaque document changé ;
- lot/ : BILAN.md et un fichier par document, lus ensuite par /maj-cours.

Un seul lot à la fois : tant qu'il n'est pas clos, une nouvelle synchronisation est
refusée, sinon les anciennes versions se mélangeraient.
"""
import argparse
import datetime
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

import chemins
import convertir
import transcrire

ICI = Path(__file__).resolve().parent
DRIVE = "gdrive:CY Tech"
SEUIL = 50  # au-delà, la transcription attend l'accord de l'utilisatrice

AVANT = "avant.json"
JOURNAL = "rclone.log"
RCLONE_OK = "rclone.ok"
CHANGEMENTS = "changements.json"
ANCIEN = "ancien"
CONVERSIONS = "conversions"
LOT = "lot"
BILAN = "BILAN.md"
TEXTE = "texte.md"
ERREUR = "erreur.txt"
CONNUS = {AVANT, JOURNAL, RCLONE_OK, CHANGEMENTS, ANCIEN, CONVERSIONS, LOT, chemins.A_FAIRE}

AJOUTE, MODIFIE, DEPLACE, SUPPRIME = "ajouté", "modifié", "déplacé", "supprimé"

# Code source : recopié tel quel dans un bloc de code, langue pour la coloration.
LANGUES_CODE = {".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp"}
FICHIERS_CODE = {"makefile": "makefile"}


def langue_code(source):
    """Langue du bloc de code d'un fichier source, ou None si ce n'en est pas un."""
    return LANGUES_CODE.get(source.suffix.lower()) or FICHIERS_CODE.get(source.name.lower())


class Erreur(Exception):
    """Arrêt propre, avec un message pour l'utilisatrice."""


class LotOuvert(Erreur):
    """Un lot précédent n'est pas clos."""


def nom_valide(nom):
    return bool(nom) and nom not in (".", "..") and "/" not in nom and "\\" not in nom


def verifier_travail(travail, coffre):
    """Refuse un dossier de travail qui engloberait le coffre, le home ou la racine,
    ou qui serait dans le coffre (Obsidian l'indexerait, git pourrait le prendre)."""
    t = Path(travail).expanduser().resolve()
    c = Path(coffre).resolve()
    home = Path.home().resolve()
    if t == Path(t.anchor) or t == home or t in home.parents:
        raise Erreur(f"dossier de travail refusé : {t}")
    if t == c or c in t.parents or t in c.parents:
        raise Erreur(f"dossier de travail refusé, il doit être hors du coffre : {t}")
    return t


def empreinte(fichier):
    h = hashlib.sha256()
    with open(fichier, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def inventaire(miroir):
    """{chemin relatif: empreinte} de chaque fichier du miroir."""
    if not miroir.is_dir():
        return {}
    return {f.relative_to(miroir).as_posix(): empreinte(f)
            for f in sorted(miroir.rglob("*")) if f.is_file()}


def lire_json(fichier):
    return json.loads(fichier.read_text(encoding="utf-8"))


def ecrire_json(fichier, valeur):
    fichier.write_text(json.dumps(valeur, ensure_ascii=False, indent=1), encoding="utf-8")


def comparer(avant, apres):
    """Liste triée des changements : {etat, chemin, origine}. Un fichier supprimé dont le
    contenu réapparaît ailleurs est un déplacement (origine = ancien chemin)."""
    ajoutes = sorted(set(apres) - set(avant))
    supprimes = sorted(set(avant) - set(apres))
    modifies = sorted(c for c in set(avant) & set(apres) if avant[c] != apres[c])
    libres = {}
    for chemin in ajoutes:
        libres.setdefault(apres[chemin], []).append(chemin)
    deplaces = {}
    for chemin in supprimes:
        candidats = libres.get(avant[chemin])
        if candidats:
            deplaces[candidats.pop(0)] = chemin
    changements = [{"etat": DEPLACE if c in deplaces else AJOUTE, "chemin": c,
                    "origine": deplaces.get(c)} for c in ajoutes]
    changements += [{"etat": MODIFIE, "chemin": c, "origine": None} for c in modifies]
    partis = set(deplaces.values())
    changements += [{"etat": SUPPRIME, "chemin": c, "origine": None}
                    for c in supprimes if c not in partis]
    return sorted(changements, key=lambda ch: ch["chemin"])


def lancer_rclone(commande, journal):
    with open(journal, "a", encoding="utf-8") as sortie:
        return subprocess.run(commande, stdout=sortie, stderr=subprocess.STDOUT).returncode


def recuperer(coffre, travail, lancer=lancer_rclone):
    """Synchronise le miroir depuis Drive en gardant les anciennes versions."""
    # rclone sync efface dans la cible tout ce qui n'est pas sur Drive : un nom vide
    # ou un chemin ferait du coffre entier, ou d'un autre dossier, la cible.
    for nom in (chemins.MIROIR, chemins.EXCLUSIONS):
        if not nom_valide(nom):
            raise Erreur(f"nom de dossier invalide dans chemins.py : « {nom} »")
    if (travail / RCLONE_OK).exists():
        raise LotOuvert(
            f"un lot n'est pas clos ({travail / LOT}). L'intégrer avec /maj-cours, "
            "puis bash .outils/maj.sh --clore ; ou le refaire avec --reprendre.")
    travail.mkdir(parents=True, exist_ok=True)
    miroir = coffre / chemins.MIROIR
    # Après un échec de rclone, on garde l'état d'avant la première tentative.
    if not (travail / AVANT).exists():
        ecrire_json(travail / AVANT, inventaire(miroir))
    miroir.mkdir(exist_ok=True)
    # --bind 0.0.0.0 force l'IPv4 : l'IPv6 ne joint pas les serveurs Google sur cette machine.
    commande = ["rclone", "sync", DRIVE, str(miroir),
                "--drive-export-formats", "docx,pptx",
                "--filter-from", str(ICI / chemins.EXCLUSIONS), "--ignore-case",
                "--backup-dir", str(travail / ANCIEN),
                "--bind", "0.0.0.0", "-v"]
    try:
        code = lancer(commande, travail / JOURNAL)
    except OSError as erreur:
        raise Erreur(f"rclone n'a pas pu être lancé : {erreur}") from erreur
    if code != 0:
        raise Erreur(f"rclone a échoué (code {code}), journal : {travail / JOURNAL}. "
                     "Le miroir peut être à moitié synchronisé : relancer maj.sh réessaie.")
    (travail / RCLONE_OK).write_text("", encoding="utf-8")


def convertir_fichier(source, sortie, base):
    """Convertit un document dans sortie/. Renvoie {image: empreinte} des images extraites.
    Un échec est écrit dans sortie/erreur.txt, pour le lot."""
    sortie.mkdir(parents=True, exist_ok=True)
    extension = source.suffix.lower()
    try:
        if extension == ".docx":
            corps, images = convertir.convertir_docx(source, base)
            for nom, octets in images.items():
                (sortie / nom).write_bytes(octets)
            (sortie / TEXTE).write_text(corps, encoding="utf-8")
            return convertir.empreintes_images(images, base)
        if extension == ".pdf":
            resultat = subprocess.run(["pdftotext", "-layout", str(source), "-"], check=True,
                                      capture_output=True, text=True, errors="replace")
            (sortie / TEXTE).write_text(resultat.stdout, encoding="utf-8")
        langue = langue_code(source)
        if langue:
            code = source.read_text(encoding="utf-8", errors="replace")
            (sortie / TEXTE).write_text(bloc(code, langue) + "\n", encoding="utf-8")
    except subprocess.CalledProcessError as erreur:
        (sortie / ERREUR).write_text((erreur.stderr or "").strip() or f"code {erreur.returncode}",
                                     encoding="utf-8")
    except OSError as erreur:
        (sortie / ERREUR).write_text(str(erreur), encoding="utf-8")
    return {}


def preparer(coffre, travail):
    """Calcule les changements, convertit chaque document changé (et son ancienne version)
    et écrit la liste des images à transcrire. Renvoie les changements."""
    if not (travail / RCLONE_OK).exists():
        raise Erreur("aucun lot ouvert : lancer d'abord bash .outils/maj.sh")
    miroir = coffre / chemins.MIROIR
    changements = comparer(lire_json(travail / AVANT), inventaire(miroir))
    for dossier in (CONVERSIONS, LOT):
        shutil.rmtree(travail / dossier, ignore_errors=True)
    ecrire_json(travail / CHANGEMENTS, changements)

    connues = {f.stem for f in (coffre / chemins.TRANSCRIPTIONS).glob("*.md")}
    a_faire = {}
    for n, ch in enumerate(changements, 1):
        dossier = f"{CONVERSIONS}/{n:02d}"
        if ch["etat"] != SUPPRIME:
            images = convertir_fichier(miroir / ch["chemin"], travail / dossier / "nouveau",
                                       f"{dossier}/nouveau")
            for image, e in images.items():
                if e not in connues:
                    a_faire.setdefault(e, (image, ch["chemin"]))
        ancien = travail / ANCIEN / ch["chemin"]
        if ch["etat"] in (MODIFIE, SUPPRIME) and ancien.is_file():
            convertir_fichier(ancien, travail / dossier / "ancien", f"{dossier}/ancien")

    # Un nom de Drive peut contenir une tabulation : elle casserait la ligne.
    lignes = [f"{e}\t{image}\t{re.sub(r'\s', ' ', document)}\n"
              for e, (image, document) in a_faire.items()]
    (travail / chemins.A_FAIRE).write_text("".join(lignes), encoding="utf-8")
    return changements


def nfc(texte):
    """Drive donne parfois des noms en Unicode décomposé (NFD), le wiki les écrit composés :
    on compare toujours sous la forme composée."""
    return unicodedata.normalize("NFC", texte)


def cible(valeur):
    """Cible d'une valeur de sources : celle du lien [[…]], sinon le texte lui-même."""
    lien = re.match(r"\s*\[\[([^\]|\\#]+)", valeur)
    return (lien[1] if lien else valeur).strip().strip("`")


def index_fiches(coffre):
    """[(fiche, cibles de son champ sources)] pour toutes les fiches du wiki : les pages des
    dossiers de matière, hors cartes (« _index », type matiere)."""
    fiches = []
    for fiche in sorted((coffre / chemins.MATIERES).rglob("*.md")):
        champs = convertir.lire_frontmatter(fiche.read_text(encoding="utf-8"))
        if fiche.name == "_index.md" or "matiere" in champs.get("type", []):
            continue
        fiches.append((fiche, [nfc(cible(v)) for v in champs.get("sources", [])]))
    return fiches


def fiches_du_document(fiches, document):
    """Fiches dont sources cite ce document (chemin préfixé par le dossier du miroir)."""
    return [fiche for fiche, cibles in fiches if nfc(document) in cibles]


def fiches_citant_le_dossier(fiches, chemin):
    """Fiches dont sources nomme le dossier du document sans le lier (« PDF du brief, dans
    Raw/Year 3/Projet courts ») : le nom du fichier porte celui d'un tiers."""
    dossier = nfc(f"{chemins.MIROIR}/{Path(chemin).parent.as_posix()}")
    return [fiche for fiche, cibles in fiches
            if any(c.endswith(dossier) and not c.startswith("[[") for c in cibles)]


def dossiers_probables(fiches, coffre, chemin):
    """Dossiers de matière (sous chemins.MATIERES) des fiches tirées du même dossier de Drive, ou d'un parent
    jusqu'au dossier de la matière (Year N/<matière>)."""
    parties = Path(chemin).parent.parts
    for k in range(len(parties), 1, -1):
        prefixe = nfc(f"{chemins.MIROIR}/{'/'.join(parties[:k])}/")
        trouves = {fiche.parent.relative_to(coffre).as_posix()
                   for fiche, cibles in fiches if any(c.startswith(prefixe) for c in cibles)}
        if trouves:
            return sorted(trouves)
    return []


def annee(chemin):
    premier = Path(chemin).parts[0] if Path(chemin).parts else ""
    trouve = re.fullmatch(r"Year\s*(\d+)", premier, re.I)
    return f"year{trouve[1]}" if trouve else "inconnue (le document n'est pas dans un dossier Year N)"


def pages_du_wiki(coffre):
    pages = {}
    for nom in chemins.WIKI:
        racine = coffre / nom
        fichiers = [racine] if racine.is_file() else sorted(racine.rglob("*.md")) if racine.is_dir() else []
        for f in fichiers:
            pages[f.relative_to(coffre).as_posix()] = nfc(f.read_text(encoding="utf-8"))
    return pages


def pages_citant(pages, fiche, document):
    """Pages qui lient la fiche ou citent le document."""
    lien = re.compile(rf"\[\[{re.escape(fiche.stem)}(?:\]\]|\\?\||#)")
    return [p for p, texte in pages.items()
            if (lien.search(texte) or nfc(document) in texte) and not p.endswith(f"/{fiche.name}")]


EMPREINTE_COURTE = 10


def copies_dans_les_fiches(fiches):
    """{empreinte: [noms]} des images copiées pour ces fiches dans images/ de leur matière
    (« <fiche> - … »). Les numéros d'image changent d'un export à l'autre :
    seul le contenu relie une copie à l'image du document."""
    copies = {}
    for fiche in fiches:
        prefixe = fiche.stem + " - "
        dossier = fiche.parent / "images"
        if not dossier.is_dir():
            continue
        for f in sorted(dossier.iterdir()):
            if f.is_file() and f.name.startswith(prefixe):
                copies.setdefault(empreinte(f), []).append(f.name)
    return copies


def par_empreinte(texte, images):
    """Remplace chaque image ![[<chemin>]] par ![[image <début de son empreinte>]]."""
    for reference, e in images.items():
        texte = texte.replace(f"![[{reference}]]", f"![[image {e[:EMPREINTE_COURTE]}]]")
    return texte


def bloc(texte, langue=""):
    """Bloc de code dont la clôture ne peut pas apparaître dans le texte."""
    plus_longue = max((len(m) for m in re.findall(r"`+", texte)), default=0)
    cloture = "`" * max(3, plus_longue + 1)
    return f"{cloture}{langue}\n{texte.rstrip()}\n{cloture}"


def fichier_du_lot(n, ch, coffre, travail, fiches, pages, concepts, textes):
    """Texte du fichier de lot d'un document, et ce qu'en retient le bilan."""
    etat, chemin, origine = ch["etat"], ch["chemin"], ch["origine"]
    document = f"{chemins.MIROIR}/{chemin}"
    dossier = travail / CONVERSIONS / f"{n:02d}"
    base_n, base_a = f"{CONVERSIONS}/{n:02d}/nouveau", f"{CONVERSIONS}/{n:02d}/ancien"

    def lire(sous_dossier, base):
        """(texte brut, texte avec transcriptions, {image: empreinte}, erreur)."""
        d = dossier / sous_dossier
        erreur = (d / ERREUR).read_text(encoding="utf-8") if (d / ERREUR).exists() else None
        if not (d / TEXTE).exists():
            return None, None, {}, erreur
        brut = (d / TEXTE).read_text(encoding="utf-8")
        images = {f"{base}/{f.name}": empreinte(f)
                  for f in sorted(d.iterdir()) if f.name not in (TEXTE, ERREUR)}
        return brut, convertir.inserer_transcriptions(brut, images, textes), images, erreur

    brut_n, texte_n, images_n, erreur_n = lire("nouveau", base_n)
    brut_a, _, images_a, erreur_a = lire("ancien", base_a)
    # Une transcription vide (image sans contenu) compte comme faite.
    sans_transcription = [i for i, e in images_n.items() if e not in textes]

    trouvees = fiches_du_document(fiches, document)
    if origine:
        trouvees += [f for f in fiches_du_document(fiches, f"{chemins.MIROIR}/{origine}")
                     if f not in trouvees]

    lignes = [f"# {Path(chemin).name}", "",
              f"- État : {etat}" + (f" (ancien chemin : `{chemins.MIROIR}/{origine}`)" if origine else ""),
              f"- Document : `{document}`"]
    if etat != SUPPRIME:
        lignes.append(f"- Lien à mettre dans la fiche : `[[{document}|{Path(chemin).name}]]`")
    lignes.append(f"- Année : {annee(chemin)}")
    if trouvees:
        lignes.append("- Fiche existante : " + ", ".join(
            f"`{f.relative_to(coffre).as_posix()}`" for f in trouvees))
    else:
        probables = dossiers_probables(fiches, coffre, chemin)
        lignes.append("- Fiche existante : aucune")
        par_dossier = fiches_citant_le_dossier(fiches, chemin)
        if par_dossier:
            lignes.append("- Fiches qui citent son dossier sans le lier (peut-être la sienne) : " + ", ".join(
                f"`{f.relative_to(coffre).as_posix()}`" for f in par_dossier))
        lignes.append("- Dossier de fiches probable : " + (
            ", ".join(f"`{p}/`" for p in probables) or "aucun (nouvelle matière ?)"))
    if etat in (SUPPRIME, DEPLACE):
        ancien_chemin = f"{chemins.MIROIR}/{origine or chemin}"
        for fiche in trouvees:
            citants = pages_citant(pages, fiche, ancien_chemin)
            lignes.append(f"- Pages qui lient `{fiche.stem}` ou citent l'ancien chemin : "
                          + (", ".join(f"`{p}`" for p in citants) or "aucune"))
        if not trouvees:
            citants = [p for p, texte in pages.items() if nfc(ancien_chemin) in texte]
            lignes.append("- Pages qui citent l'ancien chemin : "
                          + (", ".join(f"`{p}`" for p in citants) or "aucune"))
    if images_n:
        lignes.append(f"- Images : {len(images_n)}, dans `{travail / base_n}/`"
                      + (f" ; {len(sans_transcription)} sans transcription" if sans_transcription else ""))
    texte_concepts = texte_n or brut_a
    if texte_concepts and concepts:
        presents = convertir.concepts_presents(texte_concepts, concepts, chemin)
        lignes.append("- Concepts existants repérés : " + (", ".join(presents) or "aucun"))
    if Path(chemin).suffix.lower() == ".pptx":
        lignes.append(f"- Présentation : pas de conversion, lire `{coffre / chemins.MIROIR / chemin}` directement.")
    for erreur, quoi in ((erreur_n, "la nouvelle version"), (erreur_a, "l'ancienne version")):
        if erreur:
            lignes.append(f"- Échec de conversion de {quoi} : {erreur}")
    if brut_n and "<table" in brut_n:
        lignes.append("- Tableau resté en HTML dans la conversion : le relire dans le document.")

    if etat == MODIFIE:
        lignes += ["", "## Changements", ""]
        if brut_a is None or brut_n is None:
            lignes.append("Comparaison impossible (ancienne version introuvable ou non convertie) : "
                          "relire le document entier.")
        else:
            # Google renumérote les images à chaque export : comparées par leur nom, des
            # images identiques passeraient pour changées. On les désigne par leur contenu.
            diff = list(difflib.unified_diff(
                par_empreinte(brut_a, images_a).splitlines(),
                par_empreinte(brut_n, images_n).splitlines(),
                "ancienne version", "nouvelle version", n=2, lineterm=""))
            if diff:
                lignes += ["Les images y sont désignées par l'empreinte de leur contenu "
                           "(`![[image <empreinte>]]`), car leur numéro change à chaque export.", "",
                           bloc("\n".join(diff), "diff")]
            else:
                lignes.append("Texte identique après conversion.")
            # Une capture remplacée garde souvent son nom : seul son contenu la trahit.
            connues = set(images_a.values())
            changees = [f"{i.rsplit('/', 1)[-1]} (image {e[:EMPREINTE_COURTE]})"
                        for i, e in images_n.items() if e not in connues]
            if changees:
                lignes += ["", "Images nouvelles ou remplacées (contenu absent de l'ancienne "
                           "version) : " + ", ".join(changees)]
            presentes = set(images_n.values())
            parties = sorted({e for e in images_a.values() if e not in presentes})
            if parties:
                copies = copies_dans_les_fiches(trouvees)
                lignes += ["", "Images retirées ou remplacées (contenu absent de la nouvelle "
                           "version), et leur copie dans la fiche : " + ", ".join(
                               f"image {e[:EMPREINTE_COURTE]} → "
                               + (", ".join(f"`{c}`" for c in copies.get(e, [])) or "aucune copie")
                               for e in parties)]
            elif not diff:
                lignes.append("Images identiques : seuls la mise en forme ou les métadonnées "
                              "ont pu changer.")
    elif etat == DEPLACE:
        lignes += ["", "Contenu identique : seul le chemin a changé. Mettre à jour le lien "
                   "de la fiche et les pages qui citent l'ancien chemin."]
    if texte_n is not None and etat != DEPLACE:
        lignes += ["", "## Texte converti", "", texte_n]
    elif etat == SUPPRIME and brut_a is not None:
        lignes += ["", "## Texte de la version supprimée", "", brut_a]
    infos = {"fiches": [f.relative_to(coffre).as_posix() for f in trouvees],
             "sans_transcription": len(sans_transcription),
             "echec": bool(erreur_n or erreur_a)}
    return "\n".join(lignes).rstrip() + "\n", infos


def ecrire_lot(coffre, travail):
    """Écrit lot/BILAN.md et un fichier par document changé. Renvoie le chemin du bilan."""
    changements = lire_json(travail / CHANGEMENTS)
    textes = convertir.charger_transcriptions(coffre)
    dossier_concepts = coffre / chemins.CONCEPTS
    concepts = convertir.charger_concepts(dossier_concepts) if dossier_concepts.is_dir() else []
    fiches = index_fiches(coffre)
    pages = pages_du_wiki(coffre)
    lot = travail / LOT
    shutil.rmtree(lot, ignore_errors=True)
    lot.mkdir(parents=True)

    entrees = []
    for n, ch in enumerate(changements, 1):
        nom = f"{n:02d} - {convertir.nom_sur(Path(ch['chemin']).stem)}.md"
        texte, infos = fichier_du_lot(n, ch, coffre, travail, fiches, pages, concepts, textes)
        (lot / nom).write_text(texte, encoding="utf-8")
        entrees.append((ch, nom, infos))

    compte = {e: sum(ch["etat"] == e for ch, _, _ in entrees) for e in (AJOUTE, MODIFIE, DEPLACE, SUPPRIME)}
    sans = sum(i["sans_transcription"] for _, _, i in entrees)
    lignes = [f"# Lot de mise à jour du {datetime.date.today().isoformat()}", "",
              f"Dossier du lot : `{lot}`", "",
              f"{len(entrees)} documents : " + ", ".join(f"{k}s {v}" for k, v in compte.items()) + ".",
              f"Images sans transcription : {sans}."]
    for etat in (AJOUTE, MODIFIE, DEPLACE, SUPPRIME):
        choisies = [(ch, nom, i) for ch, nom, i in entrees if ch["etat"] == etat]
        if not choisies:
            continue
        lignes += ["", f"## {etat.capitalize()}s", ""]
        for ch, nom, i in choisies:
            fiche = ", ".join(f"`{f}`" for f in i["fiches"]) or "aucune fiche"
            marque = " — échec de conversion" if i["echec"] else ""
            lignes.append(f"- `{nom}` : `{chemins.MIROIR}/{ch['chemin']}` ({fiche}){marque}")
    lignes += ["", "Intégrer avec /maj-cours. Une fois le wiki à jour et validé : "
               "`bash .outils/maj.sh --clore`."]
    (lot / BILAN).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return lot / BILAN, entrees


def clore(travail):
    """Vide le dossier de travail, s'il ne contient que ce que maj.py y met."""
    if not travail.exists():
        return
    inconnus = [f.name for f in travail.iterdir() if f.name not in CONNUS]
    if inconnus:
        raise Erreur(f"{travail} contient des fichiers inattendus ({', '.join(sorted(inconnus))}) : "
                     "rien n'est supprimé.")
    shutil.rmtree(travail)


def main(argv=None, lancer=lancer_rclone, appel=transcrire.appeler_claude):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--reprendre", action="store_true", help="refaire le lot sans contacter Drive")
    action.add_argument("--clore", action="store_true", help="vider le dossier de travail")
    parser.add_argument("--sans-transcrire", action="store_true",
                        help="écrire le lot même s'il reste des images à transcrire")
    parser.add_argument("--seuil", type=int, default=SEUIL,
                        help=f"nombre d'images transcrites sans demander (défaut {SEUIL})")
    parser.add_argument("--coffre", type=Path, default=ICI.parent)
    parser.add_argument("--travail", type=Path, default=None)
    args = parser.parse_args(argv)
    coffre = args.coffre.resolve()
    try:
        travail = verifier_travail(args.travail or chemins.travail(), coffre)
        if args.clore:
            clore(travail)
            print(f"Lot clos, dossier de travail vidé : {travail}")
            return 0
        if not args.reprendre:
            recuperer(coffre, travail, lancer)
        changements = preparer(coffre, travail)
        if not changements:
            clore(travail)
            print("Aucun changement sur Drive.")
            return 0

        restantes = len(transcrire.lire_a_faire(coffre, travail=travail))
        if restantes and not args.sans_transcrire:
            if restantes > args.seuil:
                print(f"{len(changements)} documents changés, {restantes} images à transcrire : "
                      f"au-delà de {args.seuil}, la transcription attend ton accord.\n"
                      "Ensuite : python3 .outils/transcrire.py, puis bash .outils/maj.sh --reprendre "
                      "(ou --reprendre --sans-transcrire pour s'en passer).")
                return 4
            print(f"Transcription de {restantes} images…")
            reussies, echouees, arret = transcrire.transcrire(coffre, travail=travail, appel=appel)
            print(f"{reussies} transcrites, {len(echouees)} échecs" + (f", arrêt : {arret}" if arret else ""))

        bilan, entrees = ecrire_lot(coffre, travail)
    except LotOuvert as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 3
    except Erreur as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 1
    print(bilan.read_text(encoding="utf-8"))
    print(f"Bilan : {bilan}")
    return 1 if any(i["echec"] for _, _, i in entrees) else 0


if __name__ == "__main__":
    sys.exit(main())
