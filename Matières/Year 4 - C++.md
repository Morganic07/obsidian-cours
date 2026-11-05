---
type: matiere
sources: ["[[Chp1 - basiques]]", "[[chp2 - structures code]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-05
---

Programmation bas niveau. Le contenu des trois notes est du langage C (`printf`, `malloc`, `struct`), même si le dossier s'appelle C++. Les 3 notes sont intégrées.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Chp1 - basiques]] | Syntaxe, types, mémoire, erreurs, questions pièges | [[Chp1 - basiques (résumé)\|Résumé]] |
| [[chp2 - structures code]] | Boucles, `switch`, fonctions, tableaux | [[chp2 - structures code (résumé)\|Résumé]] |
| [[Chp3 - pointeurs , tableaux, listes chainées, structures]] | Adresses, pointeurs, passage par adresse, `struct`, listes chaînées | [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)\|Résumé]] |

## Concepts

- **Mémoire** : [[Pointeur et adresse mémoire]], [[Structure (struct)]], [[Liste chaînée]]
- **Langage** : [[Évaluation en court-circuit]], [[Transtypage]]

## À revoir en priorité avant un examen

- [[Chp1 - basiques (résumé)]] : `if (a=3)` n'est pas un test de possibilité, c'est une affectation vraie ; le remplacement proposé pour `a == b == c` n'est pas équivalent.
- [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]] : un `int` ne fait pas 8 octets sur un système 64 bits ; `%d` n'est pas le format d'une adresse ; le programme complet `malloc` n'est pas cohérent.

## Liens avec les autres matières

- **[[Year 2 - Algo]]** : la [[Liste chaînée]] y est vue sans pointeurs, avec la pile d'exécution et la récursivité.
- **[[Year 3 - Java]]** : les mêmes structures de contrôle, avec le [[Transtypage]] et l'[[Évaluation en court-circuit]].
