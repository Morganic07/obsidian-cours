---
type: concept
tags: [year2]
aliases: [bootloader, boot loader, chargeur d'amorçage]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : le chargeur de démarrage (*bootloader*) est le petit programme lancé par le micrologiciel ([[BIOS et UEFI|BIOS ou UEFI]]) au démarrage de la machine, chargé de charger le [[Noyau|noyau]] du système d'exploitation en mémoire et de lui passer la main. Sous Linux, il charge aussi l'[[Image initrd]] et transmet au noyau ses paramètres ; le plus répandu est GRUB, qui permet aussi de choisir entre plusieurs systèmes installés.

## Dans le cours

Nommé dans le chp 4 sans définition : ses fichiers de configuration se trouvent dans la partition `/boot` ou dans une partition amorçable.

Notion parente : [[Partition de démarrage]]. Voir aussi : [[BIOS et UEFI]], [[MBR]].

Résumés : [[OS - chp 4 (résumé)]]
