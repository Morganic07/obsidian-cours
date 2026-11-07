---
type: concept
tags:
  - year2
aliases:
  - Fichier /etc/hosts
  - /etc/hosts
  - hosts file
matieres:
  - Operating System
sources:
  - "[[3 - TP3 (résumé)|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-06
---

Fichier texte local qui associe des noms d'hôte à des adresses IP. Il sert à la résolution DNS locale, aux tests rapides et au blocage d'accès.

Il se modifie avec n'importe quel éditeur (`sudo nano /etc/hosts`, une ligne `<ip> <hostname>`), avec effet immédiat, sans redémarrage. Il faut garder l'entrée `127.0.0.1` ([[Adresse de bouclage]]). Il ne passe pas à l'échelle comme le DNS. On teste une entrée avec `ping <hostname>` ([[Commande ping]]).

Notion parente : [[DNS]]. Voir aussi : [[Nom d'hôte]].

Résumés : [[3 - TP3 (résumé)]]
