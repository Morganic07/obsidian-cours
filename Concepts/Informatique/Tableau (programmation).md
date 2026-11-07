---
type: concept
tags:
  - year2
  - year3
  - year4
aliases:
  - Tableau Bash
  - bash array
  - tableaux Bash
  - read -a
  - array
  - arrays
  - tableau Java
  - tableaux Java
  - Tableau en C
  - tableaux en C
  - indice d'un tableau
matieres:
  - Operating System
  - Java
  - C++
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-07
---

Un tableau (array) stocke plusieurs éléments sous un seul nom, chacun accessible par son indice.

**En Bash** (Operating System) : on accède à un élément par `${names[0]}`. `read -a names` lit l'entrée comme un tableau, les éléments étant séparés par des espaces.

**En Java** : déclaration `type[] nom = new type[taille]`, matrices `new type[t1][t2]`, indices de 0 à taille − 1, initialisation par `{...}`, taille par `.length`.

**En C** : déclaration `int tab[10];` (type, nom, taille). Indices de 0 à taille − 1, éléments de même type, non initialisés à zéro. `int effectifs[6];` réserve 6 entiers contigus, d'adresses espacées de 4 octets. Le nom du tableau est l'adresse de sa première case ; passé à une fonction, le tableau est converti en cette adresse : `float *t`, `float t[]` et `float t[100]` sont équivalents (la taille est ignorée).

Notion parente : [[Variable Bash]]. Voir aussi : [[Commande read]], [[Boucle (programmation)]], [[Méthode main]], [[Arithmétique des pointeurs]], [[Pointeur et adresse mémoire]], [[Passage par valeur]].

## Erreurs du cours

- [[8 - OS commandes sh|Commandes Shell + explications]] écrit `read -a names` puis `echo "names: ${name[0]}, ${name[1]}"` ; il faut `${names[0]}, ${names[1]}`. Tel quel, l'affichage est vide.
- [[1 - Intro Java|Chp1 - Intro Java]] écrit que `valeurs.length` vaut 4 pour `int valeurs[] = { 5, 2, 4, 8, 9};` ; il faut 5.
- [[2 - structures code|chp2 - structures code]] écrit que la taille d'un tableau « doit être écrite en dur » et interdit `int n; int tab[n];` ; depuis C99, un tableau de taille variable est permis si `n` a reçu une valeur (complément, hors du cours). Sans valeur pour `n`, l'exemple reste faux.

Résumés : [[8 - OS commandes sh]], [[1 - Intro Java]], [[2 - structures code]], [[3 - pointeurs , tableaux, listes chainées, structures]]
