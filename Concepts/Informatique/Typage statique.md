---
type: concept
tags: [year4]
aliases: [static typing]
sources: ["[[Chp1 - basiques]]"]
maj: 2026-11-06
---

Le C est un langage à typage statique : toutes les vérifications de type sont faites à la compilation, avant l'exécution. Exemple du cours : `int resultat = total + texte;` (un entier plus l'adresse d'une chaîne) provoque une erreur ou un avertissement du compilateur, ce qui évite des plantages (*Segmentation fault*) à l'exécution.

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Erreur de compilation]], [[Erreur de segmentation]].

## À vérifier

- Le cours dit que l'addition d'un entier et d'une adresse « n'a pas de sens » ; en C, c'est de l'arithmétique de pointeurs valide, seule l'affectation du résultat à un `int` pose problème (complément du résumé).

Résumés : [[Chp1 - basiques (résumé)]]
