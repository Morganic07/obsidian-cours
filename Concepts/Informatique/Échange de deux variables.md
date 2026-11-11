---
type: concept
tags: [year1, year4]
aliases: [permutation de deux variables, variable temporaire]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-11
---

« La base du travail sur les variables » selon le TD : permuter deux variables à l'aide d'une variable temporaire.

La procédure `permuter(x, y)`, sans mode `ES`, ne change rien chez l'appelant ; `permuter2(ES x, y)` fonctionne (voir [[Passage de paramètres]]). L'examen de janvier 2023 demande l'échange sans variable tampon.

Notion parente : [[Affectation]]. Voir aussi : [[Passage de paramètres]].

## Dans le cours

[[4 - Cours complet]] (C++) fait écrire `echange2ParAdresse()` puis sa version par référence, qui ordonnent deux `float` en les échangeant si besoin, et s'en sert pour trier trois valeurs (`ordonne3()`, trois appels au minimum).

Résumés : [[0 - diapo prof]], [[4 - Cours complet]]
