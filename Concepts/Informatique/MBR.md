---
type: concept
tags: [year2]
aliases: [master boot record, secteur d'amorçage, table de partitions MBR]
matieres: [Operating System]
sources: ["[[2 - OS|OS - chp 2]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]"]
maj: 2026-11-08
---

**Définition** (d'après [[2 - OS]]) : Master Boot Record, situé sur le disque : il indique au firmware sur quelle partition se trouve le système d'exploitation, charge l'OS en RAM, gère les partitions et permet de démarrer sur différents OS. Le cours le compare à la table des matières d'un livre. Il n'y a qu'un seul MBR même avec plusieurs OS ; s'il est corrompu, l'ordinateur ne trouve plus l'OS.

## Structure (complément, hors du cours)

Le MBR est le **premier secteur du disque**, de 512 octets :

| Octets | Taille | Contenu |
|---|---|---|
| 0 à 445 | 446 octets | code d'amorçage (*bootstrap code*) |
| 446 à 509 | 64 octets | table de partitions : 4 entrées de 16 octets |
| 510 à 511 | 2 octets | signature `0x55AA`, qui marque un secteur d'amorçage valide |

**Partitions.** Quatre entrées seulement, d'où **4 partitions principales** au plus. Pour en avoir davantage, l'une des quatre peut être une partition **étendue**, qui contient elle-même des partitions **logiques** : 3 principales et une étendue, par exemple.

**Démarrage.** Le [[BIOS et UEFI|BIOS]] lit ce secteur et exécute son code. Trop petit pour charger un système à lui seul, ce code lance un [[Chargeur de démarrage]] (GRUB sous Linux, Windows Boot Manager), qui charge le [[Noyau]] en RAM et peut proposer le choix entre plusieurs systèmes (*dual boot*).

**Limite de taille.** Chaque entrée note la position et la taille d'une partition en nombre de secteurs, sur 32 bits. Avec des secteurs de 512 octets, l'adresse maximale vaut
$$2^{32} \times 512 \text{ octets} = 2^{41} \text{ octets} = 2 \text{ Tio} \approx 2{,}2 \text{ To}.$$
Un disque plus grand ne peut pas être entièrement exploité avec un MBR.

**Successeur.** La [[Table de partitions GPT]] (*GUID Partition Table*), associée à l'UEFI, lève ces limites (128 partitions par défaut, disques bien plus grands) et garde une copie de secours de la table en fin de disque.

## Dans le cours

Le cours décrit le rôle du MBR au démarrage et le compare à une table des matières ; sa structure, la limite de 2,2 To et le passage à GPT sont des compléments de [[2 - OS]].

Notion parente : [[BIOS et UEFI]]. Voir aussi : [[Partition (disque)]], [[Chargeur de démarrage]], [[Table de partitions GPT]], [[Partition de démarrage]].

Résumés : [[2 - OS]]
