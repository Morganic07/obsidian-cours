---
type: concept
tags: [year4]
aliases: [implicit function declaration, implicit declaration of function]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : règle du C89 selon laquelle l'appel d'une fonction encore inconnue la déclarait implicitement comme `int f()` (retour `int`, paramètres non vérifiés). Elle a été supprimée en C99 ([[Norme du C]]) ; GCC la signale encore par un avertissement en C (`implicit declaration of function`), et la refuse par défaut depuis GCC 14. En **C++, elle n'a jamais existé** : appeler une fonction non déclarée est une [[Erreur de compilation|erreur de compilation]] (`'carre' was not declared in this scope`). Il faut donc définir la fonction, ou déclarer son prototype, avant l'appel (voir [[Déclaration et définition]]).

## Dans le cours

[[4 - Cours complet]] affirme qu'un appel avant toute déclaration produit en C++ un simple avertissement de déclaration implicite ; c'est une erreur, corrigée dans la fiche.

Résumés : [[4 - Cours complet]]
