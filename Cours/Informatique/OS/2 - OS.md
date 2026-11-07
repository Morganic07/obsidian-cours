---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]] (« Chapter 2 »), dans [[Cours/Informatique/OS/_index|Operating System]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Stockage secondaire : interfaces de connexion, disques, partitions, systèmes de fichiers, puis démarrage (MBR, BIOS, UEFI). Voir [[Hiérarchie de stockage]].

## Interfaces de stockage secondaire (*Secondary Storage Interface*)

L'interface est la méthode de connexion et de communication entre le [[Disque dur]] et le reste de l'ordinateur ([[Interface de stockage]]). Plusieurs types :

1. **IDE** (*Integrated Drive Electronics*) = **PATA** ([[IDE (PATA)]]) : ancienne interface pour disques durs et lecteurs optiques ; câbles parallèles à 40 ou 80 broches.
2. **[[SATA]]** (*Serial ATA*) : l'interface la plus courante aujourd'hui ; connexion série, plus rapide et plus efficace que l'IDE.
3. **[[SCSI]]** (*Small Computer System Interface*) : souvent utilisée pour les serveurs et les stations de travail.
4. **SAS** (*Serial Attached SCSI*, [[SAS (interface de stockage)]]) : version plus récente et plus rapide de SCSI.
5. **[[NVMe]]** (*Non-Volatile Memory Express*) : surtout pour les [[SSD]], mais certains disques durs modernes en ont des implémentations ; connexion extrêmement rapide, souvent via [[PCI Express|PCIe]].

Tableau du cours, « du moins rapide au plus rapide » :

| Niveau | Interface | Vitesse maximale | Signification |
|---|---|---|---|
| 1 | IDE | 133 MB/s | Integrated Drive Electronics |
| 1 | SCSI | jusqu'à 12 GB/s | Small Computer System Interface |
| 2 | SATA | 600 MB/s | Serial Advanced Technology Attachment |
| 2 | SAS | 12 Gbps | Serial Attached SCSI |
| 3 | NVMe | 32 Gbps | Non-Volatile Memory Express |

![[OS - chp 2 - image10.png]]
*Figure : disque dur Seagate Barracuda ATA IV de 3,5 pouces : connecteur IDE à 40 broches, cavaliers de configuration, connecteur d'alimentation Molex.*

Annotations du dessin : « IDE port » ; « Port for Master or Slave status » (les cavaliers).

![[OS - chp 2 - image5.png]]
*Figure : cinq supports, du plus grand au plus petit : HDD 2,5" SATA, SSD 2,5" SATA, SSD [[M.2]] SATA, SSD M.2 NVMe, SSD mSATA.*

## Le disque dur (HDD)

- Un HDD est un disque magnétique qui tourne en moyenne à **7 200 RPM** (tours par minute) ; la tête (« tige métallique ») lit ou écrit les données.
- On grave des points magnétiques sur le disque : un point = 1, pas de point = 0 ([[Numération binaire|binaire]]).
- Selon la note, le HDD est plus fiable que le SSD : si le disque est abîmé, les données restent lisibles, alors qu'une puce de SSD cassée rend les données irrécupérables. Le plus fiable serait la [[Bande magnétique]] (« utilisée dans les boîtes noires d'avion »).

![[OS - chp 2 - image7.png]]
*Figure : disque dur ouvert : plateau métallique, axe central, bras de lecture et sa tête.*

## Partitionner le disque dur

- Sous Windows, la [[Partition (disque)|partition]] principale est **C:** ; historiquement, A: et B: étaient réservés aux disquettes.

![[OS - chp 2 - image6.png]]
*Figure : Explorateur Windows avec quatre lecteurs : Win10 (C:), 46,6 Go libres sur 195 ; ENSEA (D:), 22,6 sur 182 ; General (E:), 22,1 sur 97,6 ; Google Drive (G:), 5,92 sur 15.*

- **Disque principal** (*primary drive*) : là où est l'OS (C:).
- **Disques secondaires** : là où sont les données (D:, E:…).

![[OS - chp 2 - image3.png]]
*Figure : plateau de disque dur divisé en zones colorées, illustrant le partitionnement.*

- Une couleur = une partition ; « si la partition est endommagée, on parle de [[Secteur défectueux|bad sector]] ».
- **Partitionner**, c'est diviser le disque en plusieurs sections logiques.
- Chaque partition est traitée comme un disque séparé par l'OS : si l'une est endommagée, les autres ne sont pas touchées.
- Chaque partition peut être formatée avec un système de fichiers différent.
- **[[Formatage d'un disque|Formater]]** est indispensable, sinon on ne peut ni lire ni écrire : le formatage crée un système de fichiers géré par l'OS.
  - systèmes de fichiers Windows : NTFS, [[FAT32]], [[Système de fichiers exFAT|exFAT]], [[ReFS]] ;
  - systèmes de fichiers [[Linux]] : [[EXT4]], [[XFS]], [[NFS]].

## Système de fichiers (*File system*)

- **[[Système de fichiers]]** : méthode d'organisation et de stockage des fichiers sur un support.
- Il garde la trace de l'emplacement des fichiers sur le support et de leurs attributs : taille, permissions, horodatages.

| Système | Gros fichiers et dossiers | Chiffrement | Compression | Compatibilité |
|---|---|---|---|---|
| **[[NTFS]]** | oui | oui | oui | Windows, macOS, Linux |
| **FAT32** | non | non | non | Windows, macOS, Linux |
| **exFAT** | oui | non | non | Windows, macOS, Linux |
| **ReFS** | oui | oui | oui | Windows Server |
| **EXT4** | jusqu'à 1 exaoctet | oui | oui | Linux |
| **XFS** | jusqu'à 1 exaoctet | oui | oui | Linux |
| **NFS** | jusqu'à 8 exaoctets | non | non | Linux, macOS |

- NTFS gère des fichiers de plus de 4 Go, contrairement à FAT32, limité à **4 Go par fichier**.
- Linux reconnaît tous ces systèmes ; Windows ne reconnaît que les siens.

## MBR (*Master Boot Record*)

Comment le *firmware* (BIOS ou UEFI, voir [[BIOS et UEFI]]) reconnaît-il l'OS ? Grâce au **[[MBR]]**, situé sur le disque dur.

- Le MBR indique sur quelle partition se trouve l'OS.
- Il gère aussi les partitions du support. Analogie du livre :
  - le MBR est la table des matières ;
  - les partitions sont les chapitres ;
  - l'OS est le texte, ce que l'ordinateur doit « lire » pour fonctionner ;
  - le MBR dit par quel chapitre commencer.
- Si le MBR est endommagé ou corrompu, l'ordinateur ne trouve pas l'OS.
- **Fonctions du MBR** :
  - identifier l'emplacement de l'OS sur le support ;
  - charger l'OS en mémoire ([[Mémoire vive|RAM]]) ;
  - gérer les partitions du support ;
  - permettre de démarrer sur différents systèmes d'exploitation.
- Même avec plusieurs OS sur le disque, il n'y a qu'un MBR ; il est indépendant de l'OS.

## BIOS (*Basic Input Output System*)

- *Firmware* stocké sur une puce de la [[Carte mère]].
- Fonctions :
  - identifier et configurer le matériel ;
  - effectuer le POST (*power-on self-test*) pour vérifier le matériel ;
  - charger l'OS du support de stockage vers la mémoire.
- Le BIOS équipait les anciens PC ; on a maintenant l'UEFI.

## UEFI (*Unified Extensible Firmware Interface*)

- *Firmware* stocké sur une puce de la carte mère, plus récent que le BIOS.
- Fonctions :
  - identifier et configurer le matériel ;
  - charger l'OS du support vers la mémoire ;
  - fournir une [[Interface graphique]] (GUI) pour configurer l'ordinateur ;
  - démarrage plus rapide et plus sûr ([[Démarrage sécurisé|secure boot]]) ;
  - prise en charge de plus gros supports de stockage.

## BIOS ou UEFI

| Caractéristique | BIOS | UEFI |
|---|---|---|
| Taille maximale du support | 2,2 To | 9,4 Zo |
| Temps de démarrage | lent | rapide |
| Options de *secure boot* | limitées | étendues |
| Réseau | non | oui |
| Administration à distance | non | oui |
| Interface graphique | non | oui |

## Erreurs du cours

- Le tableau des interfaces de [[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]] écrit « SCSI : Up to 12GB/s » ; il faut une valeur inférieure à celle de SAS (« 12Gbps », soit environ 1,5 Go/s), puisque le cours présente SAS comme « une version plus récente et plus rapide de SCSI ». Le tableau mélange aussi les unités (MB/s, GB/s, Gbps).
