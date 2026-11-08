---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]] (« Chp 5 - linux commands »), dans [[Cours/Informatique/OS/_index|Operating System]].
## Idée générale

Premières commandes [[Linux]] : le shell, `cat`, les permissions, les éditeurs, APT et les scripts Bash.

## Qu'est-ce qu'un shell ?

- Le [[Shell et Bash|shell]] est un programme qui fournit une interface pour interagir avec le [[Système d'exploitation]].
- Il interprète et exécute les commandes tapées par l'utilisateur.
- Il permet de gérer fichiers, répertoires et autres ressources du système.
- Exemples : [[Bourne Shell (sh)]], Bash (*Bourne-Again Shell*), [[Shell rbash|rbash]], [[Shell dash|dash]].
- Le shell par défaut de Debian / [[Ubuntu]] est **Bash**.
- Bash est un interpréteur en ligne de commande ([[Interface en ligne de commande]]) : on tape des commandes, il les exécute.
- Bash permet aussi d'écrire des scripts qui automatisent des tâches.
- Le shell n'est qu'une **couche au-dessus du [[Noyau|noyau]]** : il lit la ligne tapée, la découpe en mots, remplace variables et jokers (`*.txt`), puis crée un processus (`fork()` puis `exec()`) pour lancer la commande, et attend sa fin. Le terminal, lui, n'est que la fenêtre qui affiche le shell. [[Complément hors du cours|ⓘ]]
- L'invite (*prompt*) finit par `$` pour un utilisateur ordinaire et par `#` pour [[Super-utilisateur root|root]]. `echo $SHELL` affiche le shell de connexion de l'utilisateur, défini dans `/etc/passwd`, et `chsh` permet d'en changer. [[Complément hors du cours|ⓘ]]

Voir les shells supportés : `cat /etc/shells` ([[Fichier shells]]).

![[OS - chp 5 - image1.png]]
*Figure : sortie de `cat /etc/shells` : `/bin/sh`, `/usr/bin/sh`, `/bin/bash`, `/usr/bin/bash`, `/bin/rbash`, `/usr/bin/rbash`, `/bin/dash`, `/usr/bin/dash`.*

La commande renvoie la liste des shells installés. Ceux de `/bin/` sont essentiels au lancement de l'OS, ceux de `/usr/bin/` non essentiels ; un shell installé en plus va dans `/usr/bin` (voir [[Arborescence des répertoires Linux]]).

Sur les Debian et Ubuntu récents, `/bin` n'est plus qu'un [[Lien symbolique|lien symbolique]] vers `/usr/bin` (fusion *usrmerge*, voir [[4 - OS]]) : `/bin/bash` et `/usr/bin/bash` sont alors le même fichier, listé sous ses deux chemins. De même, `/bin/sh` n'est pas un shell à part : sous Debian et Ubuntu, c'est un lien vers dash, plus léger et plus rapide que Bash pour les scripts système (`ls -l /bin/sh` le montre). [[Complément hors du cours|ⓘ]]

Voir où se trouve bash : `which bash` ([[Commande which]]).

## La commande `cat`

La [[Commande cat]] (de *concatenate*) sert surtout à afficher le contenu d'un ou plusieurs fichiers sur la sortie standard (en général le terminal), mais aussi à d'autres tâches de gestion de fichiers.

| Usage | Commande | Remarque |
|---|---|---|
| Afficher un fichier | `cat filename.ext` | n'importe quelle extension |
| Afficher avec numéros de ligne | `cat -n filename.txt` | |
| Afficher deux fichiers | `cat file1.txt file2.txt` | |
| Créer un fichier | `cat > filename.ext` | on écrit directement dans le terminal, puis **Ctrl+D** pour sauvegarder |
| Fusionner deux fichiers | `cat file1.txt file2.txt > fileConcatenate.txt` | concaténation ([[Redirection et tube\|redirection]]) |

Le `>` **écrase** le fichier de destination s'il existe déjà ; `>>` **ajoute** à la fin sans effacer (`cat file2.txt >> file1.txt`). Attention à `cat file1.txt file2.txt > file1.txt` : le shell vide `file1.txt` avant même que `cat` ne le lise, et son contenu est perdu. [[Complément hors du cours|ⓘ]]

Supprimer un fichier : `rm filename.ext` (*remove*, [[Commande rm]]).

Sous Linux, `rm` ne passe pas par une corbeille : la suppression est définitive. `rm -i` demande confirmation, et il faut `rm -r` pour supprimer un répertoire et son contenu. [[Complément hors du cours|ⓘ]]

## Changer les permissions d'un fichier ou d'un répertoire

- `ls` liste les fichiers du répertoire courant ([[Commande ls]]) ; `cd` change de répertoire ([[Commande cd]]).
- `sudo nano testfile.sh` ([[Commande sudo]], [[Éditeur nano]]) ; l'extension `.sh` désigne un fichier shell, dont les instructions sont exécutées par un shell.
  - si `testfile.sh` n'existe pas, la commande crée un fichier vide et ouvre nano ;
  - s'il existe, elle l'ouvre pour modification ;
  - pour fermer : **Ctrl+O**, Entrée pour sauvegarder, puis **Ctrl+X** pour quitter.
  - un fichier créé avec `sudo` appartient à **root**, pas à l'utilisateur : c'est le cas de `fichiertest.sh` sur la figure ci-dessous. Pour un fichier de son propre répertoire, `nano testfile.sh` sans `sudo` suffit et évite de devoir ensuite changer le propriétaire. [[Complément hors du cours|ⓘ]]
- Sous Linux, l'extension ne détermine rien : c'est une convention pour l'humain. Ce qui rend un fichier exécutable, c'est la permission `x`, et ce qui choisit l'interpréteur, c'est le [[Shebang]]. [[Complément hors du cours|ⓘ]]

### Lire `ls -l`

`ls -l` détaille les fichiers. Pour chaque ligne :

- **Permissions** : le premier caractère donne le **type** (`d` répertoire, `-` fichier…) ; les neuf suivants les **permissions**, en trois groupes de trois (propriétaire, groupe, autres) ;
- **Nombre de liens** : nombre de liens physiques (*hard links*) vers le fichier ; les [[Lien symbolique|liens symboliques]] n'y sont pas comptés ; [[Erreurs du cours#^e-5-os|✎]]
- **Propriétaire** : l'utilisateur qui possède le fichier ;
- **Groupe** : le groupe auquel appartient le fichier ;
- **Taille** en octets ;
- **Date et heure** de dernière modification ;
- **Nom** du fichier ou du répertoire.

Autres valeurs du premier caractère : `l` pour un [[Lien symbolique|lien symbolique]], `c` et `b` pour les [[Fichier de périphérique|fichiers de périphériques]] en mode caractère (terminal) ou bloc (disque), `p` pour un tube nommé, `s` pour une socket. Options utiles : `ls -a` montre aussi les fichiers cachés (ceux dont le nom commence par `.`, comme `.bashrc`), `ls -lh` affiche les tailles en Ko, Mo, Go. [[Complément hors du cours|ⓘ]]

Lecture de la figure : `drwxr-x--x` se découpe en `d` (répertoire), `rwx` (le propriétaire momo peut tout faire), `r-x` (le groupe peut lister et entrer), `--x` (les autres peuvent seulement traverser le répertoire, sans en lister le contenu). `-rw-r--r--` est un fichier ordinaire que root peut lire et modifier et que tous les autres peuvent seulement lire. [[Complément hors du cours|ⓘ]]

![[OS - chp 5 - image3.png]]
*Figure : sortie de `ls -l` : trois répertoires `drwxr-x--x` (C, Cybotic, OperatingSystem) appartenant à momo, et un fichier `-rw-r--r--` `fichiertest.sh` appartenant à root.*

### Valeurs octales

Voir [[Permissions Unix]].

| Symbole | Permission | Valeur octale |
|---|---|---|
| `r` | lecture (*read*) | 4 |
| `w` | écriture (*write*) | 2 |
| `x` | exécution (*execute*) | 1 |
| `-` | aucune | 0 |

Les trois droits n'ont pas le même sens pour un fichier et pour un répertoire : [[Complément hors du cours|ⓘ]]

| Droit | Sur un fichier | Sur un répertoire |
|---|---|---|
| `r` | lire le contenu | lister les noms qu'il contient (`ls`) |
| `w` | modifier le contenu | créer, renommer ou supprimer des fichiers dedans (même sans droit sur ces fichiers) |
| `x` | l'exécuter comme programme | y entrer (`cd`) et accéder aux fichiers qu'il contient |

Ainsi, supprimer un fichier dépend du droit `w` sur le **répertoire** qui le contient, pas sur le fichier lui-même. Root n'est soumis à aucune de ces restrictions de lecture et d'écriture. [[Complément hors du cours|ⓘ]]

### `chmod`

`chmod` (*change mode*, [[Commande chmod]]) modifie les permissions d'un fichier ou d'un dossier.

```bash
sudo chmod 754 filename.txt
```

Signification de 754 :
- propriétaire : $7 = 4+2+1$ (lecture + écriture + exécution) ;
- groupe : $5 = 4+1$ (lecture + exécution) ;
- autres : $4$ (lecture seule).

Exemple : tous les droits au propriétaire, aucun au groupe, exécution et écriture aux autres ($3 = 2+1$) :

```bash
sudo chmod 703 filename.txt
```

Forme symbolique :

| Commande | Effet (d'après la note) |
|---|---|
| `sudo chmod +x {fichier}` | ajoute l'exécution pour le propriétaire, le groupe et les autres |
| `sudo chmod +w {fichier}` | ajoute l'écriture pour le propriétaire (« visiblement pas les autres ») |
| `sudo chmod +r {fichier}` | ajoute la lecture pour le propriétaire, le groupe et les autres |
| `sudo chmod +rwx {fichier}` | ajoute lecture, écriture et exécution pour tous |

La forme symbolique complète est `chmod [qui][opérateur][droits]` : [[Complément hors du cours|ⓘ]]
- **qui** : `u` (*user*, le propriétaire), `g` (groupe), `o` (*others*, les autres), `a` (*all*, les trois) ; [[Complément hors du cours|ⓘ]]
- **opérateur** : `+` ajoute, `-` retire, `=` fixe exactement ; [[Complément hors du cours|ⓘ]]
- exemples : `chmod u+x script.sh` (exécution pour le propriétaire seul), `chmod go-w fichier` (retire l'écriture au groupe et aux autres), `chmod a=r fichier` (lecture seule pour tous, équivalent de `chmod 444`), `chmod u=rwx,g=rx,o=r fichier` (équivalent de `chmod 754`). [[Complément hors du cours|ⓘ]]

Sans lettre devant `+`, chmod agit sur les trois catégories **sauf** les droits bloqués par le masque `umask` (voir plus bas l'annotation sur `chmod +w`). [[Complément hors du cours|ⓘ]]

Le propriétaire et le groupe se changent avec `chown` et `chgrp` (réservé à root pour `chown`) : `sudo chown momo:momo fichiertest.sh` rend le fichier de la figure à l'utilisateur et à son groupe. [[Complément hors du cours|ⓘ]]

## Éditeurs sous Ubuntu

Un [[Éditeur de texte|éditeur]] est un logiciel pour créer et modifier des fichiers texte : nano, [[Vim]], [[Gedit]].

Les trois se distinguent ainsi : nano et Vim tournent dans le terminal (utilisables sur un serveur sans interface graphique, ou via SSH), Gedit est un éditeur graphique. Vim est **modal** : on lance `vim fichier`, on appuie sur `i` pour passer en mode insertion et écrire, sur `Échap` pour revenir au mode normal, puis on tape `:wq` pour sauvegarder et quitter, ou `:q!` pour quitter sans sauvegarder. [[Complément hors du cours|ⓘ]]

## APT (*Advanced Package Tool*)

[[APT]] est un outil puissant et souple pour installer, supprimer, mettre à jour et mettre à niveau des paquets.

```bash
sudo apt update    # télécharge seulement la liste des nouvelles versions disponibles dans les dépôts
sudo apt upgrade   # installe les nouvelles versions des paquets installés, après apt update
```

Un **paquet** (fichier `.deb` sous Debian et Ubuntu) contient un logiciel, ses fichiers de configuration et la liste de ses **dépendances** (autres paquets nécessaires) ; APT les télécharge depuis des **dépôts**, serveurs listés dans `/etc/apt/sources.list` et `/etc/apt/sources.list.d/`, et installe automatiquement les dépendances. En dessous, c'est l'outil `dpkg` qui installe réellement chaque `.deb`. [[Complément hors du cours|ⓘ]]

Autres commandes courantes : [[Complément hors du cours|ⓘ]]

```bash
sudo apt install vim   # installer un paquet et ses dépendances
sudo apt remove vim    # le désinstaller en gardant sa configuration
sudo apt purge vim     # le désinstaller avec sa configuration
sudo apt autoremove    # supprimer les dépendances devenues inutiles
apt search éditeur     # chercher un paquet
apt show vim           # décrire un paquet
```

`apt` est la commande récente et interactive (barre de progression) ; `apt-get` et `apt-cache`, plus anciennes, restent conseillées dans les scripts, car leur sortie ne change pas d'une version à l'autre. [[Complément hors du cours|ⓘ]]

## Script Bash

- Chaque [[Script Bash]] commence par `#! /bin/bash`.
- `#!` s'appelle le [[Shebang]] : il indique au système quel interpréteur doit exécuter le script. Par exemple, `#! /usr/bin/python3` fait interpréter le script par Python.
- Le shebang doit être la **toute première ligne** du fichier ; l'espace après `#!` est permis, mais on écrit le plus souvent `#!/bin/bash`. Pour Bash, toute autre ligne commençant par `#` est un commentaire. `#!/usr/bin/env python3` cherche l'interpréteur dans le `PATH` au lieu d'imposer son chemin. [[Complément hors du cours|ⓘ]]
- Pour lancer un script : le rendre exécutable avec `chmod +x script.sh`, puis `./script.sh` (le `./` est nécessaire, car le répertoire courant n'est pas dans le `PATH`) ; ou bien `bash script.sh`, qui ne demande pas le droit `x` et ignore le shebang. Voir [[Exécution d'un script]]. [[Complément hors du cours|ⓘ]]
- Exemple minimal : [[Complément hors du cours|ⓘ]]

```bash
#!/bin/bash
# bonjour.sh : affiche un message et la date
nom="monde"
echo "Bonjour, $nom !"
echo "Nous sommes le $(date +%d/%m/%Y)"
```
- Un guide des options (`-o`, `-l`, `-a`…) est donné en lien : https://ioflood.com/blog/bash-options/

## Annotations de l'étudiante

Elle note que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine, et suppose un défaut de son Debian.

Ce n'est pas un défaut, c'est le comportement documenté de chmod (`man chmod`) : sans lettre `u`, `g`, `o` ou `a`, la forme symbolique agit comme `a`, **mais ne touche pas aux droits bloqués par le [[Masque umask|masque umask]]**. Le umask est le masque des droits retirés par défaut aux nouveaux fichiers ; il vaut en général `022` (écriture retirée au groupe et aux autres), ce qu'affiche la commande `umask`. Avec `022`, `chmod +w` ajoute donc l'écriture au seul propriétaire, alors que `+r` et `+x`, non masqués, s'appliquent à tous. Pour donner l'écriture à tous, écrire explicitement `chmod a+w`. [[Complément hors du cours|ⓘ]]