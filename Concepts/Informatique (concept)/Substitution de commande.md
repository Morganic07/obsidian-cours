---
type: concept
tags:
  - year2
aliases:
  - command substitution
  - backticks
  - apostrophes inversées
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh (résumé)|Commandes Shell + explications]]"
  - "[[2 - TP2 (résumé)|Cours TP2]]"
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
maj: 2026-11-06
---

`$(...)` exécute la commande entre parenthèses et la remplace par son résultat, qu'on peut stocker dans une variable (`current_datetime=$(date)`). Les apostrophes inversées font de même (``CURRENT_DATE=`date` ``, ``echo `pwd` ``). À distinguer de `$test`, qui lit la valeur d'une variable.

Notion parente : [[Script Bash]]. Voir aussi : [[Variable Bash]], [[Commande date]], [[Méta-caractère]].

## À vérifier

- Une ligne « 0 » isolée apparaît dans l'explication de `$(...)` de la fiche (reste de mise en page).

Résumés : [[8 - OS commandes sh (résumé)]], [[2 - TP2 (résumé)]], [[Copy of TP2-Commands (résumé)]], [[TP2 (résumé)]]
