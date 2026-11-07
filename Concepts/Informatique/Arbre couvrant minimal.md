---
type: concept
tags:
  - year4
aliases:
  - arbre couvrant
  - arbres couvrants
  - minimum spanning tree
  - spanning tree
matieres:
  - graph theory
sources:
  - "[[2 - tree|Chp2 - tree]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-06
---

Un [[Arbre (théorie des graphes)|arbre]] est un graphe non orienté connexe sans cycle ; une [[Forêt (graphe)|forêt]] est sans cycle, chaque composante est un arbre. Un **arbre couvrant** d'un graphe contient tous ses sommets et un sous-ensemble de ses arêtes, avec la structure d'un arbre. Tout graphe connexe fini en a un.

Pour un [[Graphe pondéré|graphe pondéré]] simple et connexe, un **arbre couvrant minimal** a une valeur $w(T)$ (somme des poids des arêtes) minimale. L'énumération de tous les arbres est exponentielle. L'[[Algorithme de Kruskal]], [[Algorithme glouton|glouton]] : trier les arêtes par poids, retenir chaque arête qui ne ferme pas de cycle, jusqu'à $|V| - 1$ arêtes. Complexité annoncée : $O(|E|\log|V|)$. Le TP Python détecte les cycles avec une structure de racines (union par rang).

Exemple du cours : sept villes, arbre de 6 arêtes ; avec Kruskal on retrouve le même arbre de valeur 2818 (complément).

Notion parente : [[Arbre (théorie des graphes)]]. Liens : [[Graphe non orienté]], [[Complexité algorithmique]], [[Pont (graphe)]]

Résumés : [[2 - tree]], [[0 - Graph - Python]]
