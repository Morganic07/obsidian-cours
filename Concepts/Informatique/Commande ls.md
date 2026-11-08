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
maj: 2026-11-08
---

`ls` liste les fichiers du répertoire courant. `ls -l` les détaille, colonne par colonne :

- type et permissions : le premier caractère vaut `d` pour un répertoire, `-` pour un fichier, puis viennent 3 groupes de 3 droits ([[Permissions Unix]]) ;
- nombre de liens physiques (*hard links*) vers le fichier ; un lien symbolique ne change pas ce compteur ; [[Erreurs du cours#^e-commande-ls|✎]]
- propriétaire, puis groupe ;
- taille en octets ;
- date de dernière modification ;
- nom.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Joker (wildcard)]], [[Lien symbolique]].

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
