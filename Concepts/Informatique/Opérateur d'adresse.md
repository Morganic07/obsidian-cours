---
type: concept
tags: [year4]
aliases: [address-of, opérateur adresse, opérateur &]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : `&` placé devant une variable donne la valeur de son adresse en mémoire, qui sert à initialiser ou affecter un [[Pointeur et adresse mémoire|pointeur]] : `ptrInt = &i;`.

Complément, hors du cours : le symbole `&` a trois sens en C++ selon sa place : opérateur d'adresse devant une expression (`&i`), déclaration d'une [[Référence (C++)|référence]] dans un type (`int &j = i;`), et ET bit à bit entre deux opérandes (`a & b`). En C, `scanf("%d", &n)` passe l'adresse de `n` pour qu'elle soit modifiée.

## Dans le cours

[[4 - Cours complet]] l'utilise dans l'exemple de pointeur et pour l'exercice 5, où `main` appelle `ordonne3(&a, &b, &c)`. L'opération inverse est le [[Déréférencement|déréférencement]] `*`.

Résumés : [[4 - Cours complet]]
