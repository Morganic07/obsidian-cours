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
  - "[[1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]"
  - "[[1 - basiques (résumé)|Chp1 - basiques]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures (résumé)|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-06
---

**Algo** : la pile d'exécution gère tous les appels de fonctions. La pile de récursion en est un cas particulier : elle ne concerne que les appels récursifs mais utilise la même structure. Chaque bloc empilé contient les paramètres, l'adresse de retour et les variables locales de l'appel.

**C++** : une variable locale d'une fonction va dans la pile (*stack*), organisée en LIFO. À l'appel, un cadre de pile (*stack frame*) est empilé avec les variables locales, les paramètres et l'adresse de retour ; à la fin de la fonction, le registre *stack pointer* est déplacé et tout le cadre est libéré. Chp3 l'illustre avec `echange` : son cadre disparaît au retour dans `main`.

Notion parente : [[Pile et file]]. Voir aussi : [[Récursivité]], [[Passage par valeur]], [[Pointeur et adresse mémoire]], [[Allocation dynamique]].

## À vérifier

Dans le schéma du second `echange`, `temp` a la même adresse que `var1` (0xabdafa0) : l'une des deux est fausse (relevé du résumé).

Résumés : [[1 - récursivité et complexité (résumé)]], [[1 - basiques (résumé)]], [[3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
