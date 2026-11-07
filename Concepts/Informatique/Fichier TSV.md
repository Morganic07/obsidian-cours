---
type: concept
tags:
  - year2
aliases:
  - TSV
  - Tab-Separated Values
  - .tsv
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[5 - TP5|Cours TP5]]"
maj: 2026-11-07
---

Fichier texte structuré dont les champs sont séparés par des tabulations ; utile quand les données contiennent des virgules. En [[AWK]], on précise la tabulation avec `-F`. Exemple du TP5 : `car.tsv`, avec les champs ID, constructeur, modèle, puissance.

Notion parente : [[Séparateur de champs]]. Voir aussi : [[Fichier CSV]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]] donne pour l'exemple sur `file.tsv` la commande « awk –F”\t” ‘{print $1, $3}’ file.csv » ; il faut « awk -F'\t' '{print $1, $3}' file.tsv » : le fichier d'entrée est `file.tsv`, et le tiret et les guillemets typographiques font échouer la commande.

Résumés : [[5 - TP5]]
