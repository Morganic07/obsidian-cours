---
type: concept
tags: [year4]
aliases: [bipartite graph, biparti complet]
sources: ["[[chp 1 - Undirected graph (résumé)|Chp 1 - Undirected graph]]", "[[Graph - Python (résumé)|Graph - Python]]"]
maj: 2026-11-06
---

Graphe dont les sommets admettent une partition $(V_1, V_2)$ telle que chaque arête relie $V_1$ à $V_2$. Il est **biparti complet** ($K_{2,2}$, $K_{2,3}$, $K_{3,3}$) si chaque sommet de $V_1$ est adjacent à chaque sommet de $V_2$.

**Caractérisation** : un graphe est biparti si et seulement si tout [[Cycle (graphe)|cycle]] est de longueur paire.

En TP, la fonction `isGraphBipartite` colorie chaque sommet de 0 ou 1 et échoue dès que deux voisins ont la même couleur.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]].

## À vérifier

- La note de l'étudiante (« minimum 2 nœuds » par partie) contredit la définition, qui demande seulement des parties non vides.

Résumés : [[chp 1 - Undirected graph (résumé)]], [[Graph - Python (résumé)]]
