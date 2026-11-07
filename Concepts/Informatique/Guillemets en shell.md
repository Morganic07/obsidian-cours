---
type: concept
tags: [year2]
aliases: [quoting, single quotes, double quotes, guillemets simples, guillemets doubles]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]", "[[Séance TP2 (résumé)|Cours TP2]]"]
maj: 2026-11-06
---

- Les apostrophes `' '` gardent la valeur littérale de chaque caractère : `echo 'Hello $USER'` affiche `Hello $USER`.
- Les guillemets `" "` gardent la plupart des caractères mais développent les variables : `echo "Hello $USER"` affiche `Hello momo`.

Notion parente : [[Méta-caractère]]. Voir aussi : [[Variable Bash]], [[Caractère d'échappement]].

## À vérifier

- Commentaire faux dans le sujet : `echo 'path $PWD'` est annoncé comme affichant « Hello $PWD », alors que la sortie réelle est `path $PWD`.

Résumés : [[Copy of TP2-Commands (résumé)]], [[Séance TP2 (résumé)]]
