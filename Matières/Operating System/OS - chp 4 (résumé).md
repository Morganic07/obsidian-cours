---
type: source
tags: [year2]
sources: [".raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf"]
maj: 2026-11-06
---

Résumé du PDF OS - chp 4 (`.raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf`) (4 pages, en anglais), dans [[Operating System (matière)]]. C'est le chapitre 4, absent jusqu'ici du coffre : la matière passe du chapitre 3 au chapitre 5.

## Idée générale

Organisation hiérarchique des fichiers de Linux, rôle du répertoire racine, et partitions usuelles. Voir [[Système de fichiers]] et [[Distribution Linux]].

## Contenu, dans l'ordre du cours

- **Arborescence Linux** : hiérarchie de répertoires sous la racine `/`. Répertoires principaux : `/bin` (binaires exécutables), `/boot` (noyau, `initrd`), `/dev` (fichiers de périphériques), `/etc` (configuration, `passwd`, `fstab`), `/home` (répertoires des utilisateurs), `/lib` (bibliothèques partagées), `/sbin` (binaires d'administration), `/tmp` (fichiers temporaires), `/var` (journaux, files d'attente), `/usr` (applications et bibliothèques).
- **Répertoire racine** : point de départ de tout le système de fichiers. Il contient les binaires système, les bibliothèques essentielles, les fichiers de configuration, les fichiers de périphériques, les points de montage et des sous-répertoires.
- **Partitions Linux** : racine (`/`, noyau, programmes de base, créée en premier), `/home` (données des utilisateurs, séparée pour que les mises à jour n'y touchent pas), `/usr` (logiciels tiers), `/var` (données qui changent souvent), `/boot` (noyau, `initrd`, configuration du chargeur de démarrage ; petite, 100 à 500 Mo), swap (extension de la mémoire vive, plus lente), partition amorçable (celle qui contient ce qu'il faut pour démarrer). Voir aussi [[BIOS et UEFI]] et [[Noyau]].
- **Bilan** : les partitions séparent les fichiers système des données, améliorent la sécurité et simplifient les mises à jour.

## Points à vérifier

1. **`/etc/passwd`** est décrit comme contenant « les mots de passe des utilisateurs ». Dans un système Linux actuel, les mots de passe hachés sont dans `/etc/shadow` (complément).
2. **`/usr`** est décrit comme « fichiers propres à l'utilisateur » et la partition `/usr` comme destinée aux logiciels tiers. `/usr` contient la majorité des programmes et bibliothèques du système lui-même (complément : usage courant).
