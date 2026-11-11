---
type: concept
tags: [year4]
aliases: [opérateur arithmétique, arithmetic operators, opérateur modulo, opérateur %]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : en C et C++, `+`, `-`, `*`, `/` et `%` (reste, ou modulo). Entre deux entiers, `/` donne le quotient entier (tronqué vers zéro) et `%` le reste : `10 / 3` vaut 3, `10 % 3` vaut 1 ; dès qu'un opérande est réel, l'autre est converti et la division est réelle (`10 / 3.0` vaut 3,333…). `%` ne s'applique qu'aux entiers. `*` et `/` sont prioritaires sur `+` et `-` (voir [[Associativité et ordre d'évaluation]]).

## Dans le cours

[[4 - Cours complet]] les utilise dès l'exercice 1 (division entière et réelle, voir [[Division euclidienne]]) et piège le calcul de la moyenne de l'exercice 3, faux si tout est `int`. Il montre aussi que le type fixe les opérations permises : `-` n'existe pas pour les chaînes.

Voir aussi : [[Opérateur d'affectation composée]], [[Transtypage]].

Résumés : [[4 - Cours complet]]
