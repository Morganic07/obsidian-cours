---
type: concept
tags: [year3]
aliases: [layer 3 switch, multilayer switch, commutateur multicouche, switch de niveau 3, SVI, switch virtual interface, interface VLAN]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : [[Commutateur|commutateur]] capable aussi de router des paquets IP entre ses [[VLAN]], c'est-à-dire de travailler aux couches 2 et 3 du [[Modèle OSI|modèle OSI]]. Le routage se fait en matériel (circuits spécialisés), donc à la vitesse de la commutation.

**Interfaces virtuelles (SVI)** : le commutateur route par des interfaces virtuelles de VLAN (*Switch Virtual Interface*), une par VLAN ; l'adresse IP de la SVI sert de [[Passerelle par défaut|passerelle par défaut]] aux hôtes du VLAN. Configuration type sur Cisco :

```
Switch(config)# ip routing
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.10.254 255.255.255.0
Switch(config-if)# no shutdown
```

`ip routing` active le routage, désactivé par défaut. Une SVI n'est active que si son VLAN existe et qu'au moins un port de ce VLAN est actif. Un port peut aussi devenir un port routé, comme celui d'un routeur, par `no switchport`.

**Usage** : c'est la solution courante pour le routage inter-VLAN dans les réseaux d'entreprise, au cœur ou à la distribution du réseau ; le [[Routeur|routeur]] reste en bordure, pour ce qu'un commutateur fait mal ou pas : [[NAT et PAT|NAT]], lien vers Internet ou le WAN.

**Avantage sur le [[Routeur sur un bâton|routeur sur un bâton]]** : pas de goulot d'un lien unique entre commutateur et routeur, le trafic inter-VLAN étant routé dans le commutateur lui-même.

**Différence avec un commutateur simple** : un commutateur de niveau 2 peut avoir une SVI (`interface vlan 1`), mais seulement pour être administré à distance (SSH, Telnet) ; il ne route pas entre VLAN.

## Dans le cours

Le cours ne le présente pas. Il apparaît dans les compléments de [[4 - VLAN ／ IVR Commands]], comme alternative au routeur relié par un *trunk* pour le routage inter-VLAN.

Voir aussi : [[Commutateur]], [[Routeur]], [[VLAN]], [[Modèle OSI]], [[Routeur sur un bâton]], [[Passerelle par défaut]].

Résumés : [[4 - VLAN ／ IVR Commands]]
