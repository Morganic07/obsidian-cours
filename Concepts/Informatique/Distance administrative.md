---
type: concept
tags: [year3]
aliases: [administrative distance, distances administratives, route statique flottante, floating static route]
sources: ["[[2 - Static Routing|Chp2 - Static Routing]]", "[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la distance administrative (AD) est une valeur de **0 à 255** qu'un [[Routeur]] attribue à chaque source d'information de routage, et qui mesure la confiance qu'il lui accorde. Quand il apprend la **même destination (même préfixe)** par plusieurs sources, il installe dans sa table la route dont la source a la distance administrative la plus faible.

**Valeurs par défaut (Cisco)**

| Source de la route | Distance administrative |
|---|---|
| Réseau directement connecté | 0 |
| Route statique | 1 |
| eBGP | 20 |
| [[EIGRP]] (interne) | 90 |
| [[OSPF]] | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP externe | 170 |
| iBGP | 200 |
| Source inconnue | 255 (route jamais utilisée) |

**Distance administrative et métrique** : la distance administrative départage des sources différentes ; la **métrique** départage ensuite des routes apprises par un même protocole (nombre de sauts pour RIP, coût pour OSPF, métrique composite pour EIGRP). Les deux n'interviennent qu'à préfixe égal : entre deux préfixes de longueurs différentes, c'est la [[Plus longue correspondance de préfixe|plus longue correspondance de préfixe]] qui choisit, quelle que soit la distance administrative.

**Lecture dans `show ip route`** : les crochets donnent `[distance/métrique]`.

```
S    10.0.1.0/24 [1/0] via 203.0.113.2       (route statique : AD 1, métrique 0)
R    10.0.3.0/24 [120/1] via 10.0.0.2        (RIP : AD 120, 1 saut)
O    10.0.4.0/24 [110/2] via 10.0.0.2        (OSPF : AD 110, coût 2)
```

**Route statique flottante** : route de secours à laquelle on donne une distance administrative plus grande que celle de la route principale, en dernier paramètre de `ip route`. Elle reste absente de la table tant que la route principale existe, et s'y installe quand celle-ci disparaît :

```
ip route 10.0.1.0 255.255.255.0 198.51.100.2 130
```

Ici, avec une AD de 130, la route statique cède la place à une route OSPF (110) ou RIP (120) vers le même réseau.

## Dans le cours

Le cours ne la nomme pas. La notation `[1/0]` apparaît dans les sorties `show ip route` de [[2 - Static Routing|Chp2 - Static Routing]] sans explication ; la notion est détaillée dans les compléments de cette fiche et de [[3 - Dynamic Routing|Chp3 - Dynamic Routing]].

Voir aussi : [[Routage statique]], [[Routage dynamique]], [[Routage IP]], [[OSPF]], [[EIGRP]], [[CLI Cisco IOS]].

Résumés : [[2 - Static Routing]], [[3 - Dynamic Routing]]
