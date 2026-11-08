---
type: concept
tags:
  - year2
aliases:
  - uniq
  - uniq -c
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[2 - TP2|Cours TP2]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"
maj: 2026-11-08
---

`uniq` omet les lignes répétées. Placée après `sort -g`, elle donne une liste triée de valeurs uniques.

## Compléments (hors du cours)

- `uniq` ne supprime que les doublons **consécutifs** : deux lignes identiques séparées par une autre restent toutes deux. D'où le `sort` préalable, qui regroupe les lignes égales.
- `sort fichier | uniq -c` compte les occurrences de chaque ligne (le nombre s'affiche en tête de ligne).
- `sort -u` trie et dédoublonne en une seule commande.
- Exemple : `cut -f4 car.tsv | sort | uniq -c` compte les voitures par puissance, comme le comptage `{count[$4]++}` du TP5 avec [[AWK]].

Notion parente : [[Shell et Bash]]. Voir aussi : [[Commande sort]], [[Redirection et tube]], [[AWK]].

Résumés : [[8 - OS commandes sh]], [[2 - TP2]]
