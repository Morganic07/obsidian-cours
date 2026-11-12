---
type: concept
tags: [year4]
aliases: [separate compilation, compilation par fichier]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[5 - Compilation séparée]]) : en [[Langage C++|C++]] (et en [[Langage C|C]]), chaque [[Fichier source|fichier source]] `.cpp` est compilé **séparément** des autres, en un [[Fichier objet|fichier objet]] `.o` ; l'[[Édition de liens|édition de liens]] réunit ensuite les fichiers objets en un [[Exécutable|exécutable]].

```bash
g++ -c Point.cpp               # produit Point.o
g++ -c Segment.cpp             # produit Segment.o
g++ -c main.cpp                # produit main.o
g++ Point.o Segment.o main.o -o programme      # édition de liens
```

Pour qu'un fichier puisse utiliser une classe ou une fonction définie ailleurs, il en inclut la [[Déclaration et définition|déclaration]], placée dans un [[Fichier d'en-tête|fichier d'en-tête]] `.h`.

## Compléments (hors du cours)

- **Intérêt** : seul le fichier modifié est recompilé, puis l'édition de liens refaite ([[Compilation incrémentale|compilation incrémentale]]) ; c'est ce qu'automatise [[Make (logiciel)|make]]. Modifier un en-tête oblige en revanche à recompiler tous les `.cpp` qui l'incluent.
- Le compilateur ne voit qu'une [[Unité de compilation|unité de compilation]] à la fois : il ne sait rien du code des autres fichiers. Un nom déclaré mais défini nulle part ne se découvre qu'à l'édition de liens (`undefined reference`).
- C'est l'organisation de la [[Programmation modulaire|programmation modulaire]] en C et C++ ; Java compile aussi chaque classe séparément, mais vers du bytecode (voir [[Compilation et bytecode]]).

Voir aussi : [[Chaîne de compilation]], [[GCC]], [[Option de compilation]].

## Dans le cours

[[4 - Cours complet]] (question 50) fait compiler séparément chaque `.cpp` en `.o`, puis lier tous les `.o` en un exécutable ; la question 53 demande l'intérêt de `make` en programmation modulaire.

- [[compilation séparée (C++)]] : `main.cpp`, `Point.cpp` et `Segment.cpp` sont compilés chacun en `.o` par `g++ -c`, puis liés en `programmeEntier` par un Makefile ; après `touch Segment.cpp`, seuls `Segment.o` et l'édition de liens sont refaits.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
