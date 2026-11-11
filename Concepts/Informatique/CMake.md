---
type: concept
tags: [year4]
aliases: [CMakeLists.txt, générateur de build]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : CMake est un générateur de systèmes de construction, libre et multiplateforme. On décrit le projet (sources, exécutables, bibliothèques, version du langage) dans un fichier `CMakeLists.txt`, et CMake en déduit un [[Make (logiciel)|Makefile]], un fichier pour [[Ninja (logiciel)|Ninja]] ou un projet [[Visual Studio]], selon la machine. Il calcule lui-même les dépendances aux [[Fichier d'en-tête|en-têtes]].

```cmake
cmake_minimum_required(VERSION 3.16)
project(Geometrie CXX)
set(CMAKE_CXX_STANDARD 17)
add_executable(programme main.cpp Point.cpp Segment.cpp)
```

```bash
cmake -B build      # génère le système de construction dans build/
cmake --build build # compile
```

C'est l'outil le plus courant des projets C++ actuels, et de nombreux [[Environnement de développement intégré|environnements de développement]] l'utilisent directement (CLion, Qt Creator, Visual Studio).

## Dans le cours

Pas nommé : [[5 - Compilation séparée]] écrit le Makefile à la main. CMake apparaît dans ses compléments.

Voir aussi : [[Compilation séparée]].

Résumés : [[5 - Compilation séparée]]
