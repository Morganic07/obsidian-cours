---
type: concept
tags: [year1]
aliases: [voyageur de commerce, travelling salesman problem, TSP]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-08
---

Exemple d'AlgoID1 d'un problème difficile : aucun algorithme exact efficace n'est connu, mais des [[Algorithme d'approximation|algorithmes d'approximation]] donnent rapidement une solution. Sa modélisation est présentée comme facile.

**Énoncé et difficulté (complément, hors du cours)** : étant données $n$ villes et les distances entre chaque paire, trouver le circuit le plus court qui passe une fois par chaque ville et revient au départ. Avec des distances symétriques, on fixe la ville de départ et on identifie un circuit à son sens inverse : il y a $\frac{(n-1)!}{2}$ circuits distincts, soit $\frac{19!}{2} \approx 6 \times 10^{16}$ pour 20 villes. La [[Recherche exhaustive]] est donc hors de portée dès quelques dizaines de villes (complexité factorielle, voir [[Classe de complexité]]).

Le problème d'optimisation est NP-difficile, et sa version de décision (existe-t-il un circuit de longueur au plus $L$ ?) est NP-complète. Aucun algorithme exact en temps polynomial n'est connu ; en trouver un prouverait $P = NP$. En pratique on recourt à des heuristiques (plus proche voisin, améliorations locales 2-opt) ou à des [[Algorithme d'approximation|algorithmes d'approximation]] : quand les distances vérifient l'inégalité triangulaire, l'algorithme de Christofides garantit un circuit au plus 1,5 fois plus long que l'optimum.

Notion parente : [[Algorithme]]. Voir aussi : [[Algorithme d'approximation]], [[Modélisation d'un problème]], [[Recherche exhaustive]], [[Classe de complexité]].

Résumés : [[0 - diapo prof]]
