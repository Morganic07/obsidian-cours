---
type: concept
tags: [year4]
aliases: [avertissement du compilateur, compiler warning]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un avertissement (*warning*) est un message du [[Compilateur|compilateur]] qui signale un code suspect sans empêcher la compilation, contrairement à une [[Erreur de compilation|erreur de compilation]]. Le programme est produit, mais il risque de ne pas faire ce que l'on croit : affectation dans une condition (`if (x = 0)`), [[Variable non initialisée|variable non initialisée]], variable inutilisée, conversion qui perd de l'information, fonction non `void` sans `return`.

Avec [[GCC]], la plupart restent muets par défaut : on les active par les [[Option de compilation|options]] `-Wall` puis `-Wextra`, et `-Werror` les transforme en erreurs. Traiter chaque avertissement comme une erreur est une bonne habitude : beaucoup annoncent un [[Comportement indéfini|comportement indéfini]].

```text
main.cpp:5:11: warning: unused variable 'n' [-Wunused-variable]
```

## Dans le cours

[[5 - Compilation séparée]] compile avec `CXXFLAGS = -Wall -std=c++17` dans son Makefile ; [[4 - Prise de note]] et [[4 - Cours complet]] avec `g++ -Wall`.

- [[tp2]] : compilés avec `-Wall -Wextra`, les programmes font apparaître variables inutilisées et fonctions sans `return`.
- [[tp3]] : la règle des années bissextiles, juste sans parenthèses, déclenche `suggest parentheses around '&&' within '||'`.
- [[tp4]] : la variable `nombre`, jamais utilisée, déclenche `unused variable`.
- [[tp5]] : `warning: too many arguments for format` (5.8) et l'avertissement de 5.3 désignaient exactement les erreurs des programmes.
- [[tp6]] : `control reaches end of non-void function` pour des fonctions `int` qui peuvent sortir sans `return` (6.2, 6.3).
- [[tp7]] : `gcc -Wall -O2` signale `'indice_min' may be used uninitialized`.
- [[td listes chaînées]] : tous les exercices sont compilés avec `gcc -std=c17 -Wall -Wextra`.
- [[formation C++]] : `unused variable 'nbFlottant'` et `unused variable 'max'` ; c'est un avertissement qui a révélé le piège de `getCoord`.
- [[exo-prof]] : `-Wdeprecated-copy` sur l'opérateur d'affectation implicite de `Point`, dont le constructeur par copie est écrit à la main.
- [[compilation séparée (C++)]] : même avertissement `-Wdeprecated-copy` sur `A = p1;` ; le Makefile d'origine ne passant aucune option, il n'apparaît pas sans `CXXFLAGS`.

Voir aussi : [[Chaîne de compilation]].

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
