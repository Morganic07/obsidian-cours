---
type: concept
tags: [year2, year4]
aliases: [chemin élémentaire, sous-chemin, longueur d'un chemin, chemin simple, elementary path, simple path]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-07
---

**Algo** : dans un graphe orienté $G=(S,A)$, un chemin de longueur $k$ est une suite de sommets $(u_0,\dots,u_k)$ reliés par des arcs ; il est **élémentaire** si ses sommets sont tous distincts. Exemples : $\langle 1,4,2,5\rangle$ est élémentaire, $\langle 3,6,6,6\rangle$ ne l'est pas. Un **sous-chemin** est une sous-suite contiguë d'un chemin.

**graph theory** : suite de sommets $v_1, \ldots, v_k$ avec un arc entre $v_i$ et $v_{i+1}$ pour tout $i < k$ ; **élémentaire** s'il ne répète pas de sommet, **simple** s'il ne répète pas d'arc. Un [[Circuit (graphe)|circuit]] est un chemin fermé (il commence et finit au même sommet).

Notion parente : [[Graphe orienté]]. Voir aussi : [[Circuit (graphe)]], [[Cycle (graphe)]], [[Chaîne (graphe)]], [[Composante fortement connexe]].

## Erreurs du cours

- [[4 - oriented graphs|chp4 - oriented graphs]] écrit « there is an arc connecting $v_i$ and $v_{i+1}$ » ; il faut « an arc from $v_i$ to $v_{i+1}$ » ($v_i \to v_{i+1}$) : dans un graphe orienté, le sens de l'arc compte. Imprécision plus qu'erreur.

Résumés : [[3 - Arbres]], [[4 - oriented graphs]]
