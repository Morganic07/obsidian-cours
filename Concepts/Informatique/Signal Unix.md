---
type: concept
tags: [year4]
aliases: [signal POSIX, SIGINT, SIGTSTP, Ctrl-C, Ctrl-Z]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : notification asynchrone envoyée par le noyau ou un autre processus à un [[Processus|processus]], qui interrompt son déroulement normal. Chaque signal a une action par défaut (terminer, suspendre, ignorer) qu'un programme peut parfois remplacer par un gestionnaire. Au terminal, **Ctrl-C** envoie `SIGINT` (interruption, termine le programme) et **Ctrl-Z** `SIGTSTP` (suspension : le programme reste en mémoire, `fg` le relance). `SIGKILL` (9) et `SIGTERM` (15) s'envoient avec [[Commande kill|`kill`]].

## Dans le cours

[[4 - Cours complet]] mentionne qu'on peut stopper un programme avec Ctrl-Z ou l'interrompre avec Ctrl-C, à côté de Ctrl-D qui signale la [[Fin de fichier|fin de la saisie]] (et n'est pas un signal).

Voir aussi : [[Commandes fg et bg]], [[Tâche en arrière-plan]].

Résumés : [[4 - Cours complet]]
