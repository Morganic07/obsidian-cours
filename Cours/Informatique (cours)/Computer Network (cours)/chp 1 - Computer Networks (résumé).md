---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/chp1 : Computer Networks.docx|chp1 - Computer Networks]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/chp1 : Computer Networks.docx|chp1 - Computer Networks]], dans [[Computer Network (index)]]. Notes personnelles de l'étudiante, en français et en anglais mêlés, des deux premiers cours Cisco : prise en main d'IOS (modes, mémoires, interfaces), puis premières commandes de configuration d'interface et de route statique. Aucune image. En cas d'écart, le cours fait foi.

## Premier cours : Cisco et IOS

### Matériel

- [[Routeur|Routeurs]] utilisés : **Cisco 2911**.
- Commutateurs (*switches*) utilisés : **Cisco 2960**.
- Le système d'exploitation Cisco est **IOS** (« *internetwork Operating System*, je crois », écrit l'étudiante). Voir [[CLI Cisco IOS]].

### Les trois modes de la ligne de commande

| Mode | Invite | Comment y entrer | Rôle |
|---|---|---|---|
| *User mode* | `>` | à l'ouverture de la CLI | commandes très restreintes, comme `show` |
| *Privilege mode* | `#` | `enable` depuis le mode utilisateur | en plus : sauvegarder, effacer, redémarrer la configuration et les appareils |
| *Global Configuration mode* | `(config)#` | `configure terminal` depuis le mode privilégié | toutes les commandes de configuration, sauf les commandes `show` |

- En cliquant sur un PC ou un commutateur (dans Packet Tracer), on accède à sa CLI.
- On **ne peut pas** sauter du mode utilisateur au mode de configuration globale : il faut **toujours passer par le mode privilégié**.
- `exit` revient au mode précédent.
- Certaines commandes d'un mode ne sont pas utilisables dans les autres modes, même dans des modes « supérieurs ».

### Les deux mémoires de configuration

| Mémoire | Caractéristiques | Commandes |
|---|---|---|
| *running-config* | dans la [[Mémoire vive\|RAM]], **effacée au redémarrage** ; c'est là qu'on crée les configurations, avant de les sauvegarder dans la *startup-config* | `show running-config` (voir) ; `write memory` (sauvegarder) |
| *startup-config* | chargée dans la RAM au démarrage (formulation de la note : « fait monter les running config dans la RAM ») | `show startup-config` |

Tout cela se fait en mode privilégié.

### Nommage des interfaces

Une interface s'affiche par exemple `interface FastEthernet0/1` : `0/1` signifie respectivement **slot/port** (voir [[Interface réseau]]).

## Deuxième cours : routage statique

### Syntaxe de la route statique

Voir [[Routage statique]] et [[chp 2 - Static Routing (résumé)]].

```
Router1(config)# ip route {destination network} {subnet mask} {accessible through}
```

Exemple : `Router1(config)# ip route 192.168.20.0 255.255.255.0 g0/2` (le [[Adressage IPv4 et CIDR|masque de sous-réseau]] 255.255.255.0 correspond à un /24).

### Configuration des interfaces, pas à pas

```
Router> enable                    (mode utilisateur : on active le mode privilégié)
Router#                           (mode privilégié)
Router# config terminal
Router(config)#                   (mode de configuration globale)
Router(config)# interface gigabitEthernet 0/1
Router(config-if)# ip address 192.168.10.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

La note commente la ligne `interface gigabitEthernet 0/1` par « *to enable the interface* » et ajoute « je sais pas à quoi tout ça sert » (voir Points à vérifier, 3). On refait la même chose pour l'interface 0/2 :

```
Router(config)# interface gigabitEthernet 0/2
Router(config-if)# ip address 203.0.113.5 255.255.255.252
Router(config-if)# no shutdown
Router(config-if)# exit
```

Route statique de Router1 vers le réseau de destination 192.168.20.0/24 :

```
Router(config)# ip route 192.168.20.0 255.255.255.0 gigabitEthernet 0/2
```

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Cette note n'a aucune image.

1. **« Internetwork Operating System, je crois »** : l'étudiant doute. C'est bien le sens de IOS (complément).
2. **« Global Config permet toutes les commandes de configuration sauf les show »** : sur IOS, `show` se lance depuis une configuration avec `do show ...`. Le cours dit que certaines commandes ne marchent pas dans les autres modes, ce qui reste vrai (complément).
3. **Étudiant : « je sais pas à quoi tout ça sert »** : `ip address` donne son adresse à l'interface et `no shutdown` l'active (une interface de routeur est désactivée par défaut, voir [[VLAN]]). Le commentaire « to enable the interface » placé à côté de `interface gigabitEthernet 0/1` est donc inexact : cette ligne sélectionne l'interface (complément).
4. **Adressage de l'exemple** : l'interface 0/2 reçoit `203.0.113.5/255.255.255.252`, alors que l'exemple de route cible 192.168.20.0 via `g0/2`. Ce n'est pas le même plan d'adressage que dans [[chp 2 - Static Routing (résumé)|Chp2 - Static Routing]].
5. **Redondance** : les sections du mode de la ligne de commande sont répétées dans [[CISCO Packet Tracer (résumé)|Formation CISCO Packet Tracer]].
