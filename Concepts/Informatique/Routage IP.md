---
type: concept
tags: [year3, year4]
aliases: [IP routing, TTL, Time To Live]
sources: ["[[Raw/Year 3/Computer Network/Chp2 : Static Routing.docx|Chp2 - Static Routing]]"]
maj: 2026-11-12
---

**Définition** (d'après [[2 - Static Routing]]) : processus qui achemine des paquets IP d'un réseau source vers un réseau de destination, à travers des routeurs interconnectés. Le [[Routeur]] choisit le chemin d'après sa table de routage.

Il apprend seul les réseaux directement connectés ; les réseaux distants demandent des routes explicites, statiques (configurées à la main) ou dynamiques (apprises par un protocole).

## Traitement d'un paquet par le routeur (complément, hors du cours)

1. Le routeur lit l'**adresse IP de destination** du paquet.
2. Il cherche dans sa table de routage les routes dont le réseau contient cette adresse, et retient celle au **préfixe le plus long** ([[Plus longue correspondance de préfixe|plus longue correspondance de préfixe]], *longest prefix match*). Pour la destination `10.0.1.5`, une route `10.0.1.0/24` l'emporte sur `10.0.0.0/8`, et toutes deux sur la route par défaut `0.0.0.0/0`.
3. Il décrémente le **TTL** (*Time To Live*) du paquet ; un paquet dont le TTL atteint 0 est détruit, ce qui empêche un paquet de tourner indéfiniment dans une boucle de routage.
4. Il transmet le paquet par l'interface de sortie de la route, vers le saut suivant ou directement vers l'hôte si le réseau est connecté.
5. Sans route correspondante ni route par défaut, il détruit le paquet et renvoie en général à l'émetteur un message [[ICMP]] « destination injoignable » (*destination unreachable*).

Quand plusieurs sources (statique, OSPF, RIP…) proposent le même préfixe, le routeur choisit d'après la [[Distance administrative]].

Voir aussi : [[Routage statique]], [[Routage dynamique]], [[Distance administrative]], [[Adresse MAC]], [[Commutation de paquets]], [[Suite des protocoles Internet]].

En Graph theory (année 4), [[4 - bellman ford]] modélise le réseau par un graphe (routeurs = sommets, lignes de communications = arcs, délais = longueurs) : déterminer le meilleur chemin pour router les messages est un problème de [[Plus court chemin|plus court chemin]].

Résumés : [[2 - Static Routing]], [[4 - bellman ford]]
