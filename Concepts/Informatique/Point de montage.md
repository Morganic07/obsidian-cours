---
type: concept
tags: [year2]
aliases: [mount point, mount points, points de montage, fstab]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-08
---

Répertoires spéciaux qui indiquent où les partitions sont montées, pour accéder aux différents volumes depuis la racine. Le fichier `/etc/fstab` indique quelles partitions monter.

## Compléments (hors du cours)

**Format de `/etc/fstab`** : une ligne par système de fichiers, six champs séparés par des espaces.

| Champ | Rôle | Exemple |
|---|---|---|
| 1. périphérique | partition à monter, de préférence par `UUID=…` | `UUID=3f2a…` ou `/dev/sda1` |
| 2. point de montage | répertoire d'accueil | `/`, `/home`, `/boot/efi` |
| 3. type | système de fichiers | `ext4`, `vfat`, `swap` |
| 4. options | options de montage | `defaults`, `ro`, `noatime` |
| 5. dump | sauvegarde par `dump` (presque toujours 0) | `0` |
| 6. fsck | ordre de vérification au démarrage : 1 pour la racine, 2 pour les autres, 0 pour aucune | `1` |

```
UUID=3f2a…  /          ext4  defaults  0  1
UUID=8C1D…  /boot/efi  vfat  umask=0077  0  1
```

L'UUID, identifiant propre au système de fichiers (affiché par `blkid` ou `lsblk -f`), reste stable si l'on ajoute ou débranche un disque, contrairement à `/dev/sda1` dont la lettre peut changer.

**Points de montage usuels** : `/mnt` (montage manuel temporaire), `/media` (supports amovibles, montés automatiquement par l'environnement de bureau), `/boot/efi` ([[Partition système EFI]]).

**Commandes** : `lsblk` (arbre des disques et partitions avec leurs points de montage), `mount /dev/sdb1 /mnt` (monter), `umount /mnt` (démonter), `mount` seul (lister les montages), [[Commande df|df -h]] (espace occupé par système de fichiers monté).

Notion parente : [[Répertoire racine]]. Voir aussi : [[Partition (disque)]], [[Partitions Linux]], [[Système de fichiers]], [[Arborescence des répertoires Linux]].

Résumés : [[4 - OS]]
