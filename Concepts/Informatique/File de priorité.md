---
type: concept
tags: [year4]
aliases: [files de priorité, file à priorités, priority queue, priority queues]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une **file de priorité** est un [[Type abstrait de données|type abstrait de données]] qui range des éléments munis d'une priorité (une clé) et offre trois opérations principales : insérer un élément, lire l'élément de plus haute priorité, l'extraire. Selon la convention, la plus haute priorité est la plus petite clé (file « min ») ou la plus grande (file « max »). Contrairement à une [[Pile et file|file]] ordinaire (FIFO), l'ordre de sortie dépend de la priorité, pas de l'ordre d'arrivée. Beaucoup d'usages ajoutent une opération de diminution de clé.

**Implémentations** :

| Structure | Insertion | Extraction du minimum |
|---|---|---|
| tableau ou liste non triés | $O(1)$ | $O(n)$ |
| liste triée | $O(n)$ | $O(1)$ |
| [[Tas binaire\|tas binaire]] | $O(\log n)$ | $O(\log n)$ |
| [[Arbre binaire de recherche\|ABR]] [[Arbre équilibré\|équilibré]] | $O(\log n)$ | $O(\log n)$ |

Le tas binaire est l'implémentation usuelle : `heapq` en Python, `std::priority_queue` dans la [[Bibliothèque standard du C++|bibliothèque standard du C++]], `PriorityQueue` en Java.

**Usages** : l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] (extraire le sommet non traité le plus proche), l'[[Algorithme de Prim|algorithme de Prim]], le [[Codage de Huffman|codage de Huffman]] (fusionner les deux arbres de plus faible fréquence), l'[[Ordonnancement des processus|ordonnancement des processus]] par priorité, la simulation à événements discrets, le tri par tas.

## Dans le cours

[[2 - tree revisions années précédentes]] ne la nomme pas ; ses compléments la citent parmi les usages des arbres, réalisée par un tas binaire.

Voir aussi : [[Tas binaire]], [[Pile et file]], [[Structure de données]], [[Complexité algorithmique]].

Résumés : [[2 - tree revisions années précédentes]]
