---
type: concept
tags: [year2]
aliases: [waitpid, wait(&status), WIFEXITED, WEXITSTATUS]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"]
maj: 2026-11-07
---

`pid = wait(&status)` : le parent attend la fin d'un enfant. L'appel renvoie le PID de l'enfant terminé et, dans `status`, la façon dont il s'est terminé.

Les labs testent `WIFEXITED(status)` et lisent `WEXITSTATUS(status)` ; ils attendent un enfant précis avec `waitpid(pid, &status, 0)`. Retirer le `wait` rend l'exécution simultanée (lab 8).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Processus zombie et orphelin]], [[Identifiant de processus]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/Cours OS/Cours TP4.docx|Cours TP4]] place `waitpid(pid, &status, 0);` juste après la boucle `while(1){ … }` du parent : l'appel n'est jamais atteint. Il faudrait sortir de la boucle (condition d'arrêt) avant d'attendre l'enfant.
- Rendu du TP4 (dans Raw/Year 2/Operating System/DM/TP4) : `waitpid(pid, &status, 0);` utilise `status` sans la ligne `int status;` du cours ; il faut la déclarer, sinon le programme ne compile pas.

Résumés : [[7 - OS]], [[4 - TP4]]
