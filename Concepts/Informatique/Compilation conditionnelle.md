---
type: concept
tags: [year4]
aliases: [conditional compilation, "#ifdef", "#ifndef", "#if"]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : la compilation conditionnelle consiste à faire garder ou sauter un bloc de texte par le [[Préprocesseur|préprocesseur]], selon une condition évaluée avant la compilation. Les directives sont `#if`, `#ifdef` (« si la [[Macro (préprocesseur)|macro]] est définie »), `#ifndef` (« si elle ne l'est pas »), `#elif`, `#else` et `#endif`. Le texte sauté n'est même pas lu par le compilateur.

Usages :
- la [[Garde d'inclusion|garde d'inclusion]] (`#ifndef POINT_H` … `#endif`) ;
- le code propre à un système : `#ifdef _WIN32` … `#else` … `#endif` (voir [[Portabilité (informatique)]]) ;
- le code de débogage, activé par `g++ -DDEBUG` qui définit la macro `DEBUG` ([[Option de compilation]]).

## Dans le cours

[[5 - Compilation séparée]] l'utilise dans la garde `#ifndef POINT_H / #define POINT_H / … / #endif` sans la nommer.

Résumés : [[5 - Compilation séparée]]
