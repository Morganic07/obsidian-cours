---
type: concept
tags: [year2, year4]
aliases: [compilateur GCC, GCC compiler, g++]
matieres: [Operating System, C／C++]
sources: ["[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]", "[[Raw/Year 4/C／C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : GCC (GNU Compiler Collection) est la suite de compilateurs libres du projet GNU, compilateur de référence sous [[Linux]] pour le [[Langage C|C]] (commande `gcc`) et le C++ (`g++`). Il traduit le code source en code machine exécutable : `gcc -o prog prog.c` produit l'exécutable `prog`, que l'on lance avec `./prog`. Les options `-Wall` (avertissements) et `-g` (informations de débogage) sont d'usage courant.

## Dans le cours

Nommé dans le TP Processes sans définition : les labs 1 à 3 demandent de compiler les programmes C avec le compilateur GCC.

En C++ ([[4 - Prise de note]]) : on compile avec `g++ monprog.cpp -o monprog -Wall`, puis on lance `./monprog`. `g++` compile aussi des fichiers `.c`.

[[5 - Compilation séparée]] : `g++ -c Point.cpp` produit le [[Fichier objet|fichier objet]] `Point.o` ; `g++ Point.o Segment.o main.o -o programme` fait l'[[Édition de liens|édition de liens]]. Dans le [[Make (logiciel)|Makefile]], `CXX = g++` et `CXXFLAGS = -Wall -std=c++17` (voir [[Option de compilation]]).

## Compléments (hors du cours)

- **Sans `-o`**, l'exécutable s'appelle `a.out` : `g++ monprog.cpp` puis `./a.out`.
- **`-Wall`** active la plupart des avertissements (variable non initialisée ou inutilisée, comparaison douteuse…). Un avertissement ne bloque pas la compilation, contrairement à une [[Erreur de compilation|erreur]] ; `-Wextra` en ajoute d'autres, `-Werror` les change en erreurs.
- **`-std=c++17`** ou **`-std=c++20`** choisit la version de la norme du langage.
- **`gcc` et `g++`** : `gcc` compile un fichier `.c` comme du C ; `g++` traite un fichier `.c` comme du C++ et lie la bibliothèque standard C++. Un programme C valide peut donc échouer avec `g++` : par exemple s'il nomme une variable `class` ou `new`, mots réservés en C++, ou s'il affecte un `void *` (retour de `malloc`) à un pointeur typé sans conversion.
- Une seule commande enchaîne préprocesseur, compilation, assemblage et édition de liens : voir [[Chaîne de compilation]]. `-c` s'arrête avant l'édition de liens et produit un fichier objet `.o`.

Voir aussi : [[Création et terminaison de processus]], [[Langage C++]].

[[4 - Cours complet]] met en œuvre la « chaîne de fabrication g++ sous Linux » ; `g++` lancé seul répond « no input files » s'il est installé, et l'exercice 1 demande pourquoi utiliser g++ plutôt que gcc pour un programme C++.

Résumés : [[1 - basiques]], [[4 - Prise de note]], [[5 - Compilation séparée]], [[4 - Cours complet]]
