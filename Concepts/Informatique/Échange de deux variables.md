---
type: concept
tags: [year1, year4]
aliases: [permutation de deux variables, variable temporaire]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-12
---

« La base du travail sur les variables » selon le TD : permuter deux variables à l'aide d'une variable temporaire.

La procédure `permuter(x, y)`, sans mode `ES`, ne change rien chez l'appelant ; `permuter2(ES x, y)` fonctionne (voir [[Passage de paramètres]]). L'examen de janvier 2023 demande l'échange sans variable tampon.

Notion parente : [[Affectation]]. Voir aussi : [[Passage de paramètres]].

## Dans le cours

[[4 - Cours complet]] (C++) fait écrire `echange2ParAdresse()` puis sa version par référence, qui ordonnent deux `float` en les échangeant si besoin, et s'en sert pour trier trois valeurs (`ordonne3()`, trois appels au minimum).

- [[tp2]] : échange de `a` et `b` avec une variable temporaire `c` (2.8), puis rotation de trois variables (2.9) ; la fiche montre aussi l'échange par OU exclusif ([[Opérateur bit à bit|opérateur bit à bit]] `^`).
- [[tp4]] : le calcul des [[Nombres de Lucas|nombres de Lucas]] (4.6) décale deux variables à chaque tour, sur le même principe (calculer le nouveau terme avant d'écraser l'ancien).
- [[pointeurs]] : fonction `echange(int *a, int *b)`, qui échange deux variables de l'appelant par leurs adresses ([[Pointeur et adresse mémoire|pointeurs]]).

Résumés : [[0 - diapo prof]], [[4 - Cours complet]]
