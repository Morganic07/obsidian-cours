---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : masque générique (*wildcard mask*), trafic entrant et sortant, principe des ACL, refus implicite, types d'ACL, configuration, et TP de placement d'ACL standard. Cours en anglais. Voir [[Liste de contrôle d'accès]].

La note s'ouvre sur une définition isolée : [[ICMP]] = *Internet Control Message Protocol*.

ICMP est le protocole de messages de contrôle et d'erreur de la couche réseau, transporté directement dans IP (sans TCP ni UDP, donc sans numéro de port) : *echo request* / *echo reply* de `ping`, « destination injoignable », « délai dépassé » utilisé par `traceroute`. Il intéresse les ACL parce qu'une ACL étendue peut filtrer ICMP à part, par exemple bloquer les `ping` sans bloquer le reste du trafic. [[Complément hors du cours|ⓘ]]

## Masque générique (*wildcard mask*)

- Le *wildcard mask* est un **[[Adressage IPv4 et CIDR|masque de sous-réseau]] inversé**.
- Tous les 1 du masque de sous-réseau deviennent des 0 dans le *wildcard*, et tous les 0 deviennent des 1.
- **Raccourci** : retrancher chaque [[Octet|octet]] du masque à 255.
- Lecture : **0 = doit correspondre** (*must match*) ; **1 = peu importe** (*don't have to match*).

| Préfixe | Masque de sous-réseau | Dernier octet (binaire) | *Wildcard* | Dernier octet (binaire) |
|---|---|---|---|---|
| /24 | 255.255.255.0 | 00000000 | 0.0.0.255 | 11111111 |
| /25 | 255.255.255.128 | 10000000 | 0.0.0.127 | 01111111 |
| /28 | 255.255.255.240 | 11110000 | 0.0.0.15 | 00001111 |
| /32 (un hôte) | 255.255.255.255 | 11111111 | 0.0.0.0 | 00000000 |

(La ligne /32 vient du TP en fin de note : PC3, 192.168.2.1/32, a pour *wildcard* 0.0.0.0.)

**Comment le routeur s'en sert.** Pour une ACE `192.168.1.0 0.0.0.255`, le routeur compare l'adresse du paquet à 192.168.1.0 bit à bit, mais seulement aux positions où le *wildcard* vaut 0 : ici les trois premiers octets doivent valoir 192.168.1, le dernier est libre. 192.168.1.37 correspond, 192.168.2.37 non. Le *wildcard* sert donc à désigner d'un coup un hôte, un sous-réseau ou une plage d'adresses. [[Complément hors du cours|ⓘ]]

**Deux raccourcis de syntaxe IOS** : [[Complément hors du cours|ⓘ]]
- `host 192.168.2.1` équivaut à `192.168.2.1 0.0.0.0` (un seul hôte) ; [[Complément hors du cours|ⓘ]]
- `any` équivaut à `0.0.0.0 255.255.255.255` (toutes les adresses). [[Complément hors du cours|ⓘ]]

Exemple de calcul pour un /26 : masque 255.255.255.192, *wildcard* $255 - 192 = 63$, soit 0.0.0.63, c'est-à-dire un bloc de 64 adresses. [[Complément hors du cours|ⓘ]]

## Trafic entrant et sortant (*inbound / outbound*)

Le sens se lit **du point de vue du routeur**, interface par interface.

![[chp6 - Access Control List - image3.png]]
*Figure : en haut, le trafic entre par Fa 0/0 (*inbound*) et sort par Fa 0/1 (*outbound*) ; en bas, la même interface Fa 0/0 voit les deux sens.*

Une ACL **en entrée** est appliquée avant la décision de routage : un paquet refusé est jeté sans que le routeur ait cherché sa route, ce qui économise du traitement. Une ACL **en sortie** est appliquée après le routage, juste avant l'envoi sur l'interface : elle ne voit que le trafic routé vers cette interface. Une ACL en sortie ne filtre pas les paquets émis par le routeur lui-même. [[Complément hors du cours|ⓘ]]

## ACL (*Access Control List*)

- Une ACL fonctionne comme un **filtre de paquets** : elle indique au [[Routeur|routeur]] d'autoriser (*permit*) ou de rejeter (*discard*) un trafic donné.
- Elle peut filtrer selon les adresses IP source et destination, les [[Numéro de port|ports de couche 4]] source et destination, etc.
- Sur un routeur, les ACL se configurent **en mode de configuration globale**.
- Une ACL est une **suite ordonnée d'ACE** (*Access Control Entries*).

Exemple du cours :

**Exigences** : les hôtes de 192.168.1.0/24 peuvent accéder à 10.0.1.0/24 ; ceux de 192.168.2.0/24 ne le peuvent pas.

**ACL 1** :
1. si IP source = 192.168.1.0/24, alors *permit* ;
2. si IP source = 192.168.2.0/24, alors *deny* ;
3. si IP source = *any*, alors *permit*.

![[chp6 - Access Control List - image4.png]]
*Figure : topologie du chapitre. R1 dessert 192.168.1.0/24 par G0/1 (.254 ; PC1 en .1, PC2 en .2) et 192.168.2.0/24 par G0/2 (.254 ; PC3 en .1, PC4 en .2). R1 G0/0 (.1) est relié à R2 G0/0 (.2) par 203.0.113.0/30. R2 dessert 10.0.1.0/24 par G0/1 (.254 ; SRV1 en .100) et 10.0.2.0/24 par G0/2 (.254 ; SRV2 en .100).*

### Application et parcours

- Configurer une ACL en mode global **ne la rend pas active** : il faut **l'appliquer à une interface**.
- Une ACL s'applique **en entrée** (*inbound*) **ou en sortie** (*outbound*).
- Une ACL est faite d'une ou plusieurs ACE.
- Le routeur examine les ACE **dans l'ordre, de haut en bas**.
- Dès qu'un paquet correspond à une ACE, le routeur applique l'action et **arrête le parcours** : les entrées suivantes sont ignorées.

**Récapitulatif** :
- **une ACL au maximum par interface et par sens** : une en entrée, une en sortie ;
- appliquer une seconde ACL sur la même interface et le même sens **remplace** la précédente.

Conséquence du parcours de haut en bas : **l'ordre des ACE compte**. Une entrée générale placée avant une entrée précise la masque : avec `permit 192.168.1.0 0.0.0.255` puis `deny host 192.168.1.1`, PC1 est autorisé, car la première ligne correspond déjà. Les entrées les plus précises se placent donc en premier. Dans une ACL numérotée, chaque nouvelle `access-list` s'ajoute à la fin de la liste. [[Complément hors du cours|ⓘ]]

## Refus implicite (*implicit deny*)

- Par défaut, **toute ACL se termine par un *deny* implicite**.
- Si aucune entrée ne correspond, le paquet est **rejeté**.

Le cours compare trois versions de l'ACL 1 :

| Version | Lignes | Effet sur une autre source |
|---|---|---|
| A | 1. 192.168.1.0/24 → *permit* ; 2. 192.168.2.0/24 → *deny* | rejetée (refus implicite) [[Erreurs du cours#^e-6-access-control-list\|✎]] |
| B | idem + 3. *any* → *deny* | rejetée (refus explicite, même effet que A) |
| C | idem + 3. *any* → *permit* | autorisée |

(La colonne « effet » résume la comparaison ; le cours ne la rédige pas.)

Le refus implicite n'apparaît pas dans `show access-lists`. Une ACL qui ne contient que des `deny` bloque donc **tout** le trafic de l'interface dans ce sens : il faut au moins un `permit`. Écrire le `deny any` explicitement (version B) a un intérêt pratique : la ligne apparaît avec un compteur de correspondances, ce qui permet de voir combien de paquets ont été rejetés. [[Complément hors du cours|ⓘ]]

## Types d'ACL

1. **ACL standard** : correspondance sur l'**IP source uniquement**.
   a. standard numérotées ; b. standard nommées.
2. **ACL étendues** (*extended*) : correspondance sur l'**IP source/destination, les ports source/destination**, etc.
   a. étendues numérotées ; b. étendues nommées.

ACL standard numérotées : identifiées par un numéro, dans les plages **1–99** et **1300–1999**.

ACL étendues numérotées : plages **100–199** et **2000–2699**. Le numéro suffit au routeur pour savoir de quel type est l'ACL. [[Complément hors du cours|ⓘ]]

Une ACL **nommée** porte un nom au lieu d'un numéro, ce qui la rend plus lisible, et se configure dans un sous-mode où l'on peut insérer ou supprimer une ligne précise par son numéro de séquence : [[Complément hors du cours|ⓘ]]

```
R2(config)# ip access-list standard BLOQUER-LAN2
R2(config-std-nacl)# deny 192.168.2.0 0.0.0.255
R2(config-std-nacl)# permit any
R2(config-std-nacl)# interface g0/1
R2(config-if)# ip access-group BLOQUER-LAN2 out
```

Une ACE **étendue** précise le protocole, la source, la destination et éventuellement le port. Exemple : autoriser le web de 192.168.1.0/24 vers SRV1, puis refuser le reste vers ce serveur : [[Complément hors du cours|ⓘ]]

```
R1(config)# access-list 100 permit tcp 192.168.1.0 0.0.0.255 host 10.0.1.100 eq 80
R1(config)# access-list 100 deny ip any host 10.0.1.100
R1(config)# access-list 100 permit ip any any
R1(config)# interface g0/1
R1(config-if)# ip access-group 100 in
```

Le mot-clé de protocole peut être `ip` (tout), `tcp`, `udp` ou `icmp` ; `eq 80` désigne le port de destination 80 (HTTP), voir [[Numéro de port]]. [[Complément hors du cours|ⓘ]]

**Placement, règle générale** : une ACL **étendue** se place **près de la source**, puisqu'elle connaît la destination et ne bloque que le trafic visé ; le trafic refusé est ainsi jeté tôt, sans traverser le réseau. Une ACL **standard** se place près de la destination (règle du TP ci-dessous) : placée près de la source, elle bloquerait cette source vers toutes les destinations. [[Complément hors du cours|ⓘ]]

Une ACL est **sans état** (*stateless*) : elle juge chaque paquet isolément, sans savoir s'il appartient à une connexion déjà ouverte. Un [[Pare-feu|pare-feu]] à états (*stateful*) suit les connexions et laisse passer les réponses à une requête autorisée ; il remplace ou complète les ACL dans les réseaux d'entreprise. [[Complément hors du cours|ⓘ]]

## Configurer une ACL

```
R1(config)# access-list <number> {deny | permit} <ip> <wildcard-mask>
R1(config-if)# ip access-group <number> {in | out}
```

La première ligne crée une ACE (en mode global) ; la seconde, saisie dans l'interface, applique l'ACL dans un sens.

![[chp6 - Access Control List - image2.png]]
*Figure : la même topologie, l'ACL 1 et les exigences, sous le titre « Router R2 » ; la syntaxe est donnée avec le prompt R1.*

Pour l'exemple (192.168.1.0/24 autorisé, 192.168.2.0/24 refusé vers 10.0.1.0/24), une traduction possible de l'ACL 1, *complément non donné par le cours* :

```
R2(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R2(config)# access-list 1 deny 192.168.2.0 0.0.0.255
R2(config)# access-list 1 permit any
R2(config)# interface gigabitEthernet 0/1
R2(config-if)# ip access-group 1 out
```

**Vérifier et retirer une ACL** : [[Complément hors du cours|ⓘ]]
- `show access-lists` affiche les ACL et, pour chaque ACE, le nombre de paquets qui y ont correspondu ; [[Complément hors du cours|ⓘ]]
- `show ip interface g0/1` indique quelle ACL est appliquée à l'interface et dans quel sens ; [[Complément hors du cours|ⓘ]]
- `no ip access-group 1 out` (dans l'interface) détache l'ACL ; `no access-list 1` (en mode global) supprime **toute** l'ACL numérotée, pas une seule ligne. [[Complément hors du cours|ⓘ]]

## TP (*LAB*)

**Règle** : une ACL standard se place **près de la destination**, parce qu'elle ne filtre que l'IP source.

**Exigences** :
1. les PC de 192.168.1.0/24 ne peuvent pas accéder à 10.0.2.0/24 ;
2. PC3 ne peut pas accéder à 10.0.1.0/24 ;
3. les autres PC de 192.168.2.0/24 peuvent accéder à 10.0.1.0/24 ;
4. PC1 peut accéder à 10.0.1.0/24 ;
5. les autres PC de 192.168.1.0/24 ne peuvent pas accéder à 10.0.1.0/24.

![[chp6 - Access Control List - image6.png]]
*Figure : les cinq exigences et la topologie R1 / R2 du chapitre.*

**Réponse du cours** (équipement, interface, sens, ACL) :

| Exigence | Placement |
|---|---|
| 1 | R2 : G0/2 en sortie, ACL 10 |
| 2 | R2 : G0/1 en sortie, ACL 20 |
| 3 | R2 : G0/1 en sortie, ACL 20 |
| 4 | R2 : G0/1 en sortie, ACL 20 (10.0.1.0/24 est derrière G0/1) [[Erreurs du cours#^e-6-access-control-list\|✎]] |
| 5 | R2 : G0/1 en sortie, ACL 20 |

*Wildcards* utiles : PC3 = 192.168.2.1/32 → 0.0.0.0 ; 192.168.1.0/24 → 0.0.0.255.

**Méthode** :
1. pour chaque exigence, trouver le bon équipement (R2), la bonne interface (par exemple G0/2) et le bon sens (*out*) ;
2. regrouper dans **une même ACL** les exigences qui ont les mêmes paramètres (par exemple, l'ACL 10).

Une écriture possible des deux ACL de la solution, sur R2, en tenant compte de l'ordre (précis d'abord) et du refus implicite (`permit any` final) : [[Complément hors du cours|ⓘ]]

```
R2(config)# access-list 10 deny 192.168.1.0 0.0.0.255
R2(config)# access-list 10 permit any
R2(config)# access-list 20 deny host 192.168.2.1
R2(config)# access-list 20 permit host 192.168.1.1
R2(config)# access-list 20 deny 192.168.1.0 0.0.0.255
R2(config)# access-list 20 permit any
R2(config)# interface g0/2
R2(config-if)# ip access-group 10 out
R2(config-if)# interface g0/1
R2(config-if)# ip access-group 20 out
```

Dans l'ACL 20, `permit host 192.168.1.1` doit précéder `deny 192.168.1.0 0.0.0.255`, sinon PC1 serait refusé par la ligne générale (exigences 4 et 5). Le `permit any` final laisse passer le reste de 192.168.2.0/24 (exigence 3) et les autres sources. [[Complément hors du cours|ⓘ]]
