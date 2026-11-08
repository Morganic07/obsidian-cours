---
type: matiere
tags:
  - year4
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[4 - C++|chp4 C++]]"
  - "[[4 - Prise de note|chp4 prise de note]]"
maj: 2026-11-08
---

Programmation bas niveau, puis objet. Les trois premières notes portent sur le langage C (`printf`, `malloc`, `struct`), même si le dossier s'appelle C++ ; le chapitre 4 passe au [[Langage C++|C++]] et à la [[Programmation orientée objet|programmation orientée objet]]. Les 5 documents sont intégrés.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - basiques\|Chp1 - basiques]] | Syntaxe, types, mémoire, erreurs, questions pièges | [[1 - basiques\|Résumé]] |
| [[2 - structures code\|chp2 - structures code]] | Boucles, `switch`, fonctions, tableaux | [[2 - structures code\|Résumé]] |
| [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3 - pointeurs , tableaux, listes chainées, structures]] | Adresses, pointeurs, passage par adresse, `struct`, listes chaînées | [[3 - pointeurs , tableaux, listes chainées, structures\|Résumé]] |
| [[4 - C++\|chp4 C++]] | Diaporama : bases du C++, `std::cout`, classes, public/privé, constructeurs, get/set, surcharge d'opérateurs, exercices `Point`, `Segment` et `Maze` | [[4 - C++\|Résumé]] |
| [[4 - Prise de note\|chp4 prise de note]] | Notes manuscrites du chapitre 4 : compilation avec `g++`, exercices `Cercle` faits en séance et leur sortie | [[4 - Prise de note\|Résumé]] |

## Concepts

- **Langage et compilation (Chp1)** : [[Langage C]], [[Typage statique]], [[Mot réservé]], [[Type primitif]], [[Transtypage]], [[Variable non initialisée]], [[Fonctions printf et scanf]], [[Erreur de compilation]], [[Erreur de segmentation]], [[Pile d'exécution]]
- **Représentation des données (Chp1)** : [[Numération binaire]], [[Notation hexadécimale]], [[Complément à deux]], [[Norme IEEE 754]], [[Code ASCII]]
- **Structures de contrôle (Chp1 et chp2)** : [[Opérateur de comparaison]], [[Évaluation en court-circuit]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Instruction vide]], [[Fonction et procédure]], [[Passage par valeur]]
- **Mémoire et pointeurs (chp2 et Chp3)** : [[Tableau (programmation)]], [[Pointeur et adresse mémoire]], [[Arithmétique des pointeurs]], [[Pointeur NULL]], [[Allocation dynamique]], [[Structure (struct)]], [[Opérateur flèche]], [[Liste chaînée]]
- **Le C++ (chp4)** : [[Langage C++]], [[GCC]] (`g++`), [[Espace de noms (namespace)]], [[Flux d'entrée-sortie (C++)]], [[Référence (C++)]]
- **Programmation objet (chp4)** : [[Programmation orientée objet]], [[Classe et objet]], [[Encapsulation (programmation)]], [[Constructeur (programmation)]], [[Accesseur et mutateur]], [[Surcharge d'opérateurs]], [[Fonction amie (friend)]], [[Distance]] (exercice `Maze`)
- **Ajoutés par l'enrichissement** : [[Comportement indéfini]], [[Chaîne de compilation]], [[Fichier d'en-tête]], [[Pointeur pendant]], [[Fuite mémoire]], [[Destructeur (programmation)]], [[Héritage (programmation)]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[1 - basiques]] : `if (a = 3)` est une affectation, toujours vraie, et non une comparaison ; `a == b == c` ne teste pas l'égalité des trois valeurs (écrire `a == b && b == c`).
- [[3 - pointeurs , tableaux, listes chainées, structures]] : un `int` fait en général 4 octets, y compris sur un système 64 bits ; une adresse s'affiche avec `%p` ; dans le programme `malloc`, `free` libère le bloc sans effacer son contenu.
- [[4 - C++]] : un attribut privé n'est pas accessible hors de la classe (passer par un accesseur).
- [[4 - Prise de note]] : dans un constructeur, `int x = 0;` déclare une variable locale ; l'attribut s'initialise par `x = 0;` ou par la liste d'initialisation ; le séparateur décimal est le point (`13.3`).

## Liens avec les autres matières

- **[[Cours/Informatique/Algo/_index|Algo]]** : la [[Liste chaînée]] y est vue sans pointeurs, avec la pile d'exécution et la récursivité ; les arbres binaires de recherche y sont programmés en objet en Python (classe `Node`, [[Méthode spéciale Python|méthodes spéciales]] `__init__` et `__str__`), à comparer aux [[Constructeur (programmation)|constructeurs]] du chapitre 4.
- **[[Cours/Informatique/Java/_index|Java]]** : les mêmes structures de contrôle, avec le [[Transtypage]] et l'[[Évaluation en court-circuit]] ; Java est aussi un langage à classes (voir [[Programmation orientée objet]]).
- **[[Cours/Informatique/OS/_index|Operating System]]** : en Bash, la [[Structure conditionnelle]], la [[Boucle (programmation)]], le [[Tableau (programmation)]], l'[[Opérateur de comparaison]] et le [[Code ASCII]] ont leur équivalent shell ; les programmes C y sont compilés avec [[GCC]].
- **[[Cours/Informatique/Algo/_index|Algo]]** : le [[Type primitif]], la [[Fonction et procédure]] et la [[Structure (struct)]] y sont introduits en pseudo-code.
- **[[Cours/Informatique/Data mining/_index|data mining]]** : les distances euclidienne et de Manhattan demandées dans l'exercice `Maze` y servent au clustering (voir [[Distance]]).
