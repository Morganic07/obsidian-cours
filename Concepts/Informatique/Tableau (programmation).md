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
  - C／C++
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[Raw/Year 4/C／C++/chp2 - structures code .docx|chp2 - structures code]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]"
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un tableau (array) stocke plusieurs éléments sous un seul nom, chacun accessible par son indice. Dans les langages compilés comme le C ou Java, les éléments sont de même type et rangés dans des cases contiguës, ce qui rend l'accès à une case quelconque immédiat, en temps constant.

**En Bash** (Operating System) : on accède à un élément par `${names[0]}`. `read -a names` lit l'entrée comme un tableau, les éléments étant séparés par des espaces ; `echo "names: ${names[0]}, ${names[1]}"` affiche ensuite les deux premiers. [[Erreurs du cours#^e-tableau-programmation|✎]]

**En Java** : déclaration `type[] nom = new type[taille]`, matrices `new type[t1][t2]`, indices de 0 à taille − 1, initialisation par `{...}`, taille par `.length` : pour `int valeurs[] = { 5, 2, 4, 8, 9};`, `valeurs.length` vaut 5. [[Erreurs du cours#^e-tableau-programmation|✎]]

Complément, hors du cours : un tableau créé par `new` est rempli de valeurs par défaut (`0`, `false`, `null`) ; sa taille est fixée à la création. Un indice hors bornes lève une `ArrayIndexOutOfBoundsException`, contrairement au C qui ne vérifie rien. Un tableau est un objet : `int[] b = a;` copie la référence, et `a` et `b` désignent alors le même tableau ; pour copier le contenu, `a.clone()` ou `Arrays.copyOf(a, a.length)`. `System.out.println(a)` affiche une adresse codée ; `Arrays.toString(a)` affiche les éléments. Une matrice est un tableau de tableaux, dont les lignes peuvent avoir des longueurs différentes. Parcours par `for (int i = 0; i < t.length; i++)` ou par la boucle for-each `for (int v : t)`.

**En C** : déclaration `int tab[10];` (type, nom, taille). Indices de 0 à taille − 1, éléments de même type, non initialisés à zéro. `int effectifs[6];` réserve 6 entiers contigus, d'adresses espacées de 4 octets. Le nom du tableau est l'adresse de sa première case ; passé à une fonction, le tableau est converti en cette adresse : `float *t`, `float t[]` et `float t[100]` sont équivalents (la taille est ignorée). La taille n'a pas à être écrite en dur : depuis la norme C99, `int n = 10; int tab[n];` déclare un tableau de taille variable, à condition que `n` ait reçu une valeur. [[Erreurs du cours#^e-tableau-programmation|✎]]

Complément, hors du cours :

- Initialisation par accolades : `int tab[5] = {4, 8, 15, 16, 23};`. Les cases non citées valent 0, donc `int tab[10] = {0};` met tout à zéro. Avec une liste, la taille peut être omise : `int tab[] = {1, 2, 3};` a 3 cases.
- Aucun contrôle des indices : `tab[10]` sur un tableau de 10 cases lit ou écrit hors du tableau, ce qui est un comportement indéfini (corruption de variables voisines, [[Erreur de segmentation]], faille de type *buffer overflow*). Erreur fréquente : `for (i = 0; i <= 10; i++)` au lieu de `i < 10`.
- Nombre de cases : `sizeof(tab) / sizeof(tab[0])`, valable seulement là où le tableau est déclaré. Dans une fonction qui le reçoit, `sizeof` donne la taille d'un pointeur : il faut passer la taille en paramètre (`void afficher(int t[], int n)`).
- Pas d'affectation en bloc : `t1 = t2;` est refusé ; on copie case par case ou avec `memcpy`.
- Une chaîne de caractères est un tableau de `char` terminé par le caractère nul `'\0'` : `char mot[] = "abc";` occupe 4 cases.
- Tableau à deux dimensions : `int m[3][4];` (3 lignes de 4 colonnes, rangées ligne après ligne en mémoire), case `m[i][j]`.

**Grille 2D dans un tableau 1D** (C++, exercice `Maze` de [[4 - C++]]) : un labyrinthe de 21 colonnes sur 12 lignes est rangé dans `int tableau[21*12];`. Pour l'afficher en grille, on passe à la ligne quand l'indice est un multiple du nombre de colonnes, avec `if (i % 21 == 0)`. [[Erreurs du cours#^e-tableau-programmation|✎]] Complément, hors du cours : la case de ligne `l` et de colonne `c` est à l'indice `l * 21 + c`.

Notion parente : [[Variable Bash]]. Voir aussi : [[Commande read]], [[Boucle (programmation)]], [[Méthode main]], [[Arithmétique des pointeurs]], [[Pointeur et adresse mémoire]], [[Passage par valeur]], [[Langage Java]], [[Langage C]].

## Dans le cours

- [[tp3]] : le minimum de trois nombres se généralise à un tableau parcouru par une boucle ; les messages du `switch` sur la magnitude (3.11) pourraient être rangés dans un tableau de chaînes.
- [[tp4]] : l'idiome `for (i = 0; i < N; i++)` part de 0 comme les indices d'un tableau ; `<=` au lieu de `<` est l'[[Erreur de décalage d'une unité|erreur de décalage d'une unité]].
- [[tp5]] : le [[Crible d'Ératosthène|crible d'Ératosthène]], alternative au programme 5.6, repose sur un tableau de $N+1$ cases.
- [[tp7]] : remplissage par `scanf`, recherche du minimum et du maximum, passage à une fonction avec la taille en paramètre, modification en place (7.4) ; `int tab[10];` ne l'initialise pas.
- [[tableaux]] : les deux écritures du § 7 de [[3 - pointeurs , tableaux, listes chainées, structures]], `t[i]` et `*(t+i)` ([[Décroissance d'un tableau en pointeur]]).
- [[td listes chaînées]] : comparaison avec la [[Liste chaînée|liste chaînée]], dont le comptage coûte $O(n)$ alors qu'un tableau connaît sa taille.

Résumés : [[8 - OS commandes sh]], [[1 - Intro Java]], [[2 - structures code]], [[3 - pointeurs , tableaux, listes chainées, structures]], [[4 - C++]]
