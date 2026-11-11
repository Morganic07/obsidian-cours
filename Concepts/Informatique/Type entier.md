---
type: concept
tags: [year4]
aliases: [int, unsigned int, entier non signé, integer type, types entiers, unsigned long long]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : `int` (*integer*) est le type des entiers, et un [[Mot réservé|mot réservé]] ; c'est le type de retour de `main`. `unsigned int` est un entier non signé, qui ne prend pas de valeurs négatives.

Complément, hors du cours : sur une machine actuelle, `int` occupe 32 bits (de −2 147 483 648 à 2 147 483 647, en [[Complément à deux|complément à deux]]) et `unsigned int` va de 0 à 4 294 967 295 ; `long long` et `unsigned long long` font 64 bits. La norme ne fixe que des minimums (16 bits pour `int`). La division de deux entiers est entière ([[Division euclidienne]]). Dépasser la capacité est un [[Dépassement d'entier|dépassement]] : calcul modulo 2ⁿ pour un non signé, [[Comportement indéfini|comportement indéfini]] pour un signé.

## Dans le cours

[[4 - Cours complet]] l'utilise partout ; l'exercice 4 emploie `unsigned int` pour la somme et la factorielle, et demande ce qui se passe quand la factorielle devient trop grande.

Voir aussi : [[Type primitif]].

Résumés : [[4 - Cours complet]]
