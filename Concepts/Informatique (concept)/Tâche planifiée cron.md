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
  - "[[4 - TP4 (résumé)|Cours TP4]]"
  - "[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"
maj: 2026-11-06
---

Cron est un ordonnanceur de tâches temporelles des systèmes de type Unix : il exécute des tâches à intervalles fixes, pour automatiser [[Sauvegarde de fichier|sauvegardes]], maintenance et scripts. Ses deux composants sont le [[Démon (informatique)|démon]] cron et la crontab (cron table).

Démarrage : `sudo systemctl start cron`, `enable` pour le lancer au boot, `status` pour vérifier (voir [[Commande systemctl]]). `crontab -e` édite la table de l'utilisateur (ne pas utiliser `sudo`, sinon c'est celle de root, voir [[Super-utilisateur root]]), `crontab -l` liste, `crontab -r` supprime tout.

Syntaxe : `minute heure jour-du-mois mois jour-de-semaine commande` (minute 0-59, heure 0-23, jour 1-31, mois 1-12, jour de semaine 0-6, dimanche = 0).

| Planification | Ligne |
|---|---|
| chaque minute | `* * * * *` |
| chaque heure pile | `0 * * * *` |
| toutes les 15 minutes | `*/15 * * * *` |
| lundi à 15 h | `0 15 * * 1` |
| le 1er du mois à 22 h 30 | `30 22 1 * *` |

L'intervalle minimal est 1 minute : cron ne sait pas lancer toutes les X secondes. `*/15` signifie « toutes les 15 unités » du champ.

**Exercices** : au TP4, cron sauvegarde `temperature.txt` ([[TP4 (résumé)]], [[UNIX Commands - Semester report (résumé)]]) ; au TP6, une tâche cron copie trois fichiers de `/home/First`, `/home/Second` et `/home/Third` vers `/home/Backup` toutes les 2 minutes ([[TP6-Assignment (résumé)]]).

Voir aussi : [[Démon (informatique)]], [[Commande systemctl]], [[Sauvegarde de fichier]], [[Super-utilisateur root]], [[Script Bash]], [[Shell et Bash]]

## À vérifier

- Le sujet du TP4 ([[TP4-Unix Commands (résumé)]]) parle de « six fields » : cinq champs de temps plus la commande.
- « Dimanche = 0 » : 7 désigne aussi le dimanche (complément du résumé).

Résumés : [[4 - TP4 (résumé)]], [[TP4-Unix Commands (résumé)]], [[TP4 (résumé)]], [[TP6-Assignment (résumé)]], [[UNIX Commands - Semester report (résumé)]]
