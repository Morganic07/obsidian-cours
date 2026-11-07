---
type: concept
tags: [year3]
aliases: [ordre d'évaluation, précédence des opérateurs, associativity, operator precedence]
matieres: [Java]
sources: ["[[chp 1 - Intro Java (résumé)|Chp1 - Intro Java]]"]
maj: 2026-11-06
---

L'**associativité** fixe l'ordre des opérations de même précédence : en Java, toutes les opérations binaires s'associent à gauche, sauf l'affectation.

Les opérandes sont évalués de gauche à droite, ce qui compte en présence d'[[Effet de bord|effets de bord]] : avec `a = 0`, `a + ++a` vaut 1 et `++a + a` vaut 2.

Notion parente : [[Langage Java]]. Voir aussi : [[Effet de bord]], [[Opérateur d'incrémentation]].

Résumés : [[chp 1 - Intro Java (résumé)]]
