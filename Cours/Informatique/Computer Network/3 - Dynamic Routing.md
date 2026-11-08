---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp3 : Dynamic Routing.docx|Chp3 - Dynamic Routing]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/Chp3 : Dynamic Routing.docx|Chp3 - Dynamic Routing]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : route par défaut, principe du routage dynamique, types de protocoles (IGP, EGP), protocole RIP et ses commandes Cisco. Cours en anglais.

## Route par défaut (*default route*)

- Si le [[Routeur|routeur]] ne sait pas atteindre une destination précise, il envoie le paquet vers la **route par défaut**.
- Le routeur utilise sa **table de routage** pour décider de la route ; s'il n'y trouve **pas de route spécifique**, il utilise la route par défaut.
- La route par défaut est courante en **bordure de réseau** (*network edges*), sur le lien vers **Internet**.
- En IPv4, elle s'écrit **`0.0.0.0/0`**. C'est une [[Routage statique|route statique]] particulière.
- Pourquoi elle ne sert qu'en dernier recours : quand plusieurs routes correspondent à une destination, le routeur choisit la **[[Plus longue correspondance de préfixe|plus longue correspondance de préfixe]]** (*longest prefix match*), c'est-à-dire la route au masque le plus long, donc la plus précise. Avec un masque /0, la route par défaut correspond à toutes les adresses mais est la moins précise : elle ne gagne que si aucune autre route ne correspond. Exemple : pour 10.0.3.5, une route 10.0.3.0/24 l'emporte sur 10.0.0.0/8, qui l'emporte sur 0.0.0.0/0. [[Complément hors du cours|ⓘ]]
- Dans `show ip route`, une route par défaut apparaît avec la mention *Gateway of last resort* (passerelle de dernier recours) et, si elle est statique, le code `S*`. [[Complément hors du cours|ⓘ]]

Syntaxe :

```
Router(config)# ip route 0.0.0.0 0.0.0.0 <next hop ip>
```

Exemple :

```
Router(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

![[Chp3 - Dynamic Routing - image5.png]]
*Figure : trois routeurs 2911. ENTERPRISE R2 dessert 10.0.3.0/24 (Switch1) et 10.0.4.0/24 (Switch2) et est relié à ENTERPRISE R1 par 10.0.1.0/30 ; R1 dessert 10.0.2.0/24 (Switch0). R1, « Enterprise Edge Router », est relié à Cloud R1 par 203.0.113.0/30 (R1 en .1, Cloud R1 en .2) : c'est la route par défaut.*

## Routage dynamique

- En **[[Routage dynamique|routage dynamique]]**, les routeurs apprennent **automatiquement** les chemins du réseau auprès des autres routeurs.
- Ils partagent leurs informations de routage grâce à des **protocoles de routage** (*routing protocols*).
- Avantages :
  - adaptation automatique aux changements du réseau (panne de lien, nouveau réseau) ;
  - moins de configuration manuelle dans les grands réseaux.
- Contreparties : les échanges entre routeurs consomment de la bande passante, du processeur et de la mémoire, et un routeur mal configuré ou malveillant peut propager de fausses routes ; le routage statique reste plus simple et plus prévisible pour un petit réseau ou une route unique vers Internet. Les deux se combinent souvent : routes dynamiques en interne, route statique par défaut en bordure. [[Complément hors du cours|ⓘ]]
- **[[Distance administrative]]** (*administrative distance*, AD) : quand un routeur apprend la même destination par plusieurs sources (route statique, RIP, OSPF…), il garde celle dont la source a la distance administrative la plus faible, c'est-à-dire la plus digne de confiance ; la métrique ne départage que des routes venues du même protocole. Valeurs par défaut chez Cisco : réseau directement connecté 0, route statique 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120. Dans `show ip route`, une route RIP s'affiche par exemple `R 10.0.3.0/24 [120/1] via 10.0.1.2` : `[120/1]` = distance administrative 120, métrique 1 saut (comme `[1/0]` pour une route statique, voir [[2 - Static Routing]]). [[Complément hors du cours|ⓘ]]

## Types de protocoles de routage

| Type | Description | Exemples |
|---|---|---|
| IGP | utilisé **à l'intérieur** d'un [[Système autonome\|système autonome]] (*autonomous system*, AS) | RIP, [[EIGRP]], [[OSPF]] |
| EGP | utilisé **entre** systèmes autonomes | [[BGP]] |

- **IGP** (*Interior Gateway Protocol*) : optimisé pour la vitesse et la [[Convergence d'un protocole de routage|convergence]] **au sein** d'une organisation ; gère efficacement le routage interne.
- **EGP** (*Exterior Gateway Protocol*) : relie les réseaux d'organisations différentes ; met l'accent sur la politique (*policy*), le passage à l'échelle (*scalability*) et le choix du chemin.

**Analogie du cours** : l'IGP, c'est le routage dans une ville (le meilleur chemin entre les rues) ; l'EGP, le routage entre villes (le meilleur chemin entre les villes).

Un système autonome est un ensemble de réseaux gérés par une même organisation (fournisseur d'accès, grande entreprise, université) avec une politique de routage commune, identifié sur Internet par un numéro d'AS (ASN) attribué par les registres régionaux sous l'autorité de l'[[IANA]]. Internet est l'interconnexion de dizaines de milliers d'AS, reliés entre eux par BGP. « EGP » est aussi le nom d'un ancien protocole des années 1980, que BGP a remplacé : aujourd'hui, BGP est en pratique le seul EGP utilisé. [[Complément hors du cours|ⓘ]]

Les IGP se rangent en deux familles, selon ce que les routeurs échangent : [[Complément hors du cours|ⓘ]]

| Famille | Ce que sait chaque routeur | Calcul | Exemples |
|---|---|---|---|
| **Vecteur de distance** (*distance-vector*) | seulement ce que lui disent ses voisins : pour chaque réseau, une distance et une direction (le voisin) ; « routage par rumeur » | [[Algorithme de Bellman-Ford]] distribué | RIP ; EIGRP (vecteur de distance dit « avancé », conçu par Cisco) |
| **État de liens** (*link-state*) | la carte complète de la zone : chaque routeur diffuse l'état de ses liens à tous | chacun calcule l'arbre des plus courts chemins par l'[[Algorithme de Dijkstra\|algorithme de Dijkstra]] | OSPF, IS-IS |

Les protocoles à état de liens convergent plus vite et sans boucle, au prix de plus de mémoire et de calcul ; ils passent mieux à l'échelle que RIP. [[Complément hors du cours|ⓘ]]

## RIP (*Routing Information Protocol*)

- RIP est un protocole de routage **à vecteur de distance** (*distance-vector*).
- Il partage les informations de routage **à l'intérieur** d'un système autonome.
- Sa **métrique** est le **nombre de sauts** (*hop count*).
- Le nombre de sauts est le nombre de routeurs à traverser pour atteindre le réseau : un réseau directement connecté est à 0 saut, le réseau d'un voisin à 1. Cette métrique ignore le débit des liens : RIP préfère deux sauts sur des liens lents à trois sauts sur des liens rapides. [[Complément hors du cours|ⓘ]]
- **Mécanisme du vecteur de distance** : toutes les 30 secondes, chaque routeur envoie sa table de routage à ses voisins directs. Un routeur qui reçoit d'un voisin $V$ une route vers le réseau $N$ à la distance $d_V(N)$ en déduit la distance $d_V(N) + 1$ par ce voisin, et garde, pour chaque réseau, le voisin qui donne la plus petite : $d(N) = \min_V \big(d_V(N) + 1\big)$. C'est l'[[Algorithme de Bellman-Ford]] exécuté de façon distribuée. Exemple sur la figure ci-dessus : R2 annonce 10.0.3.0/24 à 0 saut (connecté) ; R1 l'inscrit à 1 saut via R2. [[Complément hors du cours|ⓘ]]
- RIP circule sur [[Numéro de port|UDP, port 520]] ; RIPv1 envoie ses mises à jour en diffusion (*broadcast*, 255.255.255.255), RIPv2 en multicast. Pour IPv6, il existe une version distincte, **RIPng**. [[Complément hors du cours|ⓘ]]

**Caractéristiques clés** :
- **mises à jour de routage** envoyées **toutes les 30 secondes** ;
- **nombre maximal de sauts : 15** (16 = inatteignable, *unreachable*) ;
- **versions** :
  - **RIPv1** : [[Routage classful et classless|classful]], sans information de sous-réseau (mises à jour sans masque) ;
  - **RIPv2** : *classless*, gère le [[VLSM]] (les mises à jour incluent les masques) ;
- facile à configurer, adapté aux petits réseaux.

| Avantages | Limites |
|---|---|
| Simple à configurer | Convergence lente (*slow convergence*) |
| Pris en charge par la plupart des routeurs | 15 sauts au maximum |
| Petites tables de routage | Sensible aux [[Boucle de routage\|boucles de routage]] (*routing loops*) |

**Pourquoi 16 = inatteignable** : quand un réseau tombe, deux routeurs peuvent se le réannoncer l'un à l'autre en augmentant la distance d'un saut à chaque échange, sans fin : c'est le **comptage à l'infini** (*count to infinity*), une forme de [[Boucle de routage|boucle de routage]]. Fixer l'infini à 16 borne ce comptage, mais limite aussi la taille du réseau. RIP le complète par le *split horizon* (ne pas réannoncer une route au voisin dont on l'a apprise), le *route poisoning* (annoncer une route tombée à 16 sauts), le *poison reverse* (renvoyer à 16 sauts une route au voisin dont on l'a apprise) et des minuteries de retenue (*hold-down*). La lenteur de convergence tient au même principe : chaque routeur ne connaît le réseau que par ses voisins, et l'information se propage de proche en proche, au rythme des mises à jour et des minuteries. [[Complément hors du cours|ⓘ]]

### Exemple de configuration

Active RIP sur les interfaces d'un réseau donné (la commande `network` prend obligatoirement l'adresse du réseau à annoncer) : [[Erreurs du cours#^e-3-dynamic-routing|✎]]

```
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# no auto-summary
Router(config-router)# network <network address>
Router(config-router)# default-information originate
```

### Commandes de configuration RIP

| Commande | Rôle |
|---|---|
| `router rip` | entre dans le **mode de configuration du protocole RIP** |
| `version 2` | active **RIPv2** : routage *classless*, VLSM, authentification, mises à jour [[Multicast\|multicast]] (envoyées à 224.0.0.9) |
| `no auto-summary` | désactive le **[[Résumé automatique de routes\|résumé automatique]]** des routes à la frontière de classe ; RIP annonce alors les routes au niveau du sous-réseau. Indispensable avec des réseaux non contigus ou du VLSM |
| `network <network address>` | active les mises à jour RIP sur les interfaces dont l'adresse appartient au réseau indiqué, et **annonce ce réseau** aux autres routeurs |
| `default-information originate` | fait **annoncer une route par défaut (0.0.0.0/0)** dans RIP, *si le routeur a une route par défaut dans sa table* ; les routeurs en aval peuvent l'utiliser [[Erreurs du cours#^e-3-dynamic-routing\|✎]] |

Dans la commande `network`, RIPv2 n'accepte qu'une adresse **sans masque**, ramenée à sa classe : `network 10.0.0.0` active RIP sur toutes les interfaces en 10.x.x.x. Sur la figure, R1 et R2 n'ont donc besoin que de `network 10.0.0.0` pour annoncer leurs réseaux internes ; on n'y met pas 203.0.113.0, le lien vers Internet, que remplace `default-information originate`. [[Complément hors du cours|ⓘ]]

La commande `passive-interface <interface>` (en mode `config-router`) arrête l'envoi des mises à jour RIP sur une interface tout en continuant d'annoncer son réseau : on l'applique aux interfaces tournées vers les hôtes ou vers Internet, où aucun routeur RIP n'écoute, pour économiser la bande passante et ne pas exposer la table de routage. [[Complément hors du cours|ⓘ]]

### Commandes de gestion RIP

| Commande | Rôle |
|---|---|
| `show ip protocols` | affiche les réglages du protocole (minuteries RIP, réseaux, voisins, *default-originate*, version, etc.) |
| `show ip rip database` | affiche la base de données RIP et les routes apprises |
| `show ip route rip` | n'affiche que les routes apprises par RIP |
| `show ip route` | affiche la table de routage IPv4 complète |
| `no router rip` | supprime toute la configuration RIP du routeur |

## Fin de note : VLAN

La note se termine par deux phrases sur les [[VLAN]] : « un VLAN est toujours relié au commutateur » et « découper le [[Domaine de diffusion|domaine de diffusion]] d'un commutateur en plusieurs domaines s'appelle un VLAN ». Voir [[4 - VLAN ／ IVR Commands|Chp4 - VLAN]].