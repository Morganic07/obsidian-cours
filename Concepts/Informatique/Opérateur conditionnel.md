---
type: concept
tags: [year3, year4]
aliases: [opérateur ternaire, ternary operator, conditional operator]
matieres: [Java]
sources: ["[[1 - Intro Java|Chp1 - Intro Java]]"]
maj: 2026-11-12
---

Opérateur ternaire de Java : `condition ? vrai : faux` vaut la deuxième expression si la condition est vraie, la troisième sinon ([[1 - Intro Java|Chp1 - Intro Java]]).

Notion parente : [[Structure conditionnelle]].

## Dans le cours

- [[tp3]] : le minimum de deux nombres (3.1) s'écrit en une [[Expression (programmation)|expression]], `int nbmin = (a > b) ? b : a;`, au lieu d'un `if … else`.
- [[formation C++]] : `int max = (a > b) ? a : b;` (programme 3-conditions) ; le commentaire d'origine omettait le `:` dans la syntaxe, corrigée en `condition ? valeur_si_vraie : valeur_si_fausse`.

Résumés : [[1 - Intro Java]]
