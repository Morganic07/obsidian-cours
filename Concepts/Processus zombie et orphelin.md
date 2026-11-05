---
type: concept
aliases: [zombie, zombie process, processus zombie, orphan process, processus orphelin, orphelin]
matieres: [Operating System]
sources: ["[[OS - chp7]]"]
maj: 2026-11-05
---

- **Zombie** : processus terminé, mais dont le parent n'a pas encore appelé `wait()` pour récupérer les informations de terminaison. Il occupe de la mémoire inutilement.
- **Orphelin** : processus qui continue de s'exécuter alors que son parent est terminé sans avoir appelé `wait()`. Le système le rattache en général à `init` (ou équivalent), qui devient son parent et le nettoie.

Liens : [[Création et terminaison de processus]], [[Processus]]

Résumé : [[OS - chp7 (résumé)]]
