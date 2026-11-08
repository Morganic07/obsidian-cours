---
type: concept
tags: [year3]
aliases: [ARP, Address Resolution Protocol, cache ARP, table ARP, requête ARP]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]", "[[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]]", "[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]", "[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : ARP (*Address Resolution Protocol*, RFC 826, 1982) permet à une machine de trouver l'adresse MAC qui correspond à une adresse IPv4 de son réseau local, pour pouvoir lui livrer une trame Ethernet. Il fait le lien entre la couche 3 (IP) et la couche 2 (Ethernet) du [[Modèle OSI|modèle OSI]].

**Fonctionnement** :
1. L'hôte qui veut joindre 192.168.10.5 consulte d'abord son cache ARP.
2. S'il n'y trouve pas l'adresse, il diffuse une **requête ARP** dans une trame de diffusion (adresse MAC de destination FF:FF:FF:FF:FF:FF) : « qui a 192.168.10.5 ? Répondez à 192.168.10.1 ». Toutes les machines du [[Domaine de diffusion|domaine de diffusion]] la reçoivent.
3. Seule la machine qui possède cette adresse répond, en **unicast**, avec son adresse MAC.
4. L'hôte inscrit la correspondance dans son **cache ARP**, où elle est gardée un temps limité, puis envoie ses trames.

**Destination hors du sous-réseau** : l'hôte ne cherche pas la MAC de la destination, qu'il ne peut pas atteindre directement ; il demande en ARP la MAC de sa [[Passerelle par défaut|passerelle par défaut]] et lui remet la trame, l'adresse IP de destination restant celle de la machine finale.

**Commandes** : `arp -a` (Windows, et Linux avec le paquet net-tools), `ip neigh` sous Linux (voir [[Commande ip]]), `show ip arp` ou `show arp` sur un routeur Cisco.

**Portée** : les requêtes ARP, diffusées, ne franchissent pas un routeur et restent dans le domaine de diffusion ; découper un réseau en [[VLAN]] les limite donc. En [[IPv6]], ARP est remplacé par NDP (*Neighbor Discovery Protocol*), qui passe par ICMPv6 et des adresses multicast plutôt que par la diffusion.

## Dans le cours

Le cours ne le présente pas. Les compléments des fiches le citent :
- [[2 - IP Addressing]] : sur un réseau local, ARP trouve l'adresse MAC qui correspond à une adresse IP pour livrer la trame ;
- [[4 - VLAN ／ IVR Commands]] : la requête ARP comme exemple de trame de diffusion qui définit le domaine de diffusion ;
- [[7 - Cisco]] : il explique pourquoi le premier paquet d'un premier `ping` est souvent perdu dans Packet Tracer (*Request timed out*) : le PC attend la réponse ARP de la destination ou de sa passerelle, et la première requête expire pendant ce temps ;
- [[2 - Static Routing]] : une route statique qui ne donne que l'interface de sortie oblige le routeur à une requête ARP par destination, et à compter sur le *proxy ARP* du voisin.

Voir aussi : [[Domaine de diffusion]], [[Passerelle par défaut]], [[Modèle OSI]], [[Commutateur]], [[Commande ping]], [[DHCP]].

Résumés : [[2 - IP Addressing]], [[4 - VLAN ／ IVR Commands]], [[7 - Cisco]], [[2 - Static Routing]]
