---
type: concept
tags: [year2]
aliases: [kill %1, kill -9, SIGTERM, SIGKILL]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/DM/TP3/TP3 - PINA Morgane.docx|TP3]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

Dans les rendus des TP3 et TP4, les tâches de fond sont arrêtées par `kill %n`, où `n` est le numéro de la tâche (`kill %1; kill %2`).

## Compléments (hors du cours)

- **Rôle** : `kill` envoie un signal à un processus, désigné par son PID (`kill 1234`) ou, dans le shell, par son numéro de tâche (`kill %1`).
- **Signal par défaut** : `SIGTERM` (15), qui demande l'arrêt et laisse au processus le temps de nettoyer (fermer ses fichiers, enregistrer son état) ; il peut l'intercepter ou l'ignorer. `kill -9` envoie `SIGKILL` (9), qui impose l'arrêt immédiat et ne peut être ni intercepté ni ignoré.
- **En C** : l'appel système `kill(pid, signal)` fait la même chose. C'est ainsi qu'un parent UNIX termine un de ses fils, ce que le chapitre 7 appelle de façon générique « abort() ». La fonction C `abort()`, elle, arrête le processus qui l'appelle (en lui envoyant `SIGABRT`).
- **Sur un zombie** : sans effet, puisque le processus est déjà terminé (voir [[Processus zombie et orphelin]]).

Notion parente : [[Tâche en arrière-plan]]. Voir aussi : [[Commande jobs]], [[Processus]], [[Identifiant de processus]], [[Création et terminaison de processus]].

Résumés (rapprochement, complément hors du cours) : [[2 - TP2]], [[7 - OS]]
