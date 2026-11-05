---
type: concept
aliases: [fork, fork(), exec(), wait(), process creation, process termination, création de processus, arbre de processus, cascading termination]
matieres: [Operating System]
sources: ["[[OS - chp7]]", "[[Copy of 08 Processes-TP]]"]
maj: 2026-11-05
---

**Création** : un processus parent crée des fils, qui en créent d'autres, ce qui forme un arbre de processus (chacun identifié par son PID). Trois choix à faire : partage des ressources (tout, un sous-ensemble, rien), exécution (parent et fils en parallèle, ou le parent attend), espace d'adressage (le fils duplique le parent avec `fork()`, ou un programme est chargé dedans avec `exec()`).

Exemple UNIX : `fork()` crée le processus ; dans le fils (`pid == 0`), `exec()` remplace la mémoire par un nouveau programme ; le parent (`pid > 0`) appelle `wait()`. Une valeur négative signale une erreur.

**Terminaison** : le processus finit par `exit()`, renvoie un statut au parent (lu via `wait(&status)`) et le système libère ses ressources. Le parent peut tuer un fils avec `abort()` (ressources dépassées, tâche inutile, parent qui s'arrête). Certains systèmes interdisent à un fils de survivre à son parent : c'est la *cascading termination*, où fils, petits-fils, etc. sont tous terminés.

Un fils qui n'est pas attendu devient un [[Processus zombie et orphelin]].

Liens : [[Processus]], [[Appel système]], [[Processus zombie et orphelin]]

Résumé : [[OS - chp7 (résumé)]]
