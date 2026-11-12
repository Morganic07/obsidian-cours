---
type: concept
tags: [year4]
aliases: [initialisation, initialization, initialisation par accolades, initialisation uniforme, brace initialization]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : opération qui donne une valeur **initiale** à une variable, lors de sa définition (`int a = 3;`). Elle se distingue de l'[[Affectation|affectation]], qui donne une **nouvelle** valeur à une variable existante (`a = 4;`), bien que les deux s'écrivent avec `=`.

Complément, hors du cours : depuis C++11, on peut initialiser avec des accolades : `int n{3};`, `int n{};` (vaut 0), `std::vector<int> v{1, 2, 3};`. Cette forme refuse les conversions avec perte (`int n{3.5};` ne compile pas). Une constante ou une [[Référence (C++)|référence]] doit être initialisée et ne peut pas être affectée ensuite. Dans un constructeur, on initialise les attributs par une [[Liste d'initialisation|liste d'initialisation]].

## Dans le cours

[[4 - Cours complet]] fait de l'initialisation systématique une [[Règle de codage|règle de codage]], car trop de bugs viennent de [[Variable non initialisée|variables non initialisées]] ; il illustre initialisation et affectation par des tableaux de valeurs sur des entiers et des chaînes.

Résumés : [[4 - Cours complet]]
