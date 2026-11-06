---
type: source
tags: [year2]
sources: ["[[raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands]] (3 pages, 2 décembre 2024, « TP-4 : Backup processes, and automating the backup using Cron »), dans [[Operating System (matière)]]. Sujet de TP, en anglais. Le rendu est [[TP4 (résumé)]] ; les notes de cours, [[Cours TP4 (résumé)]].

## Ce qui est demandé

- **Tâche 1** : programme C qui crée un père et un fils avec `fork()`. Le père ajoute l'heure système à `time.txt` toutes les 5 secondes ; le fils copie ce fichier vers un dossier de sauvegarde toutes les 10 secondes, en écrasant la version précédente. Le programme tourne en arrière-plan, puis on termine la tâche. Voir [[Création et terminaison de processus]] et [[Processus]].
- **Cron** : ordonnanceur de tâches temporelles. Composants : le démon `cron` et la `crontab`. Installation avec `apt`, démarrage avec `systemctl start cron` et `enable`, état avec `status`. `crontab -e` édite la table de l'utilisateur courant (sans `sudo`, sinon c'est celle de root), `crontab -l` la liste. Exemple : `0 3 * * * /path/to/script.sh` chaque jour à 3 h ; `* * * * *` chaque minute. Cron n'exécute rien à moins d'une minute d'intervalle. Voir [[Tâche planifiée cron]].
- **Tâche 2** : planifier la copie de `temperature.txt` vers le dossier de sauvegarde, en écrasant l'ancienne, (a) chaque minute, (b) toutes les 3 minutes, (c) chaque nuit à 2 h.

## Notions mobilisées

`fork`, processus père et fils, boucles et attente (`sleep`), copie de fichiers, [[Tâche planifiée cron]], [[Script Bash]].

## Points à vérifier

1. Le sujet dit qu'une entrée de crontab a « six fields » : il y a cinq champs de temps (minute, heure, jour du mois, mois, jour de la semaine) suivis de la commande (complément).
2. L'exemple `0 0 * * * cp /home/user/data /home/backup/` copie un dossier sans l'option `-r`, ce qui échoue (complément).
