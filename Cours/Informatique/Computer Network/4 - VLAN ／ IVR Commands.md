---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : définitions (routeur, commutateur, VLAN, liens *access* et *trunk*), commandes de création des VLAN, d'affectation des ports, de lien *trunk*, et routage inter-VLAN (IVR) sur un routeur. Cours en anglais, sans image. Voir [[VLAN]].

## Définitions

| Terme | Définition du cours |
|---|---|
| [[Routeur]] (*router*) | relie entre eux des **réseaux différents** |
| [[Commutateur]] (*switch*) | relie les terminaux au [[Réseau local\|LAN]] |
| [[VLAN]] | crée **plusieurs domaines de diffusion** (*broadcast domains*) sur le commutateur ; autrement dit, découper le [[Domaine de diffusion\|domaine de diffusion]] d'un commutateur s'appelle un VLAN |
| Lien *access* (*access link*) | associé à **un seul VLAN** |
| Lien *trunk* (*trunk link*) | transporte le trafic de **plusieurs VLAN** |

- Par défaut, un commutateur Cisco a **un seul domaine de diffusion** : tous ses ports sont associés au **VLAN 1**.
- Le VLAN 1 est aussi le **VLAN par défaut**, qui **ne peut pas être supprimé**.

## Créer les VLAN

Syntaxe : `Switch(config)# vlan <ID>`, puis `name <nom>` dans le mode `config-vlan`.

```
Switch(config)# vlan 10
Switch(config-vlan)# name ADMIN
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name SALES
Switch(config-vlan)# exit

Switch(config)# vlan 30
Switch(config-vlan)# name WORKGROUP
Switch(config-vlan)# exit
```

| VLAN | Nom |
|---|---|
| 10 | ADMIN |
| 20 | SALES |
| 30 | WORKGROUP |

## Associer les ports aux VLAN

On sélectionne une plage de ports avec `interface range`, on la passe en mode *access*, puis on l'affecte à un VLAN.

```
Switch(config)# interface range fastEthernet 0/1-5
Switch(config-ifrange)# switchport mode access
Switch(config-ifrange)# switchport access vlan 10
Switch(config-ifrange)# exit

Switch(config)# interface range fastEthernet 0/6-10
Switch(config-ifrange)# switchport mode access
Switch(config-ifrange)# switchport access vlan 20
Switch(config-ifrange)# exit

Switch(config)# interface range fastEthernet 0/11-15
Switch(config-ifrange)# switchport mode access
Switch(config-ifrange)# switchport access vlan 30
Switch(config-ifrange)# exit
```

| Ports ([[Interface réseau\|FastEthernet]]) | VLAN |
|---|---|
| 0/1 à 0/5 | 10 (ADMIN) |
| 0/6 à 0/10 | 20 (SALES) |
| 0/11 à 0/15 | 30 (WORKGROUP) |

## Créer un lien *trunk* entre deux commutateurs

Même configuration des deux côtés, sur l'interface qui relie les commutateurs :

```
Switch1(config)# interface gigabitEthernet 0/1
Switch1(config-if)# switchport mode trunk
Switch1(config-if)# switchport trunk allowed vlan add 10
Switch1(config-if)# switchport trunk allowed vlan add 20
Switch1(config-if)# switchport trunk allowed vlan add 30
Switch1(config-if)# exit

Switch2(config)# interface gigabitEthernet 0/1
Switch2(config-if)# switchport mode trunk
Switch2(config-if)# switchport trunk allowed vlan add 10
Switch2(config-if)# switchport trunk allowed vlan add 20
Switch2(config-if)# switchport trunk allowed vlan add 30
Switch2(config-if)# exit
```

## IVR : routage inter-VLAN (*Inter VLAN Routing*)

- L'IVR permet la **communication entre VLAN différents**.
- Il faut un **routeur**.
- Le routeur est relié au commutateur par un **lien *trunk***.

### Commandes sur le routeur

Une [[Sous-interface|sous-interface]] par VLAN (`gigabitEthernet 0/1.<VLAN>`), avec l'[[Encapsulation 802.1Q|encapsulation `dot1q`]] du VLAN et une adresse IP qui sert de **[[Passerelle par défaut|passerelle par défaut]]** (*default gateway*) aux hôtes du VLAN. Code tel qu'il figure dans le cours :

```
Router(config)# interface gigabitEthernet 0/1.10
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip 192.168.10.254 255.255.255.0   <this is default gateway IP>
Router(config-subif)# exit

Router(config)# interface gigabitEthernet 0/1.20
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip 192.168.20.254 255.255.255.0
Router(config-subif)# exit

Router(config)# interface gigabitEthernet 0/1.30
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip 192.168.30.254 255.255.255.0
Router(config-subif)# exit
```

(les lignes `dot1q 10` des sous-interfaces `.20` et `.30`, et la commande `ip` au lieu de `ip address`, sont des erreurs du cours, voir « Erreurs du cours »).

| Sous-interface | VLAN | Passerelle des hôtes |
|---|---|---|
| G0/1.10 | 10 | 192.168.10.254/24 |
| G0/1.20 | 20 | 192.168.20.254/24 |
| G0/1.30 | 30 | 192.168.30.254/24 |

### Activer l'interface physique

```
Router(config)# interface gigabitEthernet 0/1
Router(config-if)# no shutdown
```

**À retenir : tous les ports d'un routeur sont désactivés par défaut.**

## Erreurs du cours

- [[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]], sous-interfaces du routeur : écrit `encapsulation dot1q 10` pour les trois sous-interfaces ; il faut `encapsulation dot1q 20` pour `gigabitEthernet 0/1.20` et `encapsulation dot1q 30` pour `gigabitEthernet 0/1.30` (copier-coller du premier bloc). **À retenir pour un examen.**
- Même document, adresse des sous-interfaces : écrit `ip 192.168.10.254 255.255.255.0` (et de même pour .20 et .30) ; il faut `ip address 192.168.10.254 255.255.255.0`.
