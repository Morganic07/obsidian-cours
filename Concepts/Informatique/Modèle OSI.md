---
type: concept
tags: [year3, year4]
aliases: [OSI model, modèle de référence OSI, Open Systems Interconnection, couches OSI, OSI layers, modèle TCP/IP]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]", "[[Raw/Year 3/Computer Network/Formation CISCO Packet Tracer.docx|Formation CISCO Packet Tracer]]"]
maj: 2026-11-10
---

**Définition (complément, hors du cours)** : le modèle OSI (*Open Systems Interconnection*) est le modèle de référence de l'ISO (norme ISO/IEC 7498, 1984) qui découpe la communication réseau en sept couches. Chaque couche rend un service à la couche du dessus en s'appuyant sur celle du dessous, et dialogue avec la couche de même niveau de la machine distante par son propre protocole.

| N° | Couche | Unité de données | Rôle, exemples |
|---|---|---|---|
| 7 | Application | données | services offerts aux applications : HTTP, DNS, SMTP, FTP |
| 6 | Présentation | données | représentation des données : codage, chiffrement, compression |
| 5 | Session | données | ouverture, maintien et fermeture des dialogues |
| 4 | Transport | segment (TCP), datagramme (UDP) | communication de bout en bout entre applications, identifiées par leur [[Numéro de port\|numéro de port]] : TCP (fiable, ordonné), UDP (sans garantie) |
| 3 | Réseau | paquet | adressage logique (adresses IP) et choix de la route : [[Routeur\|routeur]], IP, [[ICMP]] |
| 2 | Liaison de données | trame | livraison sur un même réseau local, adresses MAC : [[Commutateur\|commutateur]], Ethernet, [[VLAN]] |
| 1 | Physique | bit | transmission des bits sur le support : câbles, fibre, ondes, connecteurs |

**Encapsulation** : à l'émission, chaque couche ajoute son en-tête aux données reçues de la couche du dessus (un segment TCP est placé dans un paquet IP, lui-même placé dans une trame Ethernet) ; à la réception, chaque couche retire l'en-tête de son niveau et passe le reste à la couche du dessus (désencapsulation).

**Modèle TCP/IP** : celui d'Internet, conçu avant OSI et resté la référence pratique. Il regroupe les couches en quatre : accès réseau (OSI 1 et 2), Internet (OSI 3, IP), transport (OSI 4, TCP et UDP), application (OSI 5 à 7). OSI sert surtout de vocabulaire : on parle d'un « équipement de couche 2 » ou d'un « problème de couche 1 ».

**Placer les équipements** : un commutateur travaille en couche 2 (il achemine les trames selon l'adresse MAC), un routeur en couche 3 (il achemine les paquets selon l'adresse IP), un [[Commutateur de niveau 3|commutateur de niveau 3]] fait les deux. Le [[Protocole ARP|protocole ARP]] fait le lien entre couche 3 et couche 2, en trouvant l'adresse MAC qui correspond à une adresse IP.

## Dans le cours

Le cours ne le présente pas. Les compléments de [[4 - VLAN ／ IVR Commands]] et de [[7 - Cisco]] situent le routeur au niveau 3 (adresses IP, table de routage) et le commutateur au niveau 2 (adresses MAC, table MAC) ; [[6 - Access Control List]] parle des ports de couche 4.

Voir aussi : [[Commutateur]], [[Routeur]], [[Numéro de port]], [[Protocole ARP]], [[Interface réseau]], [[Modèle client-serveur]], [[Suite des protocoles Internet]], [[Ethernet]], [[HTTP]].

[[2 - Histoire du design]] : complément (le Web est une application de la couche la plus haute, au-dessus du transport TCP et de l'adressage IP).

Résumés : [[4 - VLAN ／ IVR Commands]], [[7 - Cisco]] · [[2 - Histoire du design]]
