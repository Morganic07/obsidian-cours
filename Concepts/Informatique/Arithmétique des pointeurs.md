---
type: concept
tags:
  - year4
aliases:
  - pointer arithmetic
sources:
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-07
---

Ajouter 1 à une adresse la décale de la taille du type pointé : `effectifs + i` est l'adresse de la case `i`, et `t[i]` équivaut à `*(t + i)`. Pour un `unsigned char *`, `pb++` avance d'un octet. On peut ajouter ou retrancher un entier à un pointeur.

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Tableau (programmation)]], [[Notation hexadécimale]].

## Erreurs du cours

- [[3 - pointeurs , tableaux, listes chainées, structures|Chp3]] écrit « Taille d'un entier : sur système 64 bits : 8 octets » ; il faut « 4 octets » : un `int` fait 4 octets sur les systèmes 64 bits usuels, et les adresses de l'exemple du cours avancent bien de 4 en 4.

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
