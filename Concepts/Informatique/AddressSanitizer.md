---
type: concept
tags: [year4]
aliases: [ASan, "-fsanitize=address", sanitizer d'adresses, LeakSanitizer]
sources: ["[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex3.c|ex3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : AddressSanitizer (ASan) est un outil de détection des erreurs mémoire développé par Google et intégré aux compilateurs [[Clang]] et [[GCC]]. On l'active par l'[[Option de compilation|option de compilation]] `-fsanitize=address`, avec `-g` pour que les rapports donnent les numéros de ligne du [[Code source|code source]] :

```bash
gcc -g -fsanitize=address ex3.c -o ex3
./ex3
```

Le [[Compilateur|compilateur]] instrumente chaque accès mémoire de l'[[Exécutable|exécutable]] ; à l'exécution, le programme s'arrête au premier accès fautif avec un rapport qui donne la ligne en cause, le type d'erreur et l'endroit où le bloc a été alloué ou libéré. Il détecte notamment :

- les [[Dépassement de tampon|dépassements de tampon]] sur la [[Pile d'exécution|pile]], le [[Espace mémoire d'un processus|tas]] et les variables globales ;
- l'utilisation d'un bloc après `free` (*use after free*, voir [[Pointeur pendant]]) et la double libération ;
- à la fin du programme, les [[Fuite mémoire|fuites mémoire]], grâce à LeakSanitizer, qui lui est associé (activé par défaut sous [[Linux]]).

Le surcoût est modéré, environ un facteur 2 en temps d'exécution d'après la documentation du projet, ce qui permet de l'utiliser pendant tout le développement et dans les [[Test unitaire|tests]]. Il ne voit que les erreurs effectivement commises pendant l'exécution testée : un chemin du programme qui n'est pas parcouru n'est pas vérifié. Il ne détecte pas non plus la lecture d'une [[Variable non initialisée|variable non initialisée]] (c'est le rôle de MemorySanitizer, propre à Clang, ou de [[Valgrind]]).

Contrairement à [[Valgrind]], qui exécute le programme sans le recompiler, ASan demande de recompiler, mais il est bien plus rapide. Les deux outils complètent le [[Débogueur|débogueur]] pour traquer le [[Comportement indéfini|comportement indéfini]] en [[Langage C|C]] et en [[Langage C++|C++]].

## Dans le cours

- [[td listes chaînées]] : `gcc -fsanitize=address` a signalé les fuites de `ex3.c` (48 octets en 3 blocs) et de `ex4.c` (32 octets en 2 blocs), dont les chaînons alloués par `malloc` n'étaient jamais libérés ; la fiche recommande de compiler avec `-g -fsanitize=address` pour vérifier qu'aucun bloc n'est oublié.

Voir aussi : [[Valgrind]], [[Fuite mémoire]], [[Allocation dynamique]], [[Erreur de segmentation]].
