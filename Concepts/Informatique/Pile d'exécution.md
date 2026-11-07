---
type: concept
tags:
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
matieres:
  - Algo
  - C++
sources:
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-07
---

**Algo** : la pile d'exécution gère tous les appels de fonctions. La pile de récursion en est un cas particulier : elle ne concerne que les appels récursifs mais utilise la même structure. Chaque bloc empilé contient les paramètres, l'adresse de retour et les variables locales de l'appel.

**C++** : une variable locale d'une fonction va dans la pile (*stack*), organisée en LIFO. À l'appel, un cadre de pile (*stack frame*) est empilé avec les variables locales, les paramètres et l'adresse de retour ; à la fin de la fonction, le registre *stack pointer* est déplacé et tout le cadre est libéré. Chp3 l'illustre avec `echange` : son cadre disparaît au retour dans `main`.

Notion parente : [[Pile et file]]. Voir aussi : [[Récursivité]], [[Passage par valeur]], [[Pointeur et adresse mémoire]], [[Allocation dynamique]].

## Erreurs du cours

- [[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]] donne à `temp`, dans le schéma de pile de la version par adresse de `echange`, l'adresse 0xabdafa0, déjà celle de `var1` ; il faut une adresse distincte, 0xabdafb0 en suivant le pas de 4 du schéma (après `a` en 0xabdafa8 et `b` en 0xabdafac). Vérifié sur l'image.

Résumés : [[1 - récursivité et complexité]], [[1 - basiques]], [[3 - pointeurs , tableaux, listes chainées, structures]]
