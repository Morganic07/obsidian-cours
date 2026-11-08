---
type: matiere
tags:
  - year4
sources:
  - "[[1 - Undirected graph|Chp 1 - Undirected graph]]"
  - "[[2 - tree|Chp2 - tree]]"
  - "[[3 - complexité|chp3 - complexité]]"
  - "[[4 - oriented graphs|chp4 - oriented graphs]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-08
---

Théorie des graphes : graphes non orientés, arbres, complexité des algorithmes, graphes orientés, et un TP Python. Les 5 notes sont intégrées. Cours en anglais, sauf le chapitre de complexité en français.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - Undirected graph\|Chp 1 - Undirected graph]] | Définitions, graphes particuliers | [[1 - Undirected graph\|Résumé]] |
| [[2 - tree\|Chp2 - tree]] | Arbres, arbre couvrant minimal, Kruskal | [[2 - tree\|Résumé]] |
| [[3 - complexité\|chp3 - complexité]] | Complexité, $O$, $\Omega$, $\Theta$ | [[3 - complexité\|Résumé]] |
| [[4 - oriented graphs\|chp4 - oriented graphs]] | Degrés, DFS, BFS, composantes fortement connexes | [[4 - oriented graphs\|Résumé]] |
| [[0 - Graph - Python\|Graph - Python]] | Dictionnaires, fonctions sur graphes, Kruskal | [[0 - Graph - Python\|Résumé]] |

## Concepts

- **Graphes non orientés (chapitre 1)** : [[Graphe non orienté]], [[Sommet et arête]], [[Degré d'un sommet]], [[Graphe simple]], [[Graphe sous-jacent]], [[Graphe complet]], [[Graphe régulier]], [[Graphe biparti]], [[Graphe planaire]], [[Graphe pondéré]], [[Sous-graphe]], [[Isomorphisme de graphes]], [[Matrice d'adjacence]], [[Chaîne (graphe)]], [[Cycle (graphe)]], [[Graphe connexe]]
- **Arbres (chapitre 2)** : [[Arbre (théorie des graphes)]], [[Forêt (graphe)]], [[Pont (graphe)]], [[Arbre couvrant minimal]], [[Algorithme glouton]], [[Algorithme de Kruskal]]
- **Complexité (chapitre 3)** : [[Complexité algorithmique]], [[Classe de complexité]], [[Calcul de complexité et théorème de résolution]], [[Recherche séquentielle]], [[Recherche dichotomique]], [[Tri par sélection]], [[Tri par insertion]], [[Produit matriciel]], [[Tours de Hanoï]]
- **Graphes orientés (chapitre 4)** : [[Graphe orienté]], [[Chemin (graphe)]], [[Parcours en profondeur]], [[Parcours en largeur]], [[Composante fortement connexe]], [[Algorithme de Tarjan]]
- **TP Python** : [[Dictionnaire (Python)]], [[Union-Find]]
- **Ajoutés par l'enrichissement** : [[Lemme des poignées de main]], [[Liste d'adjacence]], [[Graphe eulérien]], [[Algorithme de Prim]], [[Table de hachage]], [[Classes P et NP]], [[Tri topologique]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[3 - complexité]] : $O(m \cdot n)$ n'est pas linéaire (quadratique si $m = n$) ; avec `range(n)`, `somme_1` calcule $0 + \ldots + (n-1)$, alors que `somme_2` calcule $1 + \ldots + n$.
- [[1 - Undirected graph]] : un graphe biparti demande deux parties non vides ; une arête seule ($K_{1,1}$) suffit.

## Liens avec les autres matières

- **[[Cours/Informatique/Algo/_index|Algo]]** : les [[Tours de Hanoï]] et l'[[Algorithme glouton]] y sont introduits.
- **Algo (Year 2)** : [[Récursivité]], [[Recherche dichotomique]] et la complexité y sont traitées avec [[Complexité algorithmique]]. Son chapitre 3 rappelle aussi [[Graphe non orienté]], [[Graphe orienté]], [[Chemin (graphe)]], [[Cycle (graphe)]], [[Sous-graphe]] et [[Arbre (théorie des graphes)]] : [[Cours/Informatique/Algo/_index|Algo]].
- **[[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]]** : le [[Produit matriciel]], dont le chapitre 3 calcule la complexité.
