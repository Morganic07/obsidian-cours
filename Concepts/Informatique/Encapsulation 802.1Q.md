---
type: concept
tags: [year3]
aliases: [dot1q, encapsulation dot1q, 802.1Q, IEEE 802.1Q, étiquette 802.1Q, 802.1Q tag, VLAN tagging, VLAN natif, native VLAN]
matieres: [Computer Network]
sources: ["[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]", "[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : IEEE 802.1Q est la norme d'étiquetage des trames Ethernet sur un lien *trunk*, qui permet à un même lien de transporter le trafic de plusieurs [[VLAN]]. Une étiquette (*tag*) de 4 octets est insérée dans l'en-tête Ethernet, juste après l'adresse MAC source :

| Champ | Taille | Rôle |
|---|---|---|
| TPID (*Tag Protocol Identifier*) | 16 bits | vaut 0x8100 : signale une trame étiquetée |
| PCP (*Priority Code Point*) | 3 bits | priorité de la trame (qualité de service, 802.1p), de 0 à 7 |
| DEI (*Drop Eligible Indicator*) | 1 bit | trame à éliminer en premier en cas de congestion |
| VID (*VLAN Identifier*) | 12 bits | numéro du VLAN : $2^{12} = 4096$ valeurs, de 1 à 4094 utilisables (0 et 4095 réservés) |

L'insertion de l'étiquette modifie la trame, dont le commutateur recalcule la somme de contrôle (FCS).

- Les liens *access* transportent des trames **non étiquetées** : l'hôte ignore à quel VLAN il appartient, c'est le commutateur qui ajoute ou retire l'étiquette.
- Le **VLAN natif** (VLAN 1 par défaut chez Cisco) traverse le *trunk* **sans étiquette** ; il doit être le même aux deux bouts du lien, sinon les trames passent d'un VLAN à l'autre (Cisco le signale par un message *native VLAN mismatch*).
- **ISL** (*Inter-Switch Link*), l'ancien protocole propriétaire de Cisco, encapsulait toute la trame au lieu d'y insérer une étiquette ; il a été abandonné au profit de 802.1Q.
- **Commandes** sur un commutateur Cisco : `switchport mode trunk` ; `switchport trunk native vlan <id>` pour changer le VLAN natif ; `switchport trunk encapsulation dot1q`, à donner avant `switchport mode trunk` sur les modèles qui gèrent aussi ISL. Sur une [[Sous-interface|sous-interface]] de routeur : `encapsulation dot1q <id>` (voir [[Routeur sur un bâton]]).

## Dans le cours

[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]] donne seulement la commande de sous-interface `encapsulation dot1q <VLAN>`, qui associe la sous-interface à son VLAN, sans expliquer la norme.

Notion parente : [[VLAN]]. Voir aussi : [[Sous-interface]].

Résumés : [[4 - VLAN ／ IVR Commands]]
