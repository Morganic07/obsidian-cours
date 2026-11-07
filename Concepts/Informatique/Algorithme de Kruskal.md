---
type: concept
tags:
  - year4
aliases:
  - Kruskal
matieres:
  - graph theory
sources:
  - "[[2 - tree|Chp2 - tree]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-07
---

[[Algorithme glouton]] de calcul d'un [[Arbre couvrant minimal]] : ajouter l'arête non testée de plus petit poids si elle ne crée pas de [[Cycle (graphe)|cycle]], jusqu'à obtenir $\text{card}(V) - 1$ arêtes.

- Préconditions : graphe valué, simple et connexe.
- Postcondition : arbre couvrant minimal.
- Complexité : $O(\text{card}(E)\log\text{card}(V))$.

Le TP Python trie les arêtes par poids et rejette celles dont les extrémités ont la même racine (structure [[Union-Find]]).

Notion parente : [[Arbre couvrant minimal]]. Voir aussi : [[Algorithme glouton]], [[Union-Find]], [[Cycle (graphe)]].

## Erreurs du cours

- [[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]] écrit, dans sa dernière phrase, « en minimisant la somme des poids des noeuds » ; il faut « la somme des poids des arêtes ».
- [[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]] : la boucle `while e < V - 1` lit `graph[i]` sans vérifier que `i < len(graph)` ; sur un graphe non connexe, les arêtes s'épuisent avant d'atteindre $V - 1$ et le programme lève une `IndexError`. Le cours suppose le graphe connexe (précondition).

Résumés : [[2 - tree]], [[0 - Graph - Python]]
