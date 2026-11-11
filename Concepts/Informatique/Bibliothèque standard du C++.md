---
type: concept
tags: [year4]
aliases: [C++ Standard Library, bibliothèque standard C++, STL, Standard Template Library, libstdc++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : la bibliothèque standard du C++ est l'ensemble des classes et fonctions que la [[Norme du C++|norme du C++]] garantit avec tout compilateur. Ses noms sont rangés dans l'[[Espace de noms (namespace)|espace de noms]] `std` et se déclarent par des en-têtes sans extension, inclus avec des chevrons ([[Directive include]]) :

| En-tête | Contenu |
|---|---|
| `<iostream>` | [[Flux d'entrée-sortie (C++)\|flux]] `std::cout`, `std::cin`, `std::endl` |
| `<string>` | `std::string`, [[Chaîne de caractères\|chaîne de caractères]] de taille variable |
| `<vector>` | `std::vector`, [[Tableau (programmation)\|tableau]] dynamique |
| `<cmath>` | fonctions mathématiques : `std::sqrt` ([[Racine carrée]]), `std::pow`, `std::abs` |
| `<algorithm>` | `std::sort`, `std::max`, `std::find` |
| `<fstream>` | lecture et écriture de fichiers |

Ses conteneurs et algorithmes génériques viennent de la STL (*Standard Template Library*, 1994). Sous [[Linux]] avec [[GCC]], son code est dans la [[Bibliothèque partagée|bibliothèque partagée]] `libstdc++`, ajoutée par `g++` à l'[[Édition de liens|édition de liens]]. Les en-têtes hérités du [[Langage C|C]] existent sous deux noms : `<math.h>` et `<cmath>` (ce dernier dans `std`).

## Dans le cours

[[5 - Compilation séparée]] inclut `<iostream>` et `<cmath>` « avec chevrons : bibliothèque standard ou système », et appelle `std::sqrt`.

Voir aussi : [[Langage C++]], [[Fichier d'en-tête]].

[[4 - Cours complet]] signale que `cout` en provient et qu'on l'utilise « quasiment tout le temps », d'où `using namespace std;` ; elle fournit aussi des fonctions utiles comme `pow()`.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
