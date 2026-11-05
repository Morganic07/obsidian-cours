---
type: concept
aliases: [arbre couvrant, arbres couvrants, minimum spanning tree, spanning tree, algorithme de Kruskal, Kruskal, forêt]
matieres: [graph theory]
sources: ["[[Chp2 - tree]]", "[[Graph - Python]]"]
maj: 2026-11-05
---

Un **arbre** est un graphe non orienté connexe sans cycle ; une **forêt** est sans cycle, chaque composante est un arbre. Un **arbre couvrant** d'un graphe contient tous ses sommets et un sous-ensemble de ses arêtes, avec la structure d'un arbre. Tout graphe connexe fini en a un.

Pour un graphe pondéré simple et connexe, un **arbre couvrant minimal** a une valeur (somme des poids des arêtes) minimale. L'énumération de tous les arbres est exponentielle. **Kruskal**, algorithme [[Algorithme glouton]] : trier les arêtes par poids, retenir chaque arête qui ne ferme pas de cycle, jusqu'à $|V| - 1$ arêtes. Complexité annoncée : $O(|E|\log|V|)$. Le TP Python détecte les cycles avec une structure de racines (union par rang).

Exemple du cours : sept villes, arbre de 6 arêtes ; avec Kruskal on retrouve le même arbre de valeur 2818 (complément).

Liens : [[Graphe non orienté]], [[Complexité algorithmique]]

Résumés : [[Chp2 - tree (résumé)]], [[Graph - Python (résumé)]]
