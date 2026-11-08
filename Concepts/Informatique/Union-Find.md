---
type: concept
tags:
  - year4
aliases:
  - union par rang
  - find_parent
  - disjoint-set
  - ensembles disjoints
  - compression de chemin
  - path compression
matieres:
  - graph theory
sources:
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : structure de données qui maintient une partition d'un ensemble d'éléments en groupes disjoints, avec deux opérations : `find` (trouver le représentant du groupe d'un élément) et `union` (fusionner deux groupes). Deux éléments sont dans le même groupe si et seulement s'ils ont le même représentant.

Structure utilisée dans l'implémentation de Kruskal du TP Python : `find_parent` cherche récursivement la racine d'un sommet (un sommet est racine si `parent[i] == i`), et `union` fusionne deux ensembles par rang. Une arête est rejetée si ses deux extrémités ont la même racine, car elle créerait un cycle.

**Représentation** : le tableau `parent` code une [[Forêt (graphe)|forêt]] ; chaque arbre est un groupe, et sa racine en est le représentant. `find_parent` remonte de parent en parent jusqu'à la racine ; `union` rattache la racine d'un arbre à celle de l'autre.

**Garantie de l'union par rang** : on rattache toujours l'arbre de rang le plus petit sous la racine de l'autre, et le rang n'augmente (de 1) que lorsque deux arbres de même rang fusionnent. Par récurrence, un arbre de rang $r$ contient au moins $2^r$ sommets ; sa hauteur est donc au plus $\log_2 n$, et `find_parent` s'exécute en $O(\log n)$ (une vingtaine d'appels au plus pour un million de sommets, car $2^{20} \approx 10^6$). Sans union par rang, une suite d'unions malheureuse peut produire une chaîne de hauteur $n - 1$ et un `find` en $O(n)$.

**Compression de chemin (complément, hors du cours)** : pendant la remontée, on rattache directement à la racine chaque sommet visité, ce qui aplatit l'arbre pour les appels suivants.

```python
def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]
```

Combinée à l'union par rang, elle donne un coût amorti par opération en $O(\alpha(n))$, où $\alpha$ est l'inverse de la fonction d'Ackermann (Tarjan, 1975) : $\alpha(n) \le 4$ pour toute valeur de $n$ réaliste, soit un coût quasi constant.

**Autres usages (complément, hors du cours)** : suivre les composantes connexes d'un graphe que l'on construit arête par arête (deux sommets sont reliés si et seulement s'ils ont la même racine) ; détecter un cycle dans un graphe non orienté ; regrouper des pixels voisins en traitement d'image.

Notion parente : [[Algorithme de Kruskal]]. Voir aussi : [[Récursivité]], [[Forêt (graphe)]], [[Graphe connexe]], [[Algorithme de Prim]], [[Complexité algorithmique]].

Résumés : [[0 - Graph - Python]]
