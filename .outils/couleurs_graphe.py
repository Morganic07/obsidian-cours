#!/usr/bin/env python3
"""Change les couleurs des points du graphe Obsidian.

    python3 .outils/couleurs_graphe.py domaine   # une couleur par domaine de concepts
    python3 .outils/couleurs_graphe.py annee     # une couleur par année (tags year1 à year4)
    python3 .outils/couleurs_graphe.py type      # concepts, cartes, résumés, cours, documents
    python3 .outils/couleurs_graphe.py aucune    # pas de couleur
    python3 .outils/couleurs_graphe.py           # liste les jeux disponibles

Fermer le graphe dans Obsidian avant de lancer le script : un graphe ouvert
réenregistre ses propres réglages et efface ceux du script.

Pour changer une couleur, modifier son code dans COULEURS ci-dessous
(format #RRGGBB, voir par exemple https://htmlcolorcodes.com). Pour créer un
jeu, ajouter une entrée à JEUX : une liste de (recherche Obsidian, couleur).
Quand un point correspond à plusieurs recherches, c'est la première de la
liste qui l'emporte.
"""
import json
import sys
from pathlib import Path

COULEURS = {
    "bleu": "#4E79A7",
    "orange": "#F28E2B",
    "rouge": "#E15759",
    "violet": "#B07AA1",
    "vert": "#59A14F",
    "turquoise": "#76B7B2",
    "jaune": "#EDC948",
    "rose": "#FF9DA7",
    "brun": "#9C755F",
    "gris": "#9C9C9C",
    "gris clair": "#ccc9c9",
}

JEUX = {
    "domaine": [
        ('path:"Concepts/Mathématiques"', "bleu"),
        ('path:"Concepts/Informatique"', "orange"),
        ('path:"Concepts/Données et IA"', "rouge"),
        ('path:"Concepts/Design"', "violet"),
        ('path:"Concepts/SHS et philosophie"', "vert"),
        ('path:"Concepts/Écologie et société"', "turquoise"),
        ('file:"(matière)"', "gris clair"),
        ("path:raw", "gris"),
    ],
    "annee": [
        ('file:"(matière)"', "gris clair"),  # avant les années : les cartes en portent aussi
        ("tag:#year1", "vert"),
        ("tag:#year2", "bleu"),
        ("tag:#year3", "orange"),
        ("tag:#year4", "rouge"),
        ("path:raw", "gris"),
    ],
    "type": [
        ("path:Concepts", "bleu"),
        ('file:"(matière)"', "gris clair"),
        ('file:"(résumé)"', "vert"),
        ("path:Cours", "orange"),
        ("path:raw", "gris"),
    ],
    "aucune": [],
}

GRAPHE = Path(__file__).resolve().parent.parent / ".obsidian" / "graph.json"


def groupes(jeu):
    """Traduit un jeu en groupes de couleurs au format d'Obsidian."""
    sortie = []
    for recherche, nom in JEUX[jeu]:
        code = COULEURS.get(nom, nom).lstrip("#")
        if len(code) != 6:
            raise ValueError(f"couleur invalide : {nom}")
        sortie.append({"query": recherche, "color": {"a": 1, "rgb": int(code, 16)}})
    return sortie


def appliquer(jeu, chemin=GRAPHE):
    """Remplace les groupes de couleurs du graphe, sans toucher aux autres réglages."""
    reglages = json.loads(chemin.read_text(encoding="utf-8")) if chemin.exists() else {}
    reglages["colorGroups"] = groupes(jeu)
    chemin.write_text(json.dumps(reglages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(arguments):
    if len(arguments) != 1 or arguments[0] not in JEUX:
        print("Jeux de couleurs disponibles :", ", ".join(JEUX))
        print("Exemple : python3 .outils/couleurs_graphe.py annee")
        return 1
    appliquer(arguments[0])
    print(f"Couleurs « {arguments[0]} » enregistrées. Rouvre le graphe dans Obsidian.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
