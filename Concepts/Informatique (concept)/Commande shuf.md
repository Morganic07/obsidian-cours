---
type: concept
tags:
  - year2
aliases:
  - shuf
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh (résumé)|Commandes Shell + explications]]"
  - "[[2 - TP2 (résumé)|Cours TP2]]"
maj: 2026-11-06
---

`shuf` génère des nombres aléatoires : `-i` fixe la plage d'entrée (input-range), `-n` le nombre de sorties (head-count), `-r` autorise la répétition. Exemple : `shuf -i 1-10 -n 10 -r > number.txt`.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Commande sort]], [[Commande uniq]].

## À vérifier

- La fiche décrit `-n` comme le « nb de character à la sortie » : c'est un nombre de lignes.

Résumés : [[8 - OS commandes sh (résumé)]], [[2 - TP2 (résumé)]]
