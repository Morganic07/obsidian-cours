---
type: concept
tags: [year4]
aliases: [fichier exécutable, executable, binaire exécutable, a.out]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : le fichier exécutable (`programme`) est assemblé à partir des [[Fichier objet|fichiers objets]] par l'[[Édition de liens|édition de liens]] ; on le lance avec `./programme`.

## Compléments (hors du cours)

- Il contient du [[Code machine|code machine]] directement exécutable par le processeur, pour un système et une architecture donnés : un exécutable compilé sous [[Linux]] x86-64 ne tourne pas sous Windows ni sur un processeur ARM. Java contourne cette limite avec le bytecode (voir [[Compilation et bytecode]]).
- Sans option `-o`, [[GCC|`gcc` et `g++`]] le nomment `a.out`.
- Sous Linux, le format est ELF ; le fichier doit avoir le droit d'exécution (`chmod +x`), que `g++` lui donne. Le lancer crée un [[Processus|processus]].
- `./` est nécessaire parce que le dossier courant n'est pas dans le `PATH` du shell.

Voir aussi : [[Chaîne de compilation]], [[Compilation séparée]].

## Dans [[4 - Cours complet]]

L'exécutable est le produit de l'éditeur de liens (extension `.exe` sous Windows, aucune sous Linux) ; on le lance par `./helloWorld` depuis le répertoire courant.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
