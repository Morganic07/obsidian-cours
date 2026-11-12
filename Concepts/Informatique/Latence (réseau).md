---
type: concept
tags: [year4]
aliases: [latence réseau, network latency, délai de transmission, délai de propagation, délai réseau]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : temps que met une donnée pour aller d'un point à un autre d'un [[Réseau|réseau]]. Il additionne le délai de transmission (mettre les bits sur la ligne, la taille du paquet divisée par le [[Débit binaire|débit]]), le délai de propagation (distance divisée par la vitesse du signal, environ 200 000 km/s dans une fibre optique, soit 5 ms pour 1 000 km), le temps de traitement dans chaque [[Routeur|routeur]] et l'attente dans ses files. On le mesure souvent par le temps aller-retour (RTT), par exemple avec la [[Commande ping|commande ping]]. Une latence se distingue du débit : un lien peut avoir un grand débit et une forte latence (liaison par [[Satellite de télécommunications|satellite]] géostationnaire, environ 0,5 s aller-retour).

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : dans la correspondance entre graphe et réseau de communications, les longueurs des arcs sont des « délais » ; le plus court chemin est alors le chemin le plus rapide.

Résumés : [[4 - bellman ford]]
