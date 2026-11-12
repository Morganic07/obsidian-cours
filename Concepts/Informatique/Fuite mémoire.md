---
type: concept
tags: [year4]
aliases: [fuites mémoire, fuite de mémoire, memory leak, memory leaks]
sources: ["[[Raw/Year 4/C／C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une fuite mémoire se produit quand un bloc alloué dynamiquement (`malloc` en C, `new` en C++) n'est jamais libéré alors que le programme a perdu son adresse. Le bloc reste réservé sur le tas mais devient inaccessible : il ne pourra plus être ni utilisé ni libéré jusqu'à la fin du processus, où le système d'exploitation récupère toute la mémoire.

Causes typiques :

- un `free` (ou `delete`) oublié ;
- un pointeur écrasé par une autre adresse avant la libération (`p = malloc(…); p = malloc(…);` perd le premier bloc) ;
- une sortie anticipée d'une fonction (`return` dans un cas d'erreur, exception en C++) qui saute le `free` ;
- une structure chaînée dont on ne libère que la tête.

Conséquence : dans un programme qui tourne longtemps (serveur, démon, jeu), la mémoire occupée croît sans cesse jusqu'à ralentir la machine ou faire échouer les allocations (`malloc` renvoie alors `NULL`).

Détection : des outils comme Valgrind (`valgrind --leak-check=full ./prog`) ou l'option `-fsanitize=address` de [[GCC]] signalent les blocs non libérés à la fin de l'exécution.

En C++, on les évite en confiant la mémoire à un objet qui la libère dans son destructeur (principe RAII) : conteneurs de la bibliothèque standard (`std::vector`, `std::string`) et pointeurs intelligents (`std::unique_ptr`, `std::shared_ptr`). Java, lui, libère automatiquement les objets inaccessibles grâce au ramasse-miettes (*garbage collector*).

## Dans le cours

Le cours ne nomme pas la notion. [[3 - pointeurs , tableaux, listes chainées, structures]] pose la règle « après chaque malloc, toujours free » et donne un exemple de liste chaînée qui ne libère pas ses chaînons ; la fiche montre en complément comment les libérer en parcourant la liste, en sauvegardant `suivant` avant chaque `free`.

- [[td listes chaînées]] : `ex3.c` et `ex4.c` ne libéraient pas leurs chaînons (48 octets en 3 blocs pour `ex3.c`), fuites détectées par [[AddressSanitizer]] (`gcc -fsanitize=address`) puis corrigées par une boucle de libération ; [[Valgrind]] donne le même diagnostic.

Voir aussi : [[Allocation dynamique]], [[Pointeur pendant]], [[Liste chaînée]], [[Espace mémoire d'un processus]], [[Langage C++]].

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
