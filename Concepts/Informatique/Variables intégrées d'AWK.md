---
type: concept
tags: [year2]
aliases: [built-in variables, "variables prédéfinies d'AWK", AWK built-in variables]
sources: [".raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf", "[[Cours TP5]]", "[[TP5]]"]
maj: 2026-11-06
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

## À vérifier

- Exemple `{OFS="/"}` placé hors d'un bloc `BEGIN` : il marche ici, mais `BEGIN` est plus sûr (complément du résumé).

Résumés : [[TP5-AWK Command (résumé)]], [[Séance TP5 (résumé)]], [[TP5 (résumé)]]
