---
type: concept
tags: [year4]
aliases: [buffer overflow, débordement de tampon, débordement de tableau, accès hors limites, out of bounds]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp7/7.4.c|7.4.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un dépassement de tampon (*buffer overflow*) est une écriture, ou par extension une lecture, au-delà des limites d'une zone mémoire ([[Tampon (buffer)|tampon]]) : typiquement, un [[Tableau (programmation)|tableau]] parcouru avec un indice trop grand ou négatif, ou une chaîne copiée dans un tableau trop petit.

```c
int t[5];
for (int i = 0; i <= 5; i++)   // erreur : i = 5 est hors du tableau
    t[i] = 0;                  // écrit dans la case qui suit t
char nom[8];
strcpy(nom, "Bonjour tout le monde");   // 22 octets dans 8
```

Le [[Langage C|C]] ne vérifie pas les indices : `t[i]` est calculé comme `*(t + i)` ([[Arithmétique des pointeurs]]), quelle que soit la valeur de `i`. Sortir du tableau est un [[Comportement indéfini|comportement indéfini]] : le programme peut sembler marcher, écraser silencieusement des variables voisines, planter plus loin par une [[Erreur de segmentation|erreur de segmentation]], ou se comporter différemment selon les [[Option de compilation|options de compilation]]. Les causes les plus fréquentes sont l'[[Erreur de décalage d'une unité|erreur de décalage d'une unité]] (`<=` au lieu de `<`), une taille passée en paramètre plus grande que le tableau, et les fonctions de [[Chaîne de caractères|chaînes]] qui ne connaissent pas la taille de la destination (`strcpy`, `gets`, `scanf("%s")`).

C'est aussi une **faille de sécurité** majeure : sur la [[Pile d'exécution|pile]], un tableau local qui déborde peut écraser l'adresse de retour de la fonction, et un attaquant qui contrôle les données écrites peut détourner l'exécution vers son propre code. Le ver Morris (1988), l'un des premiers vers d'Internet, exploitait ainsi un débordement dans le service `fingerd` d'[[Unix]]. Les systèmes actuels ajoutent des protections (canaris de pile, pile non exécutable, placement aléatoire des adresses), qui compliquent l'attaque sans corriger le bug.

Pour s'en prémunir :

- passer la taille des tableaux aux fonctions et la respecter ([[Décroissance d'un tableau en pointeur]]) ;
- préférer les fonctions bornées : `fgets` plutôt que `gets` (retirée en C11), `snprintf`, `scanf("%7s", nom)` ;
- détecter les débordements pendant les tests avec [[AddressSanitizer]] ou [[Valgrind]] ;
- en [[Langage C++|C++]], utiliser `std::vector` ([[Classe vector (C++)]]) et `std::string` ([[Classe string (C++)]]), dont la méthode `at(i)` vérifie l'indice et lève une exception.

Le [[Dépassement d'entier|dépassement d'entier]] est une autre notion : un calcul qui sort des bornes du type, pas un accès mémoire hors d'une zone.

## Dans le cours

- [[tp7]] : la fonction du programme 7.4 reçoit le tableau et sa taille ; écrire `tab[i]` avec `i >= taille_tab` serait un dépassement de tampon, que le C ne détecte pas.
- [[tableaux]] : la taille 100 écrite en dur dans les fonctions ; avec une taille en paramètre, une valeur trop grande ferait écrire hors du tableau.

Voir aussi : [[Comportement indéfini]], [[Erreur de segmentation]], [[Tableau (programmation)]], [[Pointeur pendant]].
