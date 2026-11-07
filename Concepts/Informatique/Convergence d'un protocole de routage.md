---
type: concept
tags: [year3]
aliases: [convergence lente, slow convergence]
matieres: [Computer Network]
sources: ["[[Chp3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : un réseau a convergé quand tous ses [[Routeur|routeurs]] disposent d'une vision cohérente et à jour de la topologie, c'est-à-dire que leurs tables de routage ne changent plus. Le temps de convergence est la durée nécessaire pour retrouver cet état après un changement (lien coupé, routeur ajouté) ; pendant ce temps, des paquets peuvent être perdus ou pris dans des [[Boucle de routage|boucles de routage]]. Les protocoles à vecteur de distance comme RIP convergent lentement, les protocoles à état de liens comme [[OSPF]] beaucoup plus vite.

## Dans le cours

Nommée dans [[Chp3 - Dynamic Routing (résumé)|Chp3 - Dynamic Routing]] sans définition : le cours dit que les IGP sont optimisés pour la vitesse et la convergence au sein d'une organisation, et cite la convergence lente parmi les limites de RIP, avec les [[Boucle de routage|boucles de routage]].

Notion parente : [[Routage dynamique]].

Résumés : [[Chp3 - Dynamic Routing (résumé)]]
