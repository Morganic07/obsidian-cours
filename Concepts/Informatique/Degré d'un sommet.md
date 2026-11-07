---
type: concept
tags: [year4]
aliases: [degree of a vertex]
matieres: [graph theory]
sources: ["[[1 - Undirected graph|Chp 1 - Undirected graph]]", "[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-07
---

Nombre d'arêtes incidentes à un sommet. Le chapitre 1 l'utilise pour les graphes $k$-réguliers ([[Graphe régulier]]) et complets ([[Graphe complet]], chaque sommet de degré $n - 1$) ; le TP Python le calcule avec une fonction `degre`. Le chapitre 1 emploie $d(v)$ sans le définir, et énonce : si $G$ est $k$-régulier, alors $k \cdot \text{card}(V) = 2 \cdot \text{card}(E)$. Cette relation suppose qu'une boucle compte deux fois dans le degré de son sommet (convention usuelle, complément, hors du cours).

**Graphe orienté** (chapitre 4) : degré entrant $d^-(v)$ (nombre d'arcs entrants) et degré sortant $d^+(v)$ (nombre d'arcs sortants), avec $\sum_v d^+(v) = \sum_v d^-(v) = |A|$, chaque arc comptant une fois dans chaque somme.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe régulier]], [[Graphe complet]], [[Graphe orienté]].

Résumés : [[1 - Undirected graph]], [[4 - oriented graphs]], [[0 - Graph - Python]]
