---
type: concept
tags:
  - year2
aliases:
  - sudo hostname
  - hostname -f
  - hostname -I
  - hostnamectl
  - hostnamectl set-hostname
sources:
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP1/TP1.docx|TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3 - PINA Morgane.docx|TP3]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : `hostname` est la commande qui affiche ou modifie le [[Nom d'hôte|nom d'hôte]] de la machine, c'est-à-dire le nom sous lequel elle se désigne sur le réseau.

`hostname` affiche le nom de la machine ; `sudo hostname nouveau` le change. `hostname -f` affiche le FQDN (seulement `penguin`, faute de domaine) et `hostname -I` donne l'adresse IP.

## Changer le nom durablement (complément, hors du cours)

- `sudo hostname nouveau` ne modifie que le nom en mémoire : il ne dure que jusqu'au redémarrage, car le nom est relu au démarrage dans le fichier `/etc/hostname`.
- `sudo hostnamectl set-hostname nouveau` (outil de systemd) change le nom et l'écrit dans `/etc/hostname` : le changement survit au redémarrage. `hostnamectl` seul affiche le nom et des informations sur le système.
- Il faut aussi remplacer l'ancien nom dans le [[Fichier hosts|fichier `/etc/hosts`]] (ligne `127.0.1.1 ancien-nom` sous Debian et Ubuntu) ; sinon `sudo` avertit « unable to resolve host … ».
- `penguin` est le nom par défaut du conteneur Linux de ChromeOS, d'où la valeur obtenue au TP.

Notion parente : [[Nom d'hôte]]. Voir aussi : [[Commande whoami]], [[Fichier hosts]], [[Commande systemctl]].

Résumés : [[1 - TP1]] ; (rapprochement, complément hors du cours) : [[3 - TP3]]
