---
type: concept
tags: [year2]
aliases: [Linux directory structure, directory structure, arborescence Linux, hiérarchie des répertoires]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[5 - OS|OS - chp 5]]"]
maj: 2026-11-07
---

Système hiérarchique dont le sommet est la racine `/`. Répertoires principaux :

| Répertoire | Contenu |
|---|---|
| `/bin` | binaires exécutables |
| `/boot` | noyau, initrd |
| `/dev` | fichiers de périphériques |
| `/etc` | configuration (passwd, fstab) |
| `/home` | répertoires des utilisateurs |
| `/lib` | bibliothèques partagées |
| `/sbin` | binaires d'administration |
| `/tmp` | fichiers temporaires, effacés au redémarrage |
| `/var` | journaux, spool |
| `/usr` | applications et bibliothèques |

Notion parente : [[Système de fichiers]]. Voir aussi : [[Répertoire racine]], [[Répertoire personnel]], [[Fichier de périphérique]], [[Bibliothèque partagée]], [[Fichier journal]], [[Image initrd]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]] écrit « /usr: This directory contains user-specific files, such as applications and libraries » ; il faut « fichiers partagés par tous les utilisateurs (applications et bibliothèques) » : les fichiers propres à chaque utilisateur sont dans `/home` (complément, hors du cours).

Résumés : [[4 - OS]], [[5 - OS]]
