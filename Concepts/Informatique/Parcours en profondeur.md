---
type: concept
tags: [year4]
aliases: [DFS, depth first search]
matieres: [graph theory]
sources: ["[[4 - oriented graphs|chp4 - oriented graphs]]", "[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

Parcours récursif d'un graphe : marquer le sommet, l'afficher, puis appeler le parcours sur chaque fils non visité. Depuis le sommet 0, l'exemple à sept sommets du cours peut donner 0, 2, 1, 5, 4. Complexité $O(|V| + |E|)$ : chaque sommet et chaque arête sont traités une fois.

Pour le parcours en profondeur d'un arbre, voir [[Arbre binaire]].

## Compléments (hors du cours)

- **Principe** : le parcours s'enfonce le plus loin possible le long d'un chemin, et ne revient en arrière (*backtracking*) que lorsque le sommet courant n'a plus de successeur non visité.
- **Version itérative** : la récursivité peut être remplacée par une [[Pile et file|pile]] explicite : on empile le sommet de départ, puis, tant que la pile n'est pas vide, on dépile un sommet, on le marque s'il ne l'est pas et on empile ses successeurs non visités. L'ordre de visite peut différer légèrement de la version récursive selon l'ordre d'empilement.
- **Complexité selon la représentation** : la borne $O(|V| + |E|)$ suppose des [[Liste d'adjacence|listes d'adjacence]] ; avec une [[Matrice d'adjacence|matrice d'adjacence]], trouver les successeurs d'un sommet coûte $O(|V|)$, d'où $O(|V|^2)$ au total.
- **Usages** :
  - *détection de circuit* dans un [[Graphe orienté|graphe orienté]] : il existe un [[Circuit (graphe)|circuit]] si et seulement si le parcours rencontre un arc vers un sommet dont l'exploration n'est pas encore finie (arc « arrière ») ;
  - *tri topologique* d'un graphe orienté sans circuit : ranger les sommets par dates de fin d'exploration décroissantes ;
  - *[[Composante fortement connexe|composantes fortement connexes]]* : [[Algorithme de Tarjan]] (un seul parcours) ou algorithme de Kosaraju (un parcours sur le graphe, puis un second sur le graphe transposé, par dates de fin décroissantes).

Notion parente : [[Graphe orienté]]. Voir aussi : [[Parcours en largeur]], [[Récursivité]], [[Liste d'adjacence]], [[Algorithme de Tarjan]].

Résumés : [[4 - oriented graphs]]
