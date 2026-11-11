---
type: concept
tags:
  - year4
aliases:
  - static typing
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-11
---

Le C est un langage à typage statique : toutes les vérifications de type sont faites à la compilation, avant l'exécution. Exemple du cours : `int resultat = total + texte;` provoque une erreur ou un avertissement du compilateur, ce qui évite des plantages (*Segmentation fault*) à l'exécution. L'addition d'un entier et de l'adresse d'une chaîne est en elle-même valide ([[Arithmétique des pointeurs|arithmétique de pointeurs]]) ; ce qui est refusé, c'est de ranger son résultat, une adresse (`char *`), dans un `int`. [[Erreurs du cours#^e-typage-statique|✎]]

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Erreur de compilation]], [[Erreur de segmentation]].

## Dans le cours

[[4 - Cours complet]] (C++) : le compilateur se souvient du type de chaque variable et vérifie qu'on l'utilise comme le spécifie sa définition (`int n = "Robert";` est refusé) ; il sait exactement quelles opérations s'appliquent à chaque type (pas de `-` entre chaînes). Il ne vérifie pas le sens des valeurs : `int age = -100;` passe.

Résumés : [[1 - basiques]], [[4 - Cours complet]]
