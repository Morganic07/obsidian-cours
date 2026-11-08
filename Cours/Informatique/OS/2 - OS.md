---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]] (« Chapter 2 »), dans [[Cours/Informatique/OS/_index|Operating System]].
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
| 1 | SCSI | jusqu'à 320 MB/s (Ultra-320) [[Erreurs du cours#^e-2-os\|✎]] | Small Computer System Interface |
| 2 | SATA | 600 MB/s | Serial Advanced Technology Attachment |
| 2 | SAS | 12 Gbps | Serial Attached SCSI |
| 3 | NVMe | 32 Gbps | Non-Volatile Memory Express |

Pour comparer ces valeurs, il faut distinguer **bits** et **octets** : « Gbps » ou « Gb/s » compte des gigabits par seconde, « GB/s » ou « Go/s » des gigaoctets, et 1 octet = 8 bits. Les liaisons série ajoutent en plus des bits de contrôle : le SATA III circule à 6 Gbit/s, mais son codage 8b/10b (10 bits transmis pour 8 utiles) ramène le débit utile à $6 \times \frac{8}{10} = 4{,}8$ Gbit/s, soit 600 Mo/s, la valeur du tableau. Les 32 Gbit/s du NVMe correspondent à quatre voies PCIe 3.0 (environ 3,9 Go/s) ; en PCIe 4.0, on double (environ 7,9 Go/s). [[Complément hors du cours|ⓘ]]

Trois notions sont souvent confondues : le **format** (*form factor*, la forme physique : 2,5", 3,5", [[M.2]]), l'**interface** (le lien électrique : SATA, [[PCI Express|PCIe]]) et le **protocole** (le langage de commandes : AHCI pour le SATA, [[NVMe]] pour le PCIe). Un SSD M.2 peut ainsi être SATA (aussi lent qu'un SSD 2,5" SATA) ou NVMe : la forme ne dit pas la vitesse. NVMe a été conçu pour la mémoire flash, avec des milliers de files de commandes en parallèle, là où AHCI, pensé pour les disques tournants, n'en a qu'une. [[Complément hors du cours|ⓘ]]

![[OS - chp 2 - image10.png]]
*Figure : disque dur Seagate Barracuda ATA IV de 3,5 pouces : connecteur IDE à 40 broches, cavaliers de configuration, connecteur d'alimentation Molex.*

Annotations du dessin : « IDE port » ; « Port for Master or Slave status » (les cavaliers).

Un câble IDE porte **deux** appareils : l'un réglé en *master* (maître), l'autre en *slave* (esclave), par la position du cavalier ; deux appareils sur le même réglage empêchaient le démarrage. Les deux se partageaient la bande passante du câble, alors qu'en SATA chaque disque a son propre câble point à point, plus fin, sans cavalier, et branchable à chaud. [[Complément hors du cours|ⓘ]]

![[OS - chp 2 - image5.png]]
*Figure : cinq supports, du plus grand au plus petit : HDD 2,5" SATA, SSD 2,5" SATA, SSD [[M.2]] SATA, SSD M.2 NVMe, SSD mSATA.*

## Le disque dur (HDD)

- Un HDD est un disque magnétique qui tourne en moyenne à **7 200 RPM** (tours par minute) ; la tête (« tige métallique ») lit ou écrit les données.
- On grave des points magnétiques sur le disque : un point = 1, pas de point = 0 ([[Numération binaire|binaire]]).
  - Plus précisément, la surface est couverte de minuscules zones dont l'aimantation est orientée dans un sens ou dans l'autre ; la tête, qui flotte à quelques nanomètres au-dessus du plateau sans le toucher, change cette orientation pour écrire et la détecte pour lire. Les données sont rangées en **pistes** concentriques, découpées en **secteurs** (512 octets historiquement, 4 096 octets sur les disques récents) ; les pistes de même rayon sur tous les plateaux forment un **cylindre**. [[Complément hors du cours|ⓘ]]
  - Le **temps d'accès** d'un HDD est la somme du temps de recherche (*seek time*, déplacer le bras jusqu'à la piste, quelques millisecondes) et de la **latence rotationnelle** (attendre que le secteur passe sous la tête). À 7 200 tr/min, un tour dure $\frac{60}{7\,200} \approx 8{,}33$ ms, et l'attente moyenne est d'un demi-tour, soit $\approx 4{,}17$ ms. D'où des accès en millisecondes, contre des dizaines de microsecondes pour un SSD, qui n'a aucune pièce mobile. [[Complément hors du cours|ⓘ]]
- Selon la note, le HDD est plus sûr que le SSD pour récupérer les données : si le disque est abîmé, les données restent lisibles, alors qu'une puce de SSD cassée rend les données irrécupérables. Le plus durable serait la [[Bande magnétique]], longtemps utilisée dans les boîtes noires d'avion. [[Erreurs du cours#^e-2-os|✎]]
  - La fiabilité dépend du type de panne. Le HDD est mécanique : il craint les chocs (la tête peut rayer le plateau) et l'usure du moteur, mais une récupération en laboratoire reste souvent possible. Le SSD ne craint pas les chocs ; ses cellules de mémoire flash supportent un nombre limité d'écritures, mais le contrôleur répartit l'usure entre elles (*wear leveling*) et l'endurance des modèles courants suffit à des années d'usage normal ; c'est la panne soudaine du contrôleur qui rend les données difficiles à récupérer. [[Complément hors du cours|ⓘ]]
  - Les boîtes noires d'avion ont enregistré sur bande magnétique jusqu'aux années 1990, puis les compagnies sont passées à des enregistreurs à mémoire flash (*solid-state*) dans un boîtier blindé, plus fiables (NTSB, recommandations A-99-16 à 18, 1999). La bande reste en revanche le support d'archivage des data centers : peu coûteuse, durable et conservée hors ligne. [[Complément hors du cours|ⓘ]]
  - Aucun support ne dispense de [[Sauvegarde de fichier|sauvegardes]] : la règle classique « 3-2-1 » recommande trois copies des données, sur deux supports différents, dont une hors site. [[Complément hors du cours|ⓘ]]

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
  - Un secteur défectueux est une zone physique du disque (un secteur) qui ne se lit ou ne s'écrit plus correctement ; le disque le remplace par un secteur de réserve et le système de fichiers l'écarte. Il peut toucher n'importe quelle partition sans rendre toute la partition inutilisable ; leur multiplication annonce en revanche une panne du disque, ce que surveille l'auto-diagnostic **S.M.A.R.T.** des disques (lisible sous Linux avec `smartctl`). [[Complément hors du cours|ⓘ]]
- **Partitionner**, c'est diviser le disque en plusieurs sections logiques.
- Chaque partition est traitée comme un disque séparé par l'OS : si l'une est endommagée, les autres ne sont pas touchées.
- Chaque partition peut être formatée avec un système de fichiers différent.
- La liste des partitions est rangée dans une **table de partitions**, au début du disque. Il en existe deux formats : la table du [[MBR]] (ancienne, 4 partitions principales au plus, ou 3 principales et une **étendue** qui contient des partitions **logiques** ; disques de 2,2 To au plus) et la table **GPT** (*GUID Partition Table*, associée à l'UEFI : 128 partitions par défaut, disques de très grande taille, copie de secours de la table en fin de disque). Voir [[Table de partitions GPT]]. [[Complément hors du cours|ⓘ]]
- Sous Linux, il n'y a pas de lettres : chaque disque et chaque partition est un [[Fichier de périphérique|fichier de périphérique]] dans `/dev`, par exemple `/dev/sda` pour le premier disque SATA et `/dev/sda1` pour sa première partition, ou `/dev/nvme0n1p1` pour la première partition d'un SSD NVMe ; une partition devient accessible une fois **montée** dans l'arborescence ([[Point de montage]]). `lsblk` affiche disques et partitions, `fdisk -l` ou `parted -l` (en root) leurs tables. [[Complément hors du cours|ⓘ]]
- **[[Formatage d'un disque|Formater]]** est indispensable, sinon on ne peut ni lire ni écrire : le formatage crée un système de fichiers géré par l'OS.
  - systèmes de fichiers Windows : NTFS, [[FAT32]], [[Système de fichiers exFAT|exFAT]], [[ReFS]] ;
  - systèmes de fichiers [[Linux]] : [[EXT4]], [[XFS]] ; [[NFS]], système de fichiers réseau, se monte depuis un serveur sans formater de partition. [[Erreurs du cours#^e-2-os|✎]]
  - On distingue le **formatage rapide**, qui écrit seulement une structure de système de fichiers vide (les anciennes données restent sur le disque, récupérables tant qu'elles ne sont pas écrasées), et le **formatage complet**, qui vérifie en plus chaque secteur et, sous Windows depuis Vista, le remplit de zéros. Sous Linux, on formate une partition avec `mkfs` : `sudo mkfs.ext4 /dev/sdb1`. [[Complément hors du cours|ⓘ]]

## Système de fichiers (*File system*)

- **[[Système de fichiers]]** : méthode d'organisation et de stockage des fichiers sur un support.
- Il garde la trace de l'emplacement des fichiers sur le support et de leurs attributs : taille, permissions, horodatages.
  - Ces informations sur les fichiers s'appellent des **métadonnées**. Sous Linux, chaque fichier a un **inode** qui les contient (taille, propriétaire, permissions, dates, emplacement des blocs de données), le nom du fichier n'étant rangé que dans le répertoire qui pointe vers l'inode ; `ls -i` affiche le numéro d'inode. Le disque est découpé en **blocs** (souvent 4 Kio), plus petite unité allouée : un fichier d'un octet occupe tout de même un bloc. [[Complément hors du cours|ⓘ]]
  - Les systèmes modernes (NTFS, EXT4, XFS) sont **journalisés** : avant de modifier le disque, ils notent l'opération prévue dans un journal. Après une coupure de courant, le système relit le journal et termine ou annule les opérations en cours, au lieu de vérifier tout le disque ; c'est ce qui évite la plupart des corruptions. FAT32 et exFAT ne sont pas journalisés, d'où le conseil d'« éjecter » une clé USB avant de la retirer. Voir [[Journalisation (système de fichiers)]]. [[Complément hors du cours|ⓘ]]

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
  - Cette limite vient de ce que FAT32 range la taille d'un fichier sur 32 bits : au plus $2^{32} - 1$ octets, soit 4 Gio moins un octet. Une vidéo ou une [[Image ISO]] de plus de 4 Go ne peut donc pas être copiée sur une clé en FAT32, d'où l'exFAT, conçu pour les clés et cartes mémoire, avec une limite bien plus haute et une compatibilité aussi large. [[Complément hors du cours|ⓘ]]
- Linux reconnaît tous ces systèmes ; Windows ne reconnaît que les siens.
  - Nuance sur la colonne « Compatibilité » : macOS lit le NTFS mais ne l'écrit pas sans outil supplémentaire ; Linux le lit et l'écrit (pilote `ntfs3` intégré au noyau depuis la version 5.15, 2021). Pour échanger un disque entre Windows, macOS et Linux, l'exFAT est le choix le plus sûr. [[Complément hors du cours|ⓘ]]
  - NFS (*Network File System*) n'est pas un système de fichiers dont on formate un disque, mais un **protocole de partage en réseau** : un serveur exporte un dossier (lui-même stocké en EXT4 ou XFS) et les clients le montent comme un dossier local. Ses « 8 exaoctets » sont donc une limite du protocole, pas d'un format de disque ([[NFS]]). [[Complément hors du cours|ⓘ]]

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

Concrètement, le MBR est le **premier secteur** du disque, 512 octets, découpés en trois zones : [[Complément hors du cours|ⓘ]]

| Octets | Contenu |
|---|---|
| 446 | petit programme d'amorçage, que le BIOS charge et exécute |
| 64 | table des partitions : 4 entrées de 16 octets (d'où 4 partitions principales au plus) |
| 2 | signature `0x55AA`, qui marque le secteur comme amorçable |

Le programme de 446 octets est trop petit pour charger un OS : il lance un [[Chargeur de démarrage]] plus complet (GRUB sous Linux, Windows Boot Manager), qui charge à son tour le [[Noyau|noyau]] en RAM ; c'est ce chargeur qui propose le choix entre plusieurs OS (*dual boot*). La table adresse les secteurs sur 32 bits : au plus $2^{32}$ secteurs de 512 octets, soit $2^{32} \times 512 \approx 2{,}2 \times 10^{12}$ octets, d'où la limite de **2,2 To** du tableau BIOS/UEFI ci-dessous. [[Complément hors du cours|ⓘ]]

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

Le mécanisme diffère de celui du BIOS : l'UEFI ne lit pas un code d'amorçage dans le premier secteur, il lit une table **GPT** ([[Table de partitions GPT]]) et cherche la [[Partition système EFI]] (petite partition en FAT32), où chaque OS installé a déposé son chargeur sous forme de fichier `.efi` ; l'ordre de démarrage est une liste de ces fichiers, gardée dans la mémoire du *firmware*. Le *secure boot* vérifie la signature numérique de ce chargeur avant de l'exécuter ([[Démarrage sécurisé]]). Pour les anciens systèmes, beaucoup de cartes UEFI offraient un mode de compatibilité BIOS (*CSM*, *Legacy*). [[Complément hors du cours|ⓘ]]

## BIOS ou UEFI

| Caractéristique | BIOS | UEFI |
|---|---|---|
| Taille maximale du support | 2,2 To | 9,4 Zo |
| Temps de démarrage | lent | rapide |
| Options de *secure boot* | limitées | étendues |
| Réseau | non | oui |
| Administration à distance | non | oui |
| Interface graphique | non | oui |

Les deux limites de taille viennent des tables de partitions : le BIOS va avec le MBR, qui numérote les secteurs sur 32 bits ($2^{32} \times 512$ octets $\approx 2{,}2$ To) ; l'UEFI va avec la GPT, qui les numérote sur 64 bits ($2^{64} \times 512$ octets $\approx 9{,}4 \times 10^{21}$ octets $= 9{,}4$ Zo). [[Complément hors du cours|ⓘ]]

Récapitulatif du démarrage d'un PC : mise sous tension → *firmware* (BIOS ou UEFI) et POST → lecture du MBR ou de la partition EFI → [[Chargeur de démarrage]] → [[Noyau|noyau]] (avec l'[[Image initrd]] sous Linux) → premier processus (`systemd`, [[Processus init|init]]) → services et écran de connexion. [[Complément hors du cours|ⓘ]]
