---
type: concept
tags: [year4]
aliases: []
sources: ["[[Chp1 - basiques (résumé)|Chp1 - basiques]]"]
maj: 2026-11-06
---

Questions pièges du cours : un `;` placé juste après `if (x == 5);` ou `while (x < 10);` termine l'instruction.

- Pour le `if`, le bloc `{ printf("A"); }` qui suit s'exécute quand même : la sortie est « AB ».
- Pour le `while`, la boucle ne contient que l'instruction vide ; `x` n'étant jamais incrémenté, elle est infinie.

Les accolades en trop ne gênent pas la compilation.

Notion parente : [[Langage C]]. Voir aussi : [[Structure conditionnelle]], [[Boucle (programmation)]].

## À vérifier

- Le cours écrit que « le if ne s'exécute pas » : formulation ambiguë, mais le résultat « AB » est juste (relevé du résumé).
- Le nom « instruction vide » vient du résumé ; le cours dit que la condition « est vide ».

Résumés : [[Chp1 - basiques (résumé)]]
