---
type: concept
tags: [year2, year4]
aliases: [chemin élémentaire, sous-chemin, longueur d'un chemin, chemin simple, elementary path, simple path]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-12
---

**Algo** : dans un graphe orienté $G=(S,A)$, un chemin de longueur $k$ est une suite de sommets $(u_0,\dots,u_k)$ reliés par des arcs ; il est **élémentaire** si ses sommets sont tous distincts. Exemples : $\langle 1,4,2,5\rangle$ est élémentaire, $\langle 3,6,6,6\rangle$ ne l'est pas. Un **sous-chemin** est une sous-suite contiguë d'un chemin.

**graph theory** : suite de sommets $v_1, \ldots, v_k$ avec un arc de $v_i$ vers $v_{i+1}$ pour tout $i < k$ [[Erreurs du cours#^e-chemin-graphe|✎]] ; **élémentaire** s'il ne répète pas de sommet, **simple** s'il ne répète pas d'arc. Un [[Circuit (graphe)|circuit]] est un chemin fermé (il commence et finit au même sommet).

**graph theory, suppléments** : dans un graphe pondéré, [[4 - bellman ford]] définit la longueur d'un chemin comme la somme des poids de ses arcs, $\sum_{i=1}^{k-1} w(u_i, u_{i+1})$ (et non plus le nombre d'arcs) ; un chemin élémentaire a au plus $n$ sommets, donc au plus $n - 1$ arcs. Voir [[Plus court chemin]].

Notion parente : [[Graphe orienté]]. Voir aussi : [[Circuit (graphe)]], [[Cycle (graphe)]], [[Chaîne (graphe)]], [[Composante fortement connexe]].

Résumés : [[3 - Arbres]], [[4 - oriented graphs]], [[4 - bellman ford]], [[4 - dijkstra]]
