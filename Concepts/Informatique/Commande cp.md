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
maj: 2026-11-08
---

`cp` copie un fichier. Les scripts de [[Sauvegarde de fichier]] font `cp "$SOURCE" "$DESTINATION"`, en écrasant la copie précédente.

`cp --help` affiche la syntaxe, la description et les options : `-R`, `-r` ou `--recursive` pour copier des dossiers, `-i` pour le mode interactif.

Le sujet du TP4 sauvegarde un dossier chaque jour à minuit avec la ligne de [[Tâche planifiée cron|cron]] `0 0 * * * cp -r /home/user/data /home/backup/` : sans `-r`, `cp` refuse de copier un dossier. [[Erreurs du cours#^e-commande-cp|✎]]

Voir aussi : [[Sauvegarde de fichier]], [[Tâche planifiée cron]], [[Option --help]].

Résumés : [[3 - TP3]]
