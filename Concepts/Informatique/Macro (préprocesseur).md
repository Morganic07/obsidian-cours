---
type: concept
tags: [year4]
aliases: [macro, "#define", directive define, macro-constante]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : `#define PI 3.14159` crée une constante par une directive du [[Préprocesseur|préprocesseur]] : c'est une simple **substitution de texte** (un copier-coller) réalisée avant la compilation, sans aucun typage. Par convention, le nom s'écrit en MAJUSCULES pour le distinguer des variables.

Complément, hors du cours : une macro peut avoir des paramètres (`#define CARRE(x) ((x)*(x))`) ; sans parenthèses, `CARRE(1+2)` deviendrait `1+2*1+2`. En C++, on préfère `const`, `constexpr` (C++11) et les fonctions `inline`, qui sont typées et respectent la [[Portée d'une variable|portée]]. Les macros restent utiles pour la compilation conditionnelle (`#ifdef`) et les [[Garde d'inclusion|gardes d'inclusion]].

## Dans le cours

[[4 - Cours complet]] présente `#define` comme alternative à `const` pour les [[Constante (programmation)|constantes]], utile surtout pour la lisibilité.

Résumés : [[4 - Cours complet]]
