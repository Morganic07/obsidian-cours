---
type: concept
tags:
  - year4
aliases:
  - union par rang
  - find_parent
matieres:
  - graph theory
sources:
  - "[[0 - Graph - Python (résumé)|Graph - Python]]"
maj: 2026-11-06
---

Structure utilisée dans l'implémentation de Kruskal du TP Python : `find_parent` cherche récursivement la racine d'un sommet (un sommet est racine si `parent[i] == i`), et `union` fusionne deux ensembles par rang. Une arête est rejetée si ses deux extrémités ont la même racine, car elle créerait un cycle.

Notion parente : [[Algorithme de Kruskal]]. Voir aussi : [[Récursivité]].

## À vérifier

- Le nom « Union-Find » n'est pas dans le cours, qui ne nomme que `find_parent`, `union` et l'union par rang.

Résumés : [[0 - Graph - Python (résumé)]]
