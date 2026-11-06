---
type: concept
aliases: [adressage IPv4, adresse IPv4, adresses IPv4, IPv4 addressing, IPv4 address, masque de sous-réseau, subnet mask, CIDR, Classless Inter-Domain Routing, adresse de broadcast, broadcast address, adresse réseau d'un sous-réseau, classes d'adresses IPv4, subnetting, longueur de préfixe]
matieres: [Computer Network]
sources: ["[[Sources/Year 3/Computer Network/02 IP Addressing (résumé)|02 IP Addressing (résumé)]]"]
maj: 2026-11-06
---

Une adresse IPv4 est un nombre de 32 bits, écrit en quatre octets séparés par des points (notation décimale pointée). Elle contient une partie réseau et une partie hôte, que le masque de sous-réseau sépare. Cours de [[Year 3 - Computer Network]].

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
