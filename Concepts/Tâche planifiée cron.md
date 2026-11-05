---
type: concept
aliases: [cron, crontab, cron job, cron jobs, tâche cron]
matieres: [Operating System]
sources: ["[[Cours TP4]]"]
maj: 2026-11-05
---

`cron` exécute des tâches à intervalles fixes (sauvegardes, maintenance). Démarrage : `sudo systemctl start cron`, `enable` pour le lancer au boot, `status` pour vérifier. `crontab -e` édite la table de l'utilisateur (ne pas utiliser `sudo`, sinon c'est celle de root), `crontab -l` liste, `crontab -r` supprime tout.

Syntaxe : `minute heure jour-du-mois mois jour-de-semaine commande` (minute 0-59, heure 0-23, jour 1-31, mois 1-12, jour de semaine 0-6, dimanche = 0).

| Planification | Ligne |
|---|---|
| chaque minute | `* * * * *` |
| chaque heure pile | `0 * * * *` |
| toutes les 15 minutes | `*/15 * * * *` |
| lundi à 15 h | `0 15 * * 1` |
| le 1er du mois à 22 h 30 | `30 22 1 * *` |

L'intervalle minimal est 1 minute : cron ne sait pas lancer toutes les X secondes. `*/15` signifie « toutes les 15 unités » du champ.

Liens : [[Script Bash]], [[Shell et Bash]]

Résumé : [[Cours TP4 (résumé)]]
