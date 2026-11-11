---
type: concept
tags: [year4]
aliases: ["#include", include, inclusion de fichier, include directive]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : le [[Préprocesseur|préprocesseur]] remplace chaque `#include` par le contenu du fichier désigné, avant la compilation. Deux formes :

| Forme | Usage |
|---|---|
| `#include "Point.h"` | guillemets : fichier du projet |
| `#include <iostream>` | chevrons : [[Bibliothèque standard du C++\|bibliothèque standard]] ou système (`iostream`, `cmath`…) |

Avec les guillemets, le fichier est cherché d'abord dans le dossier du fichier qui contient le `#include`, puis dans les dossiers des chevrons. [[Erreurs du cours#^e-directive-include|✎]]

## Compléments (hors du cours)

- Les dossiers de recherche s'ajoutent avec `-I` : `g++ -Iinclude -c main.cpp`.
- Inclure un fichier recopie tout son texte : un même en-tête inclus deux fois dans un fichier définirait ses classes deux fois. D'où la [[Garde d'inclusion|garde d'inclusion]].
- On n'inclut que des [[Fichier d'en-tête|fichiers d'en-tête]], jamais un `.cpp` : son code serait compilé deux fois et violerait la [[Règle de la définition unique|règle de la définition unique]].
- Depuis C++20, les **modules** (`import std;`) offrent une alternative à `#include`, encore peu répandue dans les cours.

Voir aussi : [[Compilation séparée]], [[Langage C++]].

## Dans [[4 - Cours complet]]

`#include <iostream>` rend accessibles les fonctionnalités du fichier `iostream`, fourni avec le compilateur ; l'exercice 4 inclut `somme.h` dans le fichier de `main()`.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
