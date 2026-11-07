---
type: concept
tags:
  - year2
  - year3
aliases:
  - adressage IPv4
  - adresse IPv4
  - adresses IPv4
  - IPv4 addressing
  - IPv4 address
  - masque de sous-réseau
  - subnet mask
  - CIDR
  - Classless Inter-Domain Routing
  - adresse de broadcast
  - broadcast address
  - adresse réseau d'un sous-réseau
  - classes d'adresses IPv4
  - subnetting
  - longueur de préfixe
  - adresse IP
  - IP address
  - Internet Protocol
  - notation décimale pointée
  - dotted-decimal notation
  - adresse d'hôte
  - host address
  - hôtes par réseau
matieres:
  - Computer Network
  - Operating System
sources:
  - "[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]"
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-07
---

Une adresse IPv4 est un nombre de 32 bits, écrit en quatre octets séparés par des points (notation décimale pointée). Elle contient une partie réseau et une partie hôte, que le masque de sous-réseau sépare. Cours de [[Cours/Informatique/Computer Network/_index|Computer Network]].

## Principes

- Le masque a des 1 sur les bits réseau et des 0 sur les bits hôte. Une adresse est incomplète sans son masque.
- Notation par préfixe : `192.168.1.4/24` indique 24 bits réseau.
- **Adresse réseau** : partie hôte entièrement à 0. **Adresse de broadcast** : partie hôte entièrement à 1. Aucune des deux ne peut être attribuée à un hôte.
- Première adresse utilisable : celle qui suit l'adresse réseau. Dernière : celle qui précède le broadcast.
- Nombre d'hôtes par réseau : $2^n - 2$, avec $n$ le nombre de bits hôte.

## Classes (adressage classful)

| Classe | Premier octet | Masque par défaut | Bits réseau |
|---|---|---|---|
| A | 0 à 127 (de fait 1 à 126, voir ci-dessous) | 255.0.0.0 (/8) | 8 |
| B | 128 à 191 | 255.255.0.0 (/16) | 16 |
| C | 192 à 223 | 255.255.255.0 (/24) | 24 |
| D | 224 à 239 | multicast | |
| E | 240 à 255 | recherche | |

La plage 127.0.0.0 à 127.255.255.255 est réservée au bouclage (loopback), qui teste la pile réseau locale. Le cours écrit donc « classe A : 0 à 126 ».

## CIDR

Les classes gaspillaient des adresses : une entreprise de 5000 hôtes recevait un réseau de classe B et en perdait environ 60 000. Le CIDR, introduit par l'IETF en 1993, supprime le lien entre classe et préfixe : on découpe un réseau en sous-réseaux de taille quelconque. Pour `192.168.1.0` : `/24` donne 254 hôtes, `/25` 126, `/26` 62, `/27` 30, `/28` 14, `/29` 6, `/30` 2, `/31` 0 selon la formule du cours.

Masques correspondants : /25 = 255.255.255.128, /26 = .192, /27 = .224, /28 = .240, /29 = .248, /30 = .252.

## Liens

Ces notions servent au [[Routage statique]], au [[Routage dynamique]], au [[VLAN]] (complément : un VLAN correspond en général à un sous-réseau) et au [[NAT et PAT]] (adresses privées). Les commandes `ifconfig` et `ip address` affichent l'adresse et le masque : voir [[Shell et Bash]].

En Operating System (TP3), l'adresse IP est définie comme l'étiquette numérique attribuée à un appareil d'un réseau IPv4, qui l'identifie de façon unique et indique sa position pour faciliter la communication. La sortie d'exemple affiche, pour chaque interface, l'adresse, le broadcast et le masque de sous-réseau. Le cours de réseau précise qu'une adresse sur 32 bits donne environ 4,3 milliards d'adresses.

Voir aussi : [[Adresse de bouclage]], [[IANA]], [[VLSM]], [[Octet]], [[Numération binaire]], [[Interface réseau]], [[Commande ifconfig]], [[Commande ip]], [[DNS]].

## Erreurs du cours

- [[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]] (diapositive 38, quiz) donne à un PC l'adresse « 224.192.64.32/24 » ; une adresse 224.x.x.x est de classe D (multicast) et ne s'attribue pas à un hôte. Le calcul demandé (adresse réseau, broadcast, hôtes) se fait quand même avec le /24.

Résumés : [[2 - IP Addressing]], [[5 - NAT ／ PAT]], [[6 - Access Control List]], [[3 - TP3]]
