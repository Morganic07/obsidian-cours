---
type: concept
tags: [year2]
aliases: [shuf]
matieres: [Operating System]
sources: ["[[Commandes Shell + explications (résumé)|Commandes Shell + explications]]", "[[Séance TP2 (résumé)|Cours TP2]]"]
maj: 2026-11-06
---

`shuf` génère des nombres aléatoires : `-i` fixe la plage d'entrée (input-range), `-n` le nombre de sorties (head-count), `-r` autorise la répétition. Exemple : `shuf -i 1-10 -n 10 -r > number.txt`.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Commande sort]], [[Commande uniq]].

## À vérifier

- La fiche décrit `-n` comme le « nb de character à la sortie » : c'est un nombre de lignes.

Résumés : [[Commandes Shell + explications (résumé)]], [[Séance TP2 (résumé)]], [[TP2 (résumé)]]
