---
type: concept
tags: [year4]
aliases: [plus long chemin, longest path problem, longest path, plus long chemin élémentaire]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : problème qui consiste à trouver, dans un graphe pondéré, un [[Chemin (graphe)|chemin élémentaire]] (sans répétition de sommet) de longueur maximale entre deux sommets. Contrairement au [[Plus court chemin|plus court chemin]], il est NP-difficile dans le cas général (voir [[Classes P et NP]]) : il contient le problème du chemin hamiltonien, qui passe par tous les sommets. On ne peut pas le ramener à un plus court chemin en changeant le signe des poids, car le graphe obtenu contient en général des [[Circuit absorbant|circuits absorbants]], que l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] ne sait pas traiter. Sur un graphe orienté sans circuit, il se résout au contraire en temps linéaire à l'aide d'un [[Tri topologique|tri topologique]] : c'est le calcul du chemin critique en ordonnancement de projets (méthode PERT).

## Dans le cours

Pas nommé : cité en complément dans [[4 - bellman ford]] (Graph theory), pour contraster avec les plus courts chemins.

Résumés : [[4 - bellman ford]]
