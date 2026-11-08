---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/chp1 : Computer Networks.docx|chp1 - Computer Networks]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/chp1 : Computer Networks.docx|chp1 - Computer Networks]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]]. Notes personnelles de l'étudiante, en français et en anglais mêlés, des deux premiers cours Cisco : prise en main d'IOS (modes, mémoires, interfaces), puis premières commandes de configuration d'interface et de route statique. Aucune image.

## Premier cours : Cisco et IOS

### Matériel

- [[Routeur|Routeurs]] utilisés : **Cisco 2911**.
- Commutateurs (*switches*) utilisés : **Cisco 2960**.
- Le système d'exploitation Cisco est **IOS** (« *internetwork Operating System*, je crois », écrit l'étudiante). Voir [[CLI Cisco IOS]].
- IOS signifie bien *Internetwork Operating System*. Un routeur relie des réseaux différents et choisit le chemin des paquets (couche réseau, adresses IP) ; un [[Commutateur|commutateur]] relie les machines d'un même réseau local et achemine les trames d'après les adresses physiques ([[Adresse MAC|adresses MAC]]). [[Complément hors du cours|ⓘ]]
- **Cisco Packet Tracer** est le simulateur de réseau fourni par Cisco pour sa formation (Cisco Networking Academy) : on y place des équipements virtuels, on les câble et on les configure avec la même CLI IOS que sur le matériel réel. [[Complément hors du cours|ⓘ]]

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
- Pour lancer une commande `show` sans quitter la configuration, on la préfixe par `do` : `Router(config)# do show ip route`. [[Complément hors du cours|ⓘ]]
- Depuis la configuration globale, on entre dans des **sous-modes** : `interface …` donne `(config-if)#` (configuration d'une interface, utilisé plus bas), `router …` donne `(config-router)#` (protocole de routage), `line …` donne `(config-line)#` (accès console ou à distance). `exit` remonte d'un niveau, `end` (ou Ctrl+Z) revient directement au mode privilégié. [[Complément hors du cours|ⓘ]]
- Aides de la CLI : `?` liste les commandes ou les paramètres possibles à l'endroit du curseur, Tab complète un mot, et toute commande s'abrège tant qu'elle reste sans ambiguïté (`conf t` pour `configure terminal`, `sh` pour `show`, `g0/1` pour `gigabitEthernet 0/1`). [[Complément hors du cours|ⓘ]]

### Les deux mémoires de configuration

| Mémoire | Caractéristiques | Commandes |
|---|---|---|
| *running-config* | dans la [[Mémoire vive\|RAM]], **effacée au redémarrage** ; c'est là qu'on crée les configurations, avant de les sauvegarder dans la *startup-config* | `show running-config` (voir) ; `write memory` (sauvegarder) |
| *startup-config* | au démarrage, copiée dans la RAM, où elle devient la *running-config* [[Erreurs du cours#^e-1-computer-networks\|✎]] | `show startup-config` |

Tout cela se fait en mode privilégié.

La *startup-config* est stockée en **NVRAM**, une mémoire non volatile, ce qui explique qu'elle survive au redémarrage ; `write memory` équivaut à `copy running-config startup-config`. Un routeur Cisco a aussi une mémoire **flash** (qui contient l'image du système IOS) et une **ROM** (programme de démarrage et tests matériels). Pour repartir d'une configuration vierge : `erase startup-config`, puis `reload`. Voir [[Mémoire volatile et non volatile]]. [[Complément hors du cours|ⓘ]]

### Nommage des interfaces

Une interface s'affiche par exemple `interface FastEthernet0/1` : `0/1` signifie respectivement **slot/port** (voir [[Interface réseau]]).

Le type d'interface indique le débit : *FastEthernet* (abrégé `fa`) à 100 Mbit/s, *GigabitEthernet* (`g` ou `gi`) à 1 Gbit/s. Le routeur 2911 du cours a trois ports GigabitEthernet, `g0/0` à `g0/2`, utilisés dans les exemples qui suivent. [[Complément hors du cours|ⓘ]]

## Deuxième cours : routage statique

### Syntaxe de la route statique

Voir [[Routage statique]] et [[2 - Static Routing]].

```
Router1(config)# ip route {destination network} {subnet mask} {accessible through}
```

Exemple : `Router1(config)# ip route 192.168.20.0 255.255.255.0 g0/2` (le [[Adressage IPv4 et CIDR|masque de sous-réseau]] 255.255.255.0 correspond à un /24).

La commande se lit : « pour joindre le réseau 192.168.20.0 de masque 255.255.255.0, envoyer les paquets par l'interface g0/2 ». Le dernier paramètre est soit une **interface de sortie**, soit l'**adresse IP du saut suivant** (le routeur voisin) : les deux variantes sont détaillées dans [[2 - Static Routing]]. [[Complément hors du cours|ⓘ]]

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

La ligne `interface gigabitEthernet 0/1` **sélectionne** l'interface (passage en mode `config-if`) ; c'est `no shutdown` qui l'active, et `ip address` qui lui donne son adresse (une interface de routeur est désactivée par défaut). [[Erreurs du cours#^e-1-computer-networks|✎]]

À quoi sert cette suite de commandes : un routeur n'achemine des paquets que par des interfaces **activées et munies d'une adresse IP**. Chaque interface reçoit une adresse dans le réseau qu'elle dessert ; ici 192.168.10.254/24 sera la [[Passerelle par défaut|passerelle par défaut]] des PC du réseau 192.168.10.0/24, qui enverront au routeur tout ce qui sort de leur réseau. Dès que l'interface est active, le routeur ajoute ce réseau à sa table de routage comme réseau directement connecté. [[Complément hors du cours|ⓘ]]

On refait la même chose pour l'interface 0/2 :

```
Router(config)# interface gigabitEthernet 0/2
Router(config-if)# ip address 203.0.113.5 255.255.255.252
Router(config-if)# no shutdown
Router(config-if)# exit
```

Le masque 255.255.255.252 est un /30 : 2 bits hôte, donc 2 adresses utilisables, juste ce qu'il faut pour un lien point à point entre deux routeurs (voir [[2 - IP Addressing]]). La plage 203.0.113.0/24 est réservée à la documentation et aux exemples (RFC 5737, 2010), comme 192.0.2.0/24 et 198.51.100.0/24 ; 192.168.0.0/16 fait partie des [[NAT et PAT|adresses privées]] (RFC 1918). [[Complément hors du cours|ⓘ]]

Pour vérifier d'un coup l'adresse et l'état de chaque interface : `show ip interface brief` (colonnes *Status* et *Protocol* à `up`/`up` quand l'interface fonctionne, *administratively down* tant que `no shutdown` n'a pas été tapé). [[Complément hors du cours|ⓘ]]

Route statique de Router1 vers le réseau de destination 192.168.20.0/24 :

```
Router(config)# ip route 192.168.20.0 255.255.255.0 gigabitEthernet 0/2
```
