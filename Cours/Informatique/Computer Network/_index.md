---
type: matiere
tags:
  - year3
sources:
  - "[[1 - Computer Networks|chp1 - Computer Networks]]"
  - "[[7 - Cisco|Formation CISCO Packet Tracer]]"
  - "[[2 - Static Routing|Chp2 - Static Routing]]"
  - "[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]"
  - "[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]"
  - "[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]"
  - "[[6 - Access Control List|chp6 - Access Control List]]"
maj: 2026-11-06
---

Réseaux et configuration d'équipements Cisco (routeurs 2911, switchs 2960) avec Packet Tracer. Les 7 notes sont intégrées. Les cours sont surtout en anglais.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - Computer Networks\|chp1 - Computer Networks]] | Modes de la CLI, mémoires, début du routage statique | [[1 - Computer Networks\|Résumé]] |
| [[7 - Cisco\|Formation CISCO Packet Tracer]] | Récapitulatif et ping | [[7 - Cisco\|Résumé]] |
| [[2 - Static Routing\|Chp2 - Static Routing]] | Table de routage, routes statiques | [[2 - Static Routing\|Résumé]] |
| [[3 - Dynamic Routing\|Chp3 - Dynamic Routing]] | Route par défaut, RIP | [[3 - Dynamic Routing\|Résumé]] |
| [[4 - VLAN ／ IVR Commands\|Chp4 - VLAN ／ IVR Commands]] | VLAN, trunk, routage inter-VLAN | [[4 - VLAN ／ IVR Commands\|Résumé]] |
| [[5 - NAT ／ PAT\|Chp5 - NAT ／ PAT]] | Adresses privées, NAT, PAT | [[5 - NAT ／ PAT\|Résumé]] |
| [[6 - Access Control List\|chp6 - Access Control List]] | Wildcard mask, ACL | [[6 - Access Control List\|Résumé]] |

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| 02 IP Addressing ([[Raw/Year 3/Computer Network/02 IP Addressing.pdf\|02 IP Addressing.pdf]]) | Adressage IPv4 : binaire, classes, masques, CIDR, sous-réseaux | [[2 - IP Addressing\|Résumé]] |

## Concepts

- **Équipements et configuration** : [[CLI Cisco IOS]], [[Routeur]], [[Commutateur]], [[Interface réseau]], [[Réseau local]], [[Commande ping]], [[ICMP]]
- **Adressage** : [[Numération binaire]], [[Octet]], [[Adressage IPv4 et CIDR]], [[IANA]], [[IETF]], [[Multicast]], [[Adresse de bouclage]], [[IPv6]]
- **Routage statique** : [[Routage IP]], [[Routage statique]], [[Passerelle par défaut]]
- **Routage dynamique** : [[Routage dynamique]], [[Système autonome]], [[EIGRP]], [[OSPF]], [[BGP]], [[Routage classful et classless]], [[VLSM]], [[Résumé automatique de routes]], [[Convergence d'un protocole de routage]], [[Boucle de routage]]
- **Commutation** : [[VLAN]], [[Domaine de diffusion]], [[Sous-interface]], [[Encapsulation 802.1Q]]
- **Adresses et filtrage** : [[NAT et PAT]], [[Numéro de port]], [[Pare-feu]], [[Liste de contrôle d'accès]]

## À revoir en priorité avant un examen

- [[4 - VLAN ／ IVR Commands]] : `encapsulation dot1q 10` répété sur les trois sous-interfaces.
- [[6 - Access Control List]] : la solution de l'exigence 4 du TP place l'ACL sur la mauvaise interface.
- [[5 - NAT ／ PAT]] : `overlead` pour `overload`, `ip nat outside` hors du mode d'interface, NAT présenté comme un pare-feu.
- [[2 - Static Routing]] : « R3 » à la place de R2 dans le tableau des réseaux connectés.

## Liens avec les autres matières

- **[[Cours/Informatique/Data base/_index|Data base]]** : l'architecture 3 tiers d'un SGBD repose sur le réseau.
- **[[Cours/Informatique/OS/_index|Operating System]]** : le TP3 aborde côté Linux [[Adressage IPv4 et CIDR]], [[Interface réseau]], [[Adresse de bouclage]], [[Commande ping]] et [[IPv6]].
