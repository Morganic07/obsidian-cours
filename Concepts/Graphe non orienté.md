---
type: concept
aliases: [graphes non orientés, undirected graph, graphe simple, multigraphe, graphe complet, graphe connexe, graphe biparti, graphe régulier, matrice d'adjacence, isomorphisme de graphes, composante connexe, chaîne élémentaire, graphe pondéré, graphe planaire]
matieres: [graph theory]
sources: ["[[Chp 1 - Undirected graph]]"]
maj: 2026-11-05
---

Un graphe non orienté $G = (V, E, \gamma)$ a des sommets $V$ (fini, non vide), des arêtes $E$, et $\gamma$ donne les extrémités de chaque arête. Il peut avoir des boucles et des arêtes multiples ; il est **simple** sans ni l'un ni l'autre.

- **Matrice d'adjacence** : $M_{i,j}$ = nombre d'arêtes entre $v_i$ et $v_j$, symétrique.
- **Chaîne** : suite alternée sommets-arêtes ; simple (arêtes distinctes), élémentaire (sommets distincts) ; **cycle** : chaîne simple fermée.
- **Complet** : simple, toute paire adjacente ; $\binom{n}{2}$ arêtes.
- **Connexe** : deux sommets sont reliés par une chaîne ; composantes connexes disjointes.
- **Biparti** : partition $(V_1, V_2)$ avec chaque arête entre les deux ; biparti si et seulement si tout cycle est pair.
- **$k$-régulier** : tous les degrés valent $k$, donc $k\,|V| = 2|E|$.
- **Pondéré** : $w : E \to \mathbb{R}$.

Liens : [[Graphe orienté]], [[Arbre couvrant minimal]]

Résumés : [[Chp 1 - Undirected graph (résumé)]], [[Graph - Python (résumé)]]
