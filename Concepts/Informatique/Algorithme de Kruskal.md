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
maj: 2026-11-08
---

[[Algorithme glouton]] de calcul d'un [[Arbre couvrant minimal]] : ajouter l'arête non testée de plus petit poids si elle ne crée pas de [[Cycle (graphe)|cycle]], jusqu'à obtenir $\text{card}(V) - 1$ arêtes. Il relie ainsi tous les sommets en minimisant la somme des poids des arêtes. [[Erreurs du cours#^e-algorithme-de-kruskal|✎]]

- Préconditions : graphe valué, simple et connexe.
- Postcondition : arbre couvrant minimal.
- Complexité : $O(\text{card}(E)\log\text{card}(V))$.

Le TP Python trie les arêtes par poids et rejette celles dont les extrémités ont la même racine (structure [[Union-Find]]). Sa boucle `while e < V - 1` lit `graph[i]` sans vérifier `i < len(graph)` : sur un graphe non connexe, les arêtes s'épuisent avant $V - 1$ et le programme lève une `IndexError`, d'où la précondition de connexité (complément, hors du cours).

Notion parente : [[Arbre couvrant minimal]]. Voir aussi : [[Algorithme glouton]], [[Union-Find]], [[Cycle (graphe)]].

Résumés : [[2 - tree]], [[0 - Graph - Python]]
