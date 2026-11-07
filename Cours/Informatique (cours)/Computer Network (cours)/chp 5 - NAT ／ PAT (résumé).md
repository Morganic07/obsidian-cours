---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/Chp5 : NAT ／ PAT.docx|Chp5 - NAT ／ PAT]], dans [[Computer Network (index)]] : manque d'adresses IPv4, adresses privées, principe du NAT, NAT statique et sa configuration, PAT (*NAT overload*) et sa configuration. Cours mêlant français et anglais. En cas d'écart, le cours et ses images font foi. Voir [[NAT et PAT]].

## Pourquoi le NAT

- IPv4 ne fournit qu'environ **4,2 milliards** d'adresses, pas assez pour toute la population.
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
- Selon le cours, le NAT agit comme un [[Pare-feu|pare-feu]] en cachant les adresses internes aux réseaux externes, et empêche la communication directe entre les appareils internes et l'extérieur, ce qui réduit le risque d'accès non autorisé et d'attaques (voir Points à vérifier, 4).

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
(prompt tel qu'il figure dans le cours, voir Points à vérifier, 2).
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
(le cours écrit `overlead`, voir Points à vérifier, 1).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images 3 et 4 ont été ouvertes ; les autres sont lues par leur transcription.

1. **`overlead`** : image 3 ouverte. Le cours écrit bien `overlead` dans la commande et dans le texte. La commande Cisco est `overload` (complément). **À corriger avant un examen.**
2. **`R1(config)#ip nat outside`** (complément) : l'image montre ce prompt (images 1 et 3) après `interface gigabitEthernet 0/0`. `ip nat outside` est une commande d'interface, il faut le prompt `R1(config-if)#`.
3. **`196.168.0.167`** : image 4 ouverte. La note du bas écrit bien « 196.168.0.167 », alors que le PC est en 192.168.0.167. Faute du cours.
4. **« NAT acts as a firewall »** (complément). Le cours affirme que NAT joue un rôle de pare-feu en cachant les adresses internes et réduit les risques d'attaque. C'est un effet de bord, pas un mécanisme de sécurité : NAT ne remplace pas un pare-feu ou des ACL.
5. **Adresses du static NAT** : l'exemple traduit vers `100.0.0.1`, alors que l'interface externe de R1 est en 203.0.113.1 et que le PAT, juste après, traduit vers 203.0.113.1. `100.0.0.0/8` n'est pas une plage privée du RFC 1918, c'est un choix d'exemple.
6. **Phrase de transition** : « le routeur va traduire la private IP 192.168.0.0 en une public IP 150.50.0.0 » mêle adresses de réseau et adresses d'hôtes, formulation simplifiée.
7. **Fausses alertes** : le « 7 » en coin de l'image 4 est un numéro de page, sans contenu. Le PAT garde le port d'origine dans l'exemple ; en pratique, le routeur peut aussi le changer (complément).
8. **4,2 ou 4,3 milliards** : ce chapitre écrit 4,2 milliards d'adresses IPv4, [[IP Addressing (résumé)|02 IP Addressing]] écrit 4,3 milliards ($2^{32} \approx 4{,}29$ milliards).
