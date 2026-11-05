---
type: source
sources: ["TP4 du dossier DM/TP4"]
maj: 2026-11-05
---

Résumé de la note TP4 du dossier `DM/TP4` de [[Year 2 - Operating System]] (la note porte le nom de l'étudiant, d'où l'absence de lien direct).

## Ce qu'apprend le TP

Même contenu que [[Cours TP4]] : un programme C avec `fork()` (parent écrit l'heure, fils sauvegarde), puis la planification avec [[Tâche planifiée cron]]. Cette version écrit la copie par `snprintf` + `system("cp ...")` et ajoute la tâche 2 : sauvegarder `temperature.txt` toutes les minutes (`* * * * *`), toutes les 3 minutes (`*/3 * * * *`) ou chaque jour à 2 h (`0 2 * * *`).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Le programme C ne compile pas tel quel** : `waitpid` est appelé avec `status` non déclaré et sans `<sys/wait.h>` (complément) ; de plus il est inatteignable après la boucle infinie. Le même programme dans [[Cours TP4]] déclare `status`.
2. **Syntaxe `const` en italique** (`*const* char`) : mise en forme Markdown parasite dans la note, à lire `const char *`.
3. **Dossier de destination** : `/home/momo/data/backup` ici, `/home/momo/backup` ailleurs ; le dossier doit exister avant la copie.
