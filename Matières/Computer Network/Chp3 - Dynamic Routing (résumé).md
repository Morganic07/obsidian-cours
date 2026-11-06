---
type: source
tags: [year3]
sources: ["[[Chp3 - Dynamic Routing]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp3 - Dynamic Routing]], dans [[Computer Network (matière)]] : route par défaut, principe du routage dynamique, types de protocoles (IGP, EGP), protocole RIP et ses commandes Cisco. Cours en anglais. En cas d'écart, le cours et ses images font foi.

## Route par défaut (*default route*)

- Si le [[Routeur|routeur]] ne sait pas atteindre une destination précise, il envoie le paquet vers la **route par défaut**.
- Le routeur utilise sa **table de routage** pour décider de la route ; s'il n'y trouve **pas de route spécifique**, il utilise la route par défaut.
- La route par défaut est courante en **bordure de réseau** (*network edges*), sur le lien vers **Internet**.
- En IPv4, elle s'écrit **`0.0.0.0/0`**. C'est une [[Routage statique|route statique]] particulière.

Syntaxe :

```
Router(config)# ip route 0.0.0.0 0.0.0.0 <next hop ip>
```

Exemple :

```
Router(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

![[Cours/Year 3/Computer Network/medias/Chp3 - Dynamic Routing/image5.png]]
*Figure : trois routeurs 2911. ENTERPRISE R2 dessert 10.0.3.0/24 (Switch1) et 10.0.4.0/24 (Switch2) et est relié à ENTERPRISE R1 par 10.0.1.0/30 ; R1 dessert 10.0.2.0/24 (Switch0). R1, « Enterprise Edge Router », est relié à Cloud R1 par 203.0.113.0/30 (R1 en .1, Cloud R1 en .2) : c'est la route par défaut.*

## Routage dynamique

- En **[[Routage dynamique|routage dynamique]]**, les routeurs apprennent **automatiquement** les chemins du réseau auprès des autres routeurs.
- Ils partagent leurs informations de routage grâce à des **protocoles de routage** (*routing protocols*).
- Avantages :
  - adaptation automatique aux changements du réseau (panne de lien, nouveau réseau) ;
  - moins de configuration manuelle dans les grands réseaux.

## Types de protocoles de routage

| Type | Description | Exemples |
|---|---|---|
| IGP | utilisé **à l'intérieur** d'un [[Système autonome\|système autonome]] (*autonomous system*, AS) | RIP, [[EIGRP]], [[OSPF]] |
| EGP | utilisé **entre** systèmes autonomes | [[BGP]] |

- **IGP** (*Interior Gateway Protocol*) : optimisé pour la vitesse et la [[Convergence d'un protocole de routage|convergence]] **au sein** d'une organisation ; gère efficacement le routage interne.
- **EGP** (*Exterior Gateway Protocol*) : relie les réseaux d'organisations différentes ; met l'accent sur la politique (*policy*), le passage à l'échelle (*scalability*) et le choix du chemin.

**Analogie du cours** : l'IGP, c'est le routage dans une ville (le meilleur chemin entre les rues) ; l'EGP, le routage entre villes (le meilleur chemin entre les villes).

## RIP (*Routing Information Protocol*)

- RIP est un protocole de routage **à vecteur de distance** (*distance-vector*).
- Il partage les informations de routage **à l'intérieur** d'un système autonome.
- Sa **métrique** est le **nombre de sauts** (*hop count*).

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

### Exemple de configuration

Active RIP sur les interfaces d'un réseau donné :

```
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# no auto-summary
Router(config-router)# network <network address>
Router(config-router)# default-information originate
```

(la note écrit `network` sans adresse : voir Points à vérifier, 1).

### Commandes de configuration RIP

| Commande | Rôle |
|---|---|
| `router rip` | entre dans le **mode de configuration du protocole RIP** |
| `version 2` | active **RIPv2** : routage *classless*, VLSM, authentification, mises à jour [[Multicast\|multicast]] (envoyées à 224.0.0.9) |
| `no auto-summary` | désactive le **[[Résumé automatique de routes\|résumé automatique]]** des routes à la frontière de classe ; RIP annonce alors les routes au niveau du sous-réseau. Indispensable avec des réseaux non contigus ou du VLSM |
| `network <network address>` | active les mises à jour RIP sur les interfaces dont l'adresse appartient au réseau indiqué, et **annonce ce réseau** aux autres routeurs |
| `default-information originate` | fait **annoncer une route par défaut (0.0.0.0/0)** dans RIP, *si le routeur a une route par défaut dans sa table* ; les routeurs en aval peuvent l'utiliser |

### Commandes de gestion RIP

| Commande | Rôle |
|---|---|
| `show ip protocols` | affiche les réglages du protocole (minuteries RIP, réseaux, voisins, *default-originate*, version, etc.) |
| `show ip rip database` | affiche la base de données RIP et les routes apprises |
| `show ip route rip` | n'affiche que les routes apprises par RIP |
| `show ip route` | affiche la table de routage IPv4 complète |
| `no router rip` | supprime toute la configuration RIP du routeur |

## Fin de note : VLAN

La note se termine par deux phrases sur les [[VLAN]] : « un VLAN est toujours relié au commutateur » et « découper le [[Domaine de diffusion|domaine de diffusion]] d'un commutateur en plusieurs domaines s'appelle un VLAN ». Voir [[Chp4 - VLAN ／ IVR Commands (résumé)|Chp4 - VLAN]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription, aucune ouverte.

1. **`network` sans argument** : dans l'exemple de configuration, la ligne `network` n'a pas d'adresse. Elle est incomplète, il faut un réseau (le tableau de commandes écrit `network <network address>`).
2. **`default information-originate`** : le tableau de l'image l'écrit sans trait d'union ; l'exemple de configuration écrit `default-information originate`, qui est la forme correcte (complément).
3. **Titre du chapitre** : le chapitre s'appelle « Dynamic Routing » mais n'aborde que RIP. OSPF et EIGRP sont seulement nommés.
4. **Dernières lignes** : « Vlan is always connected to the switch » et « Dividing the broadcast domain ... called V-LAN » terminent la note, sans lien avec le routage. Elles relèvent du chapitre sur les VLAN, voir [[Chp4 - VLAN ／ IVR Commands (résumé)|Chp4 - VLAN]].
5. **Schéma de la route par défaut** : l'adresse « 113.1 » est lue sur l'image, probablement 203.0.113.1.
6. **Coquille** : « *automatically adopts to network changes* » : lire *adapts*.
