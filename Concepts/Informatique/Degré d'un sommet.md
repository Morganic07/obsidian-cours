---
type: concept
tags: [year4]
aliases: [degree of a vertex]
matieres: [graph theory]
sources: ["[[Chp 1 - Undirected graph]]", "[[chp4 - oriented graphs]]"]
maj: 2026-11-06
---

Nombre d'arêtes incidentes à un sommet. Le chapitre 1 l'utilise pour les graphes $k$-réguliers ([[Graphe régulier]]) et complets ([[Graphe complet]], chaque sommet de degré $n - 1$) ; le TP Python le calcule avec une fonction `degre`.

**Graphe orienté** (chapitre 4) : degré entrant $d^-(v)$ (nombre d'arcs entrants) et degré sortant $d^+(v)$ (nombre d'arcs sortants), avec $\sum_v d^+(v) = \sum_v d^-(v) = |A|$, chaque arc comptant une fois dans chaque somme.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe régulier]], [[Graphe complet]], [[Graphe orienté]].

## À vérifier

- Le degré d'un sommet non orienté n'est pas défini au chapitre 1 ; la relation $k\,\text{card}(V) = 2\,\text{card}(E)$ suppose qu'une boucle compte deux fois (relevé du résumé).

Résumés : [[Chp 1 - Undirected graph (résumé)]], [[chp4 - oriented graphs (résumé)]], [[Graph - Python (résumé)]]
