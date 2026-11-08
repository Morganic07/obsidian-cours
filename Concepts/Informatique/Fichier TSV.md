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
maj: 2026-11-08
---

Fichier texte structuré dont les champs sont séparés par des tabulations ; utile quand les données contiennent des virgules. En [[AWK]], on précise la tabulation avec `-F` : `awk -F'\t' '{print $1, $3}' file.tsv` affiche la première et la troisième colonne (sujet du TP5). [[Erreurs du cours#^e-fichier-tsv|✎]] Exemple du TP5 : `car.tsv`, avec les champs ID, constructeur, modèle, puissance.

Notion parente : [[Séparateur de champs]]. Voir aussi : [[Fichier CSV]].

Résumés : [[5 - TP5]]
