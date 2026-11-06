---
type: concept
aliases: [variable système, variables système, system variables, user defined variable, variable utilisateur, "$HOME", "$USER", "$PWD", "$BASH"]
matieres: [Operating System]
sources: ["[[Commandes Shell + explications]]", "[[DM Shell Scripting]]"]
maj: 2026-11-06
---

On affecte une variable sans espace autour de `=` (`Name="Morgane"`) et on lit sa valeur avec `$Name`. Deux types :

- **variables système**, en majuscules : `$BASH`, `$BASH_VERSION`, `$HOME`, `$PWD`, `$USER` ;
- **variables définies par l'utilisateur**, en minuscules.

Notion parente : [[Script Bash]]. Voir aussi : [[Substitution de commande]], [[Guillemets en shell]], [[Commande read]].

## À vérifier

- La fiche contient un contre-exemple au guillemet non fermé et des guillemets typographiques, qui ne marchent pas dans un vrai script.

Résumés : [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]], [[Copy of TP2-Commands (résumé)]]
