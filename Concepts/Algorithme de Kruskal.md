---
type: concept
aliases: [Kruskal]
matieres: [graph theory]
sources: ["[[Chp2 - tree]]", "[[Graph - Python]]"]
maj: 2026-11-06
---

[[Algorithme glouton]] de calcul d'un [[Arbre couvrant minimal]] : ajouter l'arête non testée de plus petit poids si elle ne crée pas de [[Cycle (graphe)|cycle]], jusqu'à obtenir $\text{card}(V) - 1$ arêtes.

- Préconditions : graphe valué, simple et connexe.
- Postcondition : arbre couvrant minimal.
- Complexité : $O(\text{card}(E)\log\text{card}(V))$.

Le TP Python trie les arêtes par poids et rejette celles dont les extrémités ont la même racine (structure [[Union-Find]]).

Notion parente : [[Arbre couvrant minimal]]. Voir aussi : [[Algorithme glouton]], [[Union-Find]], [[Cycle (graphe)]].

## À vérifier

- La note finale du cours parle de « poids des nœuds » au lieu des arêtes.
- Dans le TP, `graph[i]` peut sortir de la liste sur un graphe non connexe.

Résumés : [[Chp2 - tree (résumé)]], [[Graph - Python (résumé)]]
