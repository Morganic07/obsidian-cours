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
maj: 2026-11-07
---

On affecte une variable sans espace autour de `=` (`Name="Morgane"`) et on lit sa valeur avec `$Name`. Deux types :

- **variables système**, en majuscules : `$BASH`, `$BASH_VERSION`, `$HOME`, `$PWD`, `$USER` ;
- **variables définies par l'utilisateur**, en minuscules.

Notion parente : [[Script Bash]]. Voir aussi : [[Substitution de commande]], [[Guillemets en shell]], [[Commande read]].

## Erreurs du cours

- [[8 - OS commandes sh|Commandes Shell + explications]] donne comme bonne orthographe `Name="Morgane` (guillemet non fermé) ; il faut `Name="Morgane"`.
- Le même document écrit des guillemets typographiques et des tirets longs (`Read -p “enter a number :” number`, `if [ “$a” –eq “$b” ]`) ; il faut des guillemets droits et un tiret simple : `read -p "enter a number :" number`, `if [ "$a" -eq "$b" ]`. Copiés tels quels, ces exemples ne marchent pas dans un script.

Résumés : [[8 - OS commandes sh]]
