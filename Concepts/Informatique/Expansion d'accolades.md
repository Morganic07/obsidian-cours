---
type: concept
tags: [year2]
aliases: [brace expansion, accolades]
matieres: [Operating System]
sources: ["[[raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands]]", "[[cours TP1]]"]
maj: 2026-11-06
---

`{}` se développe en plusieurs options : `touch file{1,2,3}.txt`, `touch file{1..20}.txt`, `mkdir -p semester/{first/{os,uc},...}`. Les accolades `{ }` servent aussi à grouper des commandes dans le shell courant ([[Groupement de commandes]]).

Notion parente : [[Méta-caractère]]. Voir aussi : [[Commande touch]], [[Commande mkdir]], [[Joker (wildcard)]].

## À vérifier

- Au TP1, `{files, docs, src}` écrit avec des espaces empêche l'expansion (signalé par le résumé).

Résumés : [[Copy of TP2-Commands (résumé)]], [[cours TP1 (résumé)]], [[TP2 (résumé)]]
