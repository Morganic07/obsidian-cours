---
type: concept
tags: [year2]
aliases: [tolower, tolower(), gsub, gsub()]
matieres: [Operating System]
sources: ["[[raw/Year 2/Operating System/DM/TP5/TP5-AWK Command.pdf|TP5-AWK Command]]", "[[Cours TP5]]"]
maj: 2026-11-06
---

- `tolower()` convertit une chaîne en minuscules : `tolower($0) ~ /paris/` donne une recherche insensible à la casse.
- `gsub(/paris/, "", line)` remplace les occurrences et renvoie leur nombre, ce qui sert à compter les occurrences d'un mot.

Notion parente : [[AWK]]. Voir aussi : [[Expression régulière]].

## À vérifier

- Le sujet ne dit pas explicitement que `gsub` renvoie le nombre de remplacements ; il ne l'utilise que pour compter.

Résumés : [[TP5-AWK Command (résumé)]], [[Cours TP5 (résumé)]]
