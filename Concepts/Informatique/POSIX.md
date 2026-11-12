---
type: concept
tags: [year4]
aliases: [Portable Operating System Interface, IEEE 1003, norme POSIX, IEEE Std 1003.1]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.3.c|6.3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : POSIX (*Portable Operating System Interface*) est une famille de normes de l'[[IEEE]], numérotée IEEE 1003 et reprise par l'ISO et la CEI sous le nom ISO/IEC 9945, qui définit l'interface d'un [[Système d'exploitation|système d'exploitation]] de type [[Unix]]. Sa première version date de 1988 (IEEE Std 1003.1-1988), sa révision la plus récente de 2024 (IEEE Std 1003.1-2024). Elle est née pour mettre fin à la divergence des nombreuses variantes d'Unix des années 1980 : un programme écrit pour POSIX doit se compiler et fonctionner sur tout système conforme ([[Portabilité (informatique)]]).

Elle normalise :

- les **[[Appel système|appels système]]** et l'interface C du système : processus (`fork`, `exec`, `wait`, voir [[Appel fork()]], [[Appel exec()]], [[Appels wait() et waitpid()]]), fichiers (`open`, `read`, `write`), [[Signal Unix|signaux]], [[Thread|threads]] (*pthreads*), [[Communication interprocessus|communication entre processus]] ;
- le **shell** et ses commandes : la syntaxe de `sh` ([[Bourne Shell (sh)]]), les utilitaires `ls`, `grep`, `awk`, `sed`… et leurs options ;
- des **ajouts à la [[Bibliothèque standard du C|bibliothèque standard du C]]** : fonctions et constantes que la [[Norme du C|norme du C]] ne prévoit pas, comme la constante `M_PI` de `<math.h>`, `strdup` (entrée dans la norme du C seulement en C23) ou `getline`.

[[Linux]] et les BSD suivent largement POSIX sans être tous certifiés ; macOS est certifié UNIX 03 par l'Open Group. [[Microsoft Windows|Windows]] n'est pas POSIX : on y retrouve cette interface par des couches de compatibilité (Cygwin, WSL).

Pour le programmeur C, la conséquence est simple : un programme qui se limite à la norme du C se compile partout ; un programme qui emploie des ajouts POSIX se compile sur les systèmes de type Unix, pas forcément ailleurs. Avec [[GCC]], l'option `-std=c17` (C strict) masque certains de ces ajouts, que l'on réactive en définissant `_POSIX_C_SOURCE` ou `_DEFAULT_SOURCE` avant les `#include` ([[Macro (préprocesseur)]]).

## Dans le cours

- [[tp6]] : la macro `M_PI`, que fournit `math.h` sous Linux avec la glibc, est définie par POSIX et non par la norme du C ; la fiche conseille de définir sa propre constante.

Voir aussi : [[Unix]], [[Linux]], [[Appel système]], [[Norme du C]], [[Shell et Bash]].
