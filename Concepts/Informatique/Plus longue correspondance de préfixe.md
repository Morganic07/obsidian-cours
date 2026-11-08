---
type: concept
tags: [year3]
aliases: [longest prefix match, LPM, correspondance du préfixe le plus long]
sources: ["[[Raw/Year 3/Computer Network/Chp3 : Dynamic Routing.docx|Chp3 - Dynamic Routing]]", "[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : règle qu'applique un [[Routeur|routeur]] quand plusieurs routes de sa table de routage contiennent l'adresse IP de destination d'un paquet : il retient celle dont le masque (le préfixe, en notation [[Adressage IPv4 et CIDR|CIDR]]) est le plus long, c'est-à-dire la plus précise. Une route $R/n$ « contient » l'adresse $A$ quand les $n$ premiers bits de $A$ sont égaux à ceux de $R$.

**Exemple** : pour la destination 10.0.3.5, les routes 10.0.3.0/24, 10.0.0.0/8 et 0.0.0.0/0 conviennent toutes ; 10.0.3.0/24 (24 bits communs) l'emporte sur 10.0.0.0/8, qui l'emporte sur 0.0.0.0/0. Une route 10.0.4.0/24 ne convient pas : le troisième octet diffère.

**Conséquence** : la route par défaut, de préfixe /0, correspond à toutes les adresses mais est la moins précise possible ; elle ne sert donc qu'en dernier recours, quand aucune autre route ne correspond. Dans `show ip route` chez Cisco, elle apparaît comme *Gateway of last resort* (passerelle de dernier recours), avec le code `S*` si elle est statique.

**Ordre des critères** : d'abord le préfixe le plus long ; à préfixe égal (même réseau appris par plusieurs sources), la distance administrative la plus faible ; puis, entre routes d'un même protocole, la meilleure métrique. Une route en /24 apprise par RIP l'emporte donc sur une route statique en /16, malgré la distance administrative plus forte de RIP (120 contre 1) : les deux critères ne se comparent pas sur le même plan.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - Static Routing]] (choix de la route à chaque paquet) et de [[3 - Dynamic Routing]] (pourquoi la route par défaut ne sert qu'en dernier recours).

Voir aussi : [[Routage IP]], [[Routage statique]], [[Routage dynamique]], [[Adressage IPv4 et CIDR]], [[Passerelle par défaut]].

Résumés : [[2 - Static Routing]], [[3 - Dynamic Routing]]
