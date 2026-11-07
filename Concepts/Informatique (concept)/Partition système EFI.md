---
type: concept
tags: [year2]
aliases: [EFI system partition, partition EFI, Reserved BIOS boot area]
sources: ["[[3 - OS (résumé)|OS - chp 3]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : la partition système EFI (ESP, *EFI System Partition*) est une petite partition formatée en [[FAT32]], que le micrologiciel [[BIOS et UEFI|UEFI]] lit au démarrage. Elle contient les [[Chargeur de démarrage|chargeurs de démarrage]] des systèmes installés (fichiers `.efi`, par exemple GRUB pour Linux), et elle est en général montée sous `/boot/efi`. Elle n'est utile qu'en démarrage UEFI ; sur un disque GPT démarré en mode BIOS, GRUB utilise à la place une petite partition d'amorçage BIOS (*BIOS boot partition*).

## Dans le cours

Nommée dans le chapitre 3 sans définition : la partition système EFI figure parmi les partitions nécessaires à Ubuntu, avec le swap, la racine (`/`), la zone réservée au démarrage BIOS (Reserved BIOS boot area) et `/home`.

Notion parente : [[Partitions Linux]]. Voir aussi : [[BIOS et UEFI]].

Résumés : [[3 - OS (résumé)]]
