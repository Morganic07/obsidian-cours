---
type: source
sources: ["[[OS - chp 2]]"]
maj: 2026-11-05
---

Résumé de [[OS - chp 2]], dans [[Year 2 - Operating System]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été rouvertes.

## Idée générale

Stockage secondaire : interfaces de connexion, disques, partitions, systèmes de fichiers, puis démarrage (MBR, BIOS, UEFI).

## Contenu, dans l'ordre du cours

- **Interfaces** : IDE/PATA (ancien), SATA (série, le plus courant), SCSI et SAS (serveurs et stations), NVMe (SSD). Tableau de vitesses du cours : IDE 133 Mo/s, SCSI jusqu'à 12 Go/s, SATA 600 Mo/s, SAS 12 Gbit/s, NVMe 32 Gbit/s. Voir [[Hiérarchie de stockage]].
- **HDD** : disque magnétique à environ 7 200 tr/min, une tête lit et écrit ; un point magnétique vaut 1, son absence 0. L'étudiant écrit que le HDD est plus fiable que le SSD, car les données d'un disque abîmé restent lisibles, et que la bande magnétique est la plus fiable (boîtes noires d'avion).
- **Partitions** : voir [[Système de fichiers]]. Disque principal (système, C:) et disques secondaires (données, D:, E:).
- **Systèmes de fichiers** : tableau NTFS / FAT32 / exFAT / ReFS / EXT4 / XFS / NFS, voir [[Système de fichiers]].
- **MBR, BIOS, UEFI** : voir [[BIOS et UEFI]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Tableau des interfaces** : il mélange des unités (Mo/s, Go/s, Gbit/s), si bien que l'ordre « du moins rapide au plus rapide » n'est pas lisible directement (complément). Le niveau « SCSI jusqu'à 12 Go/s » paraît incohérent avec « SAS 12 Gbit/s » (successeur plus rapide).
2. **Fiabilité HDD, SSD, bandes** : affirmation de l'étudiant, non vérifiée ; la mention des boîtes noires est douteuse (complément).
3. **NFS** classé comme système de fichiers Linux : c'est un système de fichiers réseau (complément).
4. **Légende « bad sector »** : le texte associe une couleur de partition à un secteur défectueux ; un *bad sector* est une zone physique abîmée, pas une partition.
5. **Fausses alertes** : les « À vérifier » sur la photo du disque (étiquette illisible) et sur le texte miroir des SSD ne portent pas sur le contenu du cours.
