---
type: concept
tags: [year4]
aliases: [graph coloring, graph colouring, proper coloring, coloration propre, k-coloration, k-coloring, coloration optimale, optimal coloring, k-coloriable, k-colorable]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition** (d'après [[5 - colorier graph]]) : soit $G = (V, E)$ un [[Graphe non orienté|graphe non orienté]] et $C$ un ensemble de couleurs. Une **coloration** de $G$ est une [[Application (mathématiques)|application]] $c : V \to C$ ; elle est **propre** si deux sommets adjacents ont toujours des couleurs différentes : $\forall (v, v') \in E,\ c(v) \neq c(v')$.

- Une **$k$-coloration** est une coloration qui utilise exactement $k$ couleurs : $\text{card}(c(V)) = k$. $G$ est **$k$-coloriable** s'il admet une $k$-coloration propre.
- Une coloration propre **optimale** est une coloration propre en $\chi(G)$ couleurs, où $\chi(G)$ est le [[Nombre chromatique|nombre chromatique]].

Les sommets d'une même couleur forment un [[Ensemble stable (graphe)|ensemble stable]] : colorier proprement en $k$ couleurs, c'est [[Partition d'un ensemble|partitionner]] les sommets en $k$ stables. Décider si un graphe est 3-coloriable est NP-complet (voir [[Classes P et NP]]) ; on se contente donc souvent d'heuristiques gloutonnes comme l'[[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]] ou l'[[Algorithme DSATUR|algorithme DSATUR]]. Applications : emplois du temps (voir [[Graphe d'incompatibilité]]), [[Allocation de registres|allocation de registres]], fréquences radio, [[Sudoku]], cartes géographiques ([[Théorème des quatre couleurs]]). [[Complément hors du cours|ⓘ]]

## Dans le cours

Chapitre 5 de Graph theory ([[5 - colorier graph]]) : définitions informelle et formelle, $k$-coloration, coloration optimale, algorithme exact en $k^n$ affectations, algorithme de Welsh et Powell, exemple et deux exercices.

Voir aussi : [[Nombre chromatique]], [[Clique (graphe)]], [[Graphe biparti]], [[Graphe planaire]], [[Optimisation combinatoire]].

Résumés : [[5 - colorier graph]]
