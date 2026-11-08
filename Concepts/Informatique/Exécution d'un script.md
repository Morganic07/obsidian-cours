---
type: concept
tags:
  - year2
aliases:
  - ./script.sh
  - exécuter un script
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-08
---

`./fichier.sh` exécute le script en respectant le [[Shebang]] et exige la permission d'exécution (`chmod +x`, voir [[Permissions Unix]]). `sh fichier.sh` l'exécute avec l'interpréteur vers lequel pointe `/bin/sh` (en général dash sous Debian et Ubuntu, pas Bash), quel que soit le shebang. [[Erreurs du cours#^e-execution-d-un-script|✎]] `./script.sh &` le lance en arrière-plan (TP3).

Notion parente : [[Script Bash]]. Voir aussi : [[Bourne Shell (sh)]], [[Tâche en arrière-plan]].

Résumés : [[8 - OS commandes sh]]
