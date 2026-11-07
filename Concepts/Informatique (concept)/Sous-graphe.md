---
type: concept
tags: [year2, year4]
aliases: [sous-graphes, subgraph, spanning subgraph, graphe partiel]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[2 - tree (résumé)|Chp2 - tree]]"]
maj: 2026-11-06
---

**Algo** : un graphe $G_0=(S_0,A_0)$ est un sous-graphe de $G=(S,A)$ si ses sommets et ses arcs sont pris dans ceux de $G$ (définition coupée dans l'extraction du PDF).

**graph theory** : au chapitre 2, un sous-graphe de $G = (V, E, \gamma)$ est un graphe $G' = (V, E')$ avec $E' \subseteq E$ (mêmes sommets). Il sert à définir l'arbre couvrant et, au chapitre 1, la composante connexe (sous-graphe connexe maximal).

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe orienté]], [[Arbre couvrant minimal]], [[Graphe connexe]], [[Graphe planaire]].

## À vérifier

- La définition exacte de Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]) (condition $S_0 \subseteq S$, $A_0 \subseteq A$) est coupée dans l'extraction du PDF : à relire sur la diapositive.
- La définition de [[2 - tree (résumé)|Chp2 - tree]] garde tous les sommets (ce qu'on appelle d'habitude graphe partiel ou sous-graphe couvrant), alors que la composante connexe de [[1 - Undirected graph (résumé)|Chp 1 - Undirected graph]] suppose un sous-graphe sur une partie des sommets. « graphe partiel » n'est pas un terme du cours.

Résumés : [[3 - Arbres (résumé)]], [[2 - tree (résumé)]], [[1 - Undirected graph (résumé)]]
