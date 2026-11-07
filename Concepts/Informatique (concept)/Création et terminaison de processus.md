---
type: concept
tags: [year2]
aliases: [fork, fork(), wait(), process creation, process termination, création de processus, cascading termination, exit(), abort()]
matieres: [Operating System]
sources: ["[[OS - chp 7 (résumé)|OS - chp7]]", "[[Copy of 08 Processes-TP (résumé)|Copy of 08 Processes-TP]]", "[[Séance TP4 (résumé)|Cours TP4]]", "[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"]
maj: 2026-11-06
---

**Création** : un processus parent crée des fils, qui en créent d'autres, ce qui forme un [[Arbre de processus]] (chacun identifié par son [[Identifiant de processus|PID]]). Trois choix à faire : partage des ressources (tout, un sous-ensemble, rien), exécution (parent et fils en parallèle, ou le parent attend), espace d'adressage (le fils duplique le parent avec `fork()`, ou un programme est chargé dedans avec [[Appel exec()|exec()]]).

Exemple UNIX : `fork()` crée le processus ; dans le fils (`pid == 0`), [[Appel exec()|exec()]] remplace la mémoire par un nouveau programme ; le parent (`pid > 0`) appelle `wait()`. Une valeur négative signale une erreur.

**Terminaison** : le processus finit par `exit()`, renvoie un statut au parent (lu via `wait(&status)`) et le système libère ses ressources. Le parent peut tuer un fils avec `abort()` (ressources dépassées, tâche inutile, parent qui s'arrête). Certains systèmes interdisent à un fils de survivre à son parent : c'est la *cascading termination*, où fils, petits-fils, etc. sont tous terminés.

Un fils qui n'est pas attendu devient un [[Processus zombie et orphelin]].

Après `fork`, le père et le fils ont chacun leur copie de la mémoire : une variable globale modifiée dans l'un ne change pas dans l'autre (tâche 5 du TP6).

Notion parente : [[Processus]]. Voir aussi : [[Arbre de processus]], [[Appel exec()]], [[Identifiant de processus]], [[Processus zombie et orphelin]], [[Processus init]], [[Appel système]]

Résumés : [[OS - chp 7 (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[Séance TP4 (résumé)]], [[TP4-Unix Commands (résumé)]], [[TP4 (résumé)]], [[TP6-Assignment (résumé)]], [[Operating Systems - Semester report (résumé)]], [[UNIX Commands - Semester report (résumé)]]
