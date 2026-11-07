---
type: concept
tags:
  - year2
aliases:
  - backup
  - backing up
  - file backup
  - backup.sh
matieres:
  - Operating System
sources:
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
  - "[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"
maj: 2026-11-07
---

Sauvegarder un fichier, c'est en créer une copie à intervalles réguliers et la ranger ailleurs dans le système, pour disposer d'une copie à jour si l'original est perdu, corrompu ou modifié.

Mise en pratique : au TP3, `time.sh` ajoute la date au fichier toutes les 2 s et `backup.sh` copie le fichier toutes les 15 s ; au TP4, la sauvegarde est faite par un programme C, puis par [[Tâche planifiée cron|cron]].

Voir aussi : [[Script Bash]], [[Commande cp]], [[Boucle (programmation)]].

## Erreurs du cours

- Le script `backup.sh` de [[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]] (page 7) écrit `DESTINATION="/home/backup/"` ; il faut `/home/user/backup/`, la cible annoncée juste au-dessus.
- Le même script écrit `echo "... - $Backup Successful!"` ; il faut `Backup Successful!` sans `$` : `$Backup` n'est jamais définie et s'affiche vide.

Résumés : [[3 - TP3]]
