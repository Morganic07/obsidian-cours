---
type: concept
tags:
  - year2
aliases:
  - arithmetic expansion
  - expression arithmétique Bash
sources:
  - "[[8 - OS commandes sh (résumé)|Commandes Shell + explications]]"
  - "[[DM Shell Scripting (résumé)|DM Shell Scripting]]"
maj: 2026-11-06
---

En Bash, `((condition))` sert aux expressions arithmétiques : `if ((NombreActuel%i==0))`, `((compteur++))`, `n=$(( n+1 ))`.

Le DM note qu'on ne peut pas utiliser `sqrt` dans le test : pour chercher les diviseurs d'un [[Nombre premier]], on écrit donc `i*i<=n`.

Notion parente : [[Script Bash]]. Voir aussi : [[Opérateur de comparaison]], [[Nombre premier]].

Résumés : [[8 - OS commandes sh (résumé)]], [[DM Shell Scripting (résumé)]]
