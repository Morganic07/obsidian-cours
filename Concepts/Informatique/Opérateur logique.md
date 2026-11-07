---
type: concept
tags:
  - year2
aliases:
  - Opérateurs logiques en Bash
  - logical AND
  - logical OR
  - ET logique en Bash
  - OU logique en Bash
  - opérateurs logiques
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[5 - TP5|Cours TP5]]"
maj: 2026-11-06
---

En Bash :

- **ET** : `[ c ] && [ c ]`, `[ c -a c ]` ou `[[ c && c ]]` ;
- **OU** : `[ c ] || [ c ]`, `[ c -o c ]` ou `[[ c || c ]]`.

En [[AWK]] aussi, `||` est le OU et `&&` le ET.

Notion parente : [[Structure conditionnelle]]. Voir aussi : [[Opérateur de comparaison]].

Résumés : [[8 - OS commandes sh]], [[5 - TP5]]
