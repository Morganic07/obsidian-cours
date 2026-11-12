---
type: concept
tags: [year3, year4]
aliases: [Bellman-Ford, Bellman-Ford algorithm, algorithme de Bellman-Ford-Moore]
sources: ["[[Raw/Year 3/Computer Network/Chp3 : Dynamic Routing.docx|Chp3 - Dynamic Routing]]", "[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - bellman ford]]) : algorithme de [[Programmation dynamique|programmation dynamique]] qui calcule, depuis un sommet source $s$, les longueurs des [[Plus court chemin|plus courts chemins]] constitués d'au plus $n - 1$ arcs, dans un graphe pondéré aux arcs de poids quelconques. Sous-problèmes : $OPT(i, v)$, longueur minimale d'un chemin de $s$ à $v$ d'au plus $i$ arcs, avec $OPT(i, v) = \min\{OPT(i-1, v),\ \min_{u} (OPT(i-1, u) + w(u, v))\}$ ; complexité $O(mn)$, espace $O(n)$ avec un tableau à une dimension ; un tableau `pred` donne l'[[Arbre des plus courts chemins|arbre des plus courts chemins]].

**Compléments (hors du cours)** : algorithme de calcul des plus courts chemins depuis une source $s$ dans un [[Graphe pondéré|graphe pondéré]] orienté $G = (V, E)$, qui accepte des poids négatifs, à condition qu'aucun circuit ne soit de poids total négatif (sinon le plus court chemin n'est pas défini).

**Principe** : on pose $d(s) = 0$ et $d(v) = +\infty$ pour tout autre sommet, puis on « relâche » toutes les arêtes, $|V| - 1$ fois :
$$d(v) \leftarrow \min\big(d(v),\ d(u) + w(u,v)\big) \quad \text{pour chaque arête } (u,v).$$
Après la $k$-ième passe, $d(v)$ est au plus la longueur du plus court [[Chemin (graphe)|chemin]] de $s$ à $v$ en au plus $k$ arêtes ; comme un plus court chemin sans circuit a au plus $|V| - 1$ arêtes, $|V| - 1$ passes suffisent. En gardant pour chaque sommet le prédécesseur qui a donné sa distance, on reconstruit les chemins.

**Complexité** : $O(|V| \cdot |E|)$, plus lente que l'[[Algorithme de Dijkstra|algorithme de Dijkstra]], qui ne gère en revanche que des poids positifs ou nuls.

**Détection des circuits négatifs** : si une $|V|$-ième passe améliore encore une distance, le graphe contient un circuit de poids négatif accessible depuis $s$.

**Version distribuée (routage à vecteur de distance)** : chaque routeur ne connaît que ses voisins et les distances qu'ils lui annoncent. Il calcule pour chaque réseau $N$
$$d(N) = \min_{V \text{ voisin}} \big(d_V(N) + c(V)\big),$$
où $d_V(N)$ est la distance annoncée par le voisin $V$ et $c(V)$ le coût du lien vers lui (1 saut pour RIP), et retient le voisin qui donne ce minimum comme saut suivant. Ce calcul, répété à chaque échange de tables, est la base des protocoles à vecteur de distance (RIP).

**Limite en réseau : le comptage à l'infini.** Quand un réseau disparaît, deux routeurs peuvent continuer à se l'annoncer l'un à l'autre en augmentant la distance d'un saut à chaque échange, et créer une [[Boucle de routage|boucle de routage]] qui dure. Parades de RIP : l'infini fixé à 16 sauts (un réseau à 16 sauts est injoignable), le *split horizon* (ne pas réannoncer une route au voisin par lequel on l'a apprise) et le *poison reverse* (la lui réannoncer à distance infinie).

## Dans le cours

Le cours de Computer Network ne le nomme pas. Il apparaît dans les compléments de [[3 - Dynamic Routing]], qui présente le mécanisme du vecteur de distance de RIP, $d(N) = \min_V \big(d_V(N) + 1\big)$, comme un Bellman-Ford exécuté de façon distribuée.

Dans [[4 - bellman ford]] (Graph theory, année 4), il est présenté en détail : plus courts chemins élémentaires, sous-problèmes $OPT(i, v)$ et récurrence, quatre versions du pseudo-code (tableau à deux dimensions, parcours des arcs, tableau à une dimension, avec prédécesseurs), exemple complet à 6 sommets, puis application au routage, avec les versions R1 (arrêt quand rien ne change) et asynchrone (nœuds actifs, voir [[Algorithme SPFA]]).

Voir aussi : [[Algorithme de Dijkstra]], [[Algorithme de Floyd-Warshall]], [[Algorithme de Johnson]], [[Circuit absorbant]], [[Relâchement d'un arc]], [[Routage à vecteur de distances]], [[Comptage à l'infini]], [[Routage dynamique]], [[Boucle de routage]], [[Convergence d'un protocole de routage]], [[Graphe pondéré]], [[Chemin (graphe)]], [[Circuit (graphe)]].

Résumés : [[3 - Dynamic Routing]], [[4 - bellman ford]], [[4 - dijkstra]]
