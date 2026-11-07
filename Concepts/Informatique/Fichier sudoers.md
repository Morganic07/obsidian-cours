---
type: concept
tags:
  - year2
aliases:
  - sudoers
  - visudo
  - NOPASSWD
  - timestamp_timeout
  - sudo sans mot de passe
  - sudo passwordless
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP6/TP6-Assignment.pdf|TP6-Assignment.pdf]]"
maj: 2026-11-07
---

Le fichier sudoers s'ouvre avec `sudo visudo` (tâche 2 du TP6).

- Pour supprimer la demande de mot de passe : ajouter en fin de fichier `username ALL=(ALL) NOPASSWD:ALL`.
- Pour régler le délai avant une nouvelle demande : `Defaults timestamp_timeout=15`.

Notion parente : [[Commande sudo]].

## Erreurs du cours

- [[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]] écrit « to set a timeout of 15 minutes (meaning no password prompt for 30 minutes after the first successful sudo command) » ; il faut « for 15 minutes » : `Defaults timestamp_timeout=15` fixe le délai à 15 minutes.

Résumés (rapprochement, complément hors du cours) : [[8 - OS commandes sh]]
