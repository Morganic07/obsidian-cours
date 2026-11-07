---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/Cours TP4.docx|Cours TP4]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/Cours TP4.docx|Cours TP4]], dans [[Operating System (index)]]. Séance de TP en deux parties : un programme C à deux processus qui sauvegarde un fichier, puis la planification de tâches avec cron.

## Programme C à deux processus

*Consigne* : créer un programme C avec deux [[Processus|processus]] :
- le **parent** ajoute l'heure à un fichier toutes les 5 secondes ;
- le **fils** assure la [[Sauvegarde de fichier|sauvegarde]] de ce fichier en écrasant la sauvegarde précédente, toutes les 10 secondes.

Méthode :
1. `fork()` ([[Appel fork()]], [[Création et terminaison de processus]]) sépare les deux rôles selon le [[Identifiant de processus|pid]] renvoyé ;
2. le parent ouvre le fichier en mode ajout (`"a"`), y écrit `ctime(&current_time)`, le ferme, puis `sleep(5)` ;
3. le fils lance la commande shell `cp` grâce à `system()` ([[Fonction system() en C]]), puis `sleep(10)` ;
4. les deux tournent en boucle infinie `while(1)`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>

void append_current_date(char *filename) {
    FILE *file = fopen(filename, "a");
    time_t current_time = time(NULL);
    fprintf(file, "%s", ctime(&current_time));
    fclose(file);}

void copy_file() {
    system("cp /home/momo/data/time.txt /home/momo/backup/time.txt");
}

int main() {
    pid_t pid = fork();
    int status;
    if(pid==0){                // fils : sauvegarde toutes les 10 s
        while(1){
            copy_file();
            sleep(10);}}
    else if(pid>0){            // parent : ajoute l'heure toutes les 5 s
        while(1){
            append_current_date("time.txt");
            sleep(5);
        } waitpid(pid, &status, 0);}
    return 0;}
```

Voir aussi [[Appels wait() et waitpid()]] et [[Structure conditionnelle]].

## Cron

[[Tâche planifiée cron|Cron]] est un [[Ordonnancement des processus|ordonnanceur]] de tâches fondé sur le temps, dans les [[Système d'exploitation|systèmes]] de type Unix dont [[Ubuntu]]. Il permet de programmer des tâches (*cron jobs*) qui s'exécutent automatiquement à intervalles donnés. On s'en sert pour automatiser des tâches répétitives : sauvegardes, maintenance, scripts. C'est un [[Démon (informatique)|démon]] géré par [[Commande systemctl|systemctl]].

### Commandes

```bash
sudo systemctl start cron     # démarrer cron
sudo systemctl enable cron    # le démarrer automatiquement au boot
sudo systemctl status cron    # voir si cron tourne
crontab -e                    # éditer la table des tâches
crontab -l                    # vérifier les tâches planifiées
crontab -r                    # supprimer toutes les tâches
```

Ne pas lancer `crontab -e` avec `sudo` : on éditerait la table du [[Super-utilisateur root|super-utilisateur root]] et non celle de l'utilisateur courant.

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

`*/15` signifie « toutes les 15 unités » du champ concerné.

### Exemples

| Tâche | Ligne cron |
|---|---|
| Lancer un script toutes les minutes | `* * * * * /home/user/scripts/backup.sh` |
| Toutes les heures, à l'heure pile | `0 * * * * /home/user/scripts/backup.sh` |
| Toutes les 15 minutes | `*/15 * * * * /home/user/scripts/cleanup.sh` |
| Chaque lundi à 15 h | `0 15 * * 1 /home/user/scripts/weekly_report.sh` |
| À 22 h 30 le premier jour de chaque mois | `30 22 1 * * /home/user/scripts/monthly_report.sh` |
| Envoyer un mail chaque vendredi à 8 h | `0 8 * * 5 echo "Weekly report" \| mail -s "Report" user@example.com` |

Par défaut, cron ne permet pas de lancer une tâche toutes les X secondes : l'intervalle minimal est **1 minute**.

### Créer une tâche

1. `crontab -e` ;
2. à la fin du fichier ouvert dans l'éditeur, ajouter la ligne de la tâche ;
3. sauvegarder et fermer : la tâche est planifiée.

![[Séance TP4 - image1.png]]
*Figure : crontab ouverte dans [[Éditeur nano|GNU nano]] 7.2 : les commentaires d'aide (champs m h dom mon dow command, exemple `0 5 * * 1 tar -zcf /var/backups/home.tgz /home/`), puis la tâche ajoutée `* * * * * cp /home/momo/data/temperature.txt /home/momo/backup/temperature.txt` (copie chaque minute).*

Les commentaires de la crontab rappellent aussi que les tâches suivent l'heure et le fuseau du démon cron, et que leur sortie (erreurs comprises) est envoyée par mail au propriétaire de la crontab, sauf redirection.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`waitpid(pid, &status, 0)`** placé après une boucle infinie `while(1)` dans le parent : il n'est jamais atteint (complément). Le chemin relatif `"time.txt"` dépend du dossier de lancement.
2. **Fichier `time.txt` et dossier de sauvegarde** : le programme ne crée pas les dossiers `data` et `backup` ; ils doivent exister avant.
3. **Mention « Dimanche = 0 »** : en cron, 0 et 7 désignent tous deux dimanche (complément).
4. **Chemins incohérents** : le parent écrit dans `time.txt` du répertoire courant, le fils copie `/home/momo/data/time.txt` ; la sauvegarde ne porte sur le bon fichier que si le programme est lancé depuis `/home/momo/data` (complément).
