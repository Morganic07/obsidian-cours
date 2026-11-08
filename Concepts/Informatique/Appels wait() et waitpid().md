---
type: concept
tags: [year2]
aliases: [waitpid, wait(&status), WIFEXITED, WEXITSTATUS]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"]
maj: 2026-11-08
---

`pid = wait(&status)` : le parent attend la fin d'un enfant. L'appel renvoie le PID de l'enfant terminé et, dans `status`, la façon dont il s'est terminé.

Les labs testent `WIFEXITED(status)` et lisent `WEXITSTATUS(status)` ; ils attendent un enfant précis avec `waitpid(pid, &status, 0)`. Retirer le `wait` rend l'exécution simultanée (lab 8).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Processus zombie et orphelin]], [[Identifiant de processus]].

Dans le programme du TP4, `waitpid(pid, &status, 0)` suit la boucle infinie `while(1)` du parent : il n'est jamais atteint tant que le parent ne sort pas de la boucle. Il exige aussi la déclaration `int status;`.

Résumés : [[7 - OS]], [[4 - TP4]]
