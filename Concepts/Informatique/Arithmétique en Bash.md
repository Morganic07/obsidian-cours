---
type: concept
tags: [year2]
aliases: [arithmetic expansion, expression arithmétique Bash]
sources: ["[[Commandes Shell + explications (résumé)|Commandes Shell + explications]]", "[[DM Shell Scripting (résumé)|DM Shell Scripting]]"]
maj: 2026-11-06
---

En Bash, `((condition))` sert aux expressions arithmétiques : `if ((NombreActuel%i==0))`, `((compteur++))`, `n=$(( n+1 ))`.

Le DM note qu'on ne peut pas utiliser `sqrt` dans le test : pour chercher les diviseurs d'un [[Nombre premier]], on écrit donc `i*i<=n`.

Notion parente : [[Script Bash]]. Voir aussi : [[Opérateur de comparaison]], [[Nombre premier]].

Résumés : [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]]
