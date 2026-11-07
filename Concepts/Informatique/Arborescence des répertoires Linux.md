---
type: concept
tags: [year2]
aliases: [Linux directory structure, directory structure, arborescence Linux, hiérarchie des répertoires]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[OS - chp 5 (résumé)|OS - chp 5]]"]
maj: 2026-11-06
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

## À vérifier

Le cours décrit `/usr` comme « user-specific files » : description contestable (signalé par le résumé).

Résumés : [[OS - chp 4 (résumé)]], [[OS - chp 5 (résumé)]]
