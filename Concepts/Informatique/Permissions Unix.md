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
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
maj: 2026-11-07
---

Droits de lecture, d'écriture et d'exécution, attribués au propriétaire, au groupe et aux autres.

`ls -l` ([[Commande ls]]) affiche par fichier : type (`d` répertoire, `-` fichier), neuf caractères de permissions (trois groupes : propriétaire, groupe, autres), nombre de liens, propriétaire, groupe, taille en octets, date de modification, nom.

Valeurs octales : `r` = 4 (lecture), `w` = 2 (écriture), `x` = 1 (exécution), `-` = 0.

La commande [[Commande chmod|chmod]] (change mode) change les permissions. En octal : `chmod 754` donne 7 (rwx) au propriétaire, 5 (r-x) au groupe, 4 (r--) aux autres ; `chmod 703` donne tous les droits au propriétaire, aucun au groupe, écriture et exécution aux autres. En symbolique : `+x`, `+w`, `+r`, `+rwx`. L'option `-R` agit récursivement sur un dossier, par exemple `chmod -R 444 semester/`. Donner le droit `x` est ce qui permet de lancer un script ([[Exécution d'un script]]) ; voir aussi [[Commande sudo]].

Le cours observe que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine (l'étudiant soupçonne sa configuration). C'est le comportement normal de la plupart des systèmes (complément : le masque `umask` s'applique aux formes symboliques sans cible).

Liens : [[Shell et Bash]], [[Script Bash]]

Résumés : [[5 - OS]], [[8 - OS commandes sh]]
