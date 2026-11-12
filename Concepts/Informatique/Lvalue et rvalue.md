---
type: concept
tags: [year4]
aliases: [lvalue, rvalue, left value, right value, valeur gauche, valeur droite]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : une **lvalue** (*left value*) est un élément qui peut s'écrire à gauche de l'opérateur d'[[Affectation|affectation]] `=` : elle désigne un emplacement de stockage en mémoire, d'un type précis, modifiable. Une **rvalue** (*right value*) peut s'écrire à droite de `=` : c'est une valeur d'un type précis, sans forcément de zone de stockage (valeur, constante, variable, expression). Dans `longueur = 40;`, `longueur` est une lvalue et `40` une rvalue.

Complément, hors du cours : une lvalue n'est pas toujours modifiable (une constante `const` est une lvalue qu'on ne peut pas affecter). Une [[Référence (C++)|référence]] non constante ne peut se lier qu'à une lvalue, d'où l'erreur `int &k = 44;`. Depuis C++11, la norme distingue lvalue, xvalue et prvalue, et les références `&&` se lient aux rvalues (sémantique de déplacement).

## Dans le cours

Figure de la partie « Expressions et instructions » de [[4 - Cours complet]], et question de révision 40.

Résumés : [[4 - Cours complet]]
