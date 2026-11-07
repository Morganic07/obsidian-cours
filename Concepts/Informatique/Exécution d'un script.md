---
type: concept
tags: [year2]
aliases: [./script.sh, exécuter un script]
matieres: [Operating System]
sources: ["[[Commandes Shell + explications (résumé)|Commandes Shell + explications]]", "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"]
maj: 2026-11-06
---

`./fichier.sh` exécute le script en respectant le [[Shebang]] et exige la permission d'exécution (`chmod +x`, voir [[Permissions Unix]]). `sh fichier.sh` l'exécute avec l'interpréteur sh. `./script.sh &` le lance en arrière-plan (TP3).

Notion parente : [[Script Bash]]. Voir aussi : [[Bourne Shell (sh)]], [[Tâche en arrière-plan]].

## À vérifier

- Même erreur sh/bash que sur [[Bourne Shell (sh)]] : la fiche dit que `sh` utilise Bash, alors que sous Debian et Ubuntu `sh` pointe en général vers dash.

Résumés : [[Commandes Shell + explications (résumé)]], [[TP3-Commands (2) (résumé)]], [[DM Shell Scripting (résumé)]]
