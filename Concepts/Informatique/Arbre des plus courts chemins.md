---
type: concept
tags: [year4]
aliases: [arborescence des plus courts chemins, shortest path tree, shortest-path tree, SPT]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - bellman ford]]) : à la fin de l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]], le graphe formé des arcs $(pred[v], v)$, où $pred[v]$ est le dernier sommet intermédiaire d'un plus court chemin de $s$ à $v$, est un [[Arbre (théorie des graphes)|arbre]] ; dans cet arbre, le chemin de $s$ à $v$ est un [[Plus court chemin|plus court chemin]] du graphe. [[4 - dijkstra]] l'appelle l'« arborescence » construite par l'[[Algorithme de Dijkstra|algorithme de Dijkstra]], formée des arcs (parent, sommet).

**Compléments (hors du cours)** : c'est une [[Arborescence (graphe)|arborescence]] de racine $s$ qui couvre les sommets accessibles depuis $s$ ; on lit un chemin à l'envers, en remontant les prédécesseurs de $v$ jusqu'à $s$. Elle existe grâce au [[Principe d'optimalité de Bellman|principe d'optimalité]] : le préfixe d'un plus court chemin est un plus court chemin. Elle diffère en général de l'[[Arbre couvrant minimal|arbre couvrant minimal]], qui minimise le poids total des arêtes et non la distance à une racine. En réseau, chaque routeur à état de liens ([[OSPF]]) calcule l'arbre dont il est la racine.

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : reconstruction des chemins par `pred`, exemple à 6 sommets.
- [[4 - dijkstra]] (Graph theory) : arborescence finale de l'exemple (étape 8).

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
