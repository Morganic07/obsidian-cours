---
type: concept
tags:
  - year4
aliases:
  - arbre couvrant
  - arbres couvrants
  - minimum spanning tree
  - spanning tree
matieres:
  - graph theory
sources:
  - "[[2 - tree|Chp2 - tree]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-08
---

Un [[Arbre (théorie des graphes)|arbre]] est un graphe non orienté connexe sans cycle ; une [[Forêt (graphe)|forêt]] est sans cycle, chaque composante est un arbre. Un **arbre couvrant** d'un graphe contient tous ses sommets et un sous-ensemble de ses arêtes, avec la structure d'un arbre. Tout graphe connexe fini en a un.

Pour un [[Graphe pondéré|graphe pondéré]] simple et connexe, un **arbre couvrant minimal** a une valeur $w(T)$ (somme des poids des arêtes) minimale. L'énumération de tous les arbres est exponentielle. L'[[Algorithme de Kruskal]], [[Algorithme glouton|glouton]] : trier les arêtes par poids, retenir chaque arête qui ne ferme pas de cycle, jusqu'à $|V| - 1$ arêtes. Complexité annoncée : $O(|E|\log|V|)$. Le TP Python détecte les cycles avec une structure de racines (union par rang).

Exemple du cours : sept villes, arbre de 6 arêtes ; avec Kruskal on retrouve le même arbre de valeur 2818 (complément).

**Compléments (hors du cours)** :

- **Formule de Cayley** : le [[Graphe complet|graphe complet]] $K_n$ possède $n^{n-2}$ arbres couvrants (16 pour $n = 4$, 16 807 pour $n = 7$, environ $2{,}6 \times 10^{23}$ pour $n = 20$) ; c'est pourquoi la recherche exhaustive du minimum est exponentielle.
- **Propriété de coupe** : pour toute partition des sommets en deux groupes, une arête de poids minimal parmi celles qui relient les deux groupes appartient à un arbre couvrant minimal. Elle justifie les algorithmes gloutons : chaque arête retenue par Kruskal ou Prim est la plus légère d'une certaine coupe.
- **Propriété de cycle** : une arête strictement plus lourde que toutes les autres d'un cycle n'appartient à aucun arbre couvrant minimal.
- **Unicité** : si tous les poids sont distincts, l'arbre couvrant minimal est unique ; c'est le cas de l'exemple des sept villes. Sinon, plusieurs arbres peuvent avoir la même valeur minimale.
- **Graphe non connexe** : il n'a pas d'arbre couvrant ; Kruskal y produit une forêt couvrante minimale (un arbre couvrant minimal par [[Graphe connexe|composante connexe]]).
- **Autre algorithme** : l'[[Algorithme de Prim]] fait grandir un seul arbre à partir d'un sommet, en ajoutant à chaque étape l'arête la plus légère qui en sort ; Kruskal fusionne une forêt en parcourant les arêtes triées. La détection de cycle de Kruskal repose sur [[Union-Find]].
- **Usages** : concevoir le réseau le moins cher qui relie des sites (câbles, canalisations, routes) ; en fouille de données, couper les arêtes les plus lourdes d'un arbre couvrant minimal donne les groupes de la [[Classification hiérarchique ascendante|classification ascendante]] à saut minimal ; heuristique d'approximation pour le [[Problème du voyageur de commerce]] métrique (tournée au plus deux fois optimale).

Notion parente : [[Arbre (théorie des graphes)]]. Liens : [[Graphe non orienté]], [[Complexité algorithmique]], [[Pont (graphe)]], [[Algorithme de Prim]], [[Union-Find]]

Résumés : [[2 - tree]], [[0 - Graph - Python]]
