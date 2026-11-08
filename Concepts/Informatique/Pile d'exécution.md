---
type: concept
tags:
  - year1
  - year2
  - year4
aliases:
  - pile d'appels
  - call stack
  - cadre de pile
  - stack frame
  - stack pointer
  - pile mémoire
  - pile de récursion
  - débordement de pile
  - stack overflow
  - RecursionError
matieres:
  - Algo Maths
  - Algo
  - C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-08
---

**Algo** : la pile d'exécution gère tous les appels de fonctions. La pile de récursion en est un cas particulier : elle ne concerne que les appels récursifs mais utilise la même structure. Chaque bloc empilé contient les paramètres, l'adresse de retour et les variables locales de l'appel.

**C++** : une variable locale d'une fonction va dans la pile (*stack*), organisée en LIFO. À l'appel, un cadre de pile (*stack frame*) est empilé avec les variables locales, les paramètres et l'adresse de retour ; à la fin de la fonction, le registre *stack pointer* est déplacé et tout le cadre est libéré. Chp3 l'illustre avec `echange` : son cadre disparaît au retour dans `main`. Dans le schéma de la version par adresse, chaque variable a sa propre adresse, avec un pas de 4 : `a` en 0xabdafa8, `b` en 0xabdafac, `temp` en 0xabdafb0. [[Erreurs du cours#^e-pile-d-execution|✎]]

**Trace d'un appel récursif (complément, hors du cours)** : `fact(3)` empile `fact(2)`, qui empile `fact(1)`, qui empile `fact(0)` (cas d'arrêt). Les blocs se dépilent ensuite dans l'ordre inverse : `fact(0)` rend 1, `fact(1)` rend $1 \times 1 = 1$, `fact(2)` rend $2 \times 1 = 2$, `fact(3)` rend $3 \times 2 = 6$. La profondeur de pile est donc proportionnelle à $n$.

**Débordement de pile (complément, hors du cours)** : la pile a une taille limitée (quelques mégaoctets par fil d'exécution en général). Une récursion trop profonde, ou sans cas d'arrêt atteint, la dépasse : c'est le *stack overflow*, qui fait planter un programme C ou C++. Python s'en protège en levant une `RecursionError` au-delà d'une profondeur fixée, 1000 par défaut (`sys.getrecursionlimit()`, modifiable avec `sys.setrecursionlimit`). La [[Récursivité terminale]] ne l'évite que si le langage élimine les appels terminaux, ce que Python ne fait pas.

Notion parente : [[Pile et file]]. Voir aussi : [[Récursivité]], [[Récursivité terminale]], [[Factorielle]], [[Passage par valeur]], [[Pointeur et adresse mémoire]], [[Allocation dynamique]].

Résumés : [[0 - diapo prof]], [[1 - récursivité et complexité]], [[1 - basiques]], [[3 - pointeurs , tableaux, listes chainées, structures]]
