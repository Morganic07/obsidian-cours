---
type: concept
tags: [year3]
aliases: [dot1q, encapsulation dot1q, 802.1Q]
matieres: [Computer Network]
sources: ["[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-07
---

[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]] donne seulement la commande de sous-interface `encapsulation dot1q <VLAN>`, qui associe la sous-interface à son VLAN, sans expliquer la norme.

Notion parente : [[VLAN]]. Voir aussi : [[Sous-interface]].

## Erreurs du cours

- [[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]] écrit « encapsulation dot1q 10 » sous les sous-interfaces `gigabitEthernet 0/1.20` et `0/1.30` ; il faut « encapsulation dot1q 20 » et « encapsulation dot1q 30 », d'après leurs adresses 192.168.20.254 et 192.168.30.254. Les mêmes lignes écrivent aussi « ip 192.168.x.254 … » là où IOS attend « ip address 192.168.x.254 … ».

Résumés : [[4 - VLAN ／ IVR Commands]]
