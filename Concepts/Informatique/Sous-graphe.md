---
type: concept
tags: [year2, year4]
aliases: [sous-graphes, subgraph, spanning subgraph, graphe partiel]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-12
---

**Algo** : « on dit qu'un graphe $G_0=(S_0,A_0)$ est un sous-graphe de $G=(S,A)$ si $S_0$ est inclus dans $S$ et si $A_0$ est inclus dans $A$ » (diapositive 15 de [[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]). L'exemple retire de $G$ le sommet $c$ et ses deux arêtes : $G'$ garde $a$, $b$, $d$, $e$ et les arêtes $a$–$b$, $a$–$e$, $b$–$e$, $b$–$d$.

**graph theory** : au chapitre 2, un sous-graphe de $G = (V, E, \gamma)$ est un graphe $G' = (V, E')$ avec $E' \subseteq E$ (mêmes sommets). Il sert à définir l'arbre couvrant et, au chapitre 1, la composante connexe (sous-graphe connexe maximal).

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe orienté]], [[Arbre couvrant minimal]], [[Graphe connexe]], [[Graphe planaire]].

**graph theory, suppléments** : selon [[4 - dijkstra]], l'algorithme de Dijkstra construit progressivement un sous-graphe, l'arborescence des plus courts chemins depuis le sommet d'origine.

Résumés : [[3 - Arbres]], [[2 - tree]], [[1 - Undirected graph]], [[4 - dijkstra]]
