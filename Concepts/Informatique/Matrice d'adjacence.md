---
type: concept
tags:
  - year4
aliases:
  - adjacency matrix
sources:
  - "[[1 - Undirected graph|Chp 1 - Undirected graph]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-08
---

Matrice $M$ d'un graphe à sommets $v_1, \dots, v_n$ : $M_{i,j}$ est le nombre d'arêtes entre $v_i$ et $v_j$. Pour un graphe non orienté, elle est symétrique ; une boucle compte 1 sur la diagonale, deux arêtes parallèles donnent 2.

Pour un graphe simple pondéré : 0 sur la diagonale, $w(v_iv_j)$ si l'arête existe, $+\infty$ sinon.

Le TP Python affiche un graphe à partir de sa matrice ; pour n'afficher que les arêtes existantes, sans doublon ni boucle, il teste `if mat[i][j] == 1 and i < j:`. [[Erreurs du cours#^e-matrice-d-adjacence|✎]]

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe pondéré]], [[Dictionnaire (Python)]].

Résumés : [[1 - Undirected graph]], [[0 - Graph - Python]]
