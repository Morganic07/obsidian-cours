---
type: concept
tags:
  - year4
aliases:
  - opérateur ->
sources:
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-12
---

Accès au champ d'une structure à travers un pointeur : `nouveau->valeur` équivaut à `(*nouveau).valeur`. Le cours la présente comme une « syntaxe propre et lisible ».

Notion parente : [[Structure (struct)]]. Voir aussi : [[Pointeur et adresse mémoire]], [[Liste chaînée]].

## Dans le cours

- [[td listes chaînées]] : `nouveau->valeur = user_valeur;` remplit un chaînon neuf, `actuel = actuel->suivant` avance dans la liste, et `actuel->suivant->valeur` lit la valeur du chaînon suivant (fonction `supprimerElement`).

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
