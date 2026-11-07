---
type: concept
tags: [year2]
aliases: [bad sector, bad sectors]
sources: ["[[OS - chp 2 (résumé)|OS - chp 2]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : un secteur défectueux (*bad sector*) est un secteur d'un [[Disque dur|disque]], la plus petite unité de stockage adressable (souvent 512 octets ou 4 Ko), qu'on ne peut plus lire ou écrire de façon fiable, à cause d'un dommage physique de la surface ou d'une erreur logique ; c'est une petite zone du disque, pas une partition entière comme le laisse entendre le cours (voir « À vérifier »). Le contrôleur du disque réaffecte de lui-même les secteurs défaillants à des secteurs de réserve, et des outils comme `badblocks`, `fsck` ou `chkdsk` permettent de les repérer pour que le système de fichiers ne les utilise plus.

## Dans le cours

Nommé dans le chapitre 2 sans définition : le cours écrit seulement « one color = one partition, if the partition is damaged, its called bad sector ».

Notion parente : [[Disque dur]]. Voir aussi : [[Partition (disque)]].

## À vérifier

- Le cours assimile une partition abîmée à un bad sector ; un secteur défectueux est une zone physique abîmée du disque, pas une partition (signalé par le résumé).

Résumés : [[OS - chp 2 (résumé)]]
