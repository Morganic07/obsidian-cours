---
type: concept
tags: [year4]
aliases: [heuristique admissible, fonction heuristique, heuristic function]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en algorithmique, une heuristique est une règle ou une fonction d'estimation qui guide la recherche d'une solution sans garantir, en général, qu'elle soit optimale ; elle sert quand une [[Recherche exhaustive|recherche exhaustive]] serait trop coûteuse. Dans la recherche de chemin, c'est une fonction $h(v)$ qui estime la distance restante d'un sommet $v$ à la cible, comme la distance à vol d'oiseau. Elle est dite **admissible** si elle ne surestime jamais la vraie distance : l'[[Algorithme A étoile|algorithme A*]] trouve alors un [[Plus court chemin|plus court chemin]]. Un [[Algorithme glouton|algorithme glouton]] appliqué à un problème difficile, comme le [[Problème du voyageur de commerce|problème du voyageur de commerce]], est un autre exemple d'heuristique.

## Dans le cours

Pas nommée : citée en complément dans [[4 - dijkstra]] (Graph theory), à propos de l'algorithme A*.

Voir aussi : [[Évaluation experte]] (l'« évaluation heuristique » en design d'interface, autre sens du mot).

Résumés : [[4 - dijkstra]]
