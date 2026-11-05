---
type: concept
aliases: [script Bash, bash script, shell script, script shell, shebang, scripting Bash]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[Commandes Shell + explications]]", "[[DM Shell Scripting]]"]
maj: 2026-11-05
---

Un script Bash est un fichier `.sh` de commandes. Il commence par le **shebang** `#!/bin/bash`, qui indique l'interpréteur (`#!/usr/bin/python3` pour Python). On l'exécute avec `./script.sh` (shebang respecté, permission d'exécution requise) ou `sh script.sh`. Un commentaire commence par `#`.

**Variables** : pas d'espace autour de `=` (`Name="Alice"`), `$Name` donne la valeur. `$(cmd)` exécute une commande et récupère son résultat. Variables système en majuscules (`$HOME`, `$PWD`, `$BASH`), variables utilisateur en minuscules.

**Entrée** : `read var`, `read -p "texte" var` (prompt), `read -s` (saisie masquée), `read -a tab` (tableau).

**Tests** : `if [ condition ]; then … elif … else … fi`, avec espaces autour des crochets. Entiers : `-eq -ne -gt -ge -lt -le` ; chaînes : `= == !=`. `(( ))` pour l'arithmétique. ET : `&&` ou `-a`, OU : `||` ou `-o`.

**Boucles** : `while [ cond ]; do … done`, `for (( i=0; i<n; i++ )); do … done`.

Exemples faits en TP : boucle infinie qui ajoute la date toutes les 2 s, copie de sauvegarde toutes les 15 s (`sleep`), 500 premiers nombres premiers avec test `i*i <= n`, désactivation des cœurs via `/sys/devices/system/cpu/cpuX/online`.

Liens : [[Shell et Bash]], [[Permissions Unix]], [[Tâche planifiée cron]]

Résumé : [[OS - chp 5 (résumé)]], [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]]
