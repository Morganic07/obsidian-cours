---
type: concept
tags: [year3, year4]
aliases: [routing loop, routing loops, boucles de routage]
sources: ["[[3 - Dynamic Routing|Chp3 - Dynamic Routing]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une boucle de routage est une situation où des paquets circulent indéfiniment entre plusieurs [[Routeur|routeurs]] sans atteindre leur destination, parce que leurs tables de routage se renvoient mutuellement le trafic. Elle apparaît typiquement avec les protocoles à vecteur de distance comme RIP, quand une information de route obsolète se propage avant que le réseau ait convergé. Le champ TTL de l'en-tête IP limite les dégâts en détruisant le paquet au bout d'un certain nombre de sauts ; RIP s'en protège aussi par le maximum de 15 sauts, le *split horizon* et le *route poisoning*.

## Dans le cours

Nommée dans [[3 - Dynamic Routing|Chp3 - Dynamic Routing]] sans définition, parmi les limites de RIP (« susceptible to routing loops »), avec la [[Convergence d'un protocole de routage|convergence lente]] et le maximum de 15 sauts.

En complément de [[4 - bellman ford]] (Graph theory), le [[Comptage à l'infini|comptage à l'infini]] du [[Routage à vecteur de distances|routage à vecteur de distances]] est donné comme cause de boucles de routage.

Notion parente : [[Routage dynamique]].

Résumés : [[3 - Dynamic Routing]], [[4 - bellman ford]]
