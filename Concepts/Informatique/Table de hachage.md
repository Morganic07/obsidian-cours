---
type: concept
tags: [year4]
aliases: [hash table, hash map, fonction de hachage, hash function, hachable, hashable]
sources: ["[[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : structure de données qui stocke des couples clé-valeur dans un tableau, à une position (alvéole) calculée à partir de la clé par une **fonction de hachage** $h$ : la clé $k$ est rangée à l'indice $h(k) \bmod N$, où $N$ est la taille du tableau.

**Performances** : accès, insertion, suppression et test d'appartenance par clé se font en temps constant **en moyenne**, $O(1)$, quelle que soit la taille de la table ; dans le pire cas (toutes les clés au même endroit), $O(n)$. On ne peut en revanche pas parcourir les clés dans l'ordre de leur valeur sans les trier.

**Collisions** : deux clés distinctes envoyées à la même position. Deux façons classiques de les gérer :

- **chaînage** : chaque alvéole contient une liste des couples qui y tombent ;
- **adressage ouvert** : on cherche une autre alvéole libre selon une règle de sondage (c'est le choix de CPython).

**Facteur de charge** $\alpha = n / N$ (nombre d'éléments sur nombre d'alvéoles) : quand il dépasse un seuil, la table est agrandie et toutes les clés sont rehachées ; ce coût ponctuel reste $O(1)$ amorti par insertion.

**En Python** : les dictionnaires (`dict`) et les ensembles (`set`) sont des tables de hachage. Une clé doit être **hachable** : sa valeur de hachage (`hash(x)`) ne doit pas changer, ce qui impose en pratique un objet immuable (entier, chaîne, tuple d'objets immuables, `frozenset`). Une liste ou un dictionnaire ne peut pas servir de clé (`TypeError: unhashable type: 'list'`). Depuis Python 3.7, `dict` conserve l'ordre d'insertion (garantie du langage).

Ne pas confondre avec le [[Hachage de mot de passe]], qui utilise des fonctions de hachage cryptographiques, conçues pour être difficiles à inverser, alors qu'une table de hachage ne demande qu'une fonction rapide et bien répartie.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[0 - Graph - Python]] : le TP représente les graphes par des dictionnaires Python ([[Liste d'adjacence]]), dont l'accès aux voisins d'un sommet en temps constant moyen repose sur cette structure.

Voir aussi : [[Dictionnaire (Python)]], [[Liste d'adjacence]], [[Méthodes d'ensemble]], [[Complexité algorithmique]].

Résumés : [[0 - Graph - Python]]
