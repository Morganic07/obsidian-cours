---
type: concept
tags:
  - year2
aliases:
  - Bourne Shell
  - commande sh
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[5 - OS|OS - chp 5]]"
maj: 2026-11-07
---

`sh` est cité parmi les shells (Bourne Shell). Selon la fiche de commandes rédigée par l'étudiante, `sh fichier.sh` exécute un script « avec l'interpréteur bash, quelle que soit la mention du shebang ».

Notion parente : [[Shell et Bash]]. Voir aussi : [[Exécution d'un script]], [[Shell dash]].

## Erreurs du cours

- [[8 - OS commandes sh|Commandes Shell + explications]] écrit que `sh testfile.sh` exécute le script « en utilisant l'interpréteur bash » ; il faut « avec l'interpréteur vers lequel pointe `/bin/sh` », qui est en général dash sous Debian et Ubuntu, et non Bash. Le shebang est bien ignoré dans les deux cas.

Résumés : [[8 - OS commandes sh]], [[5 - OS]]
