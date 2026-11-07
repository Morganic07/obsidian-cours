---
type: concept
tags:
  - year2
aliases:
  - Advanced Package Tool
  - apt update
  - apt upgrade
  - apt full-upgrade
  - apt install
  - apt-get
matieres:
  - Operating System
sources:
  - "[[5 - OS (résumé)|OS - chp 5]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
maj: 2026-11-06
---

Outil pour installer, supprimer et mettre à jour les paquets d'une distribution Linux.

- `apt update` télécharge seulement la liste des nouvelles versions ;
- `apt upgrade` installe les nouvelles versions des paquets installés, sans installer ni supprimer de paquet ;
- `apt full-upgrade` peut en supprimer et en installer.

`sudo` est nécessaire, à cause des verrous placés sous `/var`.

Notion parente : [[Distribution Linux]]. Voir aussi : [[Commande sudo]].

Résumés : [[5 - OS (résumé)]], [[8 - OS commandes sh (résumé)]]
