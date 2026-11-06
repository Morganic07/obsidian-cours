---
type: matiere
sources: ["[[chp1 - Computer Networks]]", "[[Formation CISCO Packet Tracer]]", "[[Chp2 - Static Routing]]", "[[Chp3 - Dynamic Routing]]", "[[Chp4 - VLAN ／ IVR Commands]]", "[[Chp5 - NAT ／ PAT]]", "[[chp6 - Access Control List]]"]
maj: 2026-11-05
---

Réseaux et configuration d'équipements Cisco (routeurs 2911, switchs 2960) avec Packet Tracer. Les 7 notes sont intégrées. Les cours sont surtout en anglais.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[chp1 - Computer Networks]] | Modes de la CLI, mémoires, début du routage statique | [[chp1 - Computer Networks (résumé)\|Résumé]] |
| [[Formation CISCO Packet Tracer]] | Récapitulatif et ping | [[Formation CISCO Packet Tracer (résumé)\|Résumé]] |
| [[Chp2 - Static Routing]] | Table de routage, routes statiques | [[Chp2 - Static Routing (résumé)\|Résumé]] |
| [[Chp3 - Dynamic Routing]] | Route par défaut, RIP | [[Chp3 - Dynamic Routing (résumé)\|Résumé]] |
| [[Chp4 - VLAN ／ IVR Commands]] | VLAN, trunk, routage inter-VLAN | [[Chp4 - VLAN ／ IVR Commands (résumé)\|Résumé]] |
| [[Chp5 - NAT ／ PAT]] | Adresses privées, NAT, PAT | [[Chp5 - NAT ／ PAT (résumé)\|Résumé]] |
| [[chp6 - Access Control List]] | Wildcard mask, ACL | [[chp6 - Access Control List (résumé)\|Résumé]] |

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| [[raw/Year 3/Computer Network/02 IP Addressing.pdf\|02 IP Addressing]] | Adressage IPv4 : binaire, classes, masques, CIDR, sous-réseaux | [[02 IP Addressing (résumé)\|Résumé]] |

## Concepts

- **Adressage** : [[Adressage IPv4 et CIDR]]
- **Équipements** : [[CLI Cisco IOS]]
- **Routage** : [[Routage statique]], [[Routage dynamique]]
- **Commutation** : [[VLAN]]
- **Adresses et filtrage** : [[NAT et PAT]], [[Liste de contrôle d'accès]]

## À revoir en priorité avant un examen

- [[Chp4 - VLAN ／ IVR Commands (résumé)]] : `encapsulation dot1q 10` répété sur les trois sous-interfaces.
- [[chp6 - Access Control List (résumé)]] : la solution de l'exigence 4 du TP place l'ACL sur la mauvaise interface.
- [[Chp5 - NAT ／ PAT (résumé)]] : `overlead` pour `overload`, `ip nat outside` hors du mode d'interface, NAT présenté comme un pare-feu.
- [[Chp2 - Static Routing (résumé)]] : « R3 » à la place de R2 dans le tableau des réseaux connectés.

## Liens avec les autres matières

- **[[Year 3 - Data base]]** : l'architecture 3 tiers d'un SGBD repose sur le réseau.
