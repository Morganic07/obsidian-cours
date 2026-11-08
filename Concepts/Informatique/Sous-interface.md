---
type: concept
tags: [year3]
aliases: [subinterface, sub-interface, sous-interfaces, config-subif]
matieres: [Computer Network]
sources: ["[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-08
---

Pour le routage inter-VLAN, le routeur reçoit une sous-interface par VLAN sur l'interface reliée au trunk (`interface gigabitEthernet 0/1.10`). Chaque sous-interface porte `encapsulation dot1q <VLAN>`, avec le numéro de son propre VLAN, et une adresse IP donnée par `ip address`, qui sert de [[Passerelle par défaut]] aux hôtes du VLAN. [[Erreurs du cours#^e-sous-interface|✎]] L'interface physique doit aussi être activée par `no shutdown`.

Notion parente : [[VLAN]]. Voir aussi : [[Encapsulation 802.1Q]].

Résumés : [[4 - VLAN ／ IVR Commands]]
