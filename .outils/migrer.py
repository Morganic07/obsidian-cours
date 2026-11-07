#!/usr/bin/env python3
"""Migration ponctuelle du wiki, avant la suppression des notes converties (chemins.NOTES).

- Un lien vers une note de NOTES devient un lien vers sa fiche (résumé), avec le même
  texte affiché. Dans la fiche elle-même, il devient un lien vers le document du miroir.
- Une mention `.raw/<fichier>` (entre guillemets ou accents graves) devient un lien
  [[<nouveau miroir>/<fichier>|<nom du fichier>]] ; une autre mention (dossier, texte
  courant) change seulement de préfixe. Le journal (_suivi/log.md) garde ses mentions,
  qui sont de l'historique ; seuls ses liens sont migrés.
- Un lien déjà cassé vers « X » est redirigé vers « X (résumé) » si cette fiche existe
  (notes retirées volontairement du miroir).

    python3 .outils/migrer.py --nouveau-miroir Raw --correspondances fichier.tsv --essai
    python3 .outils/migrer.py --nouveau-miroir Raw --correspondances fichier.tsv
    python3 .outils/migrer.py --nouveau-miroir Raw --mesurer

Le fichier de correspondances, hors du dépôt, donne pour les fiches dont `sources` ne
cite pas la note : « nom de la fiche <tab> chemin de la note sans .md ».
À retirer du dépôt une fois la migration faite.
"""
import argparse
import collections
import re
import sys
import unicodedata
from pathlib import Path

import chemins
import convertir

ICI = Path(__file__).resolve().parent
LIEN = re.compile(r"(!?)\[\[([^\[\]\n]+?)\]\]")
CODE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.S | re.M)
INTERDITS_DANS_UN_LIEN = re.compile(r"[\[\]#^|]")


def nfc(texte):
    return unicodedata.normalize("NFC", texte)


def separer(interieur):
    """[[cible#ancre|texte]] → (cible, ancre, séparateur, texte)."""
    m = re.match(r"(.*?)(\\\||\|)(.*)\Z", interieur, re.S)
    cible, sep, texte = (m[1], m[2], m[3]) if m else (interieur, "", None)
    ancre = ""
    if "#" in cible:
        cible, ancre = cible.split("#", 1)
    return cible.strip(), ancre, sep, texte


class Coffre:
    """Index des fichiers du coffre, résolus comme Obsidian : par chemin ou par nom,
    sans tenir compte de la casse ni de la forme Unicode. Le miroir caché est indexé
    sous son nouveau nom, pour mesurer avant le renommage."""

    def __init__(self, racine, nouveau_miroir):
        self.par_chemin, self.par_nom = {}, collections.defaultdict(list)
        for f in sorted(racine.rglob("*")):
            relatif = f.relative_to(racine)
            if not f.is_file() or relatif.parts[0] in (".obsidian", ".trash", ".git"):
                continue
            if relatif.parts[0] == chemins.MIROIR:
                relatif = Path(nouveau_miroir, *relatif.parts[1:])
            elif any(p.startswith(".") for p in relatif.parts):
                continue
            nom = relatif.as_posix()
            cle = nom[:-3] if nom.endswith(".md") else nom
            self.par_chemin[nfc(cle).casefold()] = nom
            self.par_nom[nfc(Path(cle).name).casefold()].append(nom)

    def resoudre(self, cible):
        """Liste des fichiers que désigne la cible d'un lien (vide : cassé)."""
        cle = nfc(cible[:-3] if cible.lower().endswith(".md") else cible).casefold()
        if cle in self.par_chemin:
            return [self.par_chemin[cle]]
        if "/" in cle:
            return [n for c, n in self.par_chemin.items() if c.endswith("/" + cle)]
        return list(self.par_nom.get(cle, []))


def pages_du_wiki(racine):
    pages = []
    for nom in chemins.WIKI:
        r = racine / nom
        pages += [r] if r.is_file() else sorted(r.rglob("*.md")) if r.is_dir() else []
    return pages


def documents_des_notes(racine):
    """{note de NOTES (chemin sans .md): document du miroir (chemin relatif)}, d'après
    le champ source des notes, écrit avec des espaces simplifiées et sans guillemets."""
    miroir = racine / chemins.MIROIR
    lisibles = {}
    for f in miroir.rglob("*"):
        if f.is_file():
            relatif = f.relative_to(miroir).as_posix()
            lisibles[nfc(re.sub(r"\s+", " ", relatif).replace('"', ""))] = relatif
    documents = {}
    for note in (racine / chemins.NOTES).rglob("*.md"):
        source = convertir.lire_frontmatter(note.read_text(encoding="utf-8")).get("source", [""])[0]
        documents[note.relative_to(racine).as_posix()[:-3]] = lisibles.get(nfc(source))
    return documents


def fiches_des_notes(racine, coffre, correspondances):
    """{note de NOTES: fiche (chemin sans .md)}, d'après sources et les correspondances."""
    fiches, erreurs = {}, []
    for fiche in sorted((racine / chemins.MATIERES).rglob("*(résumé).md")):
        cle_fiche = fiche.relative_to(racine).as_posix()[:-3]
        for valeur in convertir.lire_frontmatter(fiche.read_text(encoding="utf-8")).get("sources", []):
            lien = re.match(r"\s*\[\[([^\]]+)\]\]", valeur)
            if not lien:
                continue
            for cible in coffre.resoudre(separer(lien[1])[0]):
                if cible.startswith(f"{chemins.NOTES}/"):
                    note = cible[:-3]
                    if fiches.setdefault(note, cle_fiche) != cle_fiche:
                        erreurs.append(f"{note} : deux fiches, {fiches[note]} et {cle_fiche}")
    for nom_fiche, note in correspondances.items():
        trouvees = [f for f in coffre.resoudre(nom_fiche) if f.startswith(f"{chemins.MATIERES}/")]
        if len(trouvees) != 1 or nfc(note).casefold() not in coffre.par_chemin:
            erreurs.append(f"correspondance introuvable : {nom_fiche} → {note}")
            continue
        if fiches.setdefault(note, trouvees[0][:-3]) != trouvees[0][:-3]:
            erreurs.append(f"{note} : correspondance contraire à sources ({fiches[note]})")
    return fiches, erreurs


def hors_code(texte, fonction, en_ligne=False):
    """Applique fonction au texte hors des blocs de code délimités, et hors du code en
    ligne si en_ligne (un [[ … ]] de bash cité entre accents graves n'est pas un lien)."""
    motif = re.compile(CODE.pattern + r"|`[^`\n]+`", CODE.flags) if en_ligne else CODE
    sortie, position = [], 0
    for bloc in motif.finditer(texte):
        sortie += [fonction(texte[position:bloc.start()]), bloc[0]]
        position = bloc.end()
    sortie.append(fonction(texte[position:]))
    return "".join(sortie)


def dans_un_tableau(texte, position):
    debut = texte.rfind("\n", 0, position) + 1
    return bool(re.match(r"[ \t]*(?:>[ \t]*)*\|", texte[debut:]))


class Migration:
    def __init__(self, racine, nouveau_miroir, correspondances):
        self.racine = racine
        self.nouveau = nouveau_miroir
        self.coffre = Coffre(racine, nouveau_miroir)
        self.documents = documents_des_notes(racine)
        self.fiches, self.erreurs = fiches_des_notes(racine, self.coffre, correspondances)
        self.correspondances = correspondances
        self.compte = collections.Counter()
        self.exemples = collections.defaultdict(list)

    def noter(self, categorie, page, detail):
        self.compte[categorie] += 1
        if len(self.exemples[categorie]) < 400:
            self.exemples[categorie].append(f"{page} : {detail}")

    def lien_document(self, document, texte, sep):
        """Lien vers un document du miroir, ou None si son nom ne peut pas être lié."""
        if INTERDITS_DANS_UN_LIEN.search(document):
            return None
        return f"[[{self.nouveau}/{document}{sep}{texte}]]"

    # Liens vers les notes converties

    def migrer_liens(self, texte, page):
        cle_page = page[:-3]

        def remplacer(m):
            embarque, interieur = m[1], m[2]
            cible, ancre, sep, affiche = separer(interieur)
            if not cible:  # [[#titre]] : lien dans la page même
                return m[0]
            trouves = self.coffre.resoudre(cible)
            sep = sep or ("\\|" if dans_un_tableau(m.string, m.start()) else "|")
            affiche = affiche if affiche is not None else (f"{cible}#{ancre}" if ancre else cible)
            if not trouves:
                nom = cible.rsplit("/", 1)[-1]
                fiche = [f for f in self.coffre.resoudre(f"{nom} (résumé)") if f.startswith(f"{chemins.MATIERES}/")]
                if len(fiche) == 1 and not embarque:
                    if fiche[0][:-3] == cle_page:
                        self.noter("lien cassé vers sa propre note, devenu texte", page, m[0])
                        return affiche
                    self.noter("lien cassé redirigé vers la fiche", page, m[0])
                    return f"[[{Path(fiche[0]).stem}{sep}{affiche}]]"
                self.noter("lien cassé, laissé", page, m[0])
                return m[0]
            notes = [t for t in trouves if t.startswith(f"{chemins.NOTES}/") and t.endswith(".md")]
            if not notes:
                if len(trouves) > 1:
                    self.noter("lien ambigu, laissé", page, m[0])
                return m[0]
            if len(trouves) > 1:
                self.noter("lien ambigu vers une note, laissé", page, f"{m[0]} → {trouves}")
                return m[0]
            note = notes[0][:-3]
            if embarque:
                self.noter("note intégrée, laissée", page, m[0])
                return m[0]
            if ancre:
                self.noter("ancre retirée", page, m[0])
            fiche = self.fiches.get(note)
            if fiche is None:
                self.noter("note sans fiche, laissée", page, m[0])
                return m[0]
            if fiche == cle_page:
                document = self.documents.get(note)
                lien = self.lien_document(document, affiche, sep) if document else None
                if lien is None:
                    self.noter("lien de la fiche vers sa note, devenu texte", page, m[0])
                    return affiche
                self.noter("lien de la fiche vers sa note → document", page, f"{m[0]} → {lien}")
                return lien
            self.noter("lien vers une note → fiche", page, f"{m[0]} → {Path(fiche).name}")
            return f"[[{Path(fiche).name}{sep}{affiche}]]"

        return hors_code(texte, lambda t: LIEN.sub(remplacer, t), en_ligne=True)

    # Mentions du miroir caché

    def migrer_mentions(self, texte, page):
        ancien = re.escape(chemins.MIROIR)

        def document(chemin):
            trouve = self.coffre.resoudre(f"{self.nouveau}/{chemin}")
            return trouve[0][len(self.nouveau) + 1:] if len(trouve) == 1 and "." in Path(chemin).name else None

        def delimitee(m):
            ouvrant, chemin = m[1], m[2]
            doc = document(chemin)
            sep = "\\|" if dans_un_tableau(m.string, m.start()) else "|"
            lien = self.lien_document(doc, Path(doc).name, sep) if doc else None
            if lien is None:
                self.noter("mention gardée en texte, préfixe changé" if not doc else
                           "nom impossible à lier, préfixe changé", page, m[0])
                return f"{ouvrant}{self.nouveau}/{chemin}{ouvrant}"
            self.noter("mention → lien", page, f"{m[0]} → {lien}")
            if ouvrant == '"':
                return f'"{lien}"'
            return lien

        def traiter(t):
            t = re.sub(rf'(["`]){ancien}/([^"`\n]+)\1', delimitee, t)

            def libre(m):
                self.noter("mention gardée en texte, préfixe changé", page, m[0])
                return f"{m[1]}{self.nouveau}/"
            return re.sub(rf"(^|[^\w/.]){ancien}/", libre, t)

        return hors_code(texte, traiter)

    def migrer_sources_textuelles(self, texte, page):
        """Fiches des correspondances : leur sources en texte devient le lien du document."""
        nom = Path(page).name[:-3]
        if nom not in self.correspondances:
            return texte
        document = self.documents.get(self.correspondances[nom])
        lien = self.lien_document(document, nom.removesuffix(" (résumé)"), "|") if document else None
        if lien is None:
            self.noter("sources textuelle sans document", page, nom)
            return texte
        nouveau, n = re.subn(r'^sources: \["[^"\[\]]*"\]$', f'sources: ["{lien}"]', texte, count=1, flags=re.M)
        self.noter("sources textuelle → document" if n else "sources textuelle introuvable", page, lien)
        return nouveau

    def migrer_page(self, f):
        page = f.relative_to(self.racine).as_posix()
        avant = f.read_text(encoding="utf-8")
        texte = self.migrer_sources_textuelles(avant, page)
        texte = self.migrer_liens(texte, page)
        if page != f"{chemins.SUIVI}/log.md":
            texte = self.migrer_mentions(texte, page)
        return avant, texte

    def lancer(self, ecrire):
        changees = 0
        for f in pages_du_wiki(self.racine):
            avant, apres = self.migrer_page(f)
            if apres != avant:
                changees += 1
                if ecrire:
                    f.write_text(apres, encoding="utf-8")
        return changees


def mesurer(racine, nouveau_miroir):
    """Liens du wiki par dossier de destination, plus les cassés et les ambigus."""
    coffre = Coffre(racine, nouveau_miroir)
    compte, casses, ambigus = collections.Counter(), [], []
    for f in pages_du_wiki(racine):
        page = f.relative_to(racine).as_posix()
        texte = f.read_text(encoding="utf-8")

        def compter(t):
            for m in LIEN.finditer(t):
                cible = separer(m[2])[0]
                if not cible:
                    continue
                trouves = coffre.resoudre(cible)
                if not trouves:
                    casses.append(f"{page} : {m[0]}")
                elif len(trouves) > 1:
                    ambigus.append(f"{page} : {m[0]} → {trouves}")
                else:
                    compte[("intégration → " if m[1] else "lien → ") + trouves[0].split("/")[0]] += 1
            return t

        hors_code(texte, compter, en_ligne=True)
    compte["cassés"], compte["ambigus"] = len(casses), len(ambigus)
    mentions = sum(len(re.findall(rf"(?<![\w/]){re.escape(chemins.MIROIR)}/", f.read_text(encoding="utf-8")))
                   for f in pages_du_wiki(racine))
    compte[f"mentions {chemins.MIROIR}/"] = mentions
    return compte, casses, ambigus


def lire_correspondances(fichier):
    if not fichier:
        return {}
    lignes = Path(fichier).read_text(encoding="utf-8").splitlines()
    return dict(l.split("\t", 1) for l in lignes if l.strip())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--coffre", type=Path, default=ICI.parent)
    parser.add_argument("--nouveau-miroir", required=True, help="nom du miroir après renommage")
    parser.add_argument("--correspondances", type=Path)
    parser.add_argument("--essai", action="store_true", help="compter sans rien écrire")
    parser.add_argument("--mesurer", action="store_true", help="seulement mesurer les liens")
    parser.add_argument("--detail", action="store_true", help="lister les exemples de chaque catégorie")
    args = parser.parse_args(argv)
    racine = args.coffre.resolve()
    if args.mesurer:
        compte, casses, ambigus = mesurer(racine, args.nouveau_miroir)
        for cle in sorted(compte):
            print(f"{cle} : {compte[cle]}")
        for ligne in casses + ambigus if args.detail else []:
            print(f"  {ligne}")
        return 0
    migration = Migration(racine, args.nouveau_miroir, lire_correspondances(args.correspondances))
    if migration.erreurs:
        for e in migration.erreurs:
            print(f"erreur : {e}", file=sys.stderr)
        return 1
    changees = migration.lancer(ecrire=not args.essai)
    print(f"{'Pages à modifier' if args.essai else 'Pages modifiées'} : {changees}")
    for categorie in sorted(migration.compte):
        print(f"{categorie} : {migration.compte[categorie]}")
        if args.detail:
            for exemple in migration.exemples[categorie]:
                print(f"  {exemple}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
