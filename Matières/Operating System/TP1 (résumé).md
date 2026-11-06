---
type: source
tags: [year2]
sources: ["[[TP1]]"]
maj: 2026-11-05
---

Résumé de [[TP1]] (rendu de TP, dossier DM), dans [[Operating System (matière)]]. Il apprend à utiliser l'aide du shell, `sudo`, les paquets, le clavier, le nom de machine et les droits. Captures lues par transcription seulement.

## Ce qu'apprend le TP

- Tâche 1 : `ls -l ; whoami` (enchaîner deux commandes).
- Tâche 2 : lire `man hostname`, `cp --help`, `info pwd`, puis les enchaîner : chaque page s'ouvre après la fermeture de la précédente.
- Tâche 3 : `sudo` est nécessaire pour `apt update` et `apt install` (verrous sous `/var`). Sur la machine de l'étudiant (Linux dans ChromeOS), `auth.log` est vide ; il utilise `sudo journalctl _COMM=sudo` pour voir l'historique de `sudo`.
- Tâche 4 : `visudo` pour supprimer la demande de mot de passe.
- Tâche 5 : `setxkbmap` absent, à installer via `x11-xkb-utils` ; avertissement XWayland ; pas de `/etc/gdm3` ni de `/etc/default/keyboard` : le changement permanent n'a pas pu se faire sur cette machine (l'étudiant suspecte ChromeOS).
- Tâche 6 : `hostname -f` (nom qualifié) ne donne que `penguin`, car aucun domaine n'est configuré ; `sudo hostname momo`.
- Tâche 7 : changement de mot de passe, non exécuté.
- Tâche 8 : accolades pour créer des arborescences, `chmod -R 444` rend `semester` en lecture seule ; questions courtes sur `cd`, `pwd`, `uname -r`, `rm -r`, `apt upgrade` / `full-upgrade`. Voir [[Shell et Bash]], [[Permissions Unix]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`sudo mkdir -p project/{files, docs, src}`** : l'espace après les virgules empêche l'expansion ; il faut écrire `{files,docs,src}` sans espace (complément).
2. **« rm is used to remove a single file »** (réponse 8) contredite par la réponse 9 : `rm` sans `-r` ne supprime pas un dossier, avec `-r` oui.
3. **`~setxkbmap fr`** : le tilde collé au nom est une faute de frappe ; l'erreur n'a rien à voir avec l'absence du paquet.
4. **Tâche 3.1** : `/root` est vide, l'étudiant s'attendait à un dossier `snap` ; sans conséquence.
5. **Alertes de transcription** (`gethostname` / `getdomainname`, curseur sur « Next ») : les premières portent sur la page de manuel elle-même, pas sur le TP ; ce sont des fausses alertes pour le contenu (images non rouvertes).
