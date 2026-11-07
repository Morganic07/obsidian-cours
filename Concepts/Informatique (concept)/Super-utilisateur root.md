---
type: concept
tags:
  - year2
aliases:
  - superuser
  - super-utilisateur
  - utilisateur root
  - root user
  - root privileges
matieres:
  - Operating System
sources:
  - "[[Raw/Year 2/Operating System/Cours OS/cours TP1.docx|cours TP1]]"
  - "[[Raw/Year 2/Operating System/DM/TP4/TP4-Unix Commands.pdf|TP4-Unix Commands.pdf]]"
maj: 2026-11-07
---

Utilisateur aux privilèges complets. `sudo` donne ses privilèges sans se connecter en root. Seul root peut lire `/etc/shadow`. `crontab -e` lancé avec `sudo` édite la table de root, pas celle de l'utilisateur.

Voir aussi : [[Commande sudo]], [[Fichiers de mots de passe]], [[Tâche planifiée cron]].

Résumés : [[4 - TP4 (résumé)]], [[8 - OS commandes sh (résumé)]]
