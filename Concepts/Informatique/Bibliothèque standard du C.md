---
type: concept
tags: [year4]
aliases: [libc, glibc, C standard library, bibliothèque C standard, en-têtes standard du C]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.3.c|6.3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la bibliothèque standard du C est l'ensemble des fonctions, types et [[Macro (préprocesseur)|macros]] que la [[Norme du C|norme du C]] impose à toute implémentation. Ils sont déclarés dans des [[Fichier d'en-tête|en-têtes]] standard, que le programme inclut par la [[Directive include|directive `#include`]] (29 en C11 et C17, 31 en C23). Les plus utilisés :

| En-tête | Contenu |
|---|---|
| `<stdio.h>` | entrées-sorties : `printf`, `scanf` ([[Fonctions printf et scanf]]), fichiers (`fopen`, `fgets`) |
| `<stdlib.h>` | `malloc`, `free` ([[Allocation dynamique]]), `rand` ([[Nombres aléatoires en C]]), `exit`, `atoi` |
| `<string.h>` | [[Chaîne de caractères|chaînes]] : `strlen`, `strcpy`, `strcmp`, `memcpy` |
| `<math.h>` | `sqrt`, `pow`, `fabs`, `sin` ([[Racine carrée]], [[Fonctions trigonométriques]]) |
| `<stdbool.h>`, `<stdint.h>` | type `bool` ([[Booléen]]), entiers de taille fixe (`int32_t`) |
| `<limits.h>`, `<float.h>` | bornes des types (`INT_MAX`, `DBL_EPSILON`) |

L'en-tête ne contient que les déclarations ([[Déclaration et définition]]) ; le code compilé des fonctions est fourni par l'implémentation et relié au programme à l'[[Édition de liens|édition de liens]], le plus souvent sous forme de [[Bibliothèque partagée|bibliothèque partagée]]. Sous [[Linux]], c'est en général la **glibc** du projet GNU (d'autres existent, comme musl) ; les fonctions de `<math.h>` y sont dans une bibliothèque séparée, la libm, d'où l'option `-lm` qu'il faut ajouter à la commande [[GCC]] d'un programme C qui les appelle (`g++` la lie d'office, la bibliothèque standard du C++ en dépendant).

Une implémentation peut ajouter des éléments hors norme : la glibc fournit par exemple la constante `M_PI` dans `<math.h>`, définie par [[POSIX]] et non par la norme du C. Un programme qui s'en sert est moins [[Portabilité (informatique)|portable]].

La [[Bibliothèque standard du C++|bibliothèque standard du C++]] reprend celle du C sous des noms sans `.h` et préfixés de `c` : `<cstdio>`, `<cstdlib>`, `<cmath>` ([[Bibliothèque cmath]]).

## Dans le cours

- [[tp6]] : `math.h` est inclus sans être utilisé ; il fournirait `pow` et, avec la glibc, la macro `M_PI`, qui vient de POSIX.
- [[td listes chaînées]] : `<stdio.h>` pour `printf`, `<stdlib.h>` pour `malloc` et `free`.

Voir aussi : [[Norme du C]], [[Bibliothèque standard du C++]], [[Directive include]], [[Édition de liens]].
