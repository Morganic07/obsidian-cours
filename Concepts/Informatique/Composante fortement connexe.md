---
type: concept
tags: [year4]
aliases: [strongly connected component, SCC]
matieres: [graph theory]
sources: ["[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

Dans un graphe orienté, sous-graphe maximal où, pour toute paire de sommets $u, v$, il existe un [[Chemin (graphe)|chemin]] de $u$ à $v$ et un chemin de $v$ à $u$.

**Algorithme 1 du cours** : avec $D(v)$ les descendants et $A(v)$ les ancêtres de $v$, la composante fortement connexe de $v$ est $\{v\} \cup (A(v) \cap D(v))$. L'[[Algorithme de Tarjan]] est cité comme alternative en $O(V + E)$.

Exemple à huit sommets : $\{B, C, E, F, G\}$, $\{A\}$, $\{D\}$, $\{H\}$.

## Compléments (hors du cours)

- **Partition** : la relation « $u$ et $v$ sont mutuellement accessibles » est une [[Relation d'équivalence|relation d'équivalence]] sur $V$ ; ses classes sont les SCC, qui forment donc une partition des sommets. Un graphe est **fortement connexe** s'il n'a qu'une seule SCC.
- **Graphe réduit** (condensation) : en contractant chaque SCC en un sommet, on obtient un graphe toujours **sans circuit** (un circuit entre deux SCC les fusionnerait), qui admet donc un [[Tri topologique|tri topologique]]. Sur l'exemple, avec $X = \{B, C, E, F, G\}$ : $\{A\} \to X$, $\{D\} \to X$, $\{D\} \to \{H\}$, $\{H\} \to X$.
- **Coût de l'algorithme 1** : $A(v)$ se calcule par un parcours depuis $v$ dans le **graphe transposé** $G^T$ (arcs inversés). Une SCC coûte deux parcours, $O(|V| + |E|)$ ; toutes les SCC, en recommençant depuis un sommet non classé, $O(|V| \cdot (|V| + |E|))$ au pire.
- **Exemple de l'algorithme 1** avec $v = B$ : $D(B) = \{B, C, E, F, G\}$ et $A(B) = \{A, B, C, D, E, F, G, H\}$, d'où la SCC $\{B\} \cup (A(B) \cap D(B)) = \{B, C, E, F, G\}$.
- L'**algorithme de Kosaraju** (deux DFS, sur $G$ puis sur $G^T$) obtient toutes les SCC en $O(V + E)$, comme Tarjan.

Notion parente : [[Graphe orienté]]. Voir aussi : [[Algorithme de Tarjan]], [[Graphe connexe]], [[Chemin (graphe)]], [[Tri topologique]], [[Relation d'équivalence]].

Résumés : [[4 - oriented graphs]]
