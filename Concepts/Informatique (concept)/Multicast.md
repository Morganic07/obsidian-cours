---
type: concept
tags: [year3]
aliases: [multidiffusion, adresse multicast, 224.0.0.9]
matieres: [Computer Network]
sources: ["[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]", "[[chp 3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : le multicast (multidiffusion) est un mode de transmission où un émetteur envoie un seul flux de paquets à un groupe de destinataires, identifié par une adresse de groupe ; le réseau ne duplique les paquets que là où c'est nécessaire. Il se distingue de l'unicast (un seul destinataire) et du broadcast (tous les hôtes du réseau). En IPv4, les adresses de groupe sont celles de la classe D, de 224.0.0.0 à 239.255.255.255 ; les protocoles de routage l'utilisent pour ne joindre que les routeurs concernés (224.0.0.9 désigne les routeurs RIPv2).

## Dans le cours

Nommé dans le cours sans définition propre. La classe D (224 à 239) est réservée au multicast, et RIPv2 envoie ses mises à jour en multicast, à l'adresse 224.0.0.9.

Notion parente : [[Adressage IPv4 et CIDR]]. Voir aussi : [[Routage dynamique]].

Résumés : [[IP Addressing (résumé)]], [[chp 3 - Dynamic Routing (résumé)]]
