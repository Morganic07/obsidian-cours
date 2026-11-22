---
type: concept
tags: [year4]
aliases: [clique, nombre de clique, clique number, full sub-graph, sous-graphe complet]
matieres: [graph theory]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition (complément, hors du cours)** : une clique d'un [[Graphe non orienté|graphe non orienté]] est un ensemble de sommets deux à deux adjacents ; le [[Sous-graphe|sous-graphe]] qu'ils forment est un [[Graphe complet|graphe complet]] $K_p$. Le **nombre de clique** $\omega(G)$ est la taille de la plus grande clique. Comme tous les sommets d'une clique doivent avoir des couleurs différentes, $\omega(G) \leq \chi(G)$ ([[Nombre chromatique]]). Un triangle est une clique à 3 sommets. Chercher une clique de taille maximale est NP-difficile (voir [[Classes P et NP]]). Notion inverse : l'[[Ensemble stable (graphe)|ensemble stable]].

## Dans le cours

Le cours parle de « sous-graphe complet à $p$ sommets » (*full sub-graph*) dans la proposition du minorant : $\chi(G) \geq p$ ([[5 - colorier graph]]). Les cliques $\{A, E, F, H\}$ de l'exemple et $\{A, B, C\}$ de l'exercice 1 servent à calculer $\chi(G)$.

Résumés : [[5 - colorier graph]]
