---
type: concept
tags: [year4]
aliases: [clang++, LLVM]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : Clang est un [[Compilateur|compilateur]] libre pour le [[Langage C|C]], le [[Langage C++|C++]] et l'Objective-C, bâti sur l'infrastructure LLVM. Il s'emploie comme [[GCC]] (`clang++ -Wall -c Point.cpp`), avec des options presque identiques, et se distingue par des messages d'erreur souvent plus lisibles. C'est le compilateur par défaut de macOS (Xcode) et de FreeBSD.

Les trois grands compilateurs C++ actuels sont GCC, Clang et MSVC ([[Visual Studio]]) ; tous suivent la [[Norme du C++|norme du C++]] et acceptent des extensions communes comme `#pragma once` ([[Garde d'inclusion]]).

## Dans le cours

Pas nommé : [[5 - Compilation séparée]] compile avec `g++`. Clang apparaît dans ses compléments.

Résumés : [[5 - Compilation séparée]]
