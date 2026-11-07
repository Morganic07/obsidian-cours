---
type: concept
tags:
  - year4
aliases:
  - two's complement
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : le complément à deux est la représentation des entiers signés utilisée par presque tous les processeurs. Sur $n$ bits, un entier positif s'écrit en [[Numération binaire|binaire]] ordinaire, et l'opposé de $x$ s'obtient en inversant tous les bits de $x$ puis en ajoutant 1 ; le bit de poids fort vaut alors $-2^{n-1}$ au lieu de $2^{n-1}$. Sur $n$ bits on représente ainsi les entiers de $-2^{n-1}$ à $2^{n-1}-1$ (de $-2^{31}$ à $2^{31}-1$ pour un `int` de 32 bits), avec un seul zéro, et l'addition se fait avec le même circuit que pour les entiers non signés.

## Dans le cours

Nommé dans le premier chapitre de C++ sans explication : le cours dit seulement que lire 4 octets comme un entier signé (`int`) revient à appliquer l'arithmétique en complément à deux.

Notion parente : [[Type primitif]]. Voir aussi : [[Norme IEEE 754]].

Résumés : [[1 - basiques]]
