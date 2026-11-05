---
type: concept
aliases: [shell, Bash, bash, Bourne-Again Shell, ligne de commande, interpréteur de commandes]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[Commandes Shell + explications]]"]
maj: 2026-11-05
---

Le shell est un programme qui offre une interface pour interagir avec le système : il interprète et exécute les commandes tapées, et gère fichiers, dossiers et ressources. Exemples : `sh`, Bash, `rbash`, `dash`. Bash est le shell par défaut de Debian/Ubuntu ; il permet aussi d'écrire des scripts (voir [[Script Bash]]).

`cat /etc/shells` liste les shells installés ; `which bash` donne l'emplacement de Bash. Dans le résultat du cours, ceux de `/bin` sont essentiels au démarrage, ceux de `/usr/bin` ne le sont pas.

Aide : `man commande`, `commande --help`, `info commande`. `sudo` exécute avec les droits du superutilisateur ; `apt update` met à jour la liste des paquets, `apt upgrade` installe les nouvelles versions, `apt full-upgrade` peut en installer et en supprimer.

Commandes de base vues : `ls`, `cd` (`..`, `~`, `-`), `pwd`, `mkdir -p`, `touch`, `rm`, `rmdir`, `cat`, `echo`, `date`, `whoami`, `hostname`, `free -h`, `df -h`, `lscpu`, `lshw`, `uname -r`.

Liens : [[Permissions Unix]], [[Redirection et tube]], [[Script Bash]], [[Tâche planifiée cron]], [[AWK]]

Résumé : [[OS - chp 5 (résumé)]], [[Commandes Shell + explications (résumé)]]
