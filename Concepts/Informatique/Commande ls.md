---
type: concept
tags:
  - year2
aliases:
  - ls -l
matieres:
  - Operating System
sources:
  - "[[5 - OS|OS - chp 5]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
maj: 2026-11-07
---

`ls` liste les fichiers du répertoire courant. `ls -l` les détaille, colonne par colonne :

- type et permissions : le premier caractère vaut `d` pour un répertoire, `-` pour un fichier, puis viennent 3 groupes de 3 droits ([[Permissions Unix]]) ;
- nombre de liens ;
- propriétaire, puis groupe ;
- taille en octets ;
- date de dernière modification ;
- nom.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Joker (wildcard)]], [[Lien symbolique]].

## Erreurs du cours

- [[5 - OS|OS - chp 5]] écrit « Nombre de liens : Montre le nombre de liens symboliques pointant vers le fichier ou le répertoire » ; il faut « le nombre de liens physiques (*hard links*) » : un lien symbolique ne change pas ce compteur.

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
