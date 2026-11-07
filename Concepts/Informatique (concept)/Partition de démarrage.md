---
type: concept
tags: [year2]
aliases: [boot partition, bootable partition, "partition /boot", partition amorçable]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-06
---

`/boot` contient le [[Noyau]], l'[[Image initrd|initrd]] et la configuration du chargeur de démarrage ; c'est une petite partition (100 à 500 Mo), souvent montée en lecture seule.

Une **partition amorçable** est toute partition contenant de quoi démarrer (souvent la racine ou une partition séparée) : au démarrage, le système la cherche et y charge noyau et initrd.

Notion parente : [[Partitions Linux]]. Voir aussi : [[Chargeur de démarrage]].

Résumés : [[4 - OS (résumé)]]
