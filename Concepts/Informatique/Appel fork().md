---
type: concept
tags: [year2]
aliases: [fork system call]
sources: ["[[OS - chp7]]", "[[Copy of 08 Processes-TP]]", ".raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf"]
maj: 2026-11-06
---

Appel système qui crée un nouveau processus, copie du parent : même code, mêmes données, même mémoire. Valeur de retour :

- négative en cas d'erreur ;
- 0 dans le fils ;
- le PID du fils ($> 0$) dans le parent.

Les labs font un `switch` ou des `if` sur cette valeur. Dans le TP6, le parent passe un nombre au fils par une variable globale.

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Appel exec()]], [[Appels wait() et waitpid()]], [[Identifiant de processus]].

## À vérifier

Après `fork()`, père et fils ont chacun leur copie des variables globales : une valeur tirée par le père après le fork ne parvient pas au fils (complément du résumé du TP6).

Résumés : [[OS - chp7 (résumé)]], [[Copy of 08 Processes-TP (résumé)]], [[TP6-Assignment (résumé)]], [[UNIX Commands - Semester report (résumé)]]
