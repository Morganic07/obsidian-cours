---
type: source
tags: [year2]
sources: ["[[TP1]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[TP1]] (rendu de TP, dossier DM), dans [[Operating System (matière)]]. Il apprend à utiliser l'aide du shell, `sudo`, les paquets, le clavier, le nom de machine et les droits, puis à manipuler des arborescences. Ce sont les réponses de l'étudiante, sur un Linux (Debian) lancé dans ChromeOS, avec ses captures du terminal ; les énoncés des tâches ne sont pas reproduits dans la note, seulement leur numéro et parfois une reformulation. Pas de corrigé officiel.

## Tâche 1 : enchaîner deux commandes

```bash
ls -l ; whoami
```

Le `;` enchaîne les commandes : on liste les fichiers du répertoire personnel ([[Commande ls]]), puis on affiche le nom d'utilisateur ([[Commande whoami]]).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image3.png]]
*Figure : `ls -l ; whoami` : trois répertoires (Apps, Coding, my_env) puis `momo`.*

## Tâche 2 : les trois sources d'aide

1. **`man hostname`** : ouvre le manuel de la commande [[Commande hostname|hostname]] ([[Commande man]]).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image42.png]]
*Figure : page de manuel HOSTNAME(1) : NAME, SYNOPSIS, DESCRIPTION (GET NAME, SET NAME, THE FQDN).*

Points utiles de la page : sans argument, `hostname` affiche le nom du système ; avec un argument, il le change, mais seulement jusqu'au prochain redémarrage (modifier `/etc/hostname` pour un changement permanent) ; seul le super-utilisateur peut changer les noms ; le FQDN (*Fully Qualified Domain Name*, par exemple `ursula.example.com`) est en général le nom d'hôte suivi du domaine DNS, il se lit avec `hostname --fqdn` et ne se change pas avec `hostname`.

2. **`cp --help`** : affiche les informations utiles de la commande [[Commande cp|cp]] ([[Option --help]]).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image29.png]]
*Figure : aide de `cp` : `Usage: cp [OPTION]... [-T] SOURCE DEST`, puis la liste des options.*

3. **`info pwd`** : ouvre la page info de [[Commande pwd|pwd]] ([[Commande info]]).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image39.png]]
*Figure : page info « 19.1 ‘pwd’: Print working directory » : options `-L` / `--logical` et `-P` / `--physical`.*

Contenu : `pwd` affiche le nom du répertoire courant ; `-L` utilise la variable `PWD` si elle donne un chemin absolu sans `.` ni `..` (liens symboliques possibles) ; `-P` affiche un chemin entièrement résolu, sans lien symbolique ; si les deux sont donnés, le dernier l'emporte ; par défaut `-P`, sauf si `POSIXLY_CORRECT` est défini ; code de sortie 0 = succès.

4. **Les trois à la fois** :

```bash
man hostname ; cp --help ; info pwd
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image21.png]]
*Figure : après les trois commandes enchaînées, le terminal affiche l'aide de `cp`.*

Le manuel de `hostname` s'ouvre ; quand on le quitte, la page info de `pwd` s'ouvre ; quand on la quitte, on revient au terminal qui affiche l'aide de `cp` (explication de l'étudiante).

## Tâche 3 : `sudo`

Voir [[Commande sudo]] et [[Super-utilisateur root]].

1. **`sudo ls /root`** :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image25.png]]
*Figure : depuis `/`, `ls` liste bin, boot, dev, etc, home, lib… var ; `sudo ls /root` ne renvoie rien.*

Le dossier `/root` est vide ; l'étudiante s'attendait à y voir un dossier `snap`, qui serait directement sous `/` sur sa machine. Voir [[Arborescence des répertoires Linux]].

2. **`sudo apt update`** ([[APT]]) :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image35.png]]
*Figure : `apt update` sans `sudo` échoue (« Could not open lock file /var/lib/apt/lists/lock … Permission denied ») ; avec `sudo`, les dépôts Debian bookworm sont lus et « All packages are up to date ».*

Pour mettre à jour les paquets, le système doit accéder à `/var`, situé sous `/` : il faut `sudo`.

3. **`sudo apt install net-tools`** (paquet qui fournit [[Commande ifconfig|ifconfig]]) :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image38.png]]
*Figure : sans `sudo`, « Unable to acquire the dpkg frontend lock … are you root? » ; avec `sudo`, « net-tools is already the newest version (2.10-0.1) ».*

Même raison : installer un paquet exige `sudo`.

4. **Consulter les journaux des actions `sudo`** (*Check logs*) : l'historique des commandes se trouve sous `/var` ; d'après sa documentation, l'étudiante cherche les journaux de `sudo` dans `auth.log` ([[Fichier journal]]), mais ne le trouve pas, peut-être parce que Linux est simulé dans ChromeOS.

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image9.png]]
*Figure : `ls` dans `/var/log` : alternatives.log, apt, bootstrap.log, dpkg.log, journal… mais pas de `auth.log`.*

Contournement avec [[Commande journalctl|journalctl]] :

```bash
sudo journalctl _COMM=sudo
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image30.png]]
*Figure : journal des `sudo` : pour chaque appel, l'utilisateur (momo), le TTY, le répertoire, `USER=root`, la commande (`apt-get update`, `apt update`, `apt list --upgradable`…), puis l'ouverture et la fermeture de la session root.*

Après avoir supprimé puis réinstallé Debian, `auth.log` apparaît, mais il est vide, sans explication trouvée.

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image24.png]]
*Figure : `auth.log` est maintenant listé dans `/var/log`, mais `sudo cat auth.log` n'affiche rien.*

## Tâche 4 : `sudo` sans mot de passe

L'enseignant a demandé de faire seulement les captures, sans valider. Après la manipulation, on pourrait utiliser `sudo` sans saisir de mot de passe.

```bash
sudo visudo
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image7.png]]
*Figure : fichier `/etc/sudoers` ouvert par `visudo` : avertissement « This file MUST be edited with the 'visudo' command as root », lignes `Defaults env_reset`, `mail_badpass`, `secure_path`, `use_pty`, puis `root ALL=(ALL:ALL) ALL` et `%sudo ALL=(ALL:ALL) ALL`.*

Il faudrait ajouter à la fin du fichier ([[Fichier sudoers]]) :

```
momo ALL=(ALL) NOPASSWD:ALL
```

## Tâche 5 : disposition du clavier

Voir [[Disposition du clavier]].

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image28.png]]
*Figure : `~setxkbmap fr` puis `sudo setxkbmap fr` : « command not found ».*

Il faut installer la commande : `sudo apt-get install x11-xkb-utils`. Mais le changement temporaire de clavier affiche un avertissement :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image19.png]]
*Figure : `setxkbmap fr` et `setxkbmap us` → « WARNING: Running setxkbmap against an XWayland server ».*

Piste trouvée sur Reddit : passer de [[Wayland et X11|Wayland à X11]] en modifiant le gestionnaire d'affichage, `sudo nano /etc/gdm3/custom.conf`, et retirer le `#` de la ligne `#WaylandEnable=false`. Mais le dossier `gdm3` n'existe pas :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image36.png]]
*Figure : contenu de `/etc` : pas de dossier `gdm3`.*

Pas non plus de fichier `keyboard` dans `/etc/default` :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image20.png]]
*Figure : `/etc/default` ne contient que dbus, hwclock, locale, networking, nss, ssh, useradd.*

Les solutions trouvées sur les forums n'ont pas marché ; l'étudiante l'attribue au fait que le terminal tourne directement dans ChromeOS.

## Tâche 6 : nom d'hôte

1. **Nom d'hôte et domaine pleinement qualifié** ([[Nom d'hôte]]) :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image34.png]]
*Figure : `hostname` et `hostname -f` affichent tous deux `penguin`.*

`hostname -f` affiche le FQDN, c'est-à-dire le nom d'hôte suivi du domaine complet ; si aucun FQDN n'est configuré, il n'affiche que le nom d'hôte.

2. **Changer le nom** :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image4.png]]
*Figure : `sudo hostname momo`, puis `hostname` affiche `momo`.*

3. **Résumé de `hostname`** :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image14.png]]
*Figure : `hostname --help` : usages et options.*

| Option | Rôle |
|---|---|
| `-a`, `--alias` | alias |
| `-A`, `--all-fqdns` | tous les noms longs (FQDN) |
| `-b`, `--boot` | nom par défaut si aucun n'est disponible |
| `-d`, `--domain` | nom de domaine DNS |
| `-f`, `--fqdn`, `--long` | nom long (FQDN) |
| `-F`, `--file` | lire le nom dans un fichier |
| `-i`, `--ip-address` | adresses du nom d'hôte |
| `-I`, `--all-ip-addresses` | toutes les adresses de l'hôte |
| `-s`, `--short` | nom court |
| `-y`, `--yp`, `--nis` | domaine NIS/YP |

Sauf usage de bind ou NIS, on peut changer le FQDN et le domaine DNS dans `/etc/hosts` ([[Fichier hosts]]).

## Tâche 7 : mot de passe

```bash
sudo passwd
```

Non exécutée : l'étudiante ayant eu des difficultés avec le mot de passe, l'enseignant lui a dit de ne pas lancer ces commandes. Sinon, le terminal demanderait le mot de passe actuel, puis le nouveau deux fois pour confirmer ([[Commande passwd]]).

## Tâche 8 : arborescences et droits

1. **Créer des arborescences avec les accolades** ([[Expansion d'accolades]], [[Commande mkdir]]). Même logique que `sudo touch test{1..3}.txt` : `sudo mkdir -p project/src project/files project/docs` équivaut à `sudo mkdir -p project/{files, docs, src}` (voir point à vérifier 1). `-p` crée les dossiers parents manquants.

```bash
mkdir -p semester/{first/{os,uc},second/{cn,db,ns,cs},third/{iot,sp,dc}}
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image26.png]]
*Figure : `tree semester/` : first (os, uc), second (cn, cs, db, ns), third (dc, iot, sp) ; 13 répertoires, 0 fichier.*

Voir [[Commande tree]].

2. **Créer et remplir un fichier dans chaque semestre** :

```bash
touch semester/first/semester.txt && echo "first" | cat > semester/first/semester.txt
touch semester/second/semester.txt && echo "second" | cat > semester/second/semester.txt
touch semester/third/semester.txt && echo "third" | cat > semester/third/semester.txt
```

`touch` crée le fichier au chemin donné ([[Commande touch]]) ; `&&` lance une autre commande dans la même ligne ; `echo "first" | cat > …` écrit « first » dans le fichier ([[Redirection et tube]]).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image33.png]]
*Figure : arborescence `semester` avec un `semester.txt` dans first, second et third.*

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image44.png]]
*Figure : `cat` des trois fichiers : first, second, third.*

3. **Rendre `semester` en lecture seule, récursivement**. Le manuel de [[Commande chmod|chmod]] donne `-R, --recursive` : changer fichiers et répertoires récursivement.

```bash
sudo chmod -R 444 semester/
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image1.png]]
*Figure : après `chmod -R 444`, `tree semester/` n'affiche plus rien : « 0 directories, 0 files ».*

4. On ne peut plus rien créer dans `semester`, puisque les droits sont en lecture seule ([[Permissions Unix]]).

5. **Créer dix fichiers** :

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image8.png]]
*Figure : `sudo touch test{1..10}.txt` puis `ls` : test1.txt à test10.txt.*

6. **En supprimer cinq** avec la même logique ([[Commande rm]]) :

```bash
sudo rm test{6..10}.txt
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image22.png]]
*Figure : il reste test1.txt à test5.txt.*

7. **Copier deux fichiers dans `/home`** :

```bash
sudo cp test4.txt test5.txt /home     # ou : sudo cp test{4..5}.txt /home
```

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image15.png]]
*Figure : `cd /home ; ls` → `momo`, `test4.txt`, `test5.txt`.*

## Questions courtes

1. **`whoami` ou `hostname`** : `whoami` donne l'utilisateur connecté ; `hostname` le nom de la machine utilisée.
2. **`cd`** (*change directory*, [[Commande cd]]) : se déplacer dans le système de fichiers en donnant le chemin voulu. Exemple : depuis `/home`, `cd /etc` quitte le [[Chemin de fichier|répertoire courant]] pour `/etc`.
3. **Raccourcis de `cd`** :
   - `cd ..` : répertoire parent (de `/home/momo/test` à `/home/momo`) ;
   - `cd ~` : comme `cd` seul, va au [[Répertoire personnel]] ;
   - `cd -` : revient au répertoire précédent (de `/etc/apt` à `/home/momo` si l'on venait de là).
4. **Afficher le répertoire courant** : `pwd` (*print working directory*).
5. **`./`** représente le répertoire courant.
6. **Options de `cp`** (manuel) :

| Option | Rôle |
|---|---|
| `-a`, `--archive` | comme `-dR --preserve=all` |
| `--attributes-only` | ne copier que les attributs, pas les données |
| `--backup[=CONTROL]` / `-b` | sauvegarder chaque fichier de destination existant |
| `--copy-contents` | copier le contenu des fichiers spéciaux en récursif |
| `-d` | comme `--no-dereference --preserve=links` |
| `-f`, `--force` | si la destination ne peut être ouverte, la supprimer et réessayer |
| `-i`, `--interactive` | demander avant d'écraser |
| `-H` | suivre les liens symboliques de la ligne de commande |
| `-l`, `--link` | créer des liens physiques au lieu de copier |
| `-L`, `--dereference` | toujours suivre les [[Lien symbolique\|liens symboliques]] de SOURCE |
| `-n`, `--no-clobber` | ne pas écraser un fichier existant |
| `-P`, `--no-dereference` | ne jamais suivre les liens symboliques |
| `-p` | comme `--preserve=mode,ownership,timestamps` |
| `--parents` | garder le chemin source complet sous DIRECTORY |
| `-R`, `-r`, `--recursive` | copier les répertoires récursivement |
| `--remove-destination` | supprimer la destination avant de l'ouvrir |
| `-s`, `--symbolic-link` | créer des liens symboliques |
| `-S`, `--suffix` | changer le suffixe de sauvegarde |
| `-t`, `--target-directory` | copier toutes les sources dans DIRECTORY |
| `-T`, `--no-target-directory` | traiter DEST comme un fichier normal |
| `-u`, `--update` | copier seulement si la source est plus récente ou la destination absente |
| `-v`, `--verbose` | expliquer ce qui est fait |
| `-x`, `--one-file-system` | rester sur ce [[Système de fichiers]] |
| `-Z`, `--context` | contexte de sécurité SELinux |

7. **Éteindre le système** : `sudo shutdown now` ou `sudo poweroff` ([[Commandes shutdown et poweroff]]).
8. **`rm` et `rm -r`** : `rm` supprime un fichier ; avec `-r` (récursif), il supprime un dossier et son contenu.

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image23.png]]
*Figure : `Test/` contient file1 à file4 ; `rm Test/file1.txt` en retire un ; `rm -r Test/` supprime le dossier.*

9. **`rm` ou `rmdir`** : `rm` supprime un fichier ou un répertoire (avec `-r`) ; [[Commande rmdir|rmdir]] ne supprime qu'un répertoire vide.

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image10.png]]
*Figure : `rmdir Test/` sur un dossier de quatre fichiers → « failed to remove 'Test/': Directory not empty ».*

10. **Informations système** : [[Commande uname|uname]] ; d'après le manuel, `-r` (`--kernel-release`) donne la version du [[Noyau]] (`-a` tout, `-s` nom du noyau, `-n` nom d'hôte réseau).

![[Cours/Year 2/Operating System/DM/TP1/medias/TP1/image31.png]]
*Figure : `uname -r` → `6.6.30-02726-gb84bbdf6955e`.*

11. **`apt upgrade` ou `apt full-upgrade`** : `upgrade` met à jour les paquets installés sans en supprimer ; il peut en installer de nouveaux si une dépendance l'exige, mais si une mise à jour demande d'en supprimer un, elle n'est pas faite. `full-upgrade` fait la même chose mais peut supprimer des paquets installés pour mettre à jour le système dans son ensemble (extrait de `man apt`). La réponse de l'étudiante dit que `upgrade` « ne peut ni installer ni supprimer » : voir point à vérifier 6.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`sudo mkdir -p project/{files, docs, src}`** : l'espace après les virgules empêche l'expansion ; il faut écrire `{files,docs,src}` sans espace (complément).
2. **« rm is used to remove a single file »** (réponse 8) contredite par la réponse 9 : `rm` sans `-r` ne supprime pas un dossier, avec `-r` oui.
3. **`~setxkbmap fr`** : le tilde collé au nom est une faute de frappe ; l'erreur n'a rien à voir avec l'absence du paquet.
4. **Tâche 3.1** : `/root` est vide, l'étudiante s'attendait à un dossier `snap` ; sans conséquence.
5. **Alertes de transcription** (`gethostname` / `getdomainname`, curseur sur « Next ») : les premières portent sur la page de manuel elle-même, pas sur le TP ; ce sont des fausses alertes pour le contenu (images non rouvertes).
6. **Question 11** : la réponse « `apt upgrade` ne permet ni d'installer ni de supprimer des paquets » est plus stricte que le manuel cité, qui dit que de nouveaux paquets peuvent être installés pour satisfaire des dépendances.
7. **Tâche 8.3, `tree` vide après `chmod -R 444`** : sans droit d'exécution (`x`), on ne peut plus parcourir les répertoires, d'où « 0 directories » ; mettre `444` sur des dossiers les rend inaccessibles, pas seulement en lecture (complément).
8. **Tâche 8.2, `echo "first" | cat > fichier`** : le `cat` est inutile, `echo "first" > fichier` suffit, et `touch` aussi puisque la redirection crée le fichier (complément).
