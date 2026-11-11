---
type: concept
tags: [year4]
aliases: [fichier .cpp, fichier .c, source file, fichier d'implémentation]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : en [[Langage C++|C++]], le fichier source `.cpp` **définit** le code des méthodes et des fonctions : c'est l'implémentation. Chaque `.cpp` est compilé séparément des autres ([[Compilation séparée]]).

Il commence d'habitude par inclure son propre [[Fichier d'en-tête|fichier d'en-tête]] (`#include "Point.h"` dans `Point.cpp`), puis définit chaque méthode sous son nom complet `Point::Point(...)` ([[Opérateur de résolution de portée]]).

## Compléments (hors du cours)

- Extensions usuelles : `.c` pour le [[Langage C|C]] ; `.cpp`, `.cc` ou `.cxx` pour le C++. `g++` traite un `.c` comme du C++.
- Un fichier source et tout ce qu'il inclut forment une [[Unité de compilation|unité de compilation]], que le compilateur transforme en [[Fichier objet|fichier objet]].
- Plus largement, le [[Code source|code source]] désigne tout texte de programme lisible par un humain, par opposition au [[Code machine|code machine]].

Voir aussi : [[Interface et implémentation]], [[Déclaration et définition]].

## Dans [[4 - Cours complet]]

Le code source (ou programme source) est ce qu'écrit le programmeur, dans un fichier `.cpp` ou `.cc` en C++, `.c` en C ; la question 9 demande sa différence avec un fichier objet.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
