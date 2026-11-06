---
type: concept
aliases: [subinterface, sub-interface, sous-interfaces, config-subif]
matieres: [Computer Network]
sources: ["[[Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-06
---

Pour le routage inter-VLAN, le routeur reçoit une sous-interface par VLAN sur l'interface reliée au trunk (`interface gigabitEthernet 0/1.10`). Chaque sous-interface porte `encapsulation dot1q <VLAN>` et une adresse IP qui sert de [[Passerelle par défaut]] aux hôtes du VLAN. L'interface physique doit aussi être activée par `no shutdown`.

Notion parente : [[VLAN]]. Voir aussi : [[Encapsulation 802.1Q]].

## À vérifier

- Le cours écrit `ip 192.168.10.254 255.255.255.0` au lieu de `ip address ...`.

Résumés : [[Chp4 - VLAN ／ IVR Commands (résumé)]]
