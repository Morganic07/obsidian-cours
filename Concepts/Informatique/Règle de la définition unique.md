---
type: concept
tags: [year4]
aliases: [one definition rule, ODR, multiple definition]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : la règle de la définition unique (*one definition rule*, ODR) de la [[Norme du C++|norme du C++]] veut qu'une fonction ou une variable (hors `inline`) soit **définie une seule fois dans tout le programme**, même si elle est **déclarée** autant de fois qu'on veut ([[Déclaration et définition]]). Une classe peut en revanche être définie dans plusieurs [[Unité de compilation|unités de compilation]], à condition qu'une seule fois par unité et à l'identique partout : c'est ce que permettent le [[Fichier d'en-tête|fichier d'en-tête]] et sa [[Garde d'inclusion|garde d'inclusion]].

Conséquence pratique : un `.h` inclus par plusieurs `.cpp` ne contient que des déclarations, des définitions de classes et des [[Fonction inline|fonctions inline]]. Une fonction ordinaire définie dans un `.h` serait compilée dans chaque [[Fichier objet|fichier objet]], et l'[[Édition de liens|édition de liens]] échouerait :

```text
/usr/bin/ld: Segment.o: multiple definition of `carre(int)'; main.o: first defined here
```

## Dans le cours

Pas nommée : elle explique, dans les compléments de [[5 - Compilation séparée]], pourquoi le code des méthodes va dans les `.cpp`.

Résumés : [[5 - Compilation séparée]]
