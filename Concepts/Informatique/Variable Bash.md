---
type: concept
tags:
  - year2
aliases:
  - variable système
  - variables système
  - system variables
  - user defined variable
  - variable utilisateur
  - $HOME
  - $USER
  - $PWD
  - $BASH
matieres:
  - Operating System
sources:
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
maj: 2026-11-08
---

On affecte une variable sans espace autour de `=` (`Name="Morgane"`) et on lit sa valeur avec `$Name`. [[Erreurs du cours#^e-variable-bash|✎]] Dans un script, les guillemets sont droits et les options s'écrivent avec un tiret simple : `read -p "enter a number :" number`, `if [ "$a" -eq "$b" ]`. [[Erreurs du cours#^e-variable-bash|✎]] Deux types :

- **variables système**, en majuscules : `$BASH`, `$BASH_VERSION`, `$HOME`, `$PWD`, `$USER` ;
- **variables définies par l'utilisateur**, en minuscules.

Notion parente : [[Script Bash]]. Voir aussi : [[Substitution de commande]], [[Guillemets en shell]], [[Commande read]].

Résumés : [[8 - OS commandes sh]]
