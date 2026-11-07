---
type: concept
tags:
  - year4
aliases:
  - static typing
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-07
---

Le C est un langage à typage statique : toutes les vérifications de type sont faites à la compilation, avant l'exécution. Exemple du cours : `int resultat = total + texte;` (un entier plus l'adresse d'une chaîne) provoque une erreur ou un avertissement du compilateur, ce qui évite des plantages (*Segmentation fault*) à l'exécution.

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Erreur de compilation]], [[Erreur de segmentation]].

## Erreurs du cours

- [[1 - basiques|Chp1 - basiques]] écrit que le compilateur bloque parce qu'« additionner un entier et une adresse mémoire de chaîne de caractères n'a pas de sens » ; il faut « c'est l'affectation du résultat (une adresse) à un `int` qui est refusée » : `total + texte` est de l'[[Arithmétique des pointeurs|arithmétique de pointeurs]] valide (complément, hors du cours).

Résumés : [[1 - basiques]]
