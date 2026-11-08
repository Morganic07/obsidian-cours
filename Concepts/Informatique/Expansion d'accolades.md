---
type: concept
tags:
  - year2
aliases:
  - brace expansion
  - accolades
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
  - "[[1 - TP1|cours TP1]]"
maj: 2026-11-08
---

`{}` se développe en plusieurs options : `touch file{1,2,3}.txt`, `touch file{1..20}.txt`, `mkdir -p semester/{first/{os,uc},...}`. Les accolades `{ }` servent aussi à grouper des commandes dans le shell courant ([[Groupement de commandes]]).

Les options s'écrivent sans espace : `sudo mkdir -p project/{files,docs,src}` (TP1). Avec des espaces, le shell coupe les mots et l'expansion n'a pas lieu (il créerait `project/{files,`, `docs,` et `src}`). [[Erreurs du cours#^e-expansion-d-accolades|✎]]

Notion parente : [[Méta-caractère]]. Voir aussi : [[Commande touch]], [[Commande mkdir]], [[Joker (wildcard)]].

Résumés : [[2 - TP2]]
