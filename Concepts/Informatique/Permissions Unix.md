---
type: concept
tags:
  - year2
aliases:
  - permissions Unix
  - permissions d'un fichier
  - file permissions
  - droits d'accès
  - chmod -R
  - octal permissions
  - valeurs octales
matieres:
  - Operating System
sources:
  - "[[5 - OS|OS - chp 5]]"
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/OS - chp 5.docx|OS - chp 5]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"
maj: 2026-11-08
---

Droits de lecture, d'écriture et d'exécution, attribués au propriétaire, au groupe et aux autres.

`ls -l` ([[Commande ls]]) affiche par fichier : type (`d` répertoire, `-` fichier), neuf caractères de permissions (trois groupes : propriétaire, groupe, autres), nombre de liens, propriétaire, groupe, taille en octets, date de modification, nom.

Valeurs octales : `r` = 4 (lecture), `w` = 2 (écriture), `x` = 1 (exécution), `-` = 0.

La commande [[Commande chmod|chmod]] (change mode) change les permissions. En octal : `chmod 754` donne 7 (rwx) au propriétaire, 5 (r-x) au groupe, 4 (r--) aux autres ; `chmod 703` donne tous les droits au propriétaire, aucun au groupe, écriture et exécution aux autres. En symbolique : `+x`, `+w`, `+r`, `+rwx`. L'option `-R` agit récursivement sur un dossier, par exemple `chmod -R 444 semester/`. Donner le droit `x` est ce qui permet de lancer un script ([[Exécution d'un script]]) ; voir aussi [[Commande sudo]].

Le cours observe que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine.

C'est le comportement normal de la plupart des systèmes, pas un problème de configuration : le [[Masque umask]] s'applique aux formes symboliques sans cible (`+w` au lieu de `a+w`). [[Complément hors du cours|ⓘ]]

## Compléments (hors du cours)

**Droits sur un répertoire** : leur sens diffère de celui d'un fichier.

| Droit | Sur un fichier | Sur un répertoire |
|---|---|---|
| `r` | lire le contenu | lister les noms qu'il contient (`ls`) |
| `w` | modifier le contenu | créer, renommer ou supprimer les fichiers qu'il contient |
| `x` | exécuter | y entrer (`cd`) et accéder aux fichiers qu'il contient |

Supprimer un fichier dépend donc du droit `w` sur le **répertoire** qui le contient, pas des droits du fichier lui-même.

**Forme symbolique complète** : `chmod [ugoa][+-=][rwx]`, avec les cibles `u` (propriétaire, *user*), `g` (groupe), `o` (autres, *others*), `a` (tous, *all*) et les opérateurs `+` (ajouter), `-` (retirer), `=` (fixer exactement).

- `chmod u+x script.sh` : exécution pour le propriétaire ;
- `chmod go-w fichier` : retire l'écriture au groupe et aux autres ;
- `chmod a+w fichier` : écriture pour tous, sans tenir compte du umask ;
- `chmod a=r fichier` : équivaut à `chmod 444` ;
- `chmod u=rwx,g=rx,o=r fichier` : équivaut à `chmod 754`.

**Valeurs usuelles** : `755` (rwxr-xr-x) pour les scripts et les répertoires, `644` (rw-r--r--) pour un fichier ordinaire, `600` (rw-------) pour un fichier privé ; `777` (tous les droits pour tous) est à éviter. Sur ses propres fichiers, `chmod` n'a pas besoin de [[Commande sudo|sudo]] : le propriétaire peut toujours changer leurs permissions.

**Autres types de fichiers** dans le premier caractère de `ls -l` : `l` [[Lien symbolique|lien symbolique]], `c` périphérique en mode caractère, `b` périphérique en mode bloc ([[Fichier de périphérique]]), `p` tube nommé, `s` socket.

**Propriétaire et groupe** : `chown utilisateur:groupe fichier` change le propriétaire et le groupe (réservé à [[Super-utilisateur root|root]]), `chgrp groupe fichier` change seulement le groupe.

Liens : [[Shell et Bash]], [[Script Bash]]

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
