---
type: concept
tags: [year4]
aliases: [handshaking lemma, formule des degrés, degree sum formula]
sources: ["[[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : dans tout graphe non orienté $G = (V, E)$, la somme des [[Degré d'un sommet|degrés]] des sommets vaut deux fois le nombre d'arêtes :

$$\sum_{v \in V} d(v) = 2\,\text{card}(E)$$

une boucle comptant 2 dans le degré de son sommet.

**Preuve** : chaque arête $\{u, v\}$ apporte 1 au degré de $u$ et 1 au degré de $v$ (ou 2 au même sommet pour une boucle) ; en sommant les degrés, chaque arête est donc comptée exactement deux fois.

**Corollaire** : le nombre de sommets de degré impair est pair. En effet, la somme des degrés est paire, et la somme des degrés pairs l'est aussi, donc la somme des degrés impairs est paire, ce qui demande un nombre pair de termes impairs. Le nom vient de l'image d'une réunion : le nombre total de mains serrées est pair, et le nombre de personnes ayant serré un nombre impair de mains est pair.

**Graphe orienté** : chaque arc a une origine et une extrémité, d'où $\sum_v d^+(v) = \sum_v d^-(v) = |A|$, et $\sum_v \big(d^+(v) + d^-(v)\big) = 2|A|$.

## Dans le cours

Le cours ne nomme pas le lemme. Il en énonce le cas particulier des [[Graphe régulier|graphes réguliers]] : si $G$ est $k$-régulier, alors $k \cdot \text{card}(V) = 2 \cdot \text{card}(E)$ (voir [[1 - Undirected graph]]). Conséquence (complément) : un graphe $k$-régulier avec $k$ impair a nécessairement un nombre pair de sommets ; il n'existe par exemple aucun graphe 3-régulier à 7 sommets.

Exemple (complément) : le cube est 3-régulier, a 8 sommets et 12 arêtes : $3 \times 8 = 2 \times 12$. Le [[Graphe complet|graphe complet]] $K_n$, $(n-1)$-régulier, a $\frac{n(n-1)}{2}$ arêtes.

En Python, avec la représentation du TP en [[Liste d'adjacence|liste d'adjacence]] (dictionnaire), le nombre d'arêtes d'un graphe simple se déduit du lemme (complément) :

```python
nb_aretes = sum(len(v) for v in dic.values()) // 2
```

Voir aussi : [[Degré d'un sommet]], [[Graphe régulier]], [[Graphe eulérien]], [[Graphe non orienté]], [[Graphe orienté]].

Résumés : [[1 - Undirected graph]]
