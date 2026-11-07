---
type: concept
tags:
  - year4
aliases:
  - bipartite graph
  - biparti complet
sources:
  - "[[1 - Undirected graph|Chp 1 - Undirected graph]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-07
---

Graphe dont les sommets admettent une partition $(V_1, V_2)$, avec $V_1$ et $V_2$ non vides, telle que chaque arête relie $V_1$ à $V_2$. Il est **biparti complet** ($K_{2,2}$, $K_{2,3}$, $K_{3,3}$) s'il est simple et si chaque sommet de $V_1$ est adjacent à chaque sommet de $V_2$.

**Caractérisation** : un graphe est biparti si et seulement si tout [[Cycle (graphe)|cycle]] est de longueur paire.

En TP, la fonction `isGraphBipartite` colorie chaque sommet de 0 ou 1 et échoue dès que deux voisins ont la même couleur.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]].

## Erreurs du cours

- [[1 - Undirected graph|Chp 1 - Undirected graph]] porte la note « attention, les sous partitions V1 et V2 doivent minimum avoir 2 noeuds » ; il faut « V1 et V2 doivent être non vides » (au moins 1 sommet chacune), comme le dit la définition de la diapositive.

Résumés : [[1 - Undirected graph]], [[0 - Graph - Python]]
