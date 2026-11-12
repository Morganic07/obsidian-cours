---
type: concept
tags: [year4]
aliases: [Floyd-Warshall, Floyd-Warshall algorithm, algorithme de Roy-Floyd-Warshall, algorithme de Floyd]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : algorithme qui calcule les longueurs des [[Plus court chemin|plus courts chemins]] entre **tous les couples** de sommets d'un [[Graphe pondéré|graphe pondéré]] orienté, poids négatifs admis, en l'absence de [[Circuit absorbant|circuit absorbant]]. Par [[Programmation dynamique|programmation dynamique]], $D_k[i][j]$ est la longueur minimale d'un chemin de $i$ à $j$ dont les sommets intermédiaires sont pris parmi $1, \ldots, k$ :
$$D_k[i][j] = \min\big(D_{k-1}[i][j],\ D_{k-1}[i][k] + D_{k-1}[k][j]\big),$$
en partant de la [[Matrice d'adjacence|matrice d'adjacence]] pondérée. Trois [[Boucle imbriquée|boucles imbriquées]] donnent une complexité $O(n^3)$ et un espace $O(n^2)$. Un coefficient diagonal négatif à la fin signale un circuit absorbant. Publié en 1962 par Robert Floyd et par Stephen Warshall (pour la fermeture transitive), après Bernard Roy (1959).

## Dans le cours

- [[4 - bellman ford]] (Graph theory) : cité pour les arcs de poids quelconques, « tous les plus courts chemins », comme exemple de programmation dynamique, sans être détaillé.

Voir aussi : [[Algorithme de Bellman-Ford]], [[Algorithme de Johnson]], [[Algorithme de Dijkstra]].

Résumés : [[4 - bellman ford]], [[4 - dijkstra]]
