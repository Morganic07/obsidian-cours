---
type: concept
tags: [year4]
aliases: [bug, bogue, erreur d'exécution, erreur de logique, runtime error]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : erreur qui se manifeste à l'exécution du programme (erreur d'exécution ou de logique), par opposition aux erreurs détectées par le [[Compilateur|compilateur]] ([[Erreur de compilation|erreurs de compilation]]) et par l'éditeur de liens ([[Édition de liens|erreurs de liaison]]). C'est la catégorie la plus difficile à comprendre et à corriger.

Complément, hors du cours : un programme qui compile peut planter ([[Erreur de segmentation]], division par zéro), boucler sans fin, ou donner un résultat faux sans rien signaler ([[Dépassement d'entier]], [[Variable non initialisée]]). On les traque avec un [[Débogueur|débogueur]] et des [[Test unitaire|tests]].

## Dans le cours

[[4 - Cours complet]] classe les erreurs en trois sortes, de la plus facile à la plus difficile : compilation, liaison, exécution ; il montre aussi que le compilateur accepte des valeurs absurdes (`int age = -100;`), source de bugs futurs.

Résumés : [[4 - Cours complet]]
