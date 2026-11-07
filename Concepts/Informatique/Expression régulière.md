---
type: concept
tags:
  - year2
aliases:
  - regular expression
  - expressions régulières
  - regex
  - pattern-based search
matieres:
  - Operating System
sources:
  - "[[5 - TP5|Cours TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5]]"
maj: 2026-11-07
---

En [[AWK]], le motif (pattern) s'écrit entre deux `/` : `/Peugeot/`, sensible à la casse. Pour chercher un motif à l'intérieur d'un champ, on utilise l'opérateur `~` au lieu de `==`, qui exige une égalité littérale :

`awk -F"|" '$6~/youtube/ || $6~/facebook/ {print $2}' log.txt`

Le manuel d'AWK dit que `FS` découpe les champs « as a regular expression ».

Notion parente : [[AWK]]. Voir aussi : [[Fonctions intégrées d'AWK]], [[Commande grep]].

Résumés : [[5 - TP5]]
