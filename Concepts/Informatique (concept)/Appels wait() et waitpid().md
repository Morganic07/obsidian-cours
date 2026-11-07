---
type: concept
tags: [year2]
aliases: [waitpid, wait(&status), WIFEXITED, WEXITSTATUS]
matieres: [Operating System]
sources: ["[[7 - OS (résumé)|OS - chp7]]", "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"]
maj: 2026-11-06
---

`pid = wait(&status)` : le parent attend la fin d'un enfant. L'appel renvoie le PID de l'enfant terminé et, dans `status`, la façon dont il s'est terminé.

Les labs testent `WIFEXITED(status)` et lisent `WEXITSTATUS(status)` ; ils attendent un enfant précis avec `waitpid(pid, &status, 0)`. Retirer le `wait` rend l'exécution simultanée (lab 8).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Processus zombie et orphelin]], [[Identifiant de processus]].

## À vérifier

TP4 : `waitpid` est placé après une boucle infinie, donc jamais atteint ; dans le rendu, `status` n'est pas déclaré (signalé par les résumés).

Résumés : [[7 - OS (résumé)]], [[4 - TP4 (résumé)]]
