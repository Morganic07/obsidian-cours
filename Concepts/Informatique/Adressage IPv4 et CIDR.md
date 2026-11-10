---
type: concept
tags:
  - year2
  - year3
  - year4
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
  - supernetting
  - agrégation de routes
  - link-local
  - APIPA
matieres:
  - Computer Network
  - Operating System
sources:
  - "[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]"
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-10
---

**Définition** (d'après [[2 - IP Addressing]]) : une adresse IPv4 est un nombre de 32 bits, écrit en quatre octets séparés par des points (notation décimale pointée). Elle contient une partie réseau et une partie hôte, que le masque de sous-réseau sépare. Cours de [[Cours/Informatique/Computer Network/_index|Computer Network]].

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

## Calculs et cas particuliers (complément, hors du cours)

**Calcul bit à bit**
- Adresse réseau = adresse **ET** masque, bit à bit.
- Adresse de broadcast = adresse réseau avec tous les bits hôte mis à 1 (adresse **OU** masque inversé).
- Un masque est toujours fait de 1 contigus suivis de 0 : un octet de masque ne peut valoir que 0, 128, 192, 224, 240, 248, 252, 254 ou 255.

**Méthode de découpage en sous-réseaux**
- En empruntant $s$ bits à la partie hôte, on obtient $2^s$ sous-réseaux.
- Avec $h$ bits hôte restants, chaque sous-réseau compte $2^h - 2$ hôtes.
- **Taille de bloc** : $2^h = 256 - \text{octet du masque}$ dans l'octet où le masque s'arrête ; les sous-réseaux commencent aux multiples de cette taille.

Exemple : `192.168.1.100/26`. Le masque est 255.255.255.192, la taille de bloc $256 - 192 = 64$ ; les sous-réseaux commencent à .0, .64, .128, .192. Donc réseau `192.168.1.64`, broadcast `192.168.1.127`, hôtes de .65 à .126 ($2^6 - 2 = 62$).

Exemple des 5000 hôtes avec le CIDR : il faut $h$ tel que $2^h - 2 \geq 5000$, soit $h = 13$ ($2^{13} - 2 = 8190$), donc un préfixe `/19` au lieu d'un réseau de classe B (65 534 hôtes).

**Préfixes extrêmes**
- `/31` : la formule du cours donne 0 hôte, mais la RFC 3021 autorise le /31 sur les liens point à point, où les deux adresses servent aux deux extrémités (pas de broadcast).
- `/32` : un seul hôte. C'est la longueur des routes `L` (adresse locale d'une interface) dans `show ip route`.

**Agrégation (supernetting)** : l'inverse du découpage. Quatre /24 contigus, de `192.168.0.0/24` à `192.168.3.0/24`, se résument en un seul `192.168.0.0/22`, ce qui réduit la taille des tables de routage (voir [[Résumé automatique de routes]]).

**Adresses particulières**

| Plage | Usage |
|---|---|
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | adresses privées (RFC 1918), non routées sur Internet, traduites par le [[NAT et PAT]] |
| `127.0.0.0/8` | bouclage (voir [[Adresse de bouclage]]) |
| `169.254.0.0/16` | link-local (APIPA) : adresse que s'attribue un hôte qui n'a obtenu aucune adresse par DHCP |
| `255.255.255.255` | broadcast limité, au réseau local |
| `0.0.0.0` | « cette machine » ou adresse non encore attribuée ; `0.0.0.0/0` désigne la route par défaut |

**Épuisement** : $2^{32} = 4\,294\,967\,296$ adresses. L'[[IANA]] a distribué ses derniers blocs /8 aux registres régionaux en février 2011 ; d'où le recours au NAT et le passage à IPv6 (adresses de 128 bits).

L'adresse IP est logique et hiérarchique ; l'identifiant physique d'une interface, utilisé dans le réseau local, est l'[[Adresse MAC]].

## Liens

Ces notions servent au [[Routage statique]], au [[Routage dynamique]], au [[VLAN]] (complément : un VLAN correspond en général à un sous-réseau) et au [[NAT et PAT]] (adresses privées). Les commandes `ifconfig` et `ip address` affichent l'adresse et le masque : voir [[Shell et Bash]].

En Operating System (TP3), l'adresse IP est définie comme l'étiquette numérique attribuée à un appareil d'un réseau IPv4, qui l'identifie de façon unique et indique sa position pour faciliter la communication. La sortie d'exemple affiche, pour chaque interface, l'adresse, le broadcast et le masque de sous-réseau. Le cours de réseau précise qu'une adresse sur 32 bits donne environ 4,3 milliards d'adresses.

Voir aussi : [[Adresse de bouclage]], [[IANA]], [[VLSM]], [[Octet]], [[Numération binaire]], [[Interface réseau]], [[Commande ifconfig]], [[Commande ip]], [[DNS]].

[[2 - Histoire du design]] : l'URL évite à l'utilisateur de manipuler des adresses IP complexes ; le Web s'appuie sur l'adressage IP d'Internet.

Résumés : [[2 - IP Addressing]], [[5 - NAT ／ PAT]], [[6 - Access Control List]], [[3 - TP3]] · [[2 - Histoire du design]]
