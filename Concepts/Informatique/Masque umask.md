---
type: concept
tags: [year2]
aliases: [umask, masque de création de fichiers, file mode creation mask]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]]", "[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le umask est un masque octal, propre à chaque processus (et hérité par ses fils), qui indique les [[Permissions Unix|droits]] retirés par défaut aux fichiers et répertoires créés.

Les droits de départ sont `666` (rw-rw-rw-) pour un fichier et `777` (rwxrwxrwx) pour un répertoire ; on leur retire les bits présents dans le masque (au sens des bits, pas d'une soustraction décimale) :

| Masque | Fichier créé | Répertoire créé |
|---|---|---|
| `022` (valeur courante) | `644` (rw-r--r--) | `755` (rwxr-xr-x) |
| `077` | `600` (rw-------) | `700` (rwx------) |
| `002` | `664` (rw-rw-r--) | `775` (rwxrwxr-x) |

Avec `022`, l'écriture est retirée au groupe et aux autres.

- `umask` affiche le masque courant ; `umask -S` l'affiche en symbolique (`u=rwx,g=rx,o=rx`).
- `umask 077` le change pour le shell courant et les commandes qu'il lance ; pour le rendre durable, on l'écrit dans `~/.bashrc` ou `~/.profile`.
- Une commande lancée par [[Commande sudo|sudo]] a par défaut un masque au moins aussi strict que `022`.

**Effet sur chmod** : le masque s'applique aussi aux formes symboliques de [[Commande chmod|chmod]] écrites sans cible `u`, `g`, `o` ou `a`. D'après `man chmod`, sans cible l'effet est celui de `a`, mais les bits présents dans le umask ne sont pas modifiés. Avec `022`, `chmod +w` ne donne donc l'écriture qu'au propriétaire, alors que `chmod +r` et `chmod +x` valent pour tous. Pour forcer l'ajout : `chmod a+w` (tous) ou `chmod go+w` (groupe et autres).

## Dans le cours

Le cours ne nomme pas le umask. Il explique l'observation de la fiche [[5 - OS]] et de [[8 - OS commandes sh]] : `sudo chmod +w file.txt` n'ajoute l'écriture qu'au propriétaire, alors que `+r` et `+x` valent pour tous, et l'étudiant soupçonne sa configuration ; c'est en fait le comportement normal.

Voir aussi : [[Permissions Unix]], [[Commande chmod]], [[Processus]].

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
