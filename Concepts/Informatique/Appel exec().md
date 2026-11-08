---
type: concept
tags: [year2]
aliases: [exec(), execlp, execlp(), execvp, famille exec]
matieres: [Operating System]
sources: ["[[7 - OS|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

Appel système utilisé après `fork()` pour remplacer l'espace mémoire du processus par un nouveau programme. Exemple du cours, dans le fils : `execlp("/bin/ls","ls",NULL)`.

## Compléments (hors du cours)

- **Arguments de `execlp`** : le premier est le programme à lancer ; le `p` du nom indique qu'il est cherché dans les répertoires du `PATH` s'il ne contient pas de `/`. Viennent ensuite `argv[0]`, par convention le nom du programme (le `"ls"` de l'exemple), puis les autres arguments un par un, et enfin `NULL`, qui marque la fin de la liste. Le `l` signifie « liste d'arguments » ; les variantes en `v` (`execv`, `execvp`) prennent un tableau `argv`.
- **Un `exec()` réussi ne revient jamais** : le code de l'appelant est remplacé. Les instructions placées après l'appel ne s'exécutent donc qu'en cas d'échec (programme introuvable, droits insuffisants) ; on y met en général un message d'erreur puis `exit(1)` :

```c
execlp("ls", "ls", "-l", NULL);
perror("execlp");   /* atteint seulement si exec a échoué */
exit(1);
```

- **Ce qui est conservé** : le processus reste le même aux yeux du système. Son PID, son parent, son utilisateur et ses fichiers ouverts sont conservés ; seuls le code, les données et la pile sont remplacés par ceux du nouveau programme.
- **Le shell** exécute chaque commande ainsi : `fork()` crée un fils, le fils appelle `exec()` sur la commande, et le shell attend sa fin par `wait()`. Avec `&`, le shell n'attend pas et rend la main aussitôt (voir [[Tâche en arrière-plan]]).

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Appel fork()]], [[Appels wait() et waitpid()]], [[Identifiant de processus]], [[Shell et Bash]].

Résumés : [[7 - OS]]
