---
type: concept
tags: [year2]
aliases: [GPT, GUID Partition Table, table GPT]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la GPT (*GUID Partition Table*) est le format de table de partitions qui remplace celle du [[MBR]], associé à l'[[BIOS et UEFI|UEFI]].

- Chaque [[Partition (disque)|partition]] est identifiée par un **GUID** (identifiant unique de 128 bits), ainsi que son type.
- Les secteurs sont numérotés sur 64 bits, d'où des disques jusqu'à $2^{64} \times 512$ octets $\approx 9{,}4$ Zo, contre $2^{32} \times 512$ octets $\approx 2{,}2$ To (2 Tio) pour le MBR, avec des secteurs de 512 octets.
- La table décrit 128 partitions par défaut, sans besoin de partition étendue ni de partitions logiques.
- Une **copie de secours** de l'en-tête et de la table est placée en fin de disque, et des sommes de contrôle (CRC32) détectent une corruption.
- Le premier secteur garde un **MBR protecteur** (*protective MBR*), qui déclare tout le disque comme une seule partition de type GPT, pour que les anciens outils ne prennent pas le disque pour un disque vide.
- Sous Linux, `sudo fdisk -l` (ligne *Disklabel type: gpt* ou *dos*) ou `gdisk` affichent le type de table.

## Dans le cours

Le cours ne la nomme pas : [[2 - OS]] présente le MBR, et [[4 - OS]] parle des partitions Linux sans nommer le format de la table. Elle apparaît dans les compléments de ces deux fiches.

Voir aussi : [[MBR]], [[BIOS et UEFI]], [[Partition (disque)]], [[Partition système EFI]].

Résumés : [[2 - OS]], [[4 - OS]]
