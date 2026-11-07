---
type: concept
tags: [year2]
aliases: [zombie, zombie process, processus zombie, orphan process, processus orphelin, orphelin]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]"]
maj: 2026-11-07
---

- **Zombie** : processus enfant terminé, mais dont le parent n'a pas encore appelé `wait()` (voir [[Appels wait() et waitpid()]]) pour récupérer les informations de terminaison. Selon le cours, il « occupe la mémoire inutilement ».
- **Orphelin** : processus qui continue de s'exécuter alors que son parent s'est terminé sans avoir appelé `wait()`. Le système le rattache en général à `init` ([[Processus init]]), ou équivalent, qui devient son parent et le nettoie.

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Processus]], [[Appels wait() et waitpid()]], [[Processus init]]

Résumé : [[7 - OS]]
