---
type: concept
tags: [year4]
aliases: [DFS, depth first search]
matieres: [graph theory]
sources: ["[[4 - oriented graphs (résumé)|chp4 - oriented graphs]]"]
maj: 2026-11-06
---

Parcours récursif d'un graphe : marquer le sommet, l'afficher, puis appeler le parcours sur chaque fils non visité. Depuis le sommet 0, l'exemple à sept sommets du cours peut donner 0, 2, 1, 5, 4. Complexité $O(|V| + |E|)$ : chaque sommet et chaque arête sont traités une fois.

Pour le parcours en profondeur d'un arbre, voir [[Arbre binaire]].

Notion parente : [[Graphe orienté]]. Voir aussi : [[Parcours en largeur]], [[Récursivité]].

## À vérifier

- Le résumé précise que $O(|V|+|E|)$ vaut avec des listes d'adjacence, et $O(|V|^2)$ avec une matrice : complément du résumé, absent du cours.
- Le cours écrit « DSF » et « BSF » (coquilles pour DFS et BFS).

Résumés : [[4 - oriented graphs (résumé)]]
