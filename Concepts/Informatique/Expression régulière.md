---
type: concept
tags: [year2]
aliases: [regular expression, expressions régulières, regex, pattern-based search]
matieres: [Operating System]
sources: ["[[Cours TP5]]", "[[raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command]]", "[[TP5]]"]
maj: 2026-11-06
---

En [[AWK]], le motif (pattern) s'écrit entre deux `/` : `/Peugeot/`, sensible à la casse. Pour chercher un motif à l'intérieur d'un champ, on utilise l'opérateur `~` au lieu de `==`, qui exige une égalité littérale :

`awk -F"|" '$6~/youtube/ || $6~/facebook/ {print $2}' log.txt`

Le manuel d'AWK dit que `FS` découpe les champs « as a regular expression ».

Notion parente : [[AWK]]. Voir aussi : [[Fonctions intégrées d'AWK]], [[Commande grep]].

## À vérifier

- Le cours ne nomme pas « regex » ni « expression régulière » comme notion, seulement « pattern » et « regular expression » dans le tableau du manuel : la définition ici est minimale.
- Fichier `log.txt` : les domaines diffèrent (.com / .org) entre les deux versions.

Résumés : [[Cours TP5 (résumé)]], [[TP5-AWK Command (résumé)]], [[TP5 (résumé)]], [[log (résumé)]], [[TP6-Assignment (résumé)]]
