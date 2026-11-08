---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du PDF 02 IP Addressing ([[Raw/Year 3/Computer Network/02 IP Addressing.pdf|02 IP Addressing.pdf]]) (57 diapositives, en anglais, « IPv4 Addressing »), dans [[Cours/Informatique/Computer Network/_index|Computer Network]]. Les tableaux et schémas ont été lus sur les diapositives (texte et images) ; les figures utiles sont intégrées ci-dessous. Le concept détaillé est [[Adressage IPv4 et CIDR]].

Plan du cours : comprendre l'adressage IP, terminologie, notation décimale pointée, décimal et binaire, adresse IPv4, classes, adresse réservée de classe A, longueur de préfixe, masques par défaut, adresses réseau et de broadcast, première et dernière adresse utilisable, nombre maximal d'hôtes, révision, quiz, récapitulatif, IANA, exemple, CIDR, notation CIDR, quiz.

## Comprendre l'adressage IP

- Une **adresse IP** (*Internet Protocol*) est un identifiant numérique attribué à chaque machine d'un réseau IP.
- C'est une adresse **logicielle** (*software address*), qui sert à trouver les hôtes sur un réseau local.
- L'adressage IP permet à un hôte d'un réseau de communiquer avec un hôte d'un **autre réseau**.
- « Logicielle » s'oppose à l'adresse **physique**, l'[[Adresse MAC]] (48 bits, notée en hexadécimal, par exemple `00:1A:2B:3C:4D:5E`), gravée dans la carte réseau par le fabricant. L'adresse IP est **logique** : on la choisit, elle change si la machine change de réseau, et elle est hiérarchique (réseau puis hôte), ce qui permet de router. Sur un réseau local, le protocole **ARP** trouve l'adresse MAC qui correspond à une adresse IP pour livrer la trame. [[Complément hors du cours|ⓘ]]

![[IP Addressing - p5.jpg]]
*Figure : deux réseaux, 192.168.1.0/24 (PC1, PC2, commutateur SW1) et 192.168.2.0/24 (PC3, PC4, SW2), reliés par le routeur R1.*

## Terminologie

| Terme | Définition du cours |
|---|---|
| *Bit* | un chiffre, 1 ou 0 ([[Bit]]) |
| *Byte* | huit bits, par exemple 10110010 |
| *Octet* | 8 bits ; *byte* et *octet* sont interchangeables dans ce cours ([[Octet]]) |
| *Network address* | adresse utilisée par le routage pour envoyer des paquets vers un réseau distant |
| *Broadcast address* | indique l'envoi des données à **tous les nœuds** d'un réseau |
| *Host address* | identifiant unique d'un appareil connecté au réseau |

## Notation décimale pointée (*dotted-decimal notation*)

- Une adresse IP contient **32 bits**, groupés par 8 ; chaque groupe est un **octet** (*byte*).
- Il y a **quatre octets**, séparés par un point.

![[IP Addressing - p8.jpg]]
*Figure : 172.16.254.1 = 10101100.00010000.11111110.00000001 ; le bit de poids fort (*most significant bit*) est à gauche, 32 bits = 4 octets numérotés 1 à 4.*

## Décimal et binaire

- Décimal : base 10, chaque position est multipliée par 10 (3294 = 3×1000 + 2×100 + 9×10 + 4×1).
- Binaire : base 2, chaque position est multipliée par 2 (voir [[Numération binaire]]).

![[IP Addressing - p9.jpg]]
*Figure : 3294 en base 10, et 192 = 11000000 en base 2 (128 + 64 = 192).*

### Exercice : décimal vers binaire sur 8 bits

Poids des bits : 128, 64, 32, 16, 8, 4, 2, 1. Correction donnée par le cours :

| Décimal | Binaire |
|---|---|
| 255 | 11111111 |
| 240 | 11110000 |
| 224 | 11100000 |
| 192 | 11000000 |
| 160 | 10100000 |
| 144 | 10010000 |
| 128 | 10000000 |
| 96 | 01100000 |
| 64 | 01000000 |
| 40 | 00101000 |

**Méthode** : pour convertir un octet, on parcourt les poids de 128 à 1 ; on écrit 1 si le poids tient dans ce qui reste (et on le retire), 0 sinon. Exemple : 172 = 128 + 32 + 8 + 4, donc 10101100 ; 172 − 128 = 44, 64 ne tient pas, 44 − 32 = 12, 16 ne tient pas, 12 − 8 = 4, 4 − 4 = 0. Dans l'autre sens, on additionne les poids des bits à 1. Les valeurs du tableau (128, 192, 224, 240…) sont celles des masques : des 1 contigus en partant de la gauche. [[Complément hors du cours|ⓘ]]

## Adresse IPv4

- IP est l'ensemble des règles qui régissent la transmission des données sur Internet.
- On parle d'adresse **IPv4** parce que c'est la **quatrième version** du protocole IP.
- Une adresse IPv4 est un nombre de **32 bits** : environ **4,3 milliards** d'adresses possibles.
- Exactement $2^{32} = 4\,294\,967\,296$ adresses, dont une partie est réservée (bouclage, multicast, plages privées…). Ce stock s'est révélé trop petit : l'IANA a distribué ses derniers blocs /8 aux registres régionaux en février 2011. La réponse de long terme est [[IPv6]], dont les adresses font 128 bits ; IPv5 n'a jamais été déployé (le numéro avait servi à un protocole expérimental). [[Complément hors du cours|ⓘ]]
- IPv4 a **cinq classes**, A, B, C, D et E ; chacune utilise un nombre différent de bits pour l'adresse réseau et l'adresse d'hôte.

**À retenir** :
- une adresse IP donne deux informations : **l'adresse réseau** et **l'adresse d'hôte** ;
- une adresse IP est **incomplète sans son masque de sous-réseau** (*subnet mask*) ;
- le masque indique les bits réseau et les bits hôte : **tous les bits réseau à 1, tous les bits hôte à 0**.

Exemple : IP `192.168.10.4`, masque `255.255.255.0`.

**Calculer l'adresse réseau** : on fait un **ET logique** bit à bit entre l'adresse et le masque (un bit vaut 1 seulement si les deux valent 1) : les bits réseau sont conservés, les bits hôte mis à 0. Ici `192.168.10.4` ET `255.255.255.0` = `192.168.10.0`. L'adresse de broadcast s'obtient en mettant au contraire tous les bits hôte à 1 : `192.168.10.255`. Deux machines sont dans le même réseau si ce calcul donne la même adresse réseau pour les deux ; sinon, l'émetteur passe par sa [[Passerelle par défaut|passerelle par défaut]]. [[Complément hors du cours|ⓘ]]

Un masque est toujours une suite de 1 **contigus** suivie de 0 : chaque octet de masque vaut donc 0, 128, 192, 224, 240, 248, 252, 254 ou 255 ; `255.255.0.255` n'est pas un masque valide. [[Complément hors du cours|ⓘ]]

## Classes d'adresses IPv4

![[IP Addressing - p14.jpg]]
*Figure : répartition des 4 octets. Classe A : 1 octet réseau, 3 octets hôte ; classe B : 2 et 2 ; classe C : 3 et 1 ; classe D : multicast ; classe E : recherche.*

| Classe | Premier octet (binaire) | Plage du premier octet | Plage d'adresses | Préfixe |
|---|---|---|---|---|
| A | 0xxxxxxx | 0 – 127 (en fait 0 – 126) | 0.0.0.0 – 127.255.255.255 | /8 |
| B | 10xxxxxx | 128 – 191 | 128.0.0.0 – 191.255.255.255 | /16 |
| C | 110xxxxx | 192 – 223 | 192.0.0.0 – 223.255.255.255 | /24 |
| D | 1110xxxx | 224 – 239 | 224.0.0.0 – 239.255.255.255 | ([[Multicast]]) |
| E | 1111xxxx | 240 – 255 | 240.0.0.0 – 255.255.255.255 | (recherche) |

Remarque du cours, en rouge : « *Class A range is 0 – 126 and not 127* ».

Tableau de la diapositive 16 :

| Classe | Bits de tête | Taille du champ réseau | Taille du reste | Nombre de réseaux | Adresses par réseau |
|---|---|---|---|---|---|
| A | 0 | 8 | 24 | 128 ($2^7$) | 16 777 216 ($2^{24}$) |
| B | 10 | 16 | 16 | 16 384 ($2^{14}$) | 65 536 ($2^{16}$) |
| C | 110 | 24 | 8 | 2 097 152 ($2^{21}$) | 256 ($2^8$) |

Lecture du tableau : les bits de tête sont fixés par la classe, seuls les bits restants du champ réseau varient. Classe A : $8 - 1 = 7$ bits libres, d'où $2^7$ réseaux ; classe B : $16 - 2 = 14$ ; classe C : $24 - 3 = 21$. En pratique la classe A n'a que 126 réseaux utilisables, car le réseau 0 (`0.0.0.0` désigne « ce réseau » ou « n'importe quelle adresse ») et le réseau 127 (bouclage) sont réservés. [[Complément hors du cours|ⓘ]]

Dans chaque classe A, B et C, une plage est réservée aux **adresses privées** (RFC 1918, 1996), utilisables librement à l'intérieur d'un réseau mais jamais acheminées sur Internet : `10.0.0.0/8`, `172.16.0.0/12` (172.16 à 172.31) et `192.168.0.0/16`. C'est pourquoi les exemples du cours (10.0.0.0, 172.16.0.0, 192.168.1.0) ressemblent aux réseaux domestiques ; la traduction vers une adresse publique est le [[NAT et PAT]]. [[Complément hors du cours|ⓘ]]

Autres adresses particulières : `169.254.0.0/16`, adresse locale au lien (*link-local*, APIPA sous Windows) qu'un hôte s'attribue seul quand il n'obtient pas d'adresse du serveur [[DHCP]] ; `255.255.255.255`, broadcast limité au réseau local. [[Complément hors du cours|ⓘ]]

## Adresse réservée de la classe A : le bouclage

- L'[[Adresse de bouclage]] (*loopback*) sert à tester la pile réseau (*network stack*) de l'appareil local ou de l'interface réseau locale.
- Elle est réservée dans la classe A : plage **127.0.0.0 – 127.255.255.255**. La classe A utile va donc de **0 à 126**.
- Une adresse réservée ne peut pas être attribuée à un hôte ou à un nœud du réseau.
- L'adresse de bouclage est **toujours joignable**, même si l'interface réseau n'est connectée à aucun réseau.

![[IP Addressing - p18.jpg]]
*Figure : capture d'une invite de commandes Windows, `ping 127.0.0.1` : 4 réponses (32 octets, temps < 1 ms, TTL = 128), 0 % de perte.*

```
C:\Windows\System32>ping 127.0.0.1
```

## Longueur de préfixe (*prefix length*)

Au lieu d'écrire le masque, on peut utiliser la **notation avec barre oblique** (*slash notation*) : le nombre après `/` est le **nombre de bits réseau**.

| Classe | Exemple |
|---|---|
| A | `10.224.64.19/8` |
| B | `172.224.32.6/16` |
| C | `192.168.1.4/24` |

## Masques par défaut des classes

| Classe | Masque | Bits réseau | Bits hôte |
|---|---|---|---|
| A | 255.0.0.0 | 8 | 24 |
| B | 255.255.0.0 | 16 | 16 |
| C | 255.255.255.0 | 24 | 8 |

![[IP Addressing - p22.jpg]]
*Figure : /8 = 255.0.0.0 = 11111111 00000000 00000000 00000000 ; /16 = 255.255.0.0 ; /24 = 255.255.255.0 = 11111111 11111111 11111111 00000000.*

## Adresse réseau et adresse de broadcast

- **Adresse réseau** : partie hôte entièrement à **0**. Elle **ne peut pas** être attribuée à un hôte. La **première adresse utilisable** est celle juste au-dessus de l'adresse réseau.
- **Adresse de broadcast** : partie hôte entièrement à **1**. Elle **ne peut pas** être attribuée à un hôte. La **dernière adresse utilisable** est celle juste en dessous du broadcast.

![[IP Addressing - p23.jpg]]
*Figure : adresse réseau. Dans la topologie à deux réseaux, 192.168.1.0/24 et 192.168.2.0/24 sont les adresses réseau (partie hôte à 0).*

![[IP Addressing - p24.jpg]]
*Figure : adresse de broadcast. Dans la même topologie, la partie hôte à 1 (192.168.1.255, 192.168.2.255) est l'adresse de broadcast.*

## Première et dernière adresse utilisable

| Classe | Réseau (hôte à 0) | Première utilisable | Dernière utilisable | Broadcast (hôte à 1) |
|---|---|---|---|---|
| C | 192.168.1.0/24 | 192.168.1.1/24 | 192.168.1.254/24 | 192.168.1.255/24 |
| B | 172.16.0.0/16 | 172.16.0.1/16 | 172.16.255.254/16 | 172.16.255.255/16 |
| A | 10.0.0.0/8 | 10.0.0.1/8 | 10.255.255.254/8 | 10.255.255.255/8 |

![[IP Addressing - p25.jpg]]
*Figure : classe C, la partie hôte 00000000 donne l'adresse réseau, 00000001 la première utilisable, 11111110 la dernière, 11111111 le broadcast.*

## Nombre maximal d'hôtes par réseau

$$\text{hôtes max} = 2^n - 2 \qquad (n = \text{nombre de bits hôte})$$

On retire l'adresse réseau et l'adresse de broadcast.

| Classe | Exemple | Bits hôte | Adresses | Hôtes max |
|---|---|---|---|---|
| C | 192.168.1.0/24 → 192.168.1.255/24 | 8 | $2^8 = 256$ | $2^8 - 2 = 254$ |
| B | 172.16.0.0/16 → 172.16.255.255/16 | 16 | $2^{16} = 65\,536$ | $2^{16} - 2 = 65\,534$ |
| A | 10.0.0.0/8 → 10.255.255.255/8 | 24 | $2^{24} = 16\,777\,216$ | $2^{24} - 2 = 16\,777\,214$ |

![[IP Addressing - p28.jpg]]
*Figure : classe C, partie hôte de 8 bits, $2^8 = 256$ adresses, $2^8 - 2 = 254$ hôtes au maximum.*

## Révision

Points listés par le cours : décimal pointé et binaire ; partie réseau / partie hôte ; classes IPv4 ; masque (*subnet mask*, *netmask*, longueur de préfixe) ; adresse réseau ; adresse de broadcast ; première et dernière adresse utilisable ; nombre maximal d'hôtes par réseau.

## Quiz (première série)

Le document ne donne **aucune correction**. Les réponses ci-dessous sont un complément calculé, pas le cours.

1. Convertir en décimal pointé : `00111111 00111000 11100111 00010011`.
   *Complément* : 63.56.231.19.
2. Une adresse IP indique quels deux types d'information ? a) adresse réseau, bits de broadcast ; b) adresse de broadcast, adresse d'hôte ; c) adresse réseau, adresse d'hôte ; d) adresse réseau, adresse de broadcast.
   *Complément* : c (cf. diapositive 13).
3. Un masque de sous-réseau indique quels deux types d'information ? a) adresse réseau, bits de broadcast ; b) bits de broadcast, bits hôte ; c) bits réseau, bits hôte ; d) adresse réseau, adresse d'hôte.
   *Complément* : c.
4. Quelles adresses ne peuvent pas être attribuées à un hôte ? a) adresse IP ; b) adresse réseau ; c) adresse de broadcast ; d) dernière adresse utilisable.
   *Complément* : b et c.
5. Pour chaque adresse, trouver : a) l'adresse réseau ; b) le nombre maximal d'hôtes ; c) le broadcast ; d) la première et e) la dernière adresse utilisable.

| Adresse | Réseau | Hôtes max | Broadcast | Première | Dernière |
|---|---|---|---|---|---|
| 43.109.23.12/8 | 43.0.0.0 | 16 777 214 | 43.255.255.255 | 43.0.0.1 | 43.255.255.254 |
| 129.221.23.13/16 | 129.221.0.0 | 65 534 | 129.221.255.255 | 129.221.0.1 | 129.221.255.254 |
| 224.192.64.32/24 | 224.192.64.0 | 254 | 224.192.64.255 | 224.192.64.1 | 224.192.64.254 |

*(Tableau de réponses : complément calculé. 224.192.64.32 est une adresse de classe D, multicast, qui n'a normalement ni hôtes ni masque par défaut ; le calcul suit le /24 donné par l'énoncé.)*

## Récapitulatif IPv4

Les diapositives 39 et 40 reprennent les deux tableaux des classes (premier octet, plage, préfixe) donnés plus haut ; la classe E est encadrée en rouge.

## IANA et gaspillage d'adresses

- L'[[IANA]] (*Internet Assigned Numbers Authority*) attribuait les réseaux IPv4 aux entreprises **selon leur taille** : classe A ou B pour une très grande entreprise, classe C pour une petite.
- Cela a conduit à **beaucoup d'adresses gaspillées**.

![[IP Addressing - p42.jpg]]
*Figure : liaison entre deux routeurs, R1 (San Francisco) et R2 (New York), sur le réseau 203.0.113.0/24 : 256 adresses, dont 1 adresse réseau (203.0.113.0), 1 broadcast (203.0.113.255), l'adresse de R1 (.1) et celle de R2 (.2), soit 252 adresses gaspillées.*

**Exemple** : l'entreprise X a besoin de 5000 hôtes. Une classe C ne suffit pas, on lui attribue donc une classe B : environ **60 000 adresses gaspillées**.

## CIDR (*Classless Inter-Domain Routing*)

- Les créateurs d'Internet n'avaient pas prévu sa taille actuelle, d'où un espace d'adresses gaspillé.
- L'[[IETF]] (*Internet Engineering Task Force*) a introduit le **CIDR en 1993** pour remplacer le système *classful* (voir [[Routage classful et classless]]).
- Avec le CIDR, les contraintes classe A = /8, classe B = /16, classe C = /24 **ont été supprimées**.
- Les grands réseaux se découpent en réseaux plus petits, plus efficaces : les **sous-réseaux** (*subnetworks*, *subnets*).

![[IP Addressing - p46.jpg]]
*Figure : 203.0.113.0/24 entre R1 et R2. Adresse 11001011.00000000.01110001.00000000 et masque 255.255.255.0 : 8 bits hôte, $2^8 - 2 = 254$ adresses utilisables.*

| Adresse | Bits réseau | Bits hôte | Adresses utilisables |
|---|---|---|---|
| 192.168.1.0/24 | 24 | 8 | $2^8 - 2 = 254$ |
| 192.168.1.0/25 | 25 | 7 | $2^7 - 2 = 126$ |
| 192.168.1.0/26 | 26 | 6 | $2^6 - 2 = 62$ |
| 192.168.1.0/27 | 27 | 5 | $2^5 - 2 = 30$ |
| 192.168.1.0/28 | 28 | 4 | $2^4 - 2 = 14$ |
| 192.168.1.0/29 | 29 | 3 | $2^3 - 2 = 6$ |
| 192.168.1.0/30 | 30 | 2 | $2^2 - 2 = 2$ |
| 192.168.1.0/31 | 31 | 1 | $2^1 - 2 = 0$ |
| 192.168.1.0/32 | 32 | 0 | $2^0 - 2 = $ X |

Les deux dernières lignes ont pourtant un usage. Un **/31** n'a ni adresse réseau ni broadcast : la RFC 3021 (2000) l'autorise sur les liens point à point, où ses 2 adresses vont aux deux routeurs. Un **/32** désigne une seule machine (route vers un hôte précis, adresse de bouclage d'un routeur) : c'est le préfixe des routes `L` de `show ip route` (voir [[2 - Static Routing]]). [[Complément hors du cours|ⓘ]]

Le CIDR sert aussi dans l'autre sens : regrouper plusieurs réseaux contigus sous un préfixe plus court (**agrégation** ou *supernetting*). Par exemple 192.168.0.0/24 à 192.168.3.0/24 s'annoncent ensemble en 192.168.0.0/22, ce qui réduit la taille des tables de routage d'Internet. [[Complément hors du cours|ⓘ]]

Reprise de l'exemple des 5000 hôtes : $2^{12} - 2 = 4094$ ne suffit pas, $2^{13} - 2 = 8190$ suffit, donc 13 bits hôte, soit un **/19**. Environ 3200 adresses inutilisées au lieu d'environ 60 000 avec une classe B. [[Complément hors du cours|ⓘ]]

Les diapositives 48 à 53 refont le calcul sur le lien 203.0.113.0 entre R1 et R2, en allongeant le préfixe d'un bit à chaque fois :

| Préfixe | Dernier octet du masque | Calcul |
|---|---|---|
| /25 | 128 | $2^7 - 2 = 126$ |
| /26 | 192 | $2^6 - 2 = 62$ |
| /27 | 224 | $2^5 - 2 = 30$ |
| /28 | 240 | $2^4 - 2 = 14$ |
| /29 | 248 | $2^3 - 2 = 6$ |
| /30 | 252 | $2^2 - 2 = 2$ |

![[IP Addressing - p48.jpg]]
*Figure : 203.0.113.0/25, le masque 255.255.255.128 emprunte un bit à la partie hôte : $2^7 - 2 = 126$ adresses utilisables.*

Pour un lien entre deux routeurs, le /30 suffit (2 adresses utilisables) : c'est la réponse au gaspillage de l'exemple précédent.

## Notation CIDR

| Masque (décimal pointé) | Notation CIDR |
|---|---|
| 255.255.255.0 | /24 |
| 255.255.255.128 | /25 |
| 255.255.255.192 | /26 |
| 255.255.255.224 | /27 |
| 255.255.255.240 | /28 |
| 255.255.255.248 | /29 |
| 255.255.255.252 | /30 |
| 255.255.255.254 | /31 |
| 255.255.255.255 | /32 |

**Méthode de découpage** (*subnetting*) : [[Complément hors du cours|ⓘ]]
1. emprunter $s$ bits à la partie hôte donne $2^s$ sous-réseaux ; il reste $h$ bits hôte, soit $2^h - 2$ hôtes par sous-réseau ;
2. on choisit $s$ d'après le nombre de sous-réseaux voulu ($2^s \ge$ nombre demandé), ou $h$ d'après le nombre d'hôtes ($2^h - 2 \ge$ hôtes demandés) ;
3. la **taille de bloc** vaut $2^h$, soit 256 moins la valeur de l'octet de masque concerné (/26 : 256 − 192 = 64) ; les adresses réseau se suivent de bloc en bloc (.0, .64, .128, .192), le broadcast est l'adresse qui précède le réseau suivant.

Exemple : `192.168.1.100/26`. Bloc de 64, et 100 est entre 64 et 127 : réseau 192.168.1.64, première adresse .65, dernière .126, broadcast .127. [[Complément hors du cours|ⓘ]]

## Quiz (découpage en sous-réseaux)

Pas de correction dans le document. Voir aussi [[VLSM]].

**Exercice 1.** Découper `192.168.1.0/24` en **quatre sous-réseaux** qui accueillent le nombre d'hôtes demandé ; donner pour chacun l'adresse réseau, la première et la dernière adresse utilisable, et le broadcast.

![[IP Addressing - p55.jpg]]
*Figure : le routeur R1 relié à quatre commutateurs SW1 à SW4, chacun avec 45 hôtes.*

*Complément calculé* : 45 hôtes demandent 6 bits hôte ($2^6 - 2 = 62$), donc des /26 :

| Sous-réseau | Réseau | Première | Dernière | Broadcast |
|---|---|---|---|---|
| SW1 | 192.168.1.0/26 | .1 | .62 | .63 |
| SW2 | 192.168.1.64/26 | .65 | .126 | .127 |
| SW3 | 192.168.1.128/26 | .129 | .190 | .191 |
| SW4 | 192.168.1.192/26 | .193 | .254 | .255 |

**Exercice 2.** Découper `192.168.255.0/24` en **cinq sous-réseaux de même taille** ; identifier les cinq sous-réseaux, avec adresse réseau, première et dernière adresse utilisable, broadcast.

![[IP Addressing - p56.jpg]]
*Figure : le routeur R1 relié à cinq commutateurs SW1 à SW5.*

*Complément calculé* : 5 sous-réseaux demandent 3 bits empruntés ($2^3 = 8 \ge 5$), donc des /27 (30 hôtes chacun) ; les cinq premiers sont 192.168.255.0/27, .32/27, .64/27, .96/27 et .128/27 (par exemple pour le premier : réseau .0, première .1, dernière .30, broadcast .31).

## Liens

Prérequis du [[Routage statique]] et du [[Routage dynamique]] ; le [[NAT et PAT]] traite les adresses privées ; [[CLI Cisco IOS]] pour configurer les adresses ; [[IPv6]] pour la version suivante du protocole.
