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
  - "[[3 - TP3 (résumé)|Cours TP3]]"
maj: 2026-11-06
---

`cp` copie un fichier. Les scripts de [[Sauvegarde de fichier]] font `cp "$SOURCE" "$DESTINATION"`, en écrasant la copie précédente.

`cp --help` affiche la syntaxe, la description et les options : `-R`, `-r` ou `--recursive` pour copier des dossiers, `-i` pour le mode interactif.

Voir aussi : [[Sauvegarde de fichier]], [[Tâche planifiée cron]], [[Option --help]].

## À vérifier

- Exemple du TP4 `0 0 * * * cp /home/user/data /home/backup/` : il copie un dossier sans `-r`, donc échoue (signalé par le résumé).

Résumés : [[3 - TP3 (résumé)]]
