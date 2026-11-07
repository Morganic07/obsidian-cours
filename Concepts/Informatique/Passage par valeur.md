---
type: concept
tags:
  - year4
aliases:
  - passage par copie
  - pass by value
  - paramètres par référence
sources:
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-07
---

En C, les arguments d'une fonction sont passés par copie : une variable simple passée à une fonction n'est pas modifiée dans `main`. `echange(int a, int b)` n'échange donc pas `var1` et `var2`.

Pour modifier la variable, on passe son adresse : `echange(int *a, int *b)`, appelée avec `echange(&var1, &var2)`. C'est le passage par adresse, traité avec [[Pointeur et adresse mémoire]].

Notion parente : [[Fonction et procédure]]. Voir aussi : [[Pile d'exécution]], [[Tableau (programmation)]].

## Erreurs du cours

- [[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]] commente la version par valeur par « on rentre dans la fonction echange(&var1, &var2) » ; il faut `echange(var1, var2)`, l'appel écrit dans le code de cette version.

Résumés : [[2 - structures code]], [[3 - pointeurs , tableaux, listes chainées, structures]]
