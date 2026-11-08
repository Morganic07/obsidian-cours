---
type: concept
tags: [year4]
aliases: [adjacency list, listes d'adjacence, liste des successeurs]
sources: ["[[Raw/Year 4/graph theory/Graph - Python.docx|Graph - Python]]", "[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : représentation d'un graphe qui associe à chaque sommet la liste de ses voisins (graphe non orienté) ou de ses successeurs (graphe orienté). En Python, c'est naturellement un [[Dictionnaire (Python)|dictionnaire]] dont les clés sont les sommets et les valeurs les listes de voisins :

```python
G = {0: [1, 2], 1: [0, 2], 2: [0, 1]}   # triangle non orienté
```

Pour un graphe non orienté, chaque arête $\{u, v\}$ apparaît deux fois : $v$ dans la liste de $u$, et $u$ dans celle de $v$ (d'où la somme des longueurs des listes égale à $2|E|$, voir [[Lemme des poignées de main]]). Pour un graphe orienté, l'arc $(u, v)$ n'apparaît qu'une fois, dans la liste de $u$, et la longueur de la liste de $u$ est son degré sortant $d^+(u)$.

**Comparaison avec la [[Matrice d'adjacence]]**, pour $n = |V|$ sommets et $m$ arêtes ou arcs :

| Opération | Liste d'adjacence | Matrice d'adjacence |
|---|---|---|
| Mémoire | $O(n + m)$ | $O(n^2)$ |
| Énumérer les voisins de $v$ | $O(d(v))$, directement | $O(n)$, parcours d'une ligne |
| Tester si $(u, v)$ existe | $O(d^+(u))$, parcours des voisins | $O(1)$ |
| Parcours complet du graphe | $O(n + m)$ | $O(n^2)$ |

La liste d'adjacence convient aux graphes creux (peu d'arêtes, $m \ll n^2$, cas des réseaux routiers ou sociaux), la matrice aux graphes denses. En remplaçant les listes par des ensembles Python (`set`, implémentés par [[Table de hachage|table de hachage]]), le test d'adjacence devient en temps constant en moyenne tout en gardant une mémoire en $O(n + m)$.

## Dans le cours

Le cours ne la nomme pas. C'est la représentation qu'utilise le TP Python, un dictionnaire de listes de voisins (voir [[0 - Graph - Python]]). Le chapitre 4 la sous-entend : la complexité $O(|V| + |E|)$ annoncée pour le [[Parcours en profondeur]] et le [[Parcours en largeur]] suppose une liste d'adjacence ; avec une matrice, ces parcours coûtent $O(|V|^2)$ (complément, voir [[4 - oriented graphs]]).

Voir aussi : [[Matrice d'adjacence]], [[Dictionnaire (Python)]], [[Table de hachage]], [[Parcours en largeur]], [[Parcours en profondeur]], [[Graphe orienté]], [[Complexité algorithmique]].

Résumés : [[0 - Graph - Python]], [[4 - oriented graphs]]
