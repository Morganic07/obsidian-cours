---
type: concept
aliases: [chmod, permissions Unix, permissions d'un fichier, file permissions, droits d'accès]
matieres: [Operating System]
sources: ["[[OS - chp 5]]", "[[cours TP1]]"]
maj: 2026-11-05
---

`ls -l` affiche par fichier : type (`d` répertoire, `-` fichier), neuf caractères de permissions (trois groupes : propriétaire, groupe, autres), nombre de liens, propriétaire, groupe, taille en octets, date de modification, nom.

Valeurs octales : `r` = 4 (lecture), `w` = 2 (écriture), `x` = 1 (exécution), `-` = 0.

`chmod` change les permissions. En octal : `chmod 754` donne 7 (rwx) au propriétaire, 5 (r-x) au groupe, 4 (r--) aux autres ; `chmod 703` donne tous les droits au propriétaire, aucun au groupe, écriture et exécution aux autres. En symbolique : `+x`, `+w`, `+r`, `+rwx`. L'option `-R` agit récursivement sur un dossier.

Le cours observe que `chmod +w` n'ajoute l'écriture qu'au propriétaire sur sa machine (l'étudiant soupçonne sa configuration). C'est le comportement normal de la plupart des systèmes (complément : le masque `umask` s'applique aux formes symboliques sans cible).

Liens : [[Shell et Bash]], [[Script Bash]]

Résumé : [[OS - chp 5 (résumé)]]
