---
type: concept
tags: [year3]
aliases: [MAC address, adresse physique, adresses MAC, MAC addresses, adresse Ethernet]
sources: ["[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'adresse MAC (*Media Access Control*) est l'identifiant physique d'une [[Interface réseau|interface réseau]] (carte Ethernet, Wi-Fi). Elle compte **48 bits**, écrits en six octets hexadécimaux : `00:1A:2B:3C:4D:5E` (ou `00-1A-2B-3C-4D-5E`, `001a.2b3c.4d5e` chez Cisco). Elle est attribuée par le fabricant :

- les **24 premiers bits** forment l'**OUI** (*Organizationally Unique Identifier*), qui identifie le fabricant ;
- les 24 bits suivants sont numérotés par le fabricant pour chaque interface.

L'adresse `FF:FF:FF:FF:FF:FF` est l'adresse de broadcast de la couche liaison : la trame est reçue par toutes les machines du réseau local.

**Rôle** : l'adresse MAC sert à livrer les **trames** à l'intérieur d'un même réseau local (couche 2). Un [[Commutateur]] achemine les trames d'après elle : il apprend sur quel port se trouve chaque adresse MAC source et range cette correspondance dans sa table d'adresses MAC.

**Adresse MAC et adresse IP**

| | Adresse MAC | Adresse IP |
|---|---|---|
| Nature | physique, fixée par le fabricant | logique, configurée ou attribuée |
| Taille | 48 bits | 32 bits (IPv4) |
| Structure | plate (fabricant puis numéro) | hiérarchique (réseau puis hôte) |
| Portée | le réseau local | de bout en bout, entre réseaux |
| Utilisée par | le commutateur | le [[Routeur]] |

Quand un paquet traverse plusieurs réseaux, ses adresses IP source et destination restent les mêmes, mais les adresses MAC de la trame changent à chaque saut.

**ARP** (*Address Resolution Protocol*) : pour envoyer un paquet à une adresse IP du réseau local, l'hôte doit connaître l'adresse MAC correspondante. Il envoie une requête ARP en broadcast (« qui a l'adresse 192.168.1.10 ? ») ; la machine concernée répond en unicast avec son adresse MAC, que l'émetteur garde dans son cache ARP. Pour une destination hors du réseau local, l'hôte cherche l'adresse MAC de sa passerelle par défaut, pas celle de la destination.

## Dans le cours

Le cours ne la nomme pas : [[2 - IP Addressing]] qualifie l'adresse IP de « software address » sans la mettre en regard de l'adresse physique. Elle apparaît dans les compléments de cette fiche.

Voir aussi : [[Adressage IPv4 et CIDR]], [[Commutateur]], [[Interface réseau]], [[Routeur]], [[Routage IP]].

Résumés : [[2 - IP Addressing]]
