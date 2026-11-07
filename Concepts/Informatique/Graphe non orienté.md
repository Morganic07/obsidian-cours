---
type: concept
tags: [year2, year4]
aliases: [graphes non orientés, undirected graph]
matieres: [graph theory, Algo]
sources: ["[[Chp 1 - Undirected graph (résumé)|Chp 1 - Undirected graph]]", "[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-06
---

Un graphe non orienté $G = (V, E, \gamma)$ a des sommets $V$ (fini, non vide), des arêtes $E$ (fini), et $\gamma$ associe à chaque arête ses extrémités ([[Sommet et arête]]). Il peut avoir des boucles et des arêtes multiples (multigraphe) ; il est **simple** sans ni l'un ni l'autre ([[Graphe simple]]).

- **[[Matrice d'adjacence]]** : $M_{i,j}$ = nombre d'arêtes entre $v_i$ et $v_j$, symétrique.
- **[[Chaîne (graphe)|Chaîne]]** : suite alternée sommets-arêtes ; simple (arêtes distinctes), élémentaire (sommets distincts) ; **[[Cycle (graphe)|cycle]]** : chaîne simple fermée.
- **[[Graphe complet|Complet]]** : simple, toute paire adjacente ; $\binom{n}{2}$ arêtes.
- **[[Graphe connexe|Connexe]]** : deux sommets sont reliés par une chaîne ; composantes connexes disjointes.
- **[[Graphe biparti|Biparti]]** : partition $(V_1, V_2)$ avec chaque arête entre les deux ; biparti si et seulement si tout cycle est pair.
- **[[Graphe régulier|$k$-régulier]]** : tous les [[Degré d'un sommet|degrés]] valent $k$, donc $k\,|V| = 2|E|$.
- **[[Graphe pondéré|Pondéré]]** : $w : E \to \mathbb{R}$.
- Voir aussi [[Sous-graphe]], [[Isomorphisme de graphes]], [[Graphe planaire]].

**En Algo (2e année)** : un graphe non orienté a pour liens des arêtes, représentées par une paire de sommets, et les boucles y sont interdites. Le degré d'un sommet est le nombre d'arêtes incidentes ; un sommet de degré 0 est isolé. Le chapitre 3 donne les propriétés équivalentes d'un [[Arbre (théorie des graphes)|arbre]] : graphe connexe sans cycle, ou connexe avec $n - 1$ arêtes, ou sans cycle avec $n - 1$ arêtes ([[Chapitre3-Arbres (résumé)]]). Les deux cours diffèrent donc sur les boucles : autorisées en graph theory, interdites en Algo.

Liens : [[Graphe orienté]], [[Arbre couvrant minimal]], [[Arbre binaire]]

## À vérifier

- [[Chp 1 - Undirected graph (résumé)]] relève $\gamma : E \to V^2$ (couple ordonné) pour un graphe non orienté, alors qu'il faudrait des paires non ordonnées.

Résumés : [[Chp 1 - Undirected graph (résumé)]], [[Graph - Python (résumé)]]
