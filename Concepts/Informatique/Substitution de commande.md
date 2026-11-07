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
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[2 - TP2|Cours TP2]]"
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
maj: 2026-11-07
---

`$(...)` exécute la commande entre parenthèses et la remplace par son résultat, qu'on peut stocker dans une variable (`current_datetime=$(date)`). Les apostrophes inversées font de même (``CURRENT_DATE=`date` ``, ``echo `pwd` ``). À distinguer de `$test`, qui lit la valeur d'une variable.

Notion parente : [[Script Bash]]. Voir aussi : [[Variable Bash]], [[Commande date]], [[Méta-caractère]].

Résumés : [[8 - OS commandes sh]], [[2 - TP2]]
