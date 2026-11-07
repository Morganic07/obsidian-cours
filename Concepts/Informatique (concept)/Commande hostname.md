---
type: concept
tags:
  - year2
aliases:
  - sudo hostname
  - hostname -f
  - hostname -I
sources:
  - "[[chp 1 - séance TP1 (résumé)|cours TP1]]"
  - "[[TP1 (résumé)|TP1]]"
  - "[[TP3 (résumé)|TP3]]"
maj: 2026-11-06
---

`hostname` affiche le nom de la machine ; `sudo hostname nouveau` le change. `hostname -f` affiche le FQDN (seulement `penguin`, faute de domaine) et `hostname -I` donne l'adresse IP.

Notion parente : [[Nom d'hôte]]. Voir aussi : [[Commande whoami]].

## À vérifier

- Le changement par `sudo hostname` n'est pas permanent (il faut modifier `/etc/hostname`) : complément apporté par le résumé, pas par le cours.

Résumés : [[chp 1 - séance TP1 (résumé)]], [[TP1 (résumé)]], [[TP3 (résumé)]]
