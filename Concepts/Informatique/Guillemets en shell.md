---
type: concept
tags:
  - year2
aliases:
  - quoting
  - single quotes
  - double quotes
  - guillemets simples
  - guillemets doubles
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
  - "[[2 - TP2|Cours TP2]]"
maj: 2026-11-07
---

- Les apostrophes `' '` gardent la valeur littérale de chaque caractère : `echo 'Hello $USER'` affiche `Hello $USER`.
- Les guillemets `" "` gardent la plupart des caractères mais développent les variables : `echo "Hello $USER"` affiche `Hello momo`.

Notion parente : [[Méta-caractère]]. Voir aussi : [[Variable Bash]], [[Caractère d'échappement]].

## Erreurs du cours

- [[2 - TP2]] écrit que `echo 'path $PWD'` affiche « Hello $PWD » ; il faut « path $PWD ». De même, `echo $USER` n'affiche pas « Hello <username> » mais seulement le nom d'utilisateur (vérifié sur l'image du sujet).

Résumés : [[2 - TP2]]
