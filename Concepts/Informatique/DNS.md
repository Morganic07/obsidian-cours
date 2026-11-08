---
type: concept
tags:
  - year2
aliases:
  - Domain Name System
  - Domain Name Server
  - résolution de noms
  - address resolution
  - résolution DNS
matieres:
  - Operating System
sources:
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Cours TP3.docx|Cours TP3]]"
maj: 2026-11-08
---

La conversion des noms d'hôte en adresses IP s'appelle la résolution d'adresse ; elle est faite par le DNS (*Domain Name System*). [[Erreurs du cours#^e-dns|✎]] Quand on tape un nom dans un navigateur, les serveurs DNS le résolvent en adresse IP.

## Fonctionnement (complément, hors du cours)

DNS signifie **Domain Name System**. C'est un annuaire réparti et hiérarchique, lu de droite à gauche dans un nom (`www.exemple.fr.`) :

1. les **serveurs racine** connaissent les serveurs de chaque domaine de premier niveau ;
2. les **serveurs des domaines de premier niveau** (TLD : `.com`, `.fr`, `.org`) connaissent les serveurs faisant autorité pour chaque domaine (`exemple.fr`) ;
3. les **serveurs faisant autorité** du domaine donnent l'adresse IP demandée (`www.exemple.fr`).

Le poste n'interroge pas lui-même cette chaîne : il envoie sa question à un **serveur récursif** (celui du fournisseur d'accès, de la box, ou un service public), qui fait le parcours à sa place et garde les réponses en **cache** pendant leur durée de validité, pour répondre plus vite aux questions suivantes.

Sous Linux, l'ordre des sources consultées est fixé par la ligne `hosts: files dns` de `/etc/nsswitch.conf` : le [[Fichier hosts|fichier /etc/hosts]] (`files`) est lu avant le DNS. `getent hosts <nom>` affiche le résultat obtenu selon cet ordre, contrairement à des outils comme `dig` ou `nslookup` qui interrogent directement le DNS.

Voir aussi : [[Nom d'hôte]], [[Fichier hosts]], [[Modèle client-serveur]], [[Mémoire cache]].

Résumés : [[3 - TP3]]
