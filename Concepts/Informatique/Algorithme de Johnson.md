---
type: concept
tags: [year4]
aliases: [Johnson's algorithm, algorithme de Johnson (plus courts chemins)]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : algorithme de calcul des [[Plus court chemin|plus courts chemins]] entre tous les couples de sommets d'un [[Graphe pondéré|graphe pondéré]] orienté peu dense, poids négatifs admis (publié par Donald B. Johnson en 1977). On ajoute un sommet relié à tous les autres par des arcs de poids 0 et on lance l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] depuis lui, ce qui donne un potentiel $h(v)$ (et détecte un éventuel [[Circuit absorbant|circuit absorbant]]). On repondère alors chaque arc par $w'(u, v) = w(u, v) + h(u) - h(v) \ge 0$, ce qui ne change pas les plus courts chemins, et on lance l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] depuis chaque sommet. Complexité $O(nm \log n)$ avec un tas binaire, meilleure que les $O(n^3)$ de l'[[Algorithme de Floyd-Warshall|algorithme de Floyd-Warshall]] quand $m$ est petit devant $n^2$.

## Dans le cours

Pas nommé : cité en complément dans [[4 - bellman ford]] et [[4 - dijkstra]], comme moyen de combiner les deux algorithmes du cours.

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
