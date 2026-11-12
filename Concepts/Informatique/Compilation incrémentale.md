---
type: concept
tags: [year4]
aliases: [incremental build, incremental compilation, recompilation incrémentale, build incrémental]
sources: ["[[Raw/Year 4/C／C++/programmes C++/compilation separée/Makefile|Makefile]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la compilation incrémentale consiste, après une modification, à ne recompiler que ce qui en dépend au lieu de tout le projet. Elle repose sur la [[Compilation séparée|compilation séparée]] : chaque [[Fichier source|fichier source]] `.cpp` donne son propre [[Fichier objet|fichier objet]] `.o`, et un `.o` à jour n'a pas besoin d'être refait. Sur un gros projet, cela ramène un temps de compilation de plusieurs minutes à quelques secondes.

L'outil le plus classique est [[Make (logiciel)|make]]. Le Makefile décrit un [[Graphe orienté|graphe]] de dépendances (chaque `.o` dépend de son `.cpp` et des [[Fichier d'en-tête|en-têtes]] qu'il inclut, l'[[Exécutable|exécutable]] dépend des `.o`). `make` compare les dates de modification : une cible n'est refaite que si l'une de ses dépendances est plus récente qu'elle, et les cibles sont traitées dans l'ordre d'un [[Tri topologique|tri topologique]].

```makefile
programme: main.o Point.o
	g++ main.o Point.o -o programme   # refaite si un .o a changé
Point.o: Point.cpp Point.h
	g++ -c Point.cpp                   # refaite si Point.cpp ou Point.h a changé
```

Conséquences :

- modifier un `.cpp` ne recompile que son `.o`, puis refait l'[[Édition de liens|édition de liens]] ;
- modifier un `.h` recompile tous les `.cpp` qui l'incluent, d'où l'intérêt de garder les en-têtes légers ;
- la méthode n'est sûre que si les dépendances sont exactes : un `#include` oublié dans le Makefile et un en-tête modifié ne déclenche plus la recompilation, ce qui laisse des `.o` incohérents. `g++ -MMD` génère ces dépendances automatiquement (fichiers `.d`), et [[CMake]] ou [[Ninja (logiciel)|Ninja]] les gèrent eux-mêmes.

En cas de doute (changement d'[[Option de compilation|options de compilation]], fichiers déplacés), on repart de zéro avec `make clean` puis `make`.

## Dans le cours

- [[compilation séparée (C++)]] : le Makefile du projet `Point`/`Segment` a été vérifié avec la [[Commande touch|commande `touch`]] : après `touch Segment.cpp`, `make` ne refait que `Segment.o` et l'édition de liens ; après `touch Point.h`, les trois `.o`, qui en dépendent tous.
- [[5 - Compilation séparée]] : le chapitre présente la compilation de chaque `.cpp` en `.o`, base de la compilation incrémentale.

Voir aussi : [[Compilation séparée]], [[Make (logiciel)]], [[Chaîne de compilation]], [[Unité de compilation]].
