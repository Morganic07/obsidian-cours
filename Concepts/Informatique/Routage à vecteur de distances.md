---
type: concept
tags: [year3, year4]
aliases: [vecteur de distance, vecteur de distances, routage à vecteur de distance, distance vector, distance-vector, distance-vector routing, protocole à vecteur de distance]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : famille de protocoles de [[Routage dynamique|routage dynamique]] dans laquelle chaque [[Routeur|routeur]] ne connaît que ses voisins directs et les distances qu'ils lui annoncent. Il envoie périodiquement à ses voisins son « vecteur » de distances (une distance par réseau destination) et calcule, pour chaque réseau $N$,
$$d(N) = \min_{V \text{ voisin}} \big(d_V(N) + c(V)\big),$$
où $d_V(N)$ est la distance annoncée par le voisin $V$ et $c(V)$ le coût du lien vers lui ; le voisin qui réalise le minimum devient le prochain saut dans sa [[Routage statique|table de routage]]. C'est l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] exécuté de façon répartie et [[Communication asynchrone|asynchrone]]. Exemples : RIP (coût de 1 par saut, infini à 16), EIGRP. Point faible : le [[Comptage à l'infini|comptage à l'infini]], source de [[Boucle de routage|boucles de routage]] et de [[Convergence d'un protocole de routage|convergence]] lente. L'autre grande famille est le [[Routage à état de liens|routage à état de liens]].

## Dans le cours

- [[3 - Dynamic Routing]] (Computer Network, année 3) : RIP, protocole à vecteur de distance, et son mécanisme $d(N) = \min_V \big(d_V(N) + 1\big)$.
- [[4 - bellman ford]] (Graph theory, année 4) : le « fonctionnement local » de Bellman-Ford, où chaque nœud n'a besoin que des marques de ses voisins, puis les versions R1 et asynchrone, où chaque nœud dont la distance change avertit ses voisins.

Voir aussi : [[EIGRP]], [[Informatique distribuée]].

Résumés : [[3 - Dynamic Routing]], [[4 - bellman ford]]
