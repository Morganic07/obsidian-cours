---
type: concept
tags: [year4]
aliases: [sizeof, size_t, taille d'un type]
sources: ["[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex2.c|ex2.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : `sizeof` est un opérateur du [[Langage C|C]] et du [[Langage C++|C++]] (un [[Mot réservé|mot réservé]], pas une fonction) qui donne la taille **en octets** d'un type ou d'une expression. Le résultat est de type `size_t`, entier non signé défini dans `<stddef.h>` ; on l'affiche avec `%zu` ([[Fonctions printf et scanf]]).

```c
sizeof(int)          // taille d'un type : parenthèses obligatoires
sizeof x             // taille d'une expression : parenthèses facultatives
sizeof(Chainon)      // taille d'une structure, rembourrage compris
```

Propriétés :

- il est calculé **à la compilation** : l'expression n'est pas évaluée (`sizeof(i++)` n'incrémente pas `i`). Seule exception, en C, un tableau de longueur variable (C99), dont la taille se calcule à l'exécution ;
- `sizeof(char)` vaut 1 par définition ; les autres tailles dépendent de la plateforme. Sur un PC 64 bits actuel ([[Linux]], modèle LP64) : `int` 4 octets, `long` 8, `double` 8, tout [[Pointeur et adresse mémoire|pointeur]] 8 ([[Type entier]], [[Octet]]) ;
- la taille d'une [[Structure (struct)|structure]] peut dépasser la somme de celles de ses champs, à cause des octets de rembourrage (*padding*) ajoutés pour l'alignement : `struct { char c; int i; }` fait en général 8 octets, pas 5.

Usages :

- **allouer** de la mémoire ([[Allocation dynamique]]) : `malloc(sizeof(Chainon))`, ou mieux `malloc(sizeof *nouveau)`, qui reste juste si le type de `nouveau` change ; pour un tableau, `malloc(n * sizeof *t)` ;
- **compter les cases d'un tableau** : `sizeof(tab) / sizeof(tab[0])`, valable seulement là où le tableau est déclaré. Dans une fonction qui le reçoit en paramètre, `tab` est devenu un pointeur et `sizeof(tab)` donne 8 ([[Décroissance d'un tableau en pointeur]]) ;
- écrire du code [[Portabilité (informatique)|portable]] qui ne suppose pas la taille des types.

## Dans le cours

- [[td listes chaînées]] : `malloc(sizeof(Chainon))` réserve sur le tas un bloc de la taille d'un chaînon.
- [[1 - basiques]] : `sizeof` figure parmi les mots réservés du C ; la fiche rappelle que `sizeof(char)` vaut 1 et que les autres tailles dépendent de la machine.
- [[2 - structures code]] : `sizeof(tab) / sizeof(tab[0])` retrouve le nombre de cases d'un tableau, seulement là où il est déclaré.

Voir aussi : [[Allocation dynamique]], [[Type primitif]], [[Structure (struct)]], [[Octet]].
