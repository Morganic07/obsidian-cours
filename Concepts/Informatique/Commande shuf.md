---
type: concept
tags:
  - year2
aliases:
  - shuf
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[2 - TP2|Cours TP2]]"
maj: 2026-11-08
---

`shuf` génère des nombres aléatoires : `-i` fixe la plage d'entrée (input-range), `-n` le nombre de lignes en sortie (head-count) [[Erreurs du cours#^e-commande-shuf|✎]], `-r` autorise la répétition. Exemple : `shuf -i 1-10 -n 10 -r > number.txt`.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Commande sort]], [[Commande uniq]].

Résumés : [[8 - OS commandes sh]], [[2 - TP2]]
