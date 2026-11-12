---
type: concept
tags: [year4]
aliases: [principe d'optimalité, principle of optimality, équation de Bellman, Bellman equation, sous-structure optimale, optimal substructure]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : énoncé par Richard Bellman dans les années 1950, ce principe dit qu'une solution optimale d'un problème se compose de solutions optimales de ses sous-problèmes ; on parle aussi de **sous-structure optimale**. Pour les [[Plus court chemin|plus courts chemins]] : tout sous-chemin d'un plus court chemin est lui-même un plus court chemin (sinon on le remplacerait par un plus court et on raccourcirait le tout). C'est la condition qui permet la [[Programmation dynamique|programmation dynamique]] : on écrit la valeur optimale par une [[Récurrence|récurrence]] sur des sous-problèmes plus petits (l'« équation de Bellman »), qu'on résout du plus petit au plus grand en mémorisant les résultats. Il fonde aussi les [[Algorithme glouton|algorithmes gloutons]] corrects, comme l'[[Algorithme de Dijkstra|algorithme de Dijkstra]], et l'existence d'un [[Arbre des plus courts chemins|arbre des plus courts chemins]].

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : utilisé sans être nommé, pour justifier la récurrence $OPT(i, v) = \min\{OPT(i-1, v),\ \min_u (OPT(i-1, u) + w(u, v))\}$ : un chemin optimal de $i$ arcs se termine par un arc $(u, v)$ précédé d'un chemin optimal de $s$ à $u$.

Voir aussi : [[Algorithme de Bellman-Ford]].

Résumés : [[4 - bellman ford]]
