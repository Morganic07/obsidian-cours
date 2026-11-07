---
type: concept
tags: [year4]
aliases: [adjacency matrix]
sources: ["[[Chp 1 - Undirected graph (résumé)|Chp 1 - Undirected graph]]", "[[Graph - Python (résumé)|Graph - Python]]"]
maj: 2026-11-06
---

Matrice $M$ d'un graphe à sommets $v_1, \dots, v_n$ : $M_{i,j}$ est le nombre d'arêtes entre $v_i$ et $v_j$. Pour un graphe non orienté, elle est symétrique ; une boucle compte 1 sur la diagonale, deux arêtes parallèles donnent 2.

Pour un graphe simple pondéré : 0 sur la diagonale, $w(v_iv_j)$ si l'arête existe, $+\infty$ sinon.

Le TP Python affiche un graphe à partir de sa matrice.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe pondéré]], [[Dictionnaire (Python)]].

## À vérifier

- Dans le TP, `if (mat[i] < mat[j])` compare deux lignes de la matrice et non des indices (relevé du résumé).

Résumés : [[Chp 1 - Undirected graph (résumé)]], [[Graph - Python (résumé)]]
