---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp4 :  VLAN ／ IVR Commands.docx|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
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

Le routeur travaille au niveau 3 du [[Modèle OSI|modèle OSI]] (adresses IP, table de routage) ; le commutateur, au niveau 2 (adresses MAC) : il apprend sur quel port se trouve chaque adresse MAC (table MAC) et n'envoie une trame que vers le port du destinataire. [[Complément hors du cours|ⓘ]]

**Domaine de diffusion** : l'ensemble des appareils qu'atteint une trame de diffusion (*broadcast*, adresse MAC FF:FF:FF:FF:FF:FF), par exemple une requête [[Protocole ARP|ARP]] (« qui a l'adresse IP 192.168.10.5 ? ») ou une demande [[DHCP]]. Le commutateur recopie une telle trame sur tous ses ports ; le routeur, lui, ne la transmet pas : il borne le domaine de diffusion. Plus le domaine est grand, plus ces diffusions encombrent le réseau et sont visibles de tous. [[Complément hors du cours|ⓘ]]

Un VLAN est donc un **réseau local logique** : les ports d'un même VLAN se comportent comme s'ils étaient sur un commutateur à part, même répartis sur plusieurs commutateurs, et deux hôtes de VLAN différents ne se voient plus au niveau 2. Intérêts : limiter les diffusions, **séparer** les services (le VLAN SALES ne voit pas le trafic du VLAN ADMIN), regrouper des utilisateurs par fonction plutôt que par emplacement. Chaque VLAN correspond en pratique à **un sous-réseau IP** distinct (ici 192.168.10.0/24, 192.168.20.0/24, 192.168.30.0/24). [[Complément hors du cours|ⓘ]]

- Par défaut, un commutateur Cisco a **un seul domaine de diffusion** : tous ses ports sont associés au **VLAN 1**.
- Le VLAN 1 est aussi le **VLAN par défaut**, qui **ne peut pas être supprimé**.
- L'identifiant de VLAN (*VLAN ID*) tient sur 12 bits dans l'étiquette 802.1Q, d'où les numéros utilisables de **1 à 4094** (0 et 4095 sont réservés). Chez Cisco, la plage normale va de 1 à 1005 (1002 à 1005 étant réservés aux anciennes technologies FDDI et Token Ring et non supprimables, comme le VLAN 1, selon les guides de configuration Cisco IOS des commutateurs Catalyst) et la plage étendue de 1006 à 4094. [[Complément hors du cours|ⓘ]]

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

Pour vérifier : `show vlan brief` liste les VLAN et les ports *access* de chacun ; `show interfaces trunk` liste les liens *trunk* et les VLAN qu'ils transportent. Les VLAN créés sont enregistrés dans le fichier `vlan.dat` de la mémoire flash du commutateur, à part de la configuration. [[Complément hors du cours|ⓘ]]

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

Sur un lien *trunk*, chaque trame reçoit une **étiquette** (*tag*) de 4 octets, insérée dans l'en-tête Ethernet selon la norme IEEE [[Encapsulation 802.1Q|802.1Q]] : elle porte le numéro de VLAN, ce qui permet au commutateur d'en face de remettre la trame dans le bon VLAN. Un lien *access* transporte des trames sans étiquette : l'hôte ignore à quel VLAN il appartient. Exception : les trames du **VLAN natif** (VLAN 1 par défaut) traversent le *trunk* sans étiquette ; il doit être le même aux deux bouts du lien. Cisco avait aussi un protocole propriétaire, ISL, abandonné au profit de 802.1Q. [[Complément hors du cours|ⓘ]]

Par défaut, un *trunk* Cisco laisse passer **tous** les VLAN : les commandes `allowed vlan add` ne changent rien tant que la liste n'a pas été restreinte. Pour n'autoriser que ces trois VLAN, on écrit `switchport trunk allowed vlan 10,20,30` (sans `add`, la liste est remplacée). Sur les commutateurs qui gèrent aussi l'ancien ISL, il faut choisir l'encapsulation avant le mode : `switchport trunk encapsulation dot1q`. [[Complément hors du cours|ⓘ]]

## IVR : routage inter-VLAN (*Inter VLAN Routing*)

- L'IVR permet la **communication entre VLAN différents**.
- Il faut un **routeur**.
- Le routeur est relié au commutateur par un **lien *trunk***.
- Pourquoi un routeur : deux VLAN sont deux réseaux IP distincts, et un hôte n'envoie directement (au niveau 2) qu'aux hôtes de son propre sous-réseau. Pour joindre un autre sous-réseau, il envoie la trame à sa **passerelle par défaut**, qui route le paquet vers l'autre VLAN : c'est un passage par le niveau 3. [[Complément hors du cours|ⓘ]]
- Ce montage, un seul lien physique en *trunk* découpé en sous-interfaces, s'appelle le **[[Routeur sur un bâton|routeur sur un bâton]]** (*router-on-a-stick*). Deux autres solutions existent : relier le routeur au commutateur par **un câble et une interface physique par VLAN** (simple, mais consomme autant de ports que de VLAN), ou utiliser un **[[Commutateur de niveau 3|commutateur de niveau 3]]**, qui route lui-même entre ses VLAN par des interfaces virtuelles (`interface vlan 10`, SVI) après `ip routing`, solution courante dans les réseaux d'entreprise. Le routeur sur un bâton a une limite : tout le trafic inter-VLAN partage le débit d'un seul lien. [[Complément hors du cours|ⓘ]]

### Commandes sur le routeur

Une [[Sous-interface|sous-interface]] par VLAN (`gigabitEthernet 0/1.<VLAN>`), avec l'[[Encapsulation 802.1Q|encapsulation `dot1q`]] du VLAN et une adresse IP qui sert de **[[Passerelle par défaut|passerelle par défaut]]** (*default gateway*) aux hôtes du VLAN. Chaque sous-interface porte le numéro de son propre VLAN dans `encapsulation dot1q`, et l'adresse se donne par `ip address` : [[Erreurs du cours#^e-4-vlan-ivr-commands|✎]]

```
Router(config)# interface gigabitEthernet 0/1.10
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip address 192.168.10.254 255.255.255.0   <this is default gateway IP>
Router(config-subif)# exit

Router(config)# interface gigabitEthernet 0/1.20
Router(config-subif)# encapsulation dot1q 20
Router(config-subif)# ip address 192.168.20.254 255.255.255.0
Router(config-subif)# exit

Router(config)# interface gigabitEthernet 0/1.30
Router(config-subif)# encapsulation dot1q 30
Router(config-subif)# ip address 192.168.30.254 255.255.255.0
Router(config-subif)# exit
```

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

Les sous-interfaces suivent l'état de l'interface physique : un seul `no shutdown`, sur `gigabitEthernet 0/1`, les active toutes. À l'inverse, les ports d'un commutateur Cisco sont actifs par défaut. Sur le commutateur, le port relié au routeur doit être en `switchport mode trunk` ; les hôtes de chaque VLAN reçoivent comme passerelle l'adresse .254 de leur sous-réseau. [[Complément hors du cours|ⓘ]]