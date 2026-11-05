---
type: concept
aliases: [dynamic routing, protocole de routage, protocoles de routage, RIP, RIPv2, Routing Information Protocol, IGP, EGP, vecteur de distance]
matieres: [Computer Network]
sources: ["[[Chp3 - Dynamic Routing]]"]
maj: 2026-11-05
---

En routage dynamique, les routeurs apprennent automatiquement les chemins en s'échangeant leurs informations par des protocoles de routage. Il s'adapte aux pannes et aux nouveaux réseaux et réduit la configuration manuelle des grands réseaux.

**Types** : IGP à l'intérieur d'un système autonome (RIP, EIGRP, OSPF), EGP entre systèmes autonomes (BGP).

**RIP** : protocole à vecteur de distance, métrique en nombre de sauts, mises à jour toutes les 30 s, 15 sauts au maximum (16 = inatteignable). RIPv1 est classful, RIPv2 est classless et gère le VLSM. Simple et répandu, mais convergence lente et boucles possibles.

**Commandes** : `router rip`, `version 2`, `no auto-summary`, `network <réseau>`, `default-information originate`. Contrôle : `show ip protocols`, `show ip rip database`, `show ip route rip`. `no router rip` supprime la configuration.

Liens : [[Routage statique]], [[CLI Cisco IOS]]

Résumé : [[Chp3 - Dynamic Routing (résumé)]]
