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
maj: 2026-11-08
---

Graphe dont les sommets admettent une partition $(V_1, V_2)$, avec $V_1$ et $V_2$ non vides (un sommet de chaque côté suffit), telle que chaque arête relie $V_1$ à $V_2$. [[Erreurs du cours#^e-graphe-biparti|✎]] Il est **biparti complet** ($K_{2,2}$, $K_{2,3}$, $K_{3,3}$) s'il est simple et si chaque sommet de $V_1$ est adjacent à chaque sommet de $V_2$.

**Caractérisation** : un graphe est biparti si et seulement si tout [[Cycle (graphe)|cycle]] est de longueur paire.

Sens direct (complément, hors du cours) : le long d'un cycle, chaque arête fait changer de côté ($V_1 \to V_2$ ou $V_2 \to V_1$) ; pour revenir au sommet de départ, il faut donc un nombre pair d'arêtes. Un triangle (cycle de longueur 3) n'est jamais biparti.

Le biparti complet $K_{p,q}$ ($|V_1| = p$, $|V_2| = q$) a $p \times q$ arêtes (complément, hors du cours).

Usage (complément, hors du cours) : les graphes bipartis modélisent les **problèmes d'affectation** (personnes et tâches, étudiants et stages), où l'on cherche un **couplage**, c'est-à-dire un ensemble d'arêtes sans extrémité commune.

En TP, la fonction `isGraphBipartite` colorie chaque sommet de 0 ou 1 et échoue dès que deux voisins ont la même couleur.

Ce test est une **2-coloration par [[Parcours en largeur|parcours en largeur]]** (complément, hors du cours) : on colorie le départ, chaque voisin reçoit la couleur opposée, et un conflit révèle un cycle impair. Avec une file `collections.deque`, il coûte $O(n + m)$ pour $n$ sommets et $m$ arêtes.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]].

Résumés : [[1 - Undirected graph]], [[0 - Graph - Python]]
