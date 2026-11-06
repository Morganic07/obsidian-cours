#!/usr/bin/env python3
"""Noms des dossiers du coffre, en un seul endroit.

Pour renommer un de ces dossiers : le renommer sur le disque, puis changer la
ligne correspondante ici. Les scripts, leurs tests et maj.sh lisent ce fichier.

    python3 .outils/chemins.py MIROIR   # affiche une valeur (utilisé par maj.sh)
"""
import sys

MIROIR = ".raw"  # copie brute de Drive ; caché, Obsidian ignore les dossiers en « . »
NOTES = "Cours"  # notes converties depuis le miroir, suivent l'arborescence de Drive
CONCEPTS = "Concepts"  # pages de concepts, dont les aliases créent les liens automatiques
TRANSCRIPTIONS = ".transcriptions"  # texte lu dans les images, une page par empreinte
A_FAIRE = "A_FAIRE.tsv"  # images restant à transcrire, dans TRANSCRIPTIONS
EXCLUSIONS = "exclusions.local"  # filtres rclone, dans .outils

NOMS = ("MIROIR", "NOTES", "CONCEPTS", "TRANSCRIPTIONS", "A_FAIRE", "EXCLUSIONS")


def main(arguments):
    if len(arguments) != 1 or arguments[0] not in NOMS:
        print("usage : chemins.py " + "|".join(NOMS), file=sys.stderr)
        return 2
    print(globals()[arguments[0]])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
