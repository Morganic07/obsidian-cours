---
type: concept
tags: [year4]
aliases: [single responsibility principle, SRP, une seule action logique]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : principe de conception selon lequel chaque unité de code (fonction, classe, module) ne doit avoir qu'une seule responsabilité, donc une seule raison de changer. Formulé par Robert C. Martin au début des années 2000 pour les classes (premier des principes SOLID), il s'applique aussi aux fonctions : une fonction qui calcule **et** affiche mélange deux responsabilités et devient difficile à tester et à réutiliser.

## Dans le cours

[[4 - Cours complet]] demande que chaque fonction réalise « une SEULE ACTION logique », celle qui correspond à son nom, et oppose le mauvais exemple `saisirUnNombreEtAfficherSonCarre()` au bon, où `carre()` ne fait que le calcul (voir [[Fonction et procédure]], [[Réutilisation de code]]).

Résumés : [[4 - Cours complet]]
