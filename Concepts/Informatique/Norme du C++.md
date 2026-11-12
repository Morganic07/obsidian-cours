---
type: concept
tags: [year4]
aliases: [C++98, C++03, C++11, C++14, C++17, C++20, C++23, ISO/IEC 14882, standard C++, norme ISO du C++]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : le [[Langage C++|C++]] est défini par une norme internationale, ISO/IEC 14882, publiée par l'[[Organisation internationale de normalisation]] et préparée par le comité WG21. Elle fixe la syntaxe, le sens des programmes et le contenu de la [[Bibliothèque standard du C++|bibliothèque standard]] ; les compilateurs ([[GCC]], [[Clang]], [[Visual Studio|MSVC]]) la mettent en œuvre, avec un temps de retard.

| Version | Apports principaux |
|---|---|
| C++98 (C++03 corrective) | première norme : classes, templates, exceptions, STL |
| C++11 | refonte : `auto`, `nullptr`, initialisation par accolades, références `&&`, lambdas, pointeurs intelligents, `std::thread` |
| C++14, C++17 | compléments : `std::optional`, `std::filesystem`, liaisons structurées (C++17) |
| C++20 | modules, concepts, coroutines, `std::format`, ranges |
| C++23 | `std::print`, `import std;` |

Un nouveau rythme triennal est suivi depuis C++11. On choisit la version avec l'[[Option de compilation|option]] `-std=c++17` ; sans elle, g++ 14 compile en C++17 étendu (`gnu++17`). Un programme qui n'emploie que la norme est portable d'un compilateur à l'autre ; une extension comme `#pragma once` ne l'est qu'en pratique.

## Dans le cours

- [[5 - Compilation séparée]] compile avec `-std=c++17` dans son Makefile.
- [[4 - Cours complet]] (2012, code en C++98) explique que le compilateur refuse ce qui « n'est pas défini précisément par la norme C++ ».

Voir aussi : [[Langage C]], [[Norme du C]].

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
