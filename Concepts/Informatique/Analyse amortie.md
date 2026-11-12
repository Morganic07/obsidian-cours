---
type: concept
tags: [year4]
aliases: [coût amorti, amortized analysis]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : méthode d'analyse de la [[Complexité algorithmique|complexité]] qui évalue le coût moyen d'une opération sur une suite d'opérations dans le pire des cas, et non le coût de chaque opération isolée. Une opération ponctuellement chère est ainsi « payée » par les nombreuses opérations bon marché qui l'entourent. Exemple classique : l'ajout dans un tableau dynamique qui double sa capacité quand il est plein coûte parfois $O(n)$, mais $O(1)$ en coût amorti. Les méthodes usuelles sont l'agrégat, la méthode comptable et la méthode du potentiel.

## Dans le cours

[[4 - dijkstra]] : les coûts du [[Tas de Fibonacci|tas de Fibonacci]], qui donnent à l'[[Algorithme de Dijkstra]] sa meilleure complexité, sont des coûts amortis (complément).

Résumés : [[4 - dijkstra]]
