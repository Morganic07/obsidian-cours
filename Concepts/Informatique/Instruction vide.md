---
type: concept
tags:
  - year4
aliases: []
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-07
---

Questions pièges du cours : un `;` placé juste après `if (x == 5);` ou `while (x < 10);` termine l'instruction.

- Pour le `if`, le bloc `{ printf("A"); }` qui suit s'exécute quand même : la sortie est « AB ».
- Pour le `while`, la boucle ne contient que l'instruction vide ; `x` n'étant jamais incrémenté, elle est infinie.

Les accolades en trop ne gênent pas la compilation.

Notion parente : [[Langage C]]. Voir aussi : [[Structure conditionnelle]], [[Boucle (programmation)]].

Résumés : [[1 - basiques]]
