---
type: concept
tags: [year4]
aliases: [affectation composée, compound assignment, "+=", opérateurs composés]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : opérateur qui combine une opération et une [[Affectation|affectation]] : `a += b` équivaut à `a = a + b`, de même `-=`, `*=`, `/=`, `%=`. L'expression `a` n'est évaluée qu'une fois, et pour une `string`, `s += "x"` ajoute à la fin sans créer de copie intermédiaire.

## Dans le cours

[[4 - Cours complet]] cite `a += 1;` parmi les quatre façons d'incrémenter un entier, avec `++a`, `a++` et `a = a + 1` (voir [[Opérateur d'incrémentation]]).

Résumés : [[4 - Cours complet]]
