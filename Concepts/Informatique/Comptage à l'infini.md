---
type: concept
tags: [year3, year4]
aliases: [count to infinity, count-to-infinity, problème du comptage à l'infini]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : défaut des protocoles de [[Routage à vecteur de distances|routage à vecteur de distances]], qui exécutent l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] de façon répartie. Quand un lien ou un réseau disparaît, deux routeurs peuvent continuer à se l'annoncer l'un à l'autre, chacun croyant que l'autre y mène, en augmentant la distance d'un cran à chaque échange : la distance « compte » lentement vers l'infini. Pendant ce temps, les paquets tournent dans une [[Boucle de routage|boucle de routage]] et la [[Convergence d'un protocole de routage|convergence]] est très lente. RIP le borne en fixant l'infini à 16 sauts et l'atténue par l'*horizon partagé* (*split horizon* : ne pas réannoncer une route au voisin par lequel on l'a apprise) et l'*empoisonnement en retour* (*poison reverse* : la lui réannoncer à distance infinie).

## Dans le cours

- Complément de [[4 - bellman ford]] (Graph theory), à propos de la version asynchrone de Bellman-Ford pour le routage.
- Déjà évoqué dans les compléments du concept [[Algorithme de Bellman-Ford]] et de [[3 - Dynamic Routing]] (Computer Network, année 3), sous le nom de comptage à l'infini.

Voir aussi : [[Routage dynamique]].

Résumés : [[3 - Dynamic Routing]], [[4 - bellman ford]]
