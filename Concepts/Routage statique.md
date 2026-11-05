---
type: concept
aliases: [route statique, routes statiques, static route, static routing, route par défaut, default route, table de routage, next hop]
matieres: [Computer Network]
sources: ["[[Chp2 - Static Routing]]", "[[Chp3 - Dynamic Routing]]", "[[chp1 - Computer Networks]]"]
maj: 2026-11-05
---

Un routeur décide du chemin d'un paquet avec sa **table de routage**. Il apprend seul les réseaux directement connectés (codes `C` et `L` dans `show ip route`) mais pas les réseaux distants : il lui faut des routes explicites, statiques (écrites par l'administrateur) ou dynamiques (voir [[Routage dynamique]]).

**Route statique** : `ip route <réseau> <masque> <sortie>`, où la sortie est une interface ou l'adresse du saut suivant (next hop). Elle apparaît avec le code `S`. Exemples du cours :
- `ip route 10.0.1.0 255.255.255.0 gigabitEthernet 0/0`
- `ip route 10.0.1.0 255.255.255.0 203.0.113.2` (affichée `[1/0] via 203.0.113.2`)
- suppression : `no ip route ...`

**Route par défaut** : utilisée quand aucune route précise n'existe, fréquente en bordure vers Internet. Réseau `0.0.0.0/0` : `ip route 0.0.0.0 0.0.0.0 <next hop>`.

> [!warning] Écart dans le cours
> Le tableau des réseaux connectés de [[Chp2 - Static Routing]] écrit « R3 » pour une ligne qui concerne R2.

Liens : [[Routage dynamique]], [[CLI Cisco IOS]]

Résumés : [[Chp2 - Static Routing (résumé)]], [[Chp3 - Dynamic Routing (résumé)]]
