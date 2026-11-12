---
type: concept
tags: [year3, year4]
aliases: [dynamic routing, protocole de routage, protocoles de routage, RIP, RIPv2, Routing Information Protocol, IGP, EGP, hop count, nombre de sauts, RIPv1, router rip, default-information originate]
matieres: [Computer Network]
sources: ["[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]"]
maj: 2026-11-12
---

En routage dynamique, les routeurs apprennent automatiquement les chemins en s'échangeant leurs informations par des protocoles de routage. Il s'adapte aux pannes et aux nouveaux réseaux et réduit la configuration manuelle des grands réseaux.

**Types** : IGP à l'intérieur d'un [[Système autonome]] (RIP, [[EIGRP]], [[OSPF]]), EGP entre systèmes autonomes ([[BGP]]).

**RIP** : protocole à [[Routage à vecteur de distances|vecteur de distance]], métrique en nombre de sauts (hop count), mises à jour toutes les 30 s, 15 sauts au maximum (16 = inatteignable). RIPv1 est classful, RIPv2 est classless et gère le [[VLSM]] (voir [[Routage classful et classless]]). Simple et répandu, mais convergence lente et [[Boucle de routage|boucles]] possibles.

**Commandes** : `router rip`, `version 2`, `no auto-summary` (désactive le [[Résumé automatique de routes]]), `network <réseau>`, `default-information originate`. Contrôle : `show ip protocols`, `show ip rip database`, `show ip route rip`. `no router rip` supprime la configuration.

Notion parente : [[Routage IP]]. Voir aussi : [[Routage statique]], [[CLI Cisco IOS]], [[Système autonome]], [[OSPF]], [[EIGRP]], [[BGP]], [[VLSM]], [[Routage classful et classless]], [[Résumé automatique de routes]], [[Boucle de routage]], [[Routage à vecteur de distances]], [[Routage à état de liens]], [[Comptage à l'infini]]

En Graph theory (année 4), [[4 - bellman ford]] présente le calcul des meilleurs chemins de routage comme un problème de plus court chemin (routeurs = sommets, lignes = arcs, délais = longueurs) et oppose le fonctionnement global de Dijkstra au fonctionnement local de Bellman-Ford.

Résumé : [[3 - Dynamic Routing]], [[4 - bellman ford]]
