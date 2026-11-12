---
type: concept
tags: [year4]
aliases: [include guard, "#pragma once", pragma once, header guard, garde d'en-tête]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[5 - Compilation séparée]]) : la garde d'inclusion évite qu'un [[Fichier d'en-tête|fichier d'en-tête]] soit lu deux fois dans la chaîne d'inclusion, ce qui définirait sa classe en double. Deux écritures :

```cpp
// version courte
#pragma once

// version classique
#ifndef POINT_H
#define POINT_H
// ... déclarations ...
#endif
```

## Compléments (hors du cours)

- La version classique est de la [[Compilation conditionnelle|compilation conditionnelle]] : à la première inclusion, la [[Macro (préprocesseur)|macro]] `POINT_H` n'existe pas, le texte est gardé et la macro définie ; aux suivantes, tout est sauté jusqu'à `#endif`. Le nom doit être propre à chaque fichier.
- `#pragma once` n'est pas dans la [[Norme du C++|norme du C++]], mais tous les compilateurs courants l'acceptent ([[GCC]], [[Clang]], [[Visual Studio|MSVC]]).
- Sans garde, un `main.cpp` qui inclut `Segment.h` (qui inclut `Point.h`) puis `Point.h` échoue : `error: redefinition of 'class Point'`.
- La garde ne vaut que dans une [[Unité de compilation|unité de compilation]] : chaque `.cpp` relit l'en-tête. Elle n'empêche donc pas une fonction définie dans un `.h` d'être définie plusieurs fois dans le programme (voir [[Règle de la définition unique]]).

Voir aussi : [[Directive include]], [[Préprocesseur]].

[[4 - Cours complet]] n'en parle pas ; la solution de son exercice 4, donnée en complément, l'ajoute dans `somme.h` (`#ifndef SOMME_H`).

## Dans le cours

- [[compilation séparée (C++)]] : `Point.h` est protégé par `#ifndef POINT_H`, `Segment.h` par `#pragma once` ; la garde est indispensable, car `main.cpp` inclut `Point.h` puis `Segment.h`, qui l'inclut à nouveau (sans garde : `redefinition of 'class Point'`).

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
