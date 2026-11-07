---
type: concept
tags: [year3]
aliases: [Variable Length Subnet Mask]
matieres: [Computer Network]
sources: ["[[chp 3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : le VLSM (*Variable Length Subnet Mask*) consiste à découper un même réseau en sous-réseaux de tailles différentes, avec des masques de longueurs différentes, au lieu d'utiliser partout le même masque. On donne ainsi à chaque sous-réseau juste le nombre d'adresses dont il a besoin : par exemple un /30 (2 hôtes utilisables) pour une liaison entre deux routeurs, un /24 pour un réseau de 200 postes. Il suppose un [[Routage classful et classless|routage classless]], dont les mises à jour transportent le masque de chaque route.

## Dans le cours

Nommé dans le chapitre sur le routage dynamique sans définition propre : RIPv2, protocole classless, gère le VLSM, car ses mises à jour incluent les masques de sous-réseau. La commande `no auto-summary` est dite essentielle avec le VLSM ou des réseaux non contigus.

Notion parente : [[Adressage IPv4 et CIDR]]. Voir aussi : [[Routage classful et classless]], [[Routage dynamique]].

## À vérifier

Le développement du sigle (Variable Length Subnet Mask) n'est pas dans le cours.

Résumés : [[chp 3 - Dynamic Routing (résumé)]]
