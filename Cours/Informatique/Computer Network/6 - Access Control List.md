---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]], dans [[Cours/Informatique/Computer Network/_index|Computer Network]] : masque générique (*wildcard mask*), trafic entrant et sortant, principe des ACL, refus implicite, types d'ACL, configuration, et TP de placement d'ACL standard. Cours en anglais. En cas d'écart, le cours et ses images font foi. Voir [[Liste de contrôle d'accès]].

La note s'ouvre sur une définition isolée : [[ICMP]] = *Internet Control Message Protocol*.

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

## Trafic entrant et sortant (*inbound / outbound*)

Le sens se lit **du point de vue du routeur**, interface par interface.

![[chp6 - Access Control List - image3.png]]
*Figure : en haut, le trafic entre par Fa 0/0 (*inbound*) et sort par Fa 0/1 (*outbound*) ; en bas, la même interface Fa 0/0 voit les deux sens.*

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

## Refus implicite (*implicit deny*)

- Par défaut, **toute ACL se termine par un *deny* implicite**.
- Si aucune entrée ne correspond, le paquet est **rejeté**.

Le cours compare trois versions de l'ACL 1 :

| Version | Lignes | Effet sur une autre source |
|---|---|---|
| A | 1. 192.168.1.0/24 → *permit* ; 2. 192.168.0.0/24 → *deny* | rejetée (refus implicite) |
| B | idem + 3. *any* → *deny* | rejetée (refus explicite, même effet que A) |
| C | idem + 3. *any* → *permit* | autorisée |

(La colonne « effet » résume la comparaison ; le cours ne la rédige pas.)

## Types d'ACL

1. **ACL standard** : correspondance sur l'**IP source uniquement**.
   a. standard numérotées ; b. standard nommées.
2. **ACL étendues** (*extended*) : correspondance sur l'**IP source/destination, les ports source/destination**, etc.
   a. étendues numérotées ; b. étendues nommées.

ACL standard numérotées : identifiées par un numéro, dans les plages **1–99** et **1300–1999**.

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
| 4 | R2 : G0/2 en sortie, ACL 10 (erreur probable : G0/1 en sortie, ACL 20, voir « Erreurs du cours ») |
| 5 | R2 : G0/1 en sortie, ACL 20 |

*Wildcards* utiles : PC3 = 192.168.2.1/32 → 0.0.0.0 ; 192.168.1.0/24 → 0.0.0.255.

**Méthode** :
1. pour chaque exigence, trouver le bon équipement (R2), la bonne interface (par exemple G0/2) et le bon sens (*out*) ;
2. regrouper dans **une même ACL** les exigences qui ont les mêmes paramètres (par exemple, l'ACL 10).

## Erreurs du cours

- [[Raw/Year 3/Computer Network/chp6 : Access Control List.docx|chp6 - Access Control List]], solution du TP, exigence 4 (topologie vérifiée sur l'image 6) : écrit « R2 : G0/2-out ACL 10 » pour « PC1 can access 10.0.1.0/24 » ; il faut « R2 : G0/1-out ACL 20 », comme les exigences 2, 3 et 5 : le réseau 10.0.1.0/24 est derrière G0/1, alors que G0/2 dessert 10.0.2.0/24 (complément). **À retenir pour un examen.**
- Même document, refus implicite (vérifié sur l'image 7) : les trois ACL de comparaison écrivent en ligne 2 « if source IP=192.168.0.0/24 then deny » ; il faut sans doute « 192.168.2.0/24 », réseau de la topologie et de l'exemple précédent (coquille probable).
