---
type: concept
tags: [year2, year4]
aliases: [compilateur GCC, GCC compiler, g++]
matieres: [Operating System, C++]
sources: ["[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : GCC (GNU Compiler Collection) est la suite de compilateurs libres du projet GNU, compilateur de référence sous [[Linux]] pour le [[Langage C|C]] (commande `gcc`) et le C++ (`g++`). Il traduit le code source en code machine exécutable : `gcc -o prog prog.c` produit l'exécutable `prog`, que l'on lance avec `./prog`. Les options `-Wall` (avertissements) et `-g` (informations de débogage) sont d'usage courant.

## Dans le cours

Nommé dans le TP Processes sans définition : les labs 1 à 3 demandent de compiler les programmes C avec le compilateur GCC.

En C++ ([[4 - Prise de note]]) : on compile avec `g++ monprog.cpp -o monprog -Wall`, puis on lance `./monprog`. `g++` compile aussi des fichiers `.c`.

Voir aussi : [[Création et terminaison de processus]], [[Langage C++]].

Résumés : [[1 - basiques]], [[4 - Prise de note]]
