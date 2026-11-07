---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]] (« Chp 5 - linux commands »), dans [[Operating System (index)]]. En cas d'écart, le cours et ses images font foi.

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

Voir les shells supportés : `cat /etc/shells` ([[Fichier shells]]).

![[OS - chp 5 - image1.png]]
*Figure : sortie de `cat /etc/shells` : `/bin/sh`, `/usr/bin/sh`, `/bin/bash`, `/usr/bin/bash`, `/bin/rbash`, `/usr/bin/rbash`, `/bin/dash`, `/usr/bin/dash`.*

La commande renvoie la liste des shells installés. Ceux de `/bin/` sont essentiels au lancement de l'OS, ceux de `/usr/bin/` non essentiels ; un shell installé en plus va dans `/usr/bin` (voir [[Arborescence des répertoires Linux]]).

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

Supprimer un fichier : `rm filename.ext` (*remove*, [[Commande rm]]).

## Changer les permissions d'un fichier ou d'un répertoire

- `ls` liste les fichiers du répertoire courant ([[Commande ls]]) ; `cd` change de répertoire ([[Commande cd]]).
- `sudo nano testfile.sh` ([[Commande sudo]], [[Éditeur nano]]) ; l'extension `.sh` désigne un fichier shell, dont les instructions sont exécutées par un shell.
  - si `testfile.sh` n'existe pas, la commande crée un fichier vide et ouvre nano ;
  - s'il existe, elle l'ouvre pour modification ;
  - pour fermer : **Ctrl+O**, Entrée pour sauvegarder, puis **Ctrl+X** pour quitter.

### Lire `ls -l`

`ls -l` détaille les fichiers. Pour chaque ligne :

- **Permissions** : le premier caractère donne le **type** (`d` répertoire, `-` fichier…) ; les neuf suivants les **permissions**, en trois groupes de trois (propriétaire, groupe, autres) ;
- **Nombre de liens** : la note dit « nombre de [[Lien symbolique|liens symboliques]] » (voir point à vérifier 1) ;
- **Propriétaire** : l'utilisateur qui possède le fichier ;
- **Groupe** : le groupe auquel appartient le fichier ;
- **Taille** en octets ;
- **Date et heure** de dernière modification ;
- **Nom** du fichier ou du répertoire.

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

## Éditeurs sous Ubuntu

Un [[Éditeur de texte|éditeur]] est un logiciel pour créer et modifier des fichiers texte : nano, [[Vim]], [[Gedit]].

## APT (*Advanced Package Tool*)

[[APT]] est un outil puissant et souple pour installer, supprimer, mettre à jour et mettre à niveau des paquets.

```bash
sudo apt update    # télécharge seulement la liste des nouvelles versions disponibles dans les dépôts
sudo apt upgrade   # installe les nouvelles versions des paquets installés, après apt update
```

## Script Bash

- Chaque [[Script Bash]] commence par `#! /bin/bash`.
- `#!` s'appelle le [[Shebang]] : il indique au système quel interpréteur doit exécuter le script. Par exemple, `#! /usr/bin/python3` fait interpréter le script par Python.
- Un guide des options (`-o`, `-l`, `-a`…) est donné en lien : https://ioflood.com/blog/bash-options/

## Annotations de l'étudiante

Elle note que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine, et suppose un défaut de son Debian.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Nombre de liens : liens symboliques »** : la colonne de `ls -l` compte les liens physiques (*hard links*), pas les liens symboliques (complément).
2. **`chmod +w` « visiblement pas les autres »** : comportement normal dû au masque `umask`, pas à un défaut de Debian (complément).
3. **Exemple 703** : « droit d'exécuter et d'écrire aux autres membres » est juste (3 = w+x).
