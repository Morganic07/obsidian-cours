---
type: concept
tags:
  - year2
aliases:
  - cp --help
  - cp -r
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
  - "[[3 - TP3|Cours TP3]]"
maj: 2026-11-07
---

`cp` copie un fichier. Les scripts de [[Sauvegarde de fichier]] font `cp "$SOURCE" "$DESTINATION"`, en écrasant la copie précédente.

`cp --help` affiche la syntaxe, la description et les options : `-R`, `-r` ou `--recursive` pour copier des dossiers, `-i` pour le mode interactif.

Voir aussi : [[Sauvegarde de fichier]], [[Tâche planifiée cron]], [[Option --help]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]] donne, pour « Backup a directory every day at midnight », « 0 0 * * * cp /home/user/data /home/backup/ » ; il faut « 0 0 * * * cp -r /home/user/data /home/backup/ » : sans `-r`, `cp` refuse de copier un dossier.

Résumés : [[3 - TP3]]
