---
type: concept
tags: [year2]
aliases: [backup, backing up, file backup, backup.sh]
matieres: [Operating System]
sources: ["[[Cours TP3]]", "[[raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2)]]", "[[raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands]]"]
maj: 2026-11-06
---

Sauvegarder un fichier, c'est en créer une copie à intervalles réguliers et la ranger ailleurs dans le système, pour disposer d'une copie à jour si l'original est perdu, corrompu ou modifié.

Mise en pratique : au TP3, `time.sh` ajoute la date au fichier toutes les 2 s et `backup.sh` copie le fichier toutes les 15 s ; au TP4, la sauvegarde est faite par un programme C, puis par [[Tâche planifiée cron|cron]].

Voir aussi : [[Script Bash]], [[Commande cp]], [[Boucle (programmation)]].

## À vérifier

- Script du sujet : destination `/home/backup/` au lieu de `/home/user/backup/`, et variable `$Backup` jamais définie (signalé par les résumés).

Résumés : [[Cours TP3 (résumé)]], [[TP3-Commands (2) (résumé)]], [[TP3 (résumé)]], [[TP4-Unix Commands (résumé)]], [[TP6-Assignment (résumé)]]
