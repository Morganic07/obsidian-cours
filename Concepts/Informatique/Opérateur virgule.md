---
type: concept
tags: [year4]
aliases: [comma operator, "opérateur « , »", opérateur de séquence]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/10-SurchargeOpérateurs1.cpp|10-SurchargeOpérateurs1.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C|C]] et en [[Langage C++|C++]], l'opérateur virgule `a, b` est un [[Opérateur unaire et opérateur binaire|opérateur binaire]] qui évalue d'abord l'opérande de gauche, **jette** sa valeur, puis évalue l'opérande de droite, qui donne sa valeur et son type à toute l'[[Expression (programmation)|expression]]. L'évaluation de gauche à droite est garantie : tous les [[Effet de bord|effets de bord]] de `a` sont faits avant que `b` commence. C'est l'opérateur de plus faible priorité ([[Associativité et ordre d'évaluation]]).

```c
int x = (1, 2);           // x vaut 2 (parenthèses nécessaires)
for (i = 0, j = n - 1; i < j; i++, j--)   // usage typique : deux compteurs
    echange(&t[i], &t[j]);
```

La virgule n'est pas toujours cet opérateur. Dans un [[Appel de fonction|appel de fonction]] `f(a, b)`, une liste de paramètres, une déclaration `int a, b;` ou un initialiseur `{1, 2}`, elle n'est qu'un **séparateur** : `Point(x, y)` passe bien deux arguments au [[Constructeur (programmation)|constructeur]].

Pièges :

- `return x, y;` ne renvoie que `y` : une fonction ne renvoie qu'une valeur ([[Instruction return]]). Pour en rendre deux, on renvoie un objet, une [[Structure (struct)|structure]], ou en C++ un `std::pair` ([[Paire et tuple (C++)]]) ;
- `x = 1, 2;` se lit `(x = 1), 2;` et donne 1 à `x`, l'affectation étant plus prioritaire ;
- en [[Langage Python|Python]], `return x, y` renvoie un tuple : l'habitude ne se transpose pas en C++.

[[GCC]] signale l'opérande gauche inutile avec `-Wall` : `left operand of comma operator has no effect` ([[Avertissement de compilation]]). En dehors de l'en-tête des boucles `for`, mieux vaut l'éviter.

## Dans le cours

- [[formation C++]] : `int getCoord(){ return x, y; }` (programme 10) ne renvoie que `y`, et g++ avertit ; le commentaire d'origine attribuait à tort cet effet à `return Point(x, y);`, où la virgule sépare deux arguments.

Voir aussi : [[Instruction return]], [[Paire et tuple (C++)]], [[Expression (programmation)]].
