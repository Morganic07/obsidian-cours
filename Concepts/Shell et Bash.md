---
type: concept
aliases: [shell, Bash, bash, Bourne-Again Shell, interpréteur de commandes]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[Commandes Shell + explications]]", "[[DM Shell Scripting]]"]
maj: 2026-11-06
---

Le shell est un programme qui offre une interface pour interagir avec le système : il interprète et exécute les commandes tapées, et gère fichiers, dossiers et ressources. Exemples : `sh` ([[Bourne Shell (sh)]]), Bash, `rbash` ([[Shell rbash]]), `dash` ([[Shell dash]]). Bash est le shell par défaut de Debian/Ubuntu ; c'est un interpréteur en [[Interface en ligne de commande|ligne de commande]] qui permet aussi d'écrire des scripts (voir [[Script Bash]]). Certains caractères y ont un sens spécial : voir [[Méta-caractère]].

`cat /etc/shells` liste les shells installés ([[Fichier shells]]) ; `which bash` donne l'emplacement de Bash. Dans le résultat du cours, ceux de `/bin` sont essentiels au démarrage, ceux de `/usr/bin` ne le sont pas.

Aide : `man commande`, `commande --help`, `info commande`. `sudo` exécute avec les droits du superutilisateur ; `apt update` met à jour la liste des paquets, `apt upgrade` installe les nouvelles versions, `apt full-upgrade` peut en installer et en supprimer.

Commandes de base vues : `ls`, `cd` (`..`, `~`, `-`), `pwd`, `mkdir -p`, `touch`, `rm`, `rmdir`, `cat`, `echo`, `date`, `whoami`, `hostname`, `free -h`, `df -h`, `lscpu`, `lshw`, `uname -r`.

Voir aussi : [[Interface en ligne de commande]], [[Bourne Shell (sh)]], [[Shell dash]], [[Shell rbash]], [[Fichier shells]], [[Méta-caractère]], [[Permissions Unix]], [[Redirection et tube]], [[Script Bash]], [[Tâche planifiée cron]], [[AWK]]

Résumés : [[OS - chp 5 (résumé)]], [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]]
