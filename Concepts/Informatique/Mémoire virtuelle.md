---
type: concept
tags: [year2]
aliases: [virtual memory, espace d'adressage virtuel, virtual address space, adresse virtuelle, virtual address]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la mémoire virtuelle est la technique par laquelle chaque processus dispose de son **propre espace d'adressage virtuel**, de l'adresse 0 à une adresse maximale, que le système d'exploitation, avec un composant matériel du processeur, la MMU (*memory management unit*), traduit en adresses physiques de la [[Mémoire vive|RAM]]. La traduction se fait en général **par pages** (blocs de taille fixe, souvent 4 Kio) grâce à une table des pages propre à chaque processus.

Conséquences :

- **isolation** : deux processus peuvent utiliser la même adresse virtuelle sans conflit, car elle correspond à deux cases physiques différentes, et aucun ne peut lire la mémoire d'un autre ;
- **mémoire plus grande que la RAM** : seule une partie du processus a besoin d'être en RAM ; les pages peu utilisées peuvent être placées dans l'[[Espace d'échange (swap)]] et rechargées à la demande (défaut de page, *page fault*) ;
- **copie sur écriture** : après [[Appel fork()|fork()]], parent et fils partagent d'abord les mêmes pages physiques, dupliquées seulement à la première écriture.

## Dans le cours

Le cours ne nomme pas la notion. Le schéma de l'[[Espace mémoire d'un processus]] (text, data, heap, stack, de l'adresse 0 à max) dans [[7 - OS]] décrit un espace d'adressage virtuel : chaque processus a le sien.

Voir aussi : [[Espace mémoire d'un processus]], [[Espace d'échange (swap)]], [[Mémoire vive]], [[Appel fork()]], [[Processus]].

Résumés : [[7 - OS]]
