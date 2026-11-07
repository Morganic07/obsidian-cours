---
type: concept
tags: [year2]
aliases: [Dynamic Host Configuration Protocol]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : DHCP (Dynamic Host Configuration Protocol) est un protocole qui attribue automatiquement à une machine qui rejoint un réseau sa configuration IP : adresse, masque, [[Passerelle par défaut|passerelle par défaut]], serveurs [[DNS]]. Un serveur DHCP prête l'adresse pour une durée limitée (le bail), au terme d'un échange en quatre messages : *Discover*, *Offer*, *Request*, *Acknowledge*. Il fonctionne sur UDP (port 67 côté serveur, 68 côté client).

## Dans le cours

Nommé au TP3 sans définition détaillée : au lieu d'attribuer l'adresse à la main, on peut l'obtenir automatiquement en configurant DHCP (Dynamic Host Configuration Protocol) pour une interface.

Notion parente : [[Netplan]]. Voir aussi : [[Adressage IPv4 et CIDR]].

Résumés (rapprochement, complément hors du cours) : [[3 - TP3]]
