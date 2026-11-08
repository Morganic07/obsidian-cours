---
type: concept
tags:
  - year4
aliases:
  - static typing
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-08
---

Le C est un langage à typage statique : toutes les vérifications de type sont faites à la compilation, avant l'exécution. Exemple du cours : `int resultat = total + texte;` provoque une erreur ou un avertissement du compilateur, ce qui évite des plantages (*Segmentation fault*) à l'exécution. L'addition d'un entier et de l'adresse d'une chaîne est en elle-même valide ([[Arithmétique des pointeurs|arithmétique de pointeurs]]) ; ce qui est refusé, c'est de ranger son résultat, une adresse (`char *`), dans un `int`. [[Erreurs du cours#^e-typage-statique|✎]]

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Erreur de compilation]], [[Erreur de segmentation]].

Résumés : [[1 - basiques]]
