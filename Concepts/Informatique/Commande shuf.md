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
maj: 2026-11-07
---

`shuf` génère des nombres aléatoires : `-i` fixe la plage d'entrée (input-range), `-n` le nombre de sorties (head-count), `-r` autorise la répétition. Exemple : `shuf -i 1-10 -n 10 -r > number.txt`.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Commande sort]], [[Commande uniq]].

## Erreurs du cours

- [[8 - OS commandes sh|Commandes Shell + explications]] décrit `-n` comme « head-count (nb de character à la sortie) » ; il faut « nombre de lignes à la sortie » : `-n 10` produit 10 lignes.

Résumés : [[8 - OS commandes sh]], [[2 - TP2]]
