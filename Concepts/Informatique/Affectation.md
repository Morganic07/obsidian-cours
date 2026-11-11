---
type: concept
tags: [year1, year4]
aliases: [affectations, affectation simultanée, affectation concurrente]
matieres: [Algo Maths]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-11
---

En pseudo-code, la flèche `←` affecte à une variable une expression de même type ; la première affectation d'une variable est son initialisation.

En Python : affectation simple `x=7`, simultanée `x=y=7`, concurrente `x,y=7,53.2`, et `x+=1`.

L'examen d'informatique de novembre 2022 demande la différence entre initialisation et affectation.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Échange de deux variables]].

## Dans le cours

**C++** ([[4 - Cours complet]]) : l'opérateur `=` est le plus important à maîtriser ; il sert à deux opérations distinctes, l'[[Initialisation (programmation)|initialisation]] (valeur initiale à la définition) et l'affectation (nouvelle valeur d'une variable existante). L'affectation est indispensable dès qu'on répète un traitement avec des valeurs différentes, « c'est le concept de variable ». Seule une [[Lvalue et rvalue|lvalue]] peut être à gauche de `=`.

Résumés : [[0 - diapo prof]], [[4 - Cours complet]]
