---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : manque d'adresses IPv4, adresses privées, principe du NAT, NAT statique et sa configuration, PAT (*NAT overload*) et sa configuration. Cours mêlant français et anglais. En cas d'écart, le cours et ses images font foi. Voir [[NAT et PAT]].

## Pourquoi le NAT

- IPv4 ne fournit qu'environ **4,2 milliards** d'adresses selon le cours (en fait environ 4,3 milliards, voir « Erreurs du cours »), pas assez pour toute la population.
- Solution **à long terme** : passer à [[IPv6]].
- Solutions **à court terme** : [[Adressage IPv4 et CIDR|CIDR]], adresses IPv4 **privées**, **NAT**.

### Adresses privées (RFC 1918)

| Plage | De | À |
|---|---|---|
| 10.0.0.0/8 | 10.0.0.0 | 10.255.255.255 |
| 172.16.0.0/12 | 172.16.0.0 | 172.31.255.255 |
| 192.168.0.0/16 | 192.168.0.0 | 192.168.255.255 |

- On est libre d'utiliser des adresses privées dans ses réseaux.
- Elles n'ont **pas** à être **uniques globalement**.
- Mais elles **ne peuvent pas être utilisées sur Internet**.

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

## NAT statique (*Static NAT*)

- Le NAT statique configure **à la main** des correspondances **une pour une** (*one-to-one*) entre adresses privées et adresses publiques.
- Une adresse *inside local* est associée à une adresse *inside global*.

| Terme | Définition |
|---|---|
| *Inside local* | adresse de l'hôte **interne**, vue du réseau local : celle réellement configurée sur l'hôte, en général privée (flèche bleue) |
| *Inside global* | adresse de l'hôte **interne**, vue des hôtes **externes** : son adresse **après NAT**, en général publique (flèche rouge) |
| *Outside local* | adresse de l'hôte **externe**, vue du réseau local |
| *Outside global* | adresse de l'hôte **externe**, vue du réseau externe |

![[Chp5 - NAT ／ PAT - image5.png]]
*Figure : zone Inside (PC1 en .167, PC2 en .168, réseau 192.168.0.0/24, R1 en .1) et zone Outside (203.0.113.0/30, nuage, serveur 8.8.8.8). L'inside local 192.168.0.167 (bleu) devient l'inside global 100.0.0.1 (rouge) ; au retour, la destination 100.0.0.1 redevient 192.168.0.167.*

Le NAT statique permet aux appareils à adresse privée de communiquer sur Internet, mais comme il impose une correspondance une pour une, il **n'économise pas** d'adresses IP.

## Configuration du NAT statique

1. Définir la ou les interfaces **internes** (reliées au réseau interne) :
```
R1(config)#interface gigabitEthernet 0/1
R1(config-if)#ip nat inside
```
2. Définir la ou les interfaces **externes** (reliées au réseau externe) :
```
R1(config)#interface gigabitEthernet 0/0
R1(config)#ip nat outside
```
(prompt tel qu'il figure dans le cours, voir « Erreurs du cours »).
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
2. Interfaces externes :
```
R1(config)#interface gigabitEthernet 0/0
R1(config)#ip nat outside
```
3. Définir le trafic à traduire, par une [[Liste de contrôle d'accès|liste d'accès]] (192.168.0.0 avec le masque générique *wildcard* 0.0.0.255, soit tout 192.168.0.0/24) :
```
R1(config)#access-list 1 permit 192.168.0.0 0.0.0.255
```
4. Configurer le PAT en associant l'ACL à l'interface externe et en activant la surcharge :
```
R1(config)# ip nat inside source list 1 interface g0/0 overload
```
(le cours écrit `overlead`, voir « Erreurs du cours »).

## Erreurs du cours

- [[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]], configuration du PAT (vérifié sur l'image 3) : écrit `overlead`, dans la commande et dans le texte ; il faut `overload` : `ip nat inside source list 1 interface g0/0 overload` (corrigé dans le bloc ci-dessus). **À retenir pour un examen.**
- Même document, interface externe (vérifié sur les images 1 et 3) : écrit `R1(config)#ip nat outside` après `interface gigabitEthernet 0/0` ; il faut le prompt `R1(config-if)#ip nat outside`, car `ip nat outside` est une commande d'interface (complément).
- Même document, note au bas de l'image 4 (vérifié sur l'image) : écrit « 196.168.0.167 » ; il faut « 192.168.0.167 », l'adresse du PC.
- Même document, introduction : écrit « IPv4 provides only 4.2 milliards de IP » ; il faut environ 4,3 milliards ($2^{32} = 4\,294\,967\,296$), valeur que donne [[2 - IP Addressing|02 IP Addressing]].
