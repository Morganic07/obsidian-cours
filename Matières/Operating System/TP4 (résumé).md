---
type: source
tags: [year2]
sources: ["TP4 du dossier DM/TP4"]
maj: 2026-11-06
complet: true
---

Résumé de la note TP4 du dossier `DM/TP4` de [[Operating System (matière)]] (la note porte le nom de l'étudiante, d'où l'absence de lien direct). Version rendue de [[Cours TP4]] (voir [[Séance TP4 (résumé)]]) : un programme C à deux processus, puis la planification avec [[Tâche planifiée cron|cron]]. Une seule image, du texte, recopiée ci-dessous.

## Programme C à deux processus

Même consigne que dans [[Séance TP4 (résumé)]] : le parent ajoute l'heure à `time.txt` toutes les 5 secondes, le fils sauvegarde le fichier toutes les 10 secondes ([[Création et terminaison de processus]], [[Appel fork()]]).

Différence avec la version du cours : la copie construit la commande `cp` dans une chaîne avec `snprintf`, puis la passe à `system()` ([[Fonction system() en C]]), ce qui permet de passer la source et la destination en paramètres.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void append_current_date(char *filename) {
    FILE *file = fopen(filename, "a");
    time_t current_time = time(NULL);
    fprintf(file, "%s", ctime(&current_time));
    fclose(file);
}

void copy_file(const char *source, const char *destination) {
    char command[256];
    snprintf(command, sizeof(command), "cp %s %s", source, destination);
    system(command);
}

int main() {
    pid_t pid = fork();
    if(pid==0){                    // fils : copie toutes les 10 s
        while(1){
            copy_file("/home/momo/data/time.txt" , "/home/momo/data/backup");
            sleep(10);
        }}
    else{                          // parent : ajoute l'heure toutes les 5 s
        while(1){
            append_current_date("time.txt");
            sleep(5);
        }}
    waitpid(pid, &status, 0);      // voir point à vérifier 1
    return 0;
}
```

Voir [[Identifiant de processus]], [[Appels wait() et waitpid()]], [[Sauvegarde de fichier]].

## Utiliser cron

```bash
sudo systemctl start cron     # démarrer cron
sudo systemctl enable cron    # le démarrer automatiquement au boot
sudo systemctl status cron    # vérifier qu'il a bien démarré
crontab -e                    # éditer la table des tâches
crontab -l                    # vérifier les tâches planifiées
crontab -r                    # supprimer toutes les tâches
```

Voir [[Commande systemctl]] et [[Commande sudo]]. Ne pas lancer `crontab -e` avec `sudo` : on éditerait la table du [[Super-utilisateur root|super-utilisateur root]], pas celle de l'utilisateur courant.

### Syntaxe d'une tâche

```
* * * * * /chemin/vers/la/commande
┬ ┬ ┬ ┬ ┬
│ │ │ │ │
│ │ │ │ └── Jour de la semaine (0 - 6) (Dimanche = 0)
│ │ │ └──── Mois (1 - 12)
│ │ └────── Jour du mois (1 - 31)
│ └──────── Heure (0 - 23)
└───────── Minute (0 - 59)
```

Réponses aux questions (image de la note) :
1. `* * * * *` : la commande s'exécute toutes les minutes ;
2. par défaut, cron ne permet pas de lancer une tâche toutes les `x` secondes, car son intervalle minimal est d'une minute.

### Tâche 2 : sauvegarder `temperature.txt`

```
* * * * * cp /home/user/data/temperature.txt /home/user/backup/temperature.txt      # toutes les minutes
*/3 * * * * cp /home/user/data/temperature.txt /home/user/backup/temperature.txt    # toutes les 3 minutes
0 2 * * * cp /home/user/data/temperature.txt /home/user/backup/temperature.txt      # chaque jour à 2 h
```

`*/3` signifie « toutes les 3 unités » du champ concerné. (Les commentaires de fin de ligne sont ajoutés ici pour la lecture ; la note donne les trois lignes seules.)

### Autres exemples

| Tâche | Ligne cron |
|---|---|
| Toutes les heures, à l'heure pile | `0 * * * * /home/user/scripts/backup.sh` |
| Toutes les 15 minutes | `*/15 * * * * /home/user/scripts/cleanup.sh` |
| Chaque lundi à 15 h | `0 15 * * 1 /home/user/scripts/weekly_report.sh` |
| À 22 h 30 le premier jour de chaque mois | `30 22 1 * * /home/user/scripts/monthly_report.sh` |
| Mail chaque vendredi à 8 h | `0 8 * * 5 echo "Weekly report" \| mail -s "Report" user@example.com` |

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Le programme C ne compile pas tel quel** : `waitpid` est appelé avec `status` non déclaré et sans `<sys/wait.h>` (complément) ; de plus il est inatteignable après la boucle infinie. Le même programme dans [[Cours TP4]] déclare `status`.
2. **Syntaxe `const` en italique** (`*const* char`) : mise en forme Markdown parasite dans la note, à lire `const char *`.
3. **Dossier de destination** : `/home/momo/data/backup` ici, `/home/momo/backup` ailleurs ; le dossier doit exister avant la copie.
4. **Correspondance des tâches** : la note ne recopie pas l'énoncé de la tâche 2 ; l'interprétation des trois lignes (chaque minute, toutes les 3 minutes, chaque jour à 2 h) est celle de l'ancien résumé, déduite de la syntaxe.
