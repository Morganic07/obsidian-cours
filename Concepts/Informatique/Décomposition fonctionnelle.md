---
type: concept
tags: [year4]
aliases: [analyse descendante, conception descendante, top-down design, raffinements successifs]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : principal outil pour organiser un programme : décomposer un traitement de grande taille en plusieurs parties plus petites, jusqu'à obtenir quelque chose de suffisamment simple à comprendre et à résoudre. Le polycopié la rattache au [[Discours de la méthode]] de Descartes.

Complément, hors du cours : chaque partie devient une [[Fonction et procédure|fonction]] au rôle unique, qui peut à son tour être décomposée (méthode des raffinements successifs, formalisée par Niklaus Wirth en 1971). Elle prépare la [[Programmation modulaire|programmation modulaire]], qui répartit les fonctions en fichiers ; elle diffère de [[Diviser pour régner|diviser pour régner]], technique algorithmique qui découpe les données et non le traitement.

## Dans le cours

[[4 - Cours complet]] l'applique en limitant les fonctions à 10 à 15 lignes, et dans l'exercice 5, où `ordonne3()` est décomposée en appels à `echange2ParAdresse()`.

Résumés : [[4 - Cours complet]]
