---
type: concept
tags:
  - year4
aliases:
  - printf
  - scanf
  - séquences de contrôle
  - spécificateur de format
  - modificateurs de format
matieres:
  - C++
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/Chp1 - basiques.docx|Chp1 - basiques]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : `printf` et `scanf` sont les fonctions d'entrée-sortie formatées de la bibliothèque standard du C, déclarées dans `stdio.h` (d'où `#include <stdio.h>`). Leur premier argument est une chaîne de format, dont les séquences `%…` disent comment convertir chacun des arguments suivants.

`printf` affiche, `scanf` lit : `scanf("%d", &i)` range l'entier lu à l'adresse de `i`.

**Pourquoi le `&` dans `scanf` (complément, hors du cours)** : le C passe les arguments [[Passage par valeur|par valeur]] ; `scanf` recevrait une copie de `i` et ne pourrait pas la modifier. On lui donne donc l'adresse de la variable. Oublier le `&` fait écrire `scanf` à une adresse quelconque (la valeur de `i` prise pour une adresse), souvent avec une [[Erreur de segmentation]]. Exception : pour une chaîne, `scanf("%s", nom)` sans `&`, le nom d'un tableau étant déjà une adresse.

Les **séquences de contrôle** commencent par `%` :

| Séquence | Interprétation |
|---|---|
| `%d`, `%i` | entier signé décimal |
| `%u` | entier non signé |
| `%o` | octal |
| `%x`, `%X` | hexadécimal |
| `%f` | réel |
| `%c` | caractère |
| `%s` | chaîne |
| `%p` | adresse (chapitre 3) ; `%d` ne convient pas, une adresse de 64 bits ne tenant pas dans un `int` [[Erreurs du cours#^e-fonctions-printf-et-scanf\|✎]] |

Des **modificateurs** règlent la largeur (`%3d`, `%03d`). Le spécificateur choisit comment interpréter les bits : `char lettre = 66` s'affiche 66 avec `%d` et B avec `%c`.

**Compléments, hors du cours** :

| Séquence ou modificateur | Effet |
|---|---|
| `%ld`, `%lld` | `long`, `long long` |
| `%e` | réel en notation scientifique (`1.500000e+02`) |
| `%%` | affiche le caractère `%` |
| `%f` | six décimales par défaut (`3.140000`) |
| `%.2f` | deux décimales, arrondies (`3.14159` → `3.14`) |
| `%8.2f` | largeur 8, deux décimales, aligné à droite |
| `%-5d` | largeur 5, aligné à gauche |

Piège classique : un `double` s'affiche avec `%f` dans `printf` mais se lit avec `%lf` dans `scanf`. `printf` reçoit des valeurs, et un `float` passé à une fonction à nombre variable d'arguments est promu en `double` : `%f` sert aux deux. `scanf` reçoit des adresses et doit savoir s'il écrit 4 octets (`float`, `%f`) ou 8 (`double`, `%lf`).

En C++, `std::cout << x + y;` remplace `printf("%d", x + y)`, sans séquence de contrôle ([[4 - Prise de note]] ; voir [[Flux d'entrée-sortie (C++)]]).

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Pointeur et adresse mémoire]], [[Flux d'entrée-sortie (C++)]], [[Passage par valeur]].

Résumés : [[1 - basiques]], [[3 - pointeurs , tableaux, listes chainées, structures]]
