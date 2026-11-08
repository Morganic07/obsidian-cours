---
type: concept
tags: [year2]
aliases: [journaling, journaling file system, système de fichiers journalisé, systèmes de fichiers journalisés]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 2.docx|OS - chp 2]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un système de fichiers **journalisé** note dans un **journal**, zone réservée du disque, les modifications qu'il s'apprête à faire, avant de les appliquer à la structure du disque. Une opération (créer un fichier, par exemple) touche plusieurs structures à la fois (répertoire, table des blocs libres, inode ou entrée de table) ; une coupure entre deux écritures laisserait le disque incohérent.

Après une coupure de courant ou un plantage, le système relit le journal au montage suivant : il rejoue les opérations enregistrées jusqu'au bout et ignore celles dont l'enregistrement est incomplet. La structure redevient cohérente en quelques secondes, sans parcourir tout le disque. Sur un système non journalisé, il faut au contraire un contrôle complet (`fsck` sous Linux, `chkdsk` sous Windows), très long sur un gros disque.

Le plus souvent, seules les **métadonnées** (structure, noms, emplacements, tailles) sont journalisées, pas le contenu des fichiers : la structure est sauve, mais les données en cours d'écriture au moment de la coupure peuvent être perdues. Ext4 offre trois modes : `journal` (métadonnées et données), `ordered` (par défaut : métadonnées seules, données écrites avant la validation de leurs métadonnées) et `writeback` (métadonnées seules, sans ordre imposé).

| Journalisés | Non journalisés |
|---|---|
| [[NTFS]] (Windows), [[EXT4]] (Linux ; ext3 a ajouté le journal à ext2), [[XFS]], APFS (macOS) | [[FAT32]], [[Système de fichiers exFAT\|exFAT]], ext2 |

C'est une raison du conseil d'« éjecter » une clé USB, souvent en FAT32 ou exFAT, avant de la retirer : l'éjection termine les écritures en attente, qu'aucun journal ne permettrait de rattraper.

Ne pas confondre avec un [[Fichier journal]] (*log*), fichier texte où un programme consigne les événements pour l'administrateur.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - OS]], à propos des systèmes de fichiers.

Voir aussi : [[Système de fichiers]], [[NTFS]], [[EXT4]], [[XFS]], [[FAT32]], [[Formatage d'un disque]], [[Partition (disque)]].

Résumés : [[2 - OS]]
