---
type: concept
tags: [year2]
aliases: [fork system call]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]", "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"]
maj: 2026-11-07
---

Appel système qui crée un nouveau processus, copie du parent : même code, mêmes données, même mémoire. Valeur de retour :

- négative en cas d'erreur ;
- 0 dans le fils ;
- le PID du fils ($> 0$) dans le parent.

Les labs font un `switch` ou des `if` sur cette valeur. Le TP6 demande que le parent passe un nombre au fils par une variable globale, ce qui ne marche pas après le `fork()` (voir « Erreurs du cours »).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Appel exec()]], [[Appels wait() et waitpid()]], [[Identifiant de processus]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]] (Task 5) écrit « The parent process generates a random number and passes it to the child process using a global variable » ; c'est impossible : après `fork()`, père et fils ont chacun leur copie des variables globales, et une valeur tirée par le père après le fork ne parvient pas au fils. Il faut tirer le nombre avant le `fork()`, ou le transmettre par un tube (`pipe`) (complément, hors du cours).

Résumés : [[7 - OS]]
