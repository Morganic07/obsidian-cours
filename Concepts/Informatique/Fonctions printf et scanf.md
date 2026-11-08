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
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"
maj: 2026-11-08
---

`printf` affiche, `scanf` lit : `scanf("%d", &i)` range l'entier lu à l'adresse de `i`.

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
| `%p` | adresse (chapitre 3) |

Des **modificateurs** règlent la largeur (`%3d`, `%03d`). Le spécificateur choisit comment interpréter les bits : `char lettre = 66` s'affiche 66 avec `%d` et B avec `%c`.

En C++, `std::cout << x + y;` remplace `printf("%d", x + y)`, sans séquence de contrôle ([[4 - Prise de note]] ; voir [[Flux d'entrée-sortie (C++)]]).

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Pointeur et adresse mémoire]], [[Flux d'entrée-sortie (C++)]].

## Erreurs du cours

- [[3 - pointeurs , tableaux, listes chainées, structures|Chp3]] écrit « Pour print une adresse mémoire soit on fait %d, soit on fait %p » ; il faut « on fait %p » : `%d` attend un `int`, et une adresse de 64 bits affichée avec `%d` est tronquée (comportement indéfini).

Résumés : [[1 - basiques]], [[3 - pointeurs , tableaux, listes chainées, structures]]
