---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : manque d'adresses IPv4, adresses privées, principe du NAT, NAT statique et sa configuration, PAT (*NAT overload*) et sa configuration. Cours mêlant français et anglais. Voir [[NAT et PAT]].

## Pourquoi le NAT

- IPv4 ne fournit qu'environ **4,3 milliards** d'adresses ($2^{32} = 4\,294\,967\,296$), pas assez pour toute la population. [[Erreurs du cours#^e-5-nat-pat|✎]]
- Solution **à long terme** : passer à [[IPv6]].
- Solutions **à court terme** : [[Adressage IPv4 et CIDR|CIDR]], adresses IPv4 **privées**, **NAT**.
- Ordre de grandeur : une adresse IPv4 tient sur 32 bits, soit $2^{32} \approx 4{,}3$ milliards de valeurs, dont une partie est réservée (adresses privées, multicast, bouclage…). L'[[IANA]] a distribué ses derniers blocs d'adresses aux registres régionaux en février 2011 ; depuis, les nouvelles adresses IPv4 sont rares et se revendent. IPv6, sur 128 bits ($2^{128} \approx 3{,}4 \times 10^{38}$ adresses), n'a plus besoin du NAT pour économiser les adresses. [[Complément hors du cours|ⓘ]]

### Adresses privées (RFC 1918)

| Plage | De | À |
|---|---|---|
| 10.0.0.0/8 | 10.0.0.0 | 10.255.255.255 |
| 172.16.0.0/12 | 172.16.0.0 | 172.31.255.255 |
| 192.168.0.0/16 | 192.168.0.0 | 192.168.255.255 |

- On est libre d'utiliser des adresses privées dans ses réseaux.
- Elles n'ont **pas** à être **uniques globalement**.
- Mais elles **ne peuvent pas être utilisées sur Internet**.
- Ces plages sont fixées par la RFC 1918 de l'[[IETF]] (1996). Les opérateurs ne les routent pas sur Internet : c'est pourquoi la même adresse 192.168.0.167 peut exister dans des millions de réseaux domestiques sans conflit. [[Complément hors du cours|ⓘ]]
- D'autres plages sont réservées, à ne pas confondre avec les adresses privées : 127.0.0.0/8 pour l'[[Adresse de bouclage|adresse de bouclage]], 169.254.0.0/16 pour l'auto-configuration locale (adresse qu'un hôte se donne quand aucun serveur DHCP ne répond), et 100.64.0.0/10, réservée au NAT des opérateurs (*carrier-grade NAT*, CGN), qui traduisent une seconde fois les adresses de leurs clients faute d'adresses publiques. [[Complément hors du cours|ⓘ]]

Deux problèmes : on ne peut pas dupliquer des adresses sur Internet, et les adresses privées n'y circulent pas. **Solution : le NAT.** Le [[Routeur|routeur]] traduit l'adresse privée (réseau 192.168.0.0) en adresse publique (réseau 150.50.0.0), et inversement.

![[Chp5 - NAT ／ PAT - image7.png]]
*Figure : deux réseaux locaux identiques en 192.168.0.0/24 (PC en .167, routeur en .1), reliés à Internet (nuage) par 150.50.0.0/30 à gauche et 203.250.0.0/30 à droite : la même adresse privée existe des deux côtés.*

## Fonctionnement du NAT

- Le NAT modifie l'adresse IP **source et/ou destination** des paquets.
- Il permet aux hôtes à adresse privée de communiquer avec d'autres hôtes sur Internet.
- Selon le cours, le NAT agit comme un [[Pare-feu|pare-feu]] en cachant les adresses internes aux réseaux externes, et empêche la communication directe entre les appareils internes et l'extérieur, ce qui réduit le risque d'accès non autorisé et d'attaques.

![[Chp5 - NAT ／ PAT - image4.png]]
*Figure : PC1 (192.168.0.167) envoie un paquet à 8.8.8.8 ; R1 remplace la source par 203.0.113.1 à l'aller, puis la destination 203.0.113.1 par 192.168.0.167 au retour.*

| Sens | Avant R1 | Après R1 |
|---|---|---|
| Aller | Src 192.168.0.167, Dst 8.8.8.8 | Src 203.0.113.1, Dst 8.8.8.8 |
| Retour | Src 8.8.8.8, Dst 203.0.113.1 | Src 8.8.8.8, Dst 192.168.0.167 |

Pour retrouver le bon hôte au retour, le routeur tient une **table de traduction** (*NAT table*) : chaque correspondance adresse interne ↔ adresse externe y est inscrite à l'aller et consultée au retour. Le NAT n'intervient que sur le routeur qui sépare les deux zones ; ni PC1 ni le serveur 8.8.8.8 ne savent que l'adresse a été changée. [[Complément hors du cours|ⓘ]]

Le NAT a des inconvénients : il rompt le principe du « bout en bout » d'Internet (un hôte externe ne peut pas ouvrir de lui-même une connexion vers un hôte interne, sauf correspondance configurée), il gêne les protocoles qui écrivent des adresses IP dans leurs données (FTP actif, voix sur IP, IPsec sans adaptation) et il ajoute un traitement à chaque paquet. [[Complément hors du cours|ⓘ]]

Sur l'effet « pare-feu » : il vient de ce qu'un paquet entrant sans correspondance dans la table de traduction n'a pas de destinataire interne et est abandonné. C'est une conséquence de la traduction, pas un filtrage choisi : le NAT ne contrôle ni les ports ni le contenu, et ne remplace pas un vrai pare-feu ou des [[Liste de contrôle d'accès|ACL]]. [[Complément hors du cours|ⓘ]]

## NAT statique (*Static NAT*)

- Le NAT statique configure **à la main** des correspondances **une pour une** (*one-to-one*) entre adresses privées et adresses publiques.
- Une adresse *inside local* est associée à une adresse *inside global*.

| Terme | Définition |
|---|---|
| *Inside local* | adresse de l'hôte **interne**, vue du réseau local : celle réellement configurée sur l'hôte, en général privée (flèche bleue) |
| *Inside global* | adresse de l'hôte **interne**, vue des hôtes **externes** : son adresse **après NAT**, en général publique (flèche rouge) |
| *Outside local* | adresse de l'hôte **externe**, vue du réseau local |
| *Outside global* | adresse de l'hôte **externe**, vue du réseau externe |

Pour lire ces termes : *inside*/*outside* dit **de quel hôte** on parle (interne ou externe), *local*/*global* dit **de quel côté du routeur** on regarde son adresse. Dans l'exemple ci-dessous : inside local = 192.168.0.167, inside global = 100.0.0.1, et outside local = outside global = 8.8.8.8, car l'adresse du serveur externe n'est pas traduite (c'est le cas habituel). [[Complément hors du cours|ⓘ]]

![[Chp5 - NAT ／ PAT - image5.png]]
*Figure : zone Inside (PC1 en .167, PC2 en .168, réseau 192.168.0.0/24, R1 en .1) et zone Outside (203.0.113.0/30, nuage, serveur 8.8.8.8). L'inside local 192.168.0.167 (bleu) devient l'inside global 100.0.0.1 (rouge) ; au retour, la destination 100.0.0.1 redevient 192.168.0.167.*

Le NAT statique permet aux appareils à adresse privée de communiquer sur Internet, mais comme il impose une correspondance une pour une, il **n'économise pas** d'adresses IP.

Son usage typique : rendre joignable depuis Internet un **serveur interne** (site web, messagerie), qui doit toujours avoir la même adresse publique. Comme la correspondance est permanente, un hôte externe peut ouvrir une connexion vers 100.0.0.1, ce que le NAT dynamique et le PAT ne permettent pas sans configuration supplémentaire. [[Complément hors du cours|ⓘ]]

Entre les deux, le **NAT dynamique** associe les adresses internes à un **groupe** (*pool*) d'adresses publiques, attribuées à la demande, au premier venu, et libérées après inactivité : la correspondance reste une pour une à un instant donné, et si le groupe est épuisé, l'hôte suivant attend. Configuration, après `ip nat inside` et `ip nat outside` : `ip nat pool PUBLIC 100.0.0.1 100.0.0.10 netmask 255.255.255.0`, une ACL qui désigne les adresses internes, puis `ip nat inside source list 1 pool PUBLIC`. [[Complément hors du cours|ⓘ]]

## Configuration du NAT statique

1. Définir la ou les interfaces **internes** (reliées au réseau interne) :
```
R1(config)#interface gigabitEthernet 0/1
R1(config-if)#ip nat inside
```
2. Définir la ou les interfaces **externes** (reliées au réseau externe) ; `ip nat outside` est une commande d'interface, d'où le prompt `(config-if)` : [[Erreurs du cours#^e-5-nat-pat|✎]]
```
R1(config)#interface gigabitEthernet 0/0
R1(config-if)#ip nat outside
```
3. Configurer les correspondances une pour une :
```
R1(config)#ip nat inside source static 192.168.0.167 100.0.0.1
R1(config)#ip nat inside source static 192.168.0.168 100.0.0.2
```
4. Gérer le NAT :

| Commande | Rôle |
|---|---|
| `show ip nat translations` | affiche la table des traductions |
| `show ip nat statistics` | affiche les statistiques du NAT |
| `clear ip nat translation *` | efface toutes les traductions dynamiques |

(Les rôles des commandes de gestion sont déduits de leur nom ; le cours ne les décrit pas.)

## PAT (*Port Address Translation*)

- Le PAT est aussi appelé **NAT overload**.
- Il traduit **à la fois l'adresse IP et le [[Numéro de port|numéro de port]]**.
- Avec un numéro de port unique par flux de communication, **une seule adresse publique** sert à de nombreux hôtes internes (il y a plus de 65 000 numéros de port).
- Le routeur garde la trace de quelle adresse *inside local* utilise quelle adresse *inside global* et quel port.
- Comme de nombreux hôtes internes partagent une seule adresse publique, le PAT **économise les adresses publiques** ; il est utilisé dans les réseaux du monde entier.
- Le numéro de port tient sur 16 bits : $2^{16} = 65\,536$ valeurs (0 à 65 535), d'où les « plus de 65 000 ». Le routeur garde le port source choisi par l'hôte quand il est libre, comme dans l'exemple ci-dessous ; si deux hôtes internes ont pris le même port source, il en attribue un autre au second pour que chaque flux reste identifiable. Le PAT traduit les flux TCP et UDP (ports) ; pour ICMP, qui n'a pas de port, il se sert de l'identifiant de la requête (*ping*). [[Complément hors du cours|ⓘ]]
- C'est le mécanisme d'une box Internet domestique : tous les appareils du foyer, en 192.168.x.x, sortent sur Internet avec l'unique adresse publique attribuée par le fournisseur d'accès. Pour rendre un service interne joignable de l'extérieur, on y configure une **redirection de port** (*port forwarding*), c'est-à-dire un NAT statique limité à un port. [[Complément hors du cours|ⓘ]]

![[Chp5 - NAT ／ PAT - image2.png]]
*Figure : PC1 (.167) et PC2 (.168) derrière R1 (G0/1 en .1, G0/0 en 203.0.113.1) ; les deux flux vers le DNS 8.8.8.8:53 partent avec la même adresse publique 203.0.113.1, distingués par leur port.*

| Flux | Aller, avant NAT | Aller, après NAT | Retour, côté externe | Retour, après NAT |
|---|---|---|---|---|
| PC1 | 192.168.0.167:65205 → 8.8.8.8:53 | 203.0.113.1:65205 → 8.8.8.8:53 | 8.8.8.8:53 → 203.0.113.1:65205 | 8.8.8.8:53 → 192.168.0.167:65205 |
| PC2 | 192.168.0.168:59641 → 8.8.8.8:53 | 203.0.113.1:59641 → 8.8.8.8:53 | 8.8.8.8:53 → 203.0.113.1:59641 | 8.8.8.8:53 → 192.168.0.168:59641 |

## Configuration du PAT

1. Interfaces internes :
```
R1(config)#interface gigabitEthernet 0/1
R1(config-if)#ip nat inside
```
2. Interfaces externes : [[Erreurs du cours#^e-5-nat-pat|✎]]
```
R1(config)#interface gigabitEthernet 0/0
R1(config-if)#ip nat outside
```
3. Définir le trafic à traduire, par une [[Liste de contrôle d'accès|liste d'accès]] (192.168.0.0 avec le masque générique *wildcard* 0.0.0.255, soit tout 192.168.0.0/24) :
```
R1(config)#access-list 1 permit 192.168.0.0 0.0.0.255
```
4. Configurer le PAT en associant l'ACL à l'interface externe et en activant la surcharge (mot-clé `overload`) : [[Erreurs du cours#^e-5-nat-pat|✎]]
```
R1(config)# ip nat inside source list 1 interface g0/0 overload
```

Le masque générique se calcule en retranchant chaque octet du masque de sous-réseau à 255 : $255.255.255.255 - 255.255.255.0 = 0.0.0.255$ ; un bit à 0 doit correspondre, un bit à 1 est indifférent (voir [[Liste de contrôle d'accès]]). Avec `interface g0/0`, le routeur utilise l'adresse de son interface externe comme adresse publique, ce qui convient même si le fournisseur d'accès la change ; on peut aussi faire du PAT sur un groupe d'adresses : `ip nat inside source list 1 pool PUBLIC overload`. [[Complément hors du cours|ⓘ]]