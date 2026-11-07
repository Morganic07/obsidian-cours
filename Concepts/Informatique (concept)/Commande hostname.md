---
type: concept
tags:
  - year2
aliases:
  - sudo hostname
  - hostname -f
  - hostname -I
sources:
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3 - PINA Morgane.docx|TP3]]"
maj: 2026-11-07
---

`hostname` affiche le nom de la machine ; `sudo hostname nouveau` le change. `hostname -f` affiche le FQDN (seulement `penguin`, faute de domaine) et `hostname -I` donne l'adresse IP.

Notion parente : [[Nom d'hôte]]. Voir aussi : [[Commande whoami]].

## À vérifier

- Le changement par `sudo hostname` n'est pas permanent (il faut modifier `/etc/hostname`) : complément apporté par le résumé, pas par le cours.

Résumés (rapprochement, complément hors du cours) : [[3 - TP3 (résumé)]]
