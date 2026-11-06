---
type: concept
tags: [year2, year3, year4]
aliases: [Tableau Bash, bash array, tableaux Bash, read -a, array, arrays, tableau Java, tableaux Java, Tableau en C, tableaux en C, "indice d'un tableau"]
matieres: [Operating System, Java, C++]
sources: ["[[Commandes Shell + explications]]", "[[DM Shell Scripting]]", "[[Chp1 - Intro Java]]", "[[chp2 - structures code]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

Un tableau (array) stocke plusieurs éléments sous un seul nom, chacun accessible par son indice.

**En Bash** (Operating System) : on accède à un élément par `${names[0]}`. `read -a names` lit l'entrée comme un tableau, les éléments étant séparés par des espaces.

**En Java** : déclaration `type[] nom = new type[taille]`, matrices `new type[t1][t2]`, indices de 0 à taille − 1, initialisation par `{...}`, taille par `.length`.

**En C** : déclaration `int tab[10];` (type, nom, taille). Indices de 0 à taille − 1, éléments de même type, non initialisés à zéro. `int effectifs[6];` réserve 6 entiers contigus, d'adresses espacées de 4 octets. Le nom du tableau est l'adresse de sa première case ; passé à une fonction, le tableau est converti en cette adresse : `float *t`, `float t[]` et `float t[100]` sont équivalents (la taille est ignorée).

Notion parente : [[Variable Bash]]. Voir aussi : [[Commande read]], [[Boucle (programmation)]], [[Méthode main]], [[Arithmétique des pointeurs]], [[Pointeur et adresse mémoire]], [[Passage par valeur]].

## À vérifier

- Bash : l'exemple du cours lit `names` puis affiche `${name[0]}`, d'où un affichage vide (signalé par les résumés).
- Java : le cours écrit que `valeurs.length` vaut 4 pour un tableau de 5 éléments (à corriger avant un examen).
- C : le cours interdit `int n; int tab[n];` ; en C99, un tableau de taille variable est permis si `n` a une valeur (complément du résumé).

Résumés : [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]], [[Chp1 - Intro Java (résumé)]], [[chp2 - structures code (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
