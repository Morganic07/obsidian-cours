---
type: concept
tags: [year2]
aliases: [fork system call, copy-on-write, copie sur écriture]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]", "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]", "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"]
maj: 2026-11-08
---

Appel système qui crée un nouveau processus, copie du parent : même code, mêmes données, même mémoire. Valeur de retour :

- négative en cas d'erreur ;
- 0 dans le fils ;
- le PID du fils ($> 0$) dans le parent.

Les labs font un `switch` ou des `if` sur cette valeur. Le TP6 demande que le parent tire un nombre au hasard et le passe au fils : le tirage doit se faire avant le `fork()` (le fils hérite alors de la valeur) ou passer par un tube (`pipe`), car après le `fork()` père et fils ont chacun leur copie des variables globales. [[Erreurs du cours#^e-appel-fork|✎]]

**Compléments (hors du cours)** :

- `fork()` est **appelé une fois et revient deux fois** : une fois dans le parent (avec le PID du fils), une fois dans le fils (avec 0). Les deux processus reprennent ensuite à l'instruction qui suit l'appel.
- **Copie sur écriture** (*copy-on-write*) : le système ne recopie pas réellement la mémoire au moment du `fork()`. Parent et fils partagent les mêmes pages physiques, marquées en lecture seule, tant qu'aucun n'écrit ; une page n'est dupliquée qu'à sa première modification ([[Mémoire virtuelle]]). Un `fork()` suivi d'un `exec()` coûte donc très peu.
- Le fils **hérite des fichiers ouverts** du parent (mêmes descripteurs) : c'est ce qui permet au shell de relier deux commandes par un tube, en créant le `pipe()` avant le `fork()` ([[Redirection et tube]]).
- **Exercice classique** : $n$ appels `fork()` successifs, exécutés par tous les processus existants, donnent $2^n$ processus au total, dont $2^n - 1$ créés. Avec 3 appels : $2^3 = 8$ processus, 7 créés.

```c
fork();
fork();
fork();
printf("hello\n");   /* affiché 8 fois */
```

- Pour échanger des données entre parent et fils après le `fork()`, il faut un mécanisme de [[Communication interprocessus]] (tube, mémoire partagée…).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Appel exec()]], [[Appels wait() et waitpid()]], [[Identifiant de processus]], [[Communication interprocessus]], [[Mémoire virtuelle]].

Résumés : [[7 - OS]]
