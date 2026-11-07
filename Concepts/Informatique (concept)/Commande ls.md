---
type: concept
tags:
  - year2
aliases:
  - ls -l
matieres:
  - Operating System
sources:
  - "[[5 - OS (résumé)|OS - chp 5]]"
  - "[[8 - OS commandes sh (résumé)|Commandes Shell + explications]]"
maj: 2026-11-06
---

`ls` liste les fichiers du répertoire courant. `ls -l` les détaille, colonne par colonne :

- type et permissions : le premier caractère vaut `d` pour un répertoire, `-` pour un fichier, puis viennent 3 groupes de 3 droits ([[Permissions Unix]]) ;
- nombre de liens ;
- propriétaire, puis groupe ;
- taille en octets ;
- date de dernière modification ;
- nom.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Joker (wildcard)]], [[Lien symbolique]].

## À vérifier

- Le cours dit que la deuxième colonne compte les liens symboliques ; elle compte les liens physiques (signalé par le résumé).

Résumés : [[5 - OS (résumé)]], [[8 - OS commandes sh (résumé)]], [[TP1 (résumé)]]
