---
type: concept
tags:
  - year1
  - year3
  - year4
aliases:
  - Type de base
  - types de base
  - types primitifs
  - basic datatypes
  - primitive type
  - primitive types
  - type objet
  - types objets
  - unsigned char
  - long double
  - type void
matieres:
  - Algo Maths
  - Java
  - C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"
maj: 2026-11-08
---

Types élémentaires fournis par le langage, par opposition aux types structurés ou objets. Le type fixe la place réservée en mémoire et la façon d'interpréter les bits.

**Pseudo-code et Python** (Algo Maths) : `ENTIER` (opérateurs `+ - * DIV MOD`), `REEL`, `BOOLEEN` (`ET OU NON`), `CARACTERE`, `CHAINE` (concaténation `&`). Python : entiers, flottants, chaînes, booléens ; `type(x)` et `isinstance(x, float)`. L'examen de novembre 2022 oppose type structuré et type primitif.

**Java** : `byte` 8 bits, `short` 16, `int` 32, `long` 64, `float` 32, `double` 64, `char` 16 (Unicode), `boolean`. À côté, les types objets (classes, interfaces) et `void`. Hiérarchie des numériques de `double` à `int`, puis `short`, `char`, `byte`.

**C** (C++) : `void` (type vide, pour les fonctions sans argument ou sans retour), `int` (qualificatifs `short`, `long`, `signed` par défaut, `unsigned`), `char` (support du [[Code ASCII]], aussi entier sur 8 bits), `float`, `double` et `long double` (précision croissante). `char` occupe 1 octet, `int` en général 4, `double` en général 8. En C, `char` est un entier : `c = 65` et `c = 'A'` sont identiques.

**C++** ([[4 - C++]]) : `int` (entier), `double` (décimal), `char` (un seul caractère), `bool` (vrai / faux, `true` / `false`) et `std::string` (chaîne de caractères, en fait une classe de la bibliothèque standard). Le cours précise : « identique au C ».

Notion parente : [[Pseudo-code]]. Voir aussi : [[Chaîne de caractères]], [[Nombre à virgule flottante]], [[Structure (struct)]], [[Typage dynamique]], [[Typage statique]], [[Transtypage]], [[Variable (programmation)]], [[Complément à deux]], [[Norme IEEE 754]].

## Erreurs du cours

- [[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]] écrit « Taille d'un entier […] Sur système 64 bits : 8 octets » ; il faut « en général 4 octets », comme le dit [[1 - basiques|Chp1 - basiques]] : sur les systèmes 64 bits courants, `int` reste sur 4 octets, ce sont les adresses qui passent à 8. Le schéma du même cours espace d'ailleurs les cases de 4 en 4.

Résumés : [[0 - diapo prof]], [[1 - Intro Java]], [[1 - basiques]], [[4 - C++]]
