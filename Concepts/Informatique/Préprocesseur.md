---
type: concept
tags: [year4]
aliases: [preprocessor, préprocesseur C, cpp (préprocesseur), directive du préprocesseur, preprocessor directive]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : le préprocesseur remplace chaque `#include` par le contenu du fichier désigné, **avant** la compilation.

## Compléments (hors du cours)

C'est la première étape de la [[Chaîne de compilation|chaîne de compilation]] du C et du C++. Le préprocesseur ne connaît pas le langage : il travaille sur le texte, ligne par ligne, et traite les **directives**, les lignes qui commencent par `#` :

| Directive | Rôle |
|---|---|
| `#include` | recopie un fichier (voir [[Directive include]]) |
| `#define N 10` | définit une [[Macro (préprocesseur)\|macro]], remplacée partout dans la suite du texte |
| `#ifdef`, `#ifndef`, `#if`, `#else`, `#endif` | [[Compilation conditionnelle\|compilation conditionnelle]] : garde ou saute un bloc de texte |
| `#pragma` | instruction propre au compilateur (`#pragma once`) |

Il retire aussi les commentaires. `g++ -E fichier.cpp` affiche son résultat sans compiler. Son usage principal en C++ est la [[Garde d'inclusion|garde d'inclusion]] des [[Fichier d'en-tête|fichiers d'en-tête]] ; le C++ moderne remplace les macros constantes par `const` ou `constexpr` (voir [[Constante (programmation)]]).

Voir aussi : [[Compilation séparée]], [[GCC]].

## Dans [[4 - Cours complet]]

Une ligne qui commence par `#` est une directive du préprocesseur (ou de précompilation) : elle ne contient pas d'instruction C/C++ et ne prend donc pas de `;`. `#define` y est présenté comme une substitution de texte faite avant la compilation, sans typage.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
