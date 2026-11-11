---
type: concept
tags: [year4]
aliases: [avertissement du compilateur, compiler warning]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : un avertissement (*warning*) est un message du [[Compilateur|compilateur]] qui signale un code suspect sans empêcher la compilation, contrairement à une [[Erreur de compilation|erreur de compilation]]. Le programme est produit, mais il risque de ne pas faire ce que l'on croit : affectation dans une condition (`if (x = 0)`), [[Variable non initialisée|variable non initialisée]], variable inutilisée, conversion qui perd de l'information, fonction non `void` sans `return`.

Avec [[GCC]], la plupart restent muets par défaut : on les active par les [[Option de compilation|options]] `-Wall` puis `-Wextra`, et `-Werror` les transforme en erreurs. Traiter chaque avertissement comme une erreur est une bonne habitude : beaucoup annoncent un [[Comportement indéfini|comportement indéfini]].

```text
main.cpp:5:11: warning: unused variable 'n' [-Wunused-variable]
```

## Dans le cours

[[5 - Compilation séparée]] compile avec `CXXFLAGS = -Wall -std=c++17` dans son Makefile ; [[4 - Prise de note]] et [[4 - Cours complet]] avec `g++ -Wall`.

Voir aussi : [[Chaîne de compilation]].

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
