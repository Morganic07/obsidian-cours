---
type: concept
aliases: [file system, file systems, partitionnement, partition, NTFS, FAT32, exFAT, ext4, EXT4, XFS]
matieres: [Operating System]
sources: ["[[OS - chp 2]]", "[[OS - chp 3]]"]
maj: 2026-11-05
---

Méthode d'organisation et de stockage des fichiers sur un support. Il suit l'emplacement des fichiers et leurs attributs (taille, permissions, dates). Un disque doit être formaté, sinon on ne peut ni lire ni écrire dessus : le formatage crée le système de fichiers que gère le système d'exploitation.

**Partitionnement** : diviser le disque en sections logiques. Chacune est vue comme un disque séparé, peut avoir son système de fichiers, et une partition endommagée n'affecte pas les autres. Sous Windows, plusieurs racines (C:, D:…) ; sous Linux, une seule racine `/`.

| Système | Gros fichiers | Chiffrement | Compression | Compatibilité |
|---|---|---|---|---|
| NTFS | oui | oui | oui | Windows, macOS, Linux |
| FAT32 | non (4 Go max par fichier) | non | non | Windows, macOS, Linux |
| exFAT | oui | non | non | Windows, macOS, Linux |
| ReFS | oui | oui | oui | Windows Server |
| EXT4, XFS | jusqu'à 1 Eo | oui | oui | Linux |
| NFS | jusqu'à 8 Eo | non | non | Linux, macOS |

Linux reconnaît tous les systèmes, Windows seulement les siens. Partitions demandées par Ubuntu : swap (utilisée quand la RAM est pleine), racine `/`, partition EFI, zone de boot BIOS réservée, `/home`.

Liens : [[Hiérarchie de stockage]], [[BIOS et UEFI]], [[Distribution Linux]]

Résumé : [[OS - chp 2 (résumé)]], [[OS - chp 3 (résumé)]]
