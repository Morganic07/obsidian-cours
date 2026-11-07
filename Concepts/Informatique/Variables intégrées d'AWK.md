---
type: concept
tags:
  - year2
aliases:
  - built-in variables
  - variables prédéfinies d'AWK
  - AWK built-in variables
sources:
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command.pdf]]"
  - "[[5 - TP5|Cours TP5]]"
  - "[[Raw/Year 2/Operating System/DM/TP5/TP5.docx|TP5]]"
maj: 2026-11-07
---

Variables prédéfinies d'AWK vues au TP5 :

| Variable | Rôle |
|---|---|
| `NR` | numéro de la ligne courante, cumulé sur tous les fichiers |
| `FNR` | numéro de ligne dans le fichier courant, remis à zéro à chaque fichier |
| `NF` | nombre de champs de la ligne |
| `FS` | [[Séparateur de champs]] (espace par défaut) |
| `OFS` | séparateur de sortie |
| `$0` | ligne entière |

Le rendu du TP5 ajoute le tableau du manuel : `ARGC`, `ARGV`, `CONVFMT`, `ENVIRON`, `FILENAME`, `OFMT`, `ORS`, `RLENGTH`, `RS`, `RSTART`, `SUBSEP`.

Notion parente : [[AWK]].

Résumés : [[5 - TP5]]
