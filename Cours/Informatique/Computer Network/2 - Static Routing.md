---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : routage IP, réseaux connectés et distants, configuration de routes statiques sous Cisco IOS (par interface de sortie ou par adresse du saut suivant), suppression d'une route.

## Idée générale

Un routeur utilise sa table de routage pour décider du chemin d'un paquet. Il apprend seul les réseaux directement connectés, mais pas les réseaux distants : il faut des routes explicites, statiques ou dynamiques. Voir [[Routage statique]].

## Qu'est-ce que le routage IP

- Le **[[Routage IP]]** (*IP routing*) est le processus qui achemine des paquets IP d'un réseau source vers un réseau de destination, à travers des [[Routeur|routeurs]] interconnectés.
- Les routeurs utilisent leur **table de routage** (*routing table*) pour décider de la route d'un paquet.
- Ce que fait un routeur à chaque paquet : il lit l'adresse IP de **destination**, cherche dans sa table les routes dont le réseau contient cette adresse et retient la plus précise, celle au **préfixe le plus long** (*longest prefix match*) : pour 10.0.1.5, une route 10.0.1.0/24 l'emporte sur 10.0.0.0/8. Il décrémente le champ TTL de l'en-tête IP (le paquet est détruit à 0) et l'envoie par l'interface de la route choisie. Si aucune route ne convient et qu'il n'y a pas de route par défaut, le paquet est détruit et le routeur renvoie en général à l'émetteur un message [[ICMP]] « destination injoignable ». [[Complément hors du cours|ⓘ]]
- Les routes peuvent être **statiques** (*static*, configurées à la main) ou **dynamiques** (*dynamic*, apprises automatiquement par des protocoles de routage, voir [[Routage dynamique]]).

## Comment un routeur apprend ses routes : connectées et statiques

- Les routeurs apprennent **automatiquement** les **réseaux directement connectés** (*directly connected networks*) et les ajoutent à la table de routage.
- Ils ne peuvent **pas** apprendre automatiquement les **réseaux de destination distants** (*remote destination networks*) : il faut des **entrées de route explicites**.
- Ces entrées viennent du routage **statique** ou **dynamique**.
- Une **route statique** est configurée **à la main par un administrateur** sur le routeur.

Avantages et limites des deux familles de routes : [[Complément hors du cours|ⓘ]]

| | Routage statique | [[Routage dynamique]] |
|---|---|---|
| Configuration | à la main, sur chaque routeur | automatique, par un protocole (RIP, OSPF, EIGRP) |
| Changement de topologie | à reprendre à la main ; une panne n'est pas contournée | les routeurs recalculent les routes seuls |
| Ressources | aucune (ni processeur, ni bande passante) | échanges de messages, calculs |
| Sécurité, prévisibilité | chemin connu, rien n'est annoncé | les annonces peuvent être falsifiées sans authentification |
| Usage typique | petits réseaux, réseau terminal (*stub*) à une seule sortie, route par défaut | réseaux moyens et grands, plusieurs chemins possibles |

## Réseaux directement connectés

Topologie d'exemple sous Packet Tracer (voir [[7 - Cisco]]) :

![[Chp2 - Static Routing - image2.png]]
*Figure : R1 (2911) relie 192.168.1.0/24 par G0/1 (Switch0, PC1, PC2) et 192.168.2.0/24 par G0/2 (Switch1, PC3, PC4) ; il est relié à R2 par G0/0 sur le lien 203.0.113.0/30. R2 (2911) relie 10.0.1.0/24 par G0/1 (Switch2, Server1) et 10.0.2.0/24 par G0/2 (Switch3, Server2). Avec le tableau des réseaux connectés.*

| Appareil | Réseau directement connecté (C) | Via l'interface |
|---|---|---|
| R1 | 192.168.1.0/24 | R1 : [[Interface réseau\|GigabitEthernet]] 0/1 |
| R1 | 192.168.2.0/24 | R1 : GigabitEthernet 0/2 |
| R1 | 203.0.113.0/30 | R1 : GigabitEthernet 0/0 |
| R2 | 10.0.1.0/24 | R2 : GigabitEthernet 0/1 |
| R2 | 10.0.2.0/24 | R2 : GigabitEthernet 0/2 |
| R2 | 203.0.113.0/30 | R2 : GigabitEthernet 0/0 [[Erreurs du cours#^e-2-static-routing\|✎]] |

## Réseaux distants

![[Chp2 - Static Routing - image4.png]]
*Figure : même topologie, avec le tableau des réseaux distants que chaque routeur doit apprendre.*

| Appareil | Réseau de destination distant | Via l'interface | Via l'adresse du saut suivant (*next hop*) |
|---|---|---|---|
| R1 | 10.0.1.0/24 | R1 : G0/0 | 203.0.113.2/30 |
| R1 | 10.0.2.0/24 | R1 : G0/0 | 203.0.113.2/30 |
| R2 | 192.168.1.0/24 | R2 : G0/0 | 203.0.113.1/30 |
| R2 | 192.168.2.0/24 | R2 : G0/0 | 203.0.113.1/30 |

Les routes se configurent **dans les deux sens** : si R1 connaît 10.0.1.0/24 mais que R2 ignore 192.168.1.0/24, le paquet de PC1 arrive à Server1, mais la réponse est détruite par R2 et le `ping` échoue. Le saut suivant est toujours l'adresse du routeur voisin **sur le lien commun** (203.0.113.2 pour R1), pas une adresse lointaine. [[Complément hors du cours|ⓘ]]

## Commandes Cisco

### Afficher la table de routage

```
Router# show ip route
```

Codes principaux : `C` (*connected*, réseau connecté), `L` (*local*, adresse de l'interface elle-même, en /32), `S` (*static*). La légende complète affichée par IOS : `L` local, `C` connected, `S` static, `R` RIP, `M` mobile, `B` BGP, `D` EIGRP, `EX` EIGRP external, `O` OSPF, `IA` OSPF inter area, `N1`/`N2` OSPF NSSA external type 1/2, `E1`/`E2` OSPF external type 1/2, `E` EGP, `i` IS-IS, `*` candidate default, `U` per-user static route, `o` ODR, `P` periodic downloaded static route.

Sortie de R1 avant toute route statique :

![[Chp2 - Static Routing - image1.png]]
*Figure : capture de `show ip route` sur R1, uniquement des routes C et L.*

```
      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, GigabitEthernet0/1
L        192.168.1.254/32 is directly connected, GigabitEthernet0/1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/24 is directly connected, GigabitEthernet0/2
L        192.168.2.254/32 is directly connected, GigabitEthernet0/2
      203.0.113.0/24 is variably subnetted, 2 subnets, 2 masks
C        203.0.113.0/30 is directly connected, GigabitEthernet0/0
L        203.0.113.1/32 is directly connected, GigabitEthernet0/0
```

Lecture de cette sortie : chaque interface active produit deux lignes, `C` pour le réseau qu'elle dessert et `L` pour sa propre adresse en /32 (les paquets destinés au routeur lui-même). Les lignes non indentées regroupent les sous-réseaux sous leur réseau de classe d'origine (192.168.1.0/24, 203.0.113.0/24) ; « *variably subnetted, 2 subnets, 2 masks* » signifie que ce réseau contient ici deux entrées de masques différents (/24 et /32, ou /30 et /32). Aucune route vers 10.0.1.0 ou 10.0.2.0 n'y figure : c'est ce que les routes statiques vont ajouter. [[Complément hors du cours|ⓘ]]

### Route statique avec interface de sortie (*exit interface*), sur R1

Syntaxe (voir [[CLI Cisco IOS]]) : [[Erreurs du cours#^e-2-static-routing|✎]]

```
Router> enable
Router# config terminal
Router(config)# ip route <réseau_destination> <masque_sous_réseau> <interface_de_sortie>
```

Sur R1 :

```
Router(config)# ip route 10.0.1.0 255.255.255.0 gigabitEthernet 0/0
Router(config)# ip route 10.0.2.0 255.255.255.0 gigabitEthernet 0/0
```

### Route statique avec interface de sortie, sur R2

```
Router> enable
Router# config terminal
Router(config)# ip route 192.168.1.0 255.255.255.0 gigabitEthernet 0/0
Router(config)# ip route 192.168.2.0 255.255.255.0 gigabitEthernet 0/0
Router# sh ip route
```

![[Chp2 - Static Routing - image3.png]]
*Figure : configuration et table de routage de R2 ; les deux routes statiques sont encadrées en rouge.*

Extrait de la table obtenue (« *Gateway of last resort is not set* ») :

```
     10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C       10.0.1.0/24 is directly connected, GigabitEthernet0/1
L       10.0.1.254/32 is directly connected, GigabitEthernet0/1
C       10.0.2.0/24 is directly connected, GigabitEthernet0/2
L       10.0.2.254/32 is directly connected, GigabitEthernet0/2
S    192.168.1.0/24 is directly connected, GigabitEthernet0/0
S    192.168.2.0/24 is directly connected, GigabitEthernet0/0
     203.0.113.0/24 is variably subnetted, 2 subnets, 2 masks
C       203.0.113.0/30 is directly connected, GigabitEthernet0/0
L       203.0.113.2/32 is directly connected, GigabitEthernet0/0
```

Une route statique par interface de sortie s'affiche « `S … is directly connected, <interface>` ».

« *Gateway of last resort is not set* » : aucune **route par défaut** n'est configurée, donc un paquet vers un réseau absent de la table est détruit. La route par défaut, `ip route 0.0.0.0 0.0.0.0 <saut suivant>`, correspond à toutes les destinations (préfixe /0, le plus court possible) et ne sert donc qu'en dernier recours ; elle apparaît avec le code `S*`. Ici, R1 n'a qu'une sortie vers les réseaux distants : `ip route 0.0.0.0 0.0.0.0 203.0.113.2` remplacerait ses deux routes. C'est la configuration habituelle d'un routeur d'accès vers Internet (voir [[Passerelle par défaut]]). [[Complément hors du cours|ⓘ]]

### Route statique avec adresse du saut suivant (*next hop IP*), sur R1 et R2

```
Router> enable
Router# config terminal
Router(config)# ip route 10.0.1.0 255.255.255.0 203.0.113.2
Router(config)# ip route 10.0.2.0 255.255.255.0 203.0.113.2
```

(sur R2, symétriquement, vers 192.168.1.0 et 192.168.2.0 via 203.0.113.1, d'après le tableau des réseaux distants).

![[Chp2 - Static Routing - image5.png]]
*Figure : configuration par saut suivant sur R1 et sortie de `sh ip route` ; les deux routes `S` sont encadrées en rouge.*

```
     10.0.0.0/24 is subnetted, 2 subnets
S       10.0.1.0/24 [1/0] via 203.0.113.2
S       10.0.2.0/24 [1/0] via 203.0.113.2
     192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C       192.168.1.0/24 is directly connected, GigabitEthernet0/1
L       192.168.1.254/32 is directly connected, GigabitEthernet0/1
...
C       203.0.113.0/30 is directly connected, GigabitEthernet0/0
L       203.0.113.1/32 is directly connected, GigabitEthernet0/0
```

La route par saut suivant s'affiche « `S <réseau> [1/0] via <adresse>` ».

`[1/0]` se lit `[distance administrative/métrique]`. La [[Distance administrative|distance administrative]] mesure la confiance accordée à la source d'une route : quand deux sources proposent le même réseau, le routeur garde la plus petite. Valeurs par défaut chez Cisco : réseau connecté 0, route statique 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120, iBGP 200 ; 255 signifie « jamais utilisée ». La **métrique** départage ensuite les routes d'un même protocole (nombre de sauts pour RIP, coût pour OSPF) ; elle vaut 0 pour une route statique. [[Complément hors du cours|ⓘ]]

Une **route statique flottante** (*floating static route*) est une route de secours à laquelle on donne une distance administrative plus grande que celle de la route principale, en dernier paramètre : `ip route 10.0.1.0 255.255.255.0 <autre saut suivant> 130`. Elle reste cachée tant que la route principale (ici apprise par OSPF, 110) existe, et entre dans la table si celle-ci disparaît. [[Complément hors du cours|ⓘ]]

**Interface de sortie ou saut suivant ?** Sur un lien point à point comme le /30 entre R1 et R2, les deux reviennent au même. Sur un réseau Ethernet à plusieurs routeurs, une route qui ne donne que l'interface de sortie ne dit pas à quel voisin remettre le paquet : le routeur doit faire une requête ARP pour chaque destination et compter sur le *proxy ARP* du voisin. On préfère alors le saut suivant, ou une **route entièrement spécifiée** qui donne les deux : `ip route 10.0.1.0 255.255.255.0 g0/0 203.0.113.2`. [[Complément hors du cours|ⓘ]]

Pour vérifier : `show ip route static` n'affiche que les routes `S` ; un `ping` de PC1 vers l'adresse de Server1 teste le chemin aller et retour ; `traceroute` (`tracert` sous Windows) liste les routeurs traversés. [[Complément hors du cours|ⓘ]]

### Supprimer une route statique

Mettre le mot-clé `no` au début de la commande :

```
Router(config)# no ip route 192.168.1.0 255.255.255.0 203.0.113.1
```
