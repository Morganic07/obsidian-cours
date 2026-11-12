---
type: concept
tags: [year4]
aliases: [Memcheck, valgrind --leak-check]
sources: ["[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/tous_les_exo.c|tous_les_exo.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : Valgrind est un [[Logiciel libre|logiciel libre]] d'analyse dynamique de programmes, créé par Julian Seward (première version publique en 2002), surtout utilisé sous [[Linux]]. Il exécute le programme sur un processeur virtuel et observe chacune de ses instructions, sans qu'il soit nécessaire de le recompiler ; compiler avec `-g` lui permet seulement de donner les numéros de ligne.

Son outil par défaut, **Memcheck**, signale :

- les lectures de mémoire [[Variable non initialisée|non initialisée]] qui influencent le programme (un test, un affichage) ;
- les accès en dehors des blocs alloués par `malloc` ([[Dépassement de tampon]]) et après `free` ([[Pointeur pendant]]) ;
- les libérations incorrectes : double `free`, `free` d'une adresse non allouée, `delete` sur un bloc obtenu par `malloc` ;
- à la fin de l'exécution, les [[Fuite mémoire|fuites mémoire]], avec la pile d'appels de l'allocation fautive si l'on ajoute `--leak-check=full`.

```bash
gcc -g programme.c -o programme
valgrind --leak-check=full ./programme
# ==1234== definitely lost: 48 bytes in 3 blocks
```

Le prix est la lenteur : d'après le guide de démarrage du projet, le programme tourne environ 20 à 30 fois moins vite sous Memcheck. D'autres outils de la suite mesurent le cache (Cachegrind), les appels de fonctions (Callgrind) ou détectent les conflits entre [[Thread|threads]] (Helgrind).

[[AddressSanitizer]] couvre un champ voisin, beaucoup plus vite, mais demande de recompiler ; Valgrind détecte en plus les lectures de mémoire non initialisée. Les deux complètent le [[Débogueur|débogueur]] dans la chasse au [[Comportement indéfini|comportement indéfini]] en [[Langage C|C]] et en [[Langage C++|C++]].

## Dans le cours

- [[td listes chaînées]] : cité, avec AddressSanitizer, comme moyen de vérifier qu'aucun chaînon n'est oublié (`valgrind --leak-check=full ./prog`) après les fuites de `ex3.c` et `ex4.c`.

Voir aussi : [[AddressSanitizer]], [[Fuite mémoire]], [[Allocation dynamique]], [[Débogueur]].
