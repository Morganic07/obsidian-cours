---
type: concept
tags: [year3]
aliases: [routing loop, routing loops, boucles de routage]
sources: ["[[Chp3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une boucle de routage est une situation où des paquets circulent indéfiniment entre plusieurs [[Routeur|routeurs]] sans atteindre leur destination, parce que leurs tables de routage se renvoient mutuellement le trafic. Elle apparaît typiquement avec les protocoles à vecteur de distance comme RIP, quand une information de route obsolète se propage avant que le réseau ait convergé. Le champ TTL de l'en-tête IP limite les dégâts en détruisant le paquet au bout d'un certain nombre de sauts ; RIP s'en protège aussi par le maximum de 15 sauts, le *split horizon* et le *route poisoning*.

## Dans le cours

Nommée dans [[Chp3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]] sans définition, parmi les limites de RIP (« susceptible to routing loops »), avec la [[Convergence d'un protocole de routage|convergence lente]] et le maximum de 15 sauts.

Notion parente : [[Routage dynamique]].

Résumés : [[Chp3 - Dynamic Routing (résumé)]]
