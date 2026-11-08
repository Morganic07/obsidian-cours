---
type: concept
tags: [year4]
aliases: [topological sort, topological sorting, ordre topologique, DAG, directed acyclic graph, graphe orienté sans circuit]
sources: ["[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : dans un [[Graphe orienté|graphe orienté]] $G = (V, E)$, un tri topologique est un ordre total des sommets tel que tout arc $u \to v$ va d'un sommet $u$ à un sommet $v$ placé après lui.

**Existence** : un graphe orienté admet un tri topologique si et seulement s'il est **sans [[Circuit (graphe)|circuit]]** (*DAG*, *directed acyclic graph*). Un circuit $v_1 \to \dots \to v_k \to v_1$ exigerait de placer $v_1$ avant lui-même.

**Algorithmes**, tous deux en $O(|V| + |E|)$ :

- **Kahn** : on calcule le degré entrant de chaque sommet ; on retire une à une les **sources** (degré entrant nul), on les place dans l'ordre et on diminue le degré entrant de leurs successeurs, qui deviennent sources à leur tour. Si un circuit existe, l'algorithme s'arrête avant d'avoir placé tous les sommets : c'est aussi un test d'absence de circuit.
- **Par [[Parcours en profondeur|parcours en profondeur]]** : on range les sommets par **date de fin décroissante** (un sommet est terminé après tous ses descendants, il passe donc avant eux).

Un graphe peut avoir plusieurs tris topologiques ; il n'y en a qu'un si et seulement si le graphe contient un [[Chemin (graphe)|chemin]] passant par tous les sommets.

**Usages** : ordonnancement de tâches dépendantes, prérequis de cours, ordre de compilation de modules, installation de paquets avec leurs dépendances.

**Lien avec les SCC** : le graphe réduit obtenu en contractant chaque [[Composante fortement connexe|composante fortement connexe]] en un sommet est toujours un DAG. Sur l'exemple à 8 sommets du cours, un tri topologique du graphe réduit est $\{A\}, \{D\}, \{H\}, \{B, C, E, F, G\}$.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[4 - oriented graphs]], à propos du graphe réduit des composantes fortement connexes et des usages du parcours en profondeur.

Voir aussi : [[Graphe orienté]], [[Cycle (graphe)]], [[Circuit (graphe)]], [[Parcours en profondeur]], [[Composante fortement connexe]], [[Algorithme de Tarjan]].

Résumés : [[4 - oriented graphs]]
