---
type: concept
tags: [year4]
aliases: [strongly connected component, SCC]
matieres: [graph theory]
sources: ["[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-06
---

Dans un graphe orienté, sous-graphe maximal où, pour toute paire de sommets $u, v$, il existe un [[Chemin (graphe)|chemin]] de $u$ à $v$ et un chemin de $v$ à $u$.

**Algorithme 1 du cours** : avec $D(v)$ les descendants et $A(v)$ les ancêtres de $v$, la composante fortement connexe de $v$ est $\{v\} \cup (A(v) \cap D(v))$. L'[[Algorithme de Tarjan]] est cité comme alternative en $O(V + E)$.

Exemple à huit sommets : $\{B, C, E, F, G\}$, $\{A\}$, $\{D\}$, $\{H\}$.

Notion parente : [[Graphe orienté]]. Voir aussi : [[Algorithme de Tarjan]], [[Graphe connexe]], [[Chemin (graphe)]].

Résumés : [[4 - oriented graphs]]
