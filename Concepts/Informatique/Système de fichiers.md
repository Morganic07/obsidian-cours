---
type: concept
tags: [year2]
aliases: [file system, file systems, partitionnement]
matieres: [Operating System]
sources: ["[[2 - OS|OS - chp 2]]", "[[3 - OS|OS - chp 3]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-06
---

Méthode d'organisation et de stockage des fichiers sur un support. Il suit l'emplacement des fichiers et leurs attributs (taille, permissions, dates). Un disque doit être formaté, sinon on ne peut ni lire ni écrire dessus : le [[Formatage d'un disque|formatage]] crée le système de fichiers que gère le système d'exploitation.

**[[Partition (disque)|Partitionnement]]** : diviser le disque en sections logiques. Chacune est vue comme un disque séparé, peut avoir son système de fichiers, et une partition endommagée n'affecte pas les autres. Sous Windows, plusieurs racines (C:, D:…) ; sous Linux, une seule racine `/`.

| Système | Gros fichiers | Chiffrement | Compression | Compatibilité |
|---|---|---|---|---|
| [[NTFS]] | oui | oui | oui | Windows, macOS, Linux |
| [[FAT32]] | non (4 Go max par fichier) | non | non | Windows, macOS, Linux |
| [[Système de fichiers exFAT\|exFAT]] | oui | non | non | Windows, macOS, Linux |
| [[ReFS]] | oui | oui | oui | Windows Server |
| [[EXT4]], [[XFS]] | jusqu'à 1 Eo | oui | oui | Linux |
| [[NFS]] | jusqu'à 8 Eo | non | non | Linux, macOS |

Linux reconnaît tous les systèmes, Windows seulement les siens. Partitions demandées par Ubuntu : swap (utilisée quand la RAM est pleine), racine `/`, partition EFI, zone de boot BIOS réservée, `/home`.

**Arborescence Linux** (chapitre 4) : `/bin` et `/sbin` pour les commandes, `/etc` pour la configuration, `/home` pour les utilisateurs, `/usr` pour les logiciels, `/var` pour les données variables. Partitions conseillées : racine, `/home`, `/boot` et swap (voir [[Partitions Linux]]).

Voir aussi : [[Partition (disque)]], [[Formatage d'un disque]], [[NTFS]], [[FAT32]], [[Système de fichiers exFAT]], [[ReFS]], [[EXT4]], [[XFS]], [[NFS]], [[Partitions Linux]], [[Hiérarchie de stockage]], [[BIOS et UEFI]], [[Distribution Linux]]

Résumés : [[2 - OS]], [[3 - OS]], [[4 - OS]]
