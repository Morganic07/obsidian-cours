---
type: concept
tags:
  - year4
aliases:
  - pointeur nul
  - "NULL"
  - nullptr
  - null pointer
matieres:
  - C／C++
sources:
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[Raw/Year 4/C／C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : `NULL` est une valeur de pointeur qui ne désigne **aucun objet**. Déréférencer un pointeur nul (`*p` ou `p->champ` avec `p == NULL`) est un **comportement indéfini** ; en pratique, le programme s'arrête sur une [[Erreur de segmentation]].

- `malloc` renvoie `NULL` quand l'allocation échoue : on teste le résultat avant de s'en servir (`if (p == NULL) { ... }`) ; voir [[Allocation dynamique]].
- Bonne pratique : **initialiser** un pointeur à `NULL` quand on n'a pas encore d'adresse à lui donner, et **l'y remettre après `free`** (`free(p); p = NULL;`). Un pointeur qui garde l'adresse d'une zone libérée est un pointeur pendant (*dangling pointer*) ; remis à `NULL`, il devient détectable par un test.
- En C++ moderne (depuis C++11), on écrit **`nullptr`** : il a son propre type (`std::nullptr_t`) et ne se confond pas avec l'entier `0`, alors que `NULL` est une macro qui vaut `0` ou équivalent, ce qui peut tromper la surcharge de fonctions (`f(NULL)` peut appeler `f(int)` plutôt que `f(char*)`).

## Dans le cours

Dans une [[Liste chaînée]], le pointeur du dernier élément contient `NULL`, et une liste vide a son premier pointeur à `NULL`. Le cours recommande de vérifier qu'un pointeur n'est pas `NULL` avant d'y accéder.

- [[pointeurs]] : appeler `echange(NULL, &var2)` déréférencerait le pointeur nul ; c'est à l'appelant de passer des adresses valides.
- [[td listes chaînées]] : `*ptrpremier = NULL;` crée une liste vide, `NULL` marque la fin de la liste ([[Valeur sentinelle|valeur sentinelle]] du parcours `while (actuel != NULL)`), et `rechercherElement` renvoie `NULL` si la valeur est absente ; un `malloc` échoué renvoie aussi `NULL`.

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Allocation dynamique]].

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
