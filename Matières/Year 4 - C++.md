---
type: matiere
sources: ["[[Chp1 - basiques]]", "[[chp2 - structures code]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

Programmation bas niveau. Le contenu des trois notes est du langage C (`printf`, `malloc`, `struct`), même si le dossier s'appelle C++. Les 3 notes sont intégrées.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Chp1 - basiques]] | Syntaxe, types, mémoire, erreurs, questions pièges | [[Chp1 - basiques (résumé)\|Résumé]] |
| [[chp2 - structures code]] | Boucles, `switch`, fonctions, tableaux | [[chp2 - structures code (résumé)\|Résumé]] |
| [[Chp3 - pointeurs , tableaux, listes chainées, structures]] | Adresses, pointeurs, passage par adresse, `struct`, listes chaînées | [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)\|Résumé]] |

## Concepts

- **Langage et compilation (Chp1)** : [[Langage C]], [[Typage statique]], [[Mot réservé]], [[Type primitif]], [[Transtypage]], [[Variable non initialisée]], [[Fonctions printf et scanf]], [[Erreur de compilation]], [[Erreur de segmentation]], [[Pile d'exécution]]
- **Représentation des données (Chp1)** : [[Numération binaire]], [[Notation hexadécimale]], [[Complément à deux]], [[Norme IEEE 754]], [[Code ASCII]]
- **Structures de contrôle (Chp1 et chp2)** : [[Opérateur de comparaison]], [[Évaluation en court-circuit]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Instruction vide]], [[Fonction et procédure]], [[Passage par valeur]]
- **Mémoire et pointeurs (chp2 et Chp3)** : [[Tableau (programmation)]], [[Pointeur et adresse mémoire]], [[Arithmétique des pointeurs]], [[Pointeur NULL]], [[Allocation dynamique]], [[Structure (struct)]], [[Opérateur flèche]], [[Liste chaînée]]

## À revoir en priorité avant un examen

- [[Chp1 - basiques (résumé)]] : `if (a=3)` n'est pas un test de possibilité, c'est une affectation vraie ; le remplacement proposé pour `a == b == c` n'est pas équivalent.
- [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]] : un `int` ne fait pas 8 octets sur un système 64 bits ; `%d` n'est pas le format d'une adresse ; le programme complet `malloc` n'est pas cohérent.

## Liens avec les autres matières

- **[[Year 2 - Algo]]** : la [[Liste chaînée]] y est vue sans pointeurs, avec la pile d'exécution et la récursivité.
- **[[Year 3 - Java]]** : les mêmes structures de contrôle, avec le [[Transtypage]] et l'[[Évaluation en court-circuit]].
- **[[Year 2 - Operating System]]** : en Bash, la [[Structure conditionnelle]], la [[Boucle (programmation)]], le [[Tableau (programmation)]], l'[[Opérateur de comparaison]] et le [[Code ASCII]] ont leur équivalent shell.
- **[[Year 1 - Algo Maths]]** : le [[Type primitif]], la [[Fonction et procédure]] et la [[Structure (struct)]] y sont introduits en pseudo-code.
