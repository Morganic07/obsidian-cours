---
type: concept
tags: [year4]
aliases: [Fibonacci heap]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : structure de données réalisant une [[File de priorité|file de priorité]], proposée en 1984 et formée d'une collection d'arbres en ordre de [[Tas binaire|tas]] dont la structure est réorganisée paresseusement. En coût [[Analyse amortie|amorti]], l'insertion, la lecture du minimum et la diminution de clé coûtent $O(1)$, et l'extraction du minimum $O(\log n)$. Ces bornes donnent à l'[[Algorithme de Dijkstra]] une [[Complexité algorithmique|complexité]] en $O(m + n \log n)$, contre $O((n + m) \log n)$ avec un tas binaire ; mais les constantes élevées font qu'on lui préfère souvent le tas binaire en pratique. Son nom vient de la [[Suite de Fibonacci|suite de Fibonacci]], qui intervient dans l'analyse de la taille des arbres.

## Dans le cours

[[4 - dijkstra]] : cité dans le tableau des complexités de l'algorithme selon la file de priorité utilisée (complément).

Voir aussi : [[Tas binaire]], [[File de priorité]].

Résumés : [[4 - dijkstra]]
