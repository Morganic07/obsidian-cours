---
type: concept
tags: [year4]
aliases: [plus courts chemins, shortest path, shortest paths, problème du plus court chemin, shortest path problem, PCC, distance dans un graphe]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - bellman ford]]) : dans un [[Graphe pondéré|graphe pondéré]] $G = (S, A, w)$, la longueur du [[Chemin (graphe)|chemin]] $(u_1, \ldots, u_k)$ est $\sum_{i=1}^{k-1} w(u_i, u_{i+1})$, et $\delta(u, v)$ désigne la longueur d'un plus court chemin de $u$ à $v$. S'il n'y a pas de [[Circuit absorbant|circuit de longueur négative]], il existe un plus court chemin **élémentaire**, donc d'au plus $n - 1$ arcs.

**Choix de l'algorithme** (d'après [[4 - bellman ford]]) : poids positifs, [[Algorithme de Dijkstra]] (source unique) ; poids quelconques, [[Algorithme de Bellman-Ford]] (source unique) ou [[Algorithme de Floyd-Warshall]] (tous les couples).

**Compléments (hors du cours)** : par convention $\delta(u, v) = +\infty$ si $v$ est inaccessible depuis $u$, et $-\infty$ si un circuit absorbant se trouve sur un chemin de $u$ à $v$. Un sous-chemin d'un plus court chemin est un plus court chemin ([[Principe d'optimalité de Bellman]]), ce qui permet de résumer tous les plus courts chemins issus d'une source par un [[Arbre des plus courts chemins|arbre des plus courts chemins]]. Sans poids, un [[Parcours en largeur|parcours en largeur]] suffit. Le problème inverse, le [[Problème du plus long chemin|plus long chemin élémentaire]], est NP-difficile.

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : définitions, tableau des cas selon les poids, plus courts chemins élémentaires, application au [[Routage IP|routage]].
- [[4 - dijkstra]] (Graph theory) : problème résolu par Dijkstra, exemple et exercices.

Voir aussi : [[Relâchement d'un arc]], [[Algorithme de Johnson]], [[Algorithme A étoile]].

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
