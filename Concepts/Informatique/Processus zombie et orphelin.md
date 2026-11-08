---
type: concept
tags: [year2]
aliases: [zombie, zombie process, processus zombie, orphan process, processus orphelin, orphelin, defunct]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

- **Zombie** : processus enfant terminé, mais dont le parent n'a pas encore appelé `wait()` (voir [[Appels wait() et waitpid()]]) pour récupérer les informations de terminaison. Selon le cours, il « occupe la mémoire inutilement ».
- **Orphelin** : processus qui continue de s'exécuter alors que son parent s'est terminé sans avoir appelé `wait()`. Le système le rattache en général à `init` ([[Processus init]]), ou équivalent, qui devient son parent et le nettoie.

## Compléments (hors du cours)

- **Ce que garde un zombie** : sa mémoire et ses fichiers ouverts sont déjà libérés. Il ne conserve que son entrée dans la table des processus : PID, code de retour, temps CPU consommé, que le parent lira avec `wait()`.
- **Le vrai risque** : un zombie seul coûte peu. Le problème vient d'un parent qui en accumule sans jamais appeler `wait()` : les entrées occupées finissent par épuiser les PID disponibles, et plus aucun processus ne peut être créé.
- **Repérage** : `ps` affiche l'état `Z` et la mention `<defunct>` à côté du nom.
- **Suppression** : `kill` est sans effet, puisque le processus est déjà terminé (voir [[Commande kill]]). Le zombie disparaît quand son parent appelle `wait()`, ou quand le parent se termine : le zombie, devenu orphelin, est adopté par `init` (`systemd` sur la plupart des distributions actuelles), qui appelle `wait()` et le nettoie.

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Processus]], [[Appels wait() et waitpid()]], [[Processus init]], [[États d'un processus]], [[Identifiant de processus]]

Résumé : [[7 - OS]]
