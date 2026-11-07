---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]], dans [[Computer Network (matière)]] : routage IP, réseaux connectés et distants, configuration de routes statiques sous Cisco IOS (par interface de sortie ou par adresse du saut suivant), suppression d'une route. En cas d'écart, le cours et ses images font foi.

## Idée générale

Un routeur utilise sa table de routage pour décider du chemin d'un paquet. Il apprend seul les réseaux directement connectés, mais pas les réseaux distants : il faut des routes explicites, statiques ou dynamiques. Voir [[Routage statique]].

## Qu'est-ce que le routage IP

- Le **[[Routage IP]]** (*IP routing*) est le processus qui achemine des paquets IP d'un réseau source vers un réseau de destination, à travers des [[Routeur|routeurs]] interconnectés.
- Les routeurs utilisent leur **table de routage** (*routing table*) pour décider de la route d'un paquet.
- Les routes peuvent être **statiques** (*static*, configurées à la main) ou **dynamiques** (*dynamic*, apprises automatiquement par des protocoles de routage, voir [[Routage dynamique]]).

## Comment un routeur apprend ses routes : connectées et statiques

- Les routeurs apprennent **automatiquement** les **réseaux directement connectés** (*directly connected networks*) et les ajoutent à la table de routage.
- Ils ne peuvent **pas** apprendre automatiquement les **réseaux de destination distants** (*remote destination networks*) : il faut des **entrées de route explicites**.
- Ces entrées viennent du routage **statique** ou **dynamique**.
- Une **route statique** est configurée **à la main par un administrateur** sur le routeur.

## Réseaux directement connectés

Topologie d'exemple sous Packet Tracer (voir [[Formation CISCO Packet Tracer (résumé)]]) :

![[Chp2 - Static Routing - image2.png]]
*Figure : R1 (2911) relie 192.168.1.0/24 par G0/1 (Switch0, PC1, PC2) et 192.168.2.0/24 par G0/2 (Switch1, PC3, PC4) ; il est relié à R2 par G0/0 sur le lien 203.0.113.0/30. R2 (2911) relie 10.0.1.0/24 par G0/1 (Switch2, Server1) et 10.0.2.0/24 par G0/2 (Switch3, Server2). Avec le tableau des réseaux connectés.*

| Appareil | Réseau directement connecté (C) | Via l'interface |
|---|---|---|
| R1 | 192.168.1.0/24 | R1 : [[Interface réseau\|GigabitEthernet]] 0/1 |
| R1 | 192.168.2.0/24 | R1 : GigabitEthernet 0/2 |
| R1 | 203.0.113.0/30 | R1 : GigabitEthernet 0/0 |
| R2 | 10.0.1.0/24 | R2 : GigabitEthernet 0/1 |
| R2 | 10.0.2.0/24 | R2 : GigabitEthernet 0/2 |
| R3 (lire R2, voir Points à vérifier, 1) | 203.0.113.0/30 | R2 : GigabitEthernet 0/0 |

## Réseaux distants

![[Chp2 - Static Routing - image4.png]]
*Figure : même topologie, avec le tableau des réseaux distants que chaque routeur doit apprendre.*

| Appareil | Réseau de destination distant | Via l'interface | Via l'adresse du saut suivant (*next hop*) |
|---|---|---|---|
| R1 | 10.0.1.0/24 | R1 : G0/0 | 203.0.113.2/30 |
| R1 | 10.0.2.0/24 | R1 : G0/0 | 203.0.113.2/30 |
| R2 | 192.168.1.0/24 | R2 : G0/0 | 203.0.113.1/30 |
| R2 | 192.168.2.0/24 | R2 : G0/0 | 203.0.113.1/30 |

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

### Route statique avec interface de sortie (*exit interface*), sur R1

Syntaxe (voir [[CLI Cisco IOS]]) :

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

La route par saut suivant s'affiche « `S <réseau> [1/0] via <adresse>` » ; `[1/0]` est la distance administrative et la métrique (complément : la note ne l'explique pas).

### Supprimer une route statique

Mettre le mot-clé `no` au début de la commande :

```
Router(config)# no ip route 192.168.1.0 255.255.255.0 203.0.113.1
```

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. L'image 2 (tableau des réseaux connectés) a été ouverte ; les autres sont lues par leur transcription.

1. **Dernière ligne du tableau des réseaux connectés** : image ouverte, « R3 » est écrit pour la ligne 203.0.113.0/30, alors que l'interface citée est « R2: GigabitEthernet 0/0 » et que le schéma n'a que deux routeurs. C'est une erreur du cours, il faut lire R2.
2. **Interface de sortie et adresse du saut suivant** (complément) : sur un lien Ethernet entre deux routeurs, la route avec le saut suivant est la forme usuelle, car la route avec l'interface de sortie oblige le routeur à résoudre l'adresse de chaque destination sur ce lien. Packet Tracer accepte les deux.
3. **Image 1** : la sortie `show ip route` de R1 avant configuration n'a que des routes `C` et `L`, aucune `S`, ce qui est cohérent avec le texte.
4. **Exemple de suppression** : la commande `no ip route 192.168.1.0 255.255.255.0 203.0.113.1` correspond à une route configurée sur R2 par saut suivant, alors que la note ne montre que la configuration par saut suivant de R1. La commande `no` doit reprendre exactement la route à supprimer.
5. **Coquille** : la note écrit `Routere(config)#` dans la syntaxe générale ; il faut lire `Router(config)#`.
