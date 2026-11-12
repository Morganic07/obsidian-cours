---
type: concept
tags: [year3, year4]
aliases: [ordre d'évaluation, précédence des opérateurs, associativity, operator precedence]
matieres: [Java]
sources: ["[[1 - Intro Java|Chp1 - Intro Java]]"]
maj: 2026-11-12
---

L'**associativité** fixe l'ordre des opérations de même précédence : en Java, toutes les opérations binaires s'associent à gauche, sauf l'affectation.

Les opérandes sont évalués de gauche à droite, ce qui compte en présence d'[[Effet de bord|effets de bord]] : avec `a = 0`, `a + ++a` vaut 1 et `++a + a` vaut 2.

Notion parente : [[Langage Java]]. Voir aussi : [[Effet de bord]], [[Opérateur d'incrémentation]].

## Dans le cours

- [[tp3]] : la règle des années bissextiles (3.8), `annee%4==0 && annee%100!=0 || annee%400==0`, est juste sans parenthèses parce que `&&` a une priorité plus forte que `||` ; GCC conseille quand même des parenthèses.
- [[tp5]] : `2<=nombre_tour<=5` (5.3) s'évalue de gauche à droite, `(2<=nombre_tour)<=5`, donc vaut toujours vrai ; il faut `nombre_tour >= 2 && nombre_tour <= 5`.
- [[formation C++]] : la [[Surcharge d'opérateurs|surcharge d'un opérateur]] ne change ni sa priorité ni son associativité ; `std::cout << p1 << std::endl` se lit `(std::cout << p1) << std::endl` (associativité à gauche de `<<`).

Résumés : [[1 - Intro Java]]
