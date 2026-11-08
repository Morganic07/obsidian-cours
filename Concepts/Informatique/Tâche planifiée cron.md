---
type: concept
tags:
  - year2
aliases:
  - cron
  - crontab
  - cron job
  - cron jobs
  - tâche cron
  - crontab -e
  - crontab -l
  - crontab -r
  - cron table
matieres:
  - Operating System
sources:
  - "[[4 - TP4|Cours TP4]]"
  - "[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Cours TP4.docx|Cours TP4]]"
maj: 2026-11-08
---

Cron est un ordonnanceur de tâches temporelles des systèmes de type Unix : il exécute des tâches à intervalles fixes, pour automatiser [[Sauvegarde de fichier|sauvegardes]], maintenance et scripts. Ses deux composants sont le [[Démon (informatique)|démon]] cron et la crontab (cron table).

Démarrage : `sudo systemctl start cron`, `enable` pour le lancer au boot, `status` pour vérifier (voir [[Commande systemctl]]). `crontab -e` édite la table de l'utilisateur (ne pas utiliser `sudo`, sinon c'est celle de root, voir [[Super-utilisateur root]]), `crontab -l` liste, `crontab -r` supprime tout.

Syntaxe : `minute heure jour-du-mois mois jour-de-semaine commande` (minute 0-59, heure 0-23, jour 1-31, mois 1-12, jour de semaine 0-6, dimanche = 0). Le sujet du TP4 compte « six fields » : les cinq champs de temps plus la commande ([[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands]]).

| Planification | Ligne |
|---|---|
| chaque minute | `* * * * *` |
| chaque heure pile | `0 * * * *` |
| toutes les 15 minutes | `*/15 * * * *` |
| lundi à 15 h | `0 15 * * 1` |
| le 1er du mois à 22 h 30 | `30 22 1 * *` |

L'intervalle minimal est 1 minute : cron ne sait pas lancer toutes les X secondes. `*/15` signifie « toutes les 15 unités » du champ.

## Compléments (hors du cours)

**Notations d'un champ** :

| Notation | Sens | Exemple |
|---|---|---|
| `a,b` | liste | `0 9 1,15 * *` : le 1er et le 15 du mois à 9 h |
| `a-b` | intervalle | `0 8 * * 1-5` : du lundi au vendredi à 8 h |
| `a-b/n` | intervalle avec un pas | `0 8-18/2 * * *` : à 8 h, 10 h, …, 18 h |

Dans le jour de la semaine, `7` vaut aussi dimanche. Si le jour du mois **et** le jour de la semaine sont tous deux restreints (aucun n'est `*`), la tâche tourne quand l'un **ou** l'autre correspond : `0 0 13 * 5` s'exécute chaque 13 du mois et chaque vendredi.

**Raccourcis** : `@reboot` (au démarrage), `@hourly` (`0 * * * *`), `@daily` (`0 0 * * *`), `@weekly` (`0 0 * * 0`), `@monthly` (`0 0 1 * *`), `@yearly` (`0 0 1 1 *`).

**Environnement** : cron lance les commandes avec un environnement minimal (`PATH=/usr/bin:/bin`, sans lire `.bashrc`) et depuis le répertoire personnel. D'où deux règles : utiliser des [[Chemin de fichier|chemins absolus]] pour les commandes et les fichiers, et rediriger la sortie pour garder une trace des erreurs ([[Redirection et tube]]) :

```
*/2 * * * * /home/user/backup.sh >> /home/user/backup.log 2>&1
```

**Journaux** : les exécutions apparaissent dans `/var/log/syslog` ou avec `journalctl -u cron` ([[Commande journalctl]]).

**Crontabs système** : `/etc/crontab` et les fichiers de `/etc/cron.d/` ont un champ de plus, l'utilisateur sous lequel lancer la commande, entre les champs de temps et la commande (`0 3 * * * root /usr/local/bin/sauvegarde.sh`). Les scripts déposés dans `/etc/cron.hourly/`, `/etc/cron.daily/`, `/etc/cron.weekly/` et `/etc/cron.monthly/` sont lancés à la fréquence indiquée.

**Alternative** : les timers de systemd (unités `.timer`, voir [[Commande systemctl]]) planifient aussi des tâches, avec une précision à la seconde.

**Exercices** : au TP4, cron sauvegarde `temperature.txt` ([[Raw/Year 2/Operating System/DM/TP4/TP4 - Pina Morgane.docx|TP4]], UNIX Commands - Semester report) ; au TP6, une tâche cron copie trois fichiers de `/home/First`, `/home/Second` et `/home/Third` vers `/home/Backup` toutes les 2 minutes ([[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment]]).

Voir aussi : [[Démon (informatique)]], [[Commande systemctl]], [[Sauvegarde de fichier]], [[Super-utilisateur root]], [[Script Bash]], [[Shell et Bash]]

Résumés : [[4 - TP4]]
