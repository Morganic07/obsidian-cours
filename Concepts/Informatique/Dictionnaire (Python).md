---
type: concept
tags:
  - year4
aliases:
  - dictionnaire Python
  - dictionnaires Python
  - dict
matieres:
  - graph theory
sources:
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-08
---

Structure Python d'associations clé-valeur, par exemple `{"nom": "Michel", "age": 33}` : on y accède par la clé (pas par la valeur), on peut ajouter une clé, et on la parcourt avec `keys()` et `items()`.

**Compléments (hors du cours)** :
- accéder à une clé absente (`dic["x"]`) lève une `KeyError` ; on l'évite avec le test `if cle in dic` (`in` porte sur les clés, pas sur les valeurs) ou avec `dic.get(cle, defaut)`, qui renvoie `defaut`, ou `None` si aucun défaut n'est donné ;
- `values()` donne les valeurs ;
- un dictionnaire est une [[Table de hachage|table de hachage]] : accès, ajout et test `in` se font en temps constant en moyenne ; les clés doivent être immuables (hachables) : un entier, une chaîne ou un tuple, mais pas une liste ;
- depuis Python 3.7, l'ordre d'insertion des clés est conservé lors du parcours.

En TP de théorie des graphes, un graphe est représenté par un dictionnaire : la clé est un sommet, la valeur la liste de ses voisins. On n'affiche chaque arête qu'une fois grâce au test `node < neighbor`.

Voir aussi : [[Matrice d'adjacence]], [[Graphe non orienté]].

Résumés : [[0 - Graph - Python]]
