---
type: concept
tags: [year3]
aliases: [route statique, routes statiques, static route, static routing, route par défaut, default route, table de routage, next hop, directly connected network, réseau directement connecté, réseaux directement connectés, remote network, réseau distant, show ip route]
matieres: [Computer Network]
sources: ["[[2 - Static Routing (résumé)|Chp2 - Static Routing]]", "[[3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]]", "[[1 - Computer Networks (résumé)|chp1 - Computer Networks]]"]
maj: 2026-11-06
---

Un routeur décide du chemin d'un paquet avec sa **table de routage**. Il apprend seul les réseaux directement connectés (codes `C` et `L` dans `show ip route`) mais pas les réseaux distants : il lui faut des routes explicites, statiques (écrites par l'administrateur) ou dynamiques (voir [[Routage dynamique]]).

**Route statique** : `ip route <réseau> <masque> <sortie>`, où la sortie est une interface ou l'adresse du saut suivant (next hop). Elle apparaît avec le code `S`. Exemples du cours :
- `ip route 10.0.1.0 255.255.255.0 gigabitEthernet 0/0`
- `ip route 10.0.1.0 255.255.255.0 203.0.113.2` (affichée `[1/0] via 203.0.113.2`)
- suppression : `no ip route ...`

**Route par défaut** : utilisée quand aucune route précise n'existe, fréquente en bordure vers Internet. Réseau `0.0.0.0/0` : `ip route 0.0.0.0 0.0.0.0 <next hop>`.

> [!warning] Écart dans le cours
> Le tableau des réseaux connectés de [[2 - Static Routing (résumé)|Chp2 - Static Routing]] écrit « R3 » pour une ligne qui concerne R2.

Dans `show ip route`, `L` (local) désigne l'adresse de l'interface elle-même, en /32.

Notion parente : [[Routage IP]]. Liens : [[Routage dynamique]], [[Routeur]], [[CLI Cisco IOS]], [[Adressage IPv4 et CIDR]]

Résumés : [[2 - Static Routing (résumé)]], [[3 - Dynamic Routing (résumé)]], [[1 - Computer Networks (résumé)]]
