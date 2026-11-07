---
type: concept
tags:
  - year4
aliases:
  - pointeur
  - pointeurs
  - double pointeur
  - doubles pointeurs
  - adresse mémoire
  - passage par adresse
matieres:
  - C++
sources:
  - "[[chp 3 - pointeurs , tableaux, listes chainées, structures (résumé)|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[chp 2 - structures code (résumé)|chp2 - structures code]]"
maj: 2026-11-06
---

Toute donnée en mémoire est rangée à une **adresse**, notée en hexadécimal (préfixe `0x`). Un **pointeur** est une variable destinée à contenir une adresse.

- `&x` : adresse de `x` (affichée avec `%p`).
- `int *p;` : `p` contient l'adresse d'un entier. `p = &x;` lui affecte l'adresse de `x`.
- `*p` : valeur stockée à l'adresse contenue dans `p`. `*p = 2;` modifie `x`.
- Ajouter ou retrancher un entier à un pointeur décale d'autant de fois la taille du type ([[Arithmétique des pointeurs]]). `t[i]` équivaut à `*(t + i)`, et le nom d'un tableau est l'adresse de sa première case.
- `malloc` ([[Allocation dynamique]]) réserve un bloc sur le tas et renvoie son adresse, le pointeur ne contient pas les octets. Chaque `malloc` appelle un `free`, qui libère le bloc mais laisse l'adresse dans les pointeurs.
- `p->champ` équivaut à `(*p).champ`.

**Passage par adresse** : le C passe les arguments par copie ([[Passage par valeur]]). Pour qu'une fonction modifie une variable de `main`, on lui passe son adresse : `echange(int *a, int *b)` appelée par `echange(&var1, &var2)`. Un tableau passé à une fonction est converti en l'adresse de son premier élément.

**Double pointeur** : `int **dptr` contient l'adresse d'un pointeur. Il sert à modifier un pointeur depuis une fonction, par exemple la tête d'une [[Liste chaînée]]. Précautions du cours : initialiser, libérer, tester `NULL` ([[Pointeur NULL]]).

Liens : [[Structure (struct)]], [[Liste chaînée]], [[Arithmétique des pointeurs]], [[Allocation dynamique]], [[Passage par valeur]], [[Pointeur NULL]]

Résumés : [[chp 3 - pointeurs , tableaux, listes chainées, structures (résumé)]], [[chp 2 - structures code (résumé)]]
