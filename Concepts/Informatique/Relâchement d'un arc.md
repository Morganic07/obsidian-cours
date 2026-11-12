---
type: concept
tags: [year4]
aliases: [relâchement, relaxation, relaxation d'un arc, edge relaxation, relâcher un arc]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : relâcher l'arc $(u, v)$ de poids $w(u, v)$, c'est tester si passer par $u$ améliore la meilleure longueur connue pour atteindre $v$ :
$$\text{si } d[v] > d[u] + w(u, v) \text{ alors } d[v] := d[u] + w(u, v),\ pred[v] := u.$$
C'est l'opération de base des algorithmes de [[Plus court chemin|plus court chemin]] : l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] relâche tous les arcs $n - 1$ fois, dans n'importe quel ordre ; l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] relâche une seule fois les arcs de chaque sommet, au moment où il le traite. Un relâchement ne fait jamais descendre $d[v]$ sous la vraie distance $\delta(s, v)$, puisque $d[v]$ reste la longueur d'un chemin réel. Le terme vient de l'image d'une contrainte $d[v] \le d[u] + w(u, v)$ qu'on « relâche » en la rendant vraie.

## Dans le cours

Le mot n'est pas employé, mais l'opération est au cœur des deux documents :
- [[4 - bellman ford]] : test `si d[i, v] > d[i − 1, u] + w(u, v) alors …` et mise à jour de `pred` ;
- [[4 - dijkstra]] : mise à jour du poids et du parent des voisins du sommet traité.

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
