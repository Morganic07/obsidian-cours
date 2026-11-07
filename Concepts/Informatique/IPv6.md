---
type: concept
tags:
  - year2
  - year3
aliases:
  - adresse IPv6
  - inet6
matieres:
  - Operating System
  - Computer Network
sources:
  - "[[3 - TP3|Cours TP3]]"
  - "[[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]]"
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : IPv6 (Internet Protocol version 6) est la version du protocole IP qui succède à IPv4. Ses adresses font 128 bits au lieu de 32, soit environ 3,4 × 10³⁸ adresses, et s'écrivent en huit groupes de quatre chiffres hexadécimaux séparés par `:` (par exemple `2001:db8::1`, où `::` abrège une suite de groupes nuls).

## Dans le cours

Nommé sans définition dans deux matières :

- **Operating System** : dans l'annotation de la sortie de `ifconfig`, `inet6` désigne l'adresse IPv6 (l'IPv4 étant `inet`).
- **Computer Network** : le cours cite IPv6 comme la solution à long terme au manque d'adresses IPv4 (environ 4,3 milliards, soit $2^{32}$) ; à court terme, on recourt à CIDR, aux adresses privées et au [[NAT et PAT|NAT]].

Notion parente : [[Adressage IPv4 et CIDR]]. Voir aussi : [[Interface réseau]].

## Erreurs du cours

- [[5 - NAT ／ PAT|Chp5 - NAT ／ PAT]] écrit « IPv4 provides only 4.2 milliards de IP » ; il faut 4,3 milliards ($2^{32} = 4\,294\,967\,296$), comme l'écrit 02 IP Addressing ([[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]).

Résumés : [[3 - TP3]], [[5 - NAT ／ PAT]]
