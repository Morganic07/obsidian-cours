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
maj: 2026-11-07
---

`{}` se développe en plusieurs options : `touch file{1,2,3}.txt`, `touch file{1..20}.txt`, `mkdir -p semester/{first/{os,uc},...}`. Les accolades `{ }` servent aussi à grouper des commandes dans le shell courant ([[Groupement de commandes]]).

Notion parente : [[Méta-caractère]]. Voir aussi : [[Commande touch]], [[Commande mkdir]], [[Joker (wildcard)]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]] écrit « sudo mkdir -p project/{files, docs, src} » ; il faut « sudo mkdir -p project/{files,docs,src} » : avec des espaces, le shell coupe les mots et l'expansion n'a pas lieu (il crée `project/{files,`, `docs,` et `src}`).

Résumés : [[2 - TP2]]
