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
maj: 2026-11-08
---

- Les apostrophes `' '` gardent la valeur littérale de chaque caractère : `echo 'Hello $USER'` affiche `Hello $USER`, et `echo 'path $PWD'` affiche `path $PWD`. [[Erreurs du cours#^e-guillemets-en-shell|✎]]
- Les guillemets `" "` gardent la plupart des caractères mais développent les variables : `echo "Hello $USER"` affiche `Hello momo`.
- Sans guillemets, `echo $USER` affiche seulement le nom d'utilisateur. [[Erreurs du cours#^e-guillemets-en-shell|✎]]

Notion parente : [[Méta-caractère]]. Voir aussi : [[Variable Bash]], [[Caractère d'échappement]].

Résumés : [[2 - TP2]]
