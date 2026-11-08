---
type: concept
tags:
  - year4
aliases:
  - pointer arithmetic
sources:
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-08
---

Ajouter 1 à une adresse la décale de la taille du type pointé : `effectifs + i` est l'adresse de la case `i`, et `t[i]` équivaut à `*(t + i)`. Pour un `unsigned char *`, `pb++` avance d'un octet ; pour un `int *`, de 4 octets, taille d'un `int` sur les systèmes 32 bits comme sur les systèmes 64 bits usuels. [[Erreurs du cours#^e-arithmetique-des-pointeurs|✎]] On peut ajouter ou retrancher un entier à un pointeur.

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Tableau (programmation)]], [[Notation hexadécimale]].

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
