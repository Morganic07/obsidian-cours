---
type: concept
aliases: [script Bash, bash script, shell script, script shell, scripting Bash, fichier .sh]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[Commandes Shell + explications]]", "[[DM Shell Scripting]]", "[[Cours TP3]]"]
maj: 2026-11-06
---

Un script Bash est un fichier `.sh` d'instructions exécutées par un shell. Il commence par le [[Shebang|shebang]] `#!/bin/bash`, qui indique l'interpréteur (`#!/usr/bin/python3` pour Python). On l'exécute avec `./script.sh` (shebang respecté, permission d'exécution requise) ou `sh script.sh` : voir [[Exécution d'un script]]. Un commentaire commence par `#`.

**[[Variable Bash|Variables]]** : pas d'espace autour de `=` (`Name="Alice"`), `$Name` donne la valeur. `$(cmd)` exécute une commande et récupère son résultat. Variables système en majuscules (`$HOME`, `$PWD`, `$BASH`), variables utilisateur en minuscules.

**Entrée** : `read var`, `read -p "texte" var` (prompt), `read -s` (saisie masquée), `read -a tab` (tableau).

**Tests** ([[Structure conditionnelle]]) : `if [ condition ]; then … elif … else … fi`, avec espaces autour des crochets. Entiers : `-eq -ne -gt -ge -lt -le` ; chaînes : `= == !=`. `(( ))` pour l'arithmétique. ET : `&&` ou `-a`, OU : `||` ou `-o`.

**[[Boucle (programmation)|Boucles]]** : `while [ cond ]; do … done`, `for (( i=0; i<n; i++ )); do … done`.

Exemples faits en TP et en DM : boucle infinie qui ajoute la date toutes les 2 s, copie de [[Sauvegarde de fichier|sauvegarde]] toutes les 15 s (`sleep`), 500 premiers nombres premiers avec test `i*i <= n`, désactivation des cœurs via `/sys/devices/system/cpu/cpuX/online`, création de fichiers.

Notion parente : [[Shell et Bash]]. Voir aussi : [[Shebang]], [[Exécution d'un script]], [[Variable Bash]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Sauvegarde de fichier]], [[Permissions Unix]], [[Tâche planifiée cron]]

Résumés : [[OS - chp 5 (résumé)]], [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]], [[Cours TP3 (résumé)]], [[TP3-Commands (2) (résumé)]]
