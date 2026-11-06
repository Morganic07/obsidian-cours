#!/usr/bin/env python3
"""Noms des dossiers du coffre, en un seul endroit.

Pour renommer un de ces dossiers : le renommer sur le disque, puis changer la
ligne correspondante ici. Les scripts et leurs tests lisent ce fichier.

    python3 .outils/chemins.py MIROIR   # affiche une valeur
"""
import os
import sys
from pathlib import Path

MIROIR = ".raw"  # copie brute de Drive, suit son arborescence
NOTES = "Cours"  # ancien dossier des notes converties : lu seulement par la migration des liens
CONCEPTS = "Concepts"  # pages de concepts ; aliases et matieres servent à les repérer dans un document
MATIERES = "Matières"  # cartes de matière et fiches (résumés)
SYNTHESES = "Synthèses"
SUIVI = "_suivi"
ACCUEIL = "Accueil.md"
TRANSCRIPTIONS = ".transcriptions"  # texte lu dans les images, une page par empreinte
A_FAIRE = "A_FAIRE.tsv"  # images restant à transcrire, dans le dossier de travail
EXCLUSIONS = "exclusions.local"  # filtres rclone, dans .outils

NOMS = ("MIROIR", "NOTES", "CONCEPTS", "MATIERES", "SYNTHESES", "SUIVI", "ACCUEIL",
        "TRANSCRIPTIONS", "A_FAIRE", "EXCLUSIONS")

# Pages du wiki, celles dont on cherche les liens.
WIKI = (CONCEPTS, MATIERES, SYNTHESES, SUIVI, ACCUEIL)


def travail():
    """Dossier de travail de la mise à jour, hors du coffre : il ne doit jamais être indexé
    par Obsidian ni versionné. MAJ_COURS_TRAVAIL le remplace (tests, essais)."""
    autre = os.environ.get("MAJ_COURS_TRAVAIL")
    return Path(autre) if autre else Path.home() / ".cache" / "obsidian-cours" / "maj"


def main(arguments):
    if len(arguments) != 1 or arguments[0] not in NOMS:
        print("usage : chemins.py " + "|".join(NOMS), file=sys.stderr)
        return 2
    print(globals()[arguments[0]])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
