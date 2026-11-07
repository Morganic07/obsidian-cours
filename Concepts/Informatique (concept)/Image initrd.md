---
type: concept
tags: [year2]
aliases: [initrd, initial RAM disk]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : l'initrd (*initial RAM disk*) est une image de système de fichiers minimal que le [[Chargeur de démarrage|chargeur de démarrage]] place en mémoire vive avec le [[Noyau|noyau]] Linux. Le noyau s'en sert comme racine provisoire : elle contient les pilotes et les outils nécessaires pour accéder au vrai système de fichiers racine (pilotes de disque, chiffrement, RAID…). Une fois la racine réelle montée, le démarrage s'y poursuit. Les distributions actuelles utilisent en fait une variante, l'initramfs, qu'on continue souvent d'appeler initrd.

## Dans le cours

Nommée dans le chapitre 4 sans définition détaillée : l'initrd (initial RAM disk) est un fichier nécessaire au démarrage, rangé avec le noyau dans `/boot`. Au démarrage, le système charge le noyau et l'initrd depuis la partition amorçable.

Notion parente : [[Partition de démarrage]]. Voir aussi : [[Noyau]].

Résumés : [[OS - chp 4 (résumé)]]
