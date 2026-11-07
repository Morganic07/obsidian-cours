---
type: concept
tags: [year3]
aliases: [subinterface, sub-interface, sous-interfaces, config-subif]
matieres: [Computer Network]
sources: ["[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-07
---

Pour le routage inter-VLAN, le routeur reçoit une sous-interface par VLAN sur l'interface reliée au trunk (`interface gigabitEthernet 0/1.10`). Chaque sous-interface porte `encapsulation dot1q <VLAN>` et une adresse IP qui sert de [[Passerelle par défaut]] aux hôtes du VLAN. L'interface physique doit aussi être activée par `no shutdown`.

Notion parente : [[VLAN]]. Voir aussi : [[Encapsulation 802.1Q]].

## Erreurs du cours

- [[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]] écrit `Router(config-subif)# ip 192.168.10.254 255.255.255.0` (de même pour .20 et .30) ; il faut `ip address 192.168.10.254 255.255.255.0`.
- Le même exemple écrit `encapsulation dot1q 10` sur les trois sous-interfaces ; il faut `encapsulation dot1q 20` pour `gigabitEthernet 0/1.20` et `encapsulation dot1q 30` pour `0/1.30`, le numéro du VLAN de chaque sous-interface.

Résumés : [[4 - VLAN ／ IVR Commands]]
