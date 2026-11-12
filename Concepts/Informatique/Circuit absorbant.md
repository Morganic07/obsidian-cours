---
type: concept
tags: [year4]
aliases: [circuit de longueur négative, circuits de longueur négative, circuit négatif, cycle négatif, cycle de poids négatif, negative cycle, negative-weight cycle]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - bellman ford]]) : [[Circuit (graphe)|circuit]] d'un [[Graphe pondéré|graphe pondéré]] orienté dont la longueur, somme des poids de ses arcs, est négative. En sa présence, il n'y a pas de [[Plus court chemin|plus court chemin]] vers les sommets qu'il permet d'atteindre.

**Compléments (hors du cours)** : chaque tour du circuit diminue la longueur du chemin, qu'on peut rendre aussi petite qu'on veut : on pose $\delta(s, v) = -\infty$ pour tout sommet $v$ accessible depuis un circuit absorbant lui-même accessible depuis $s$ ; les autres sommets gardent une distance finie. L'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] le détecte : si une $n$-ième passe de [[Relâchement d'un arc|relâchement]] fait encore baisser une distance, un tel circuit est accessible depuis la source. L'[[Algorithme de Floyd-Warshall|algorithme de Floyd-Warshall]] le révèle par une valeur négative sur la diagonale. Dans un graphe non orienté, une seule arête de poids négatif suffit à en former un (aller-retour).

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : « circuits de longueur négative » dans le tableau des cas ; leur absence garantit un plus court chemin élémentaire d'au plus $n - 1$ arcs.

Voir aussi : [[Cycle (graphe)]], [[Algorithme de Dijkstra]].

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
