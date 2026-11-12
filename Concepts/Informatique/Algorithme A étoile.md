---
type: concept
tags: [year4]
aliases: [A*, A star, algorithme A*, A* search, A* search algorithm]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : algorithme de recherche d'un [[Plus court chemin|plus court chemin]] vers **une** cible, publié en 1968 par Peter Hart, Nils Nilsson et Bertram Raphael. Il procède comme l'[[Algorithme de Dijkstra|algorithme de Dijkstra]], mais choisit à chaque étape le sommet $v$ qui minimise $d(v) + h(v)$, où $d(v)$ est la distance déjà parcourue depuis la source et $h(v)$ une [[Heuristique (algorithmique)|heuristique]] estimant la distance restante jusqu'à la cible (par exemple la [[Distance|distance]] à vol d'oiseau sur une carte). Si $h$ est admissible, c'est-à-dire ne surestime jamais la distance réelle, le chemin trouvé est optimal ; avec $h = 0$, on retrouve exactement Dijkstra. Une bonne heuristique oriente la recherche vers la cible et réduit fortement le nombre de sommets explorés : A* est très utilisé en [[Jeu vidéo|jeu vidéo]] et en navigation.

## Dans le cours

Pas nommé : cité en complément dans [[4 - dijkstra]] (Graph theory), comme variante de Dijkstra.

Résumés : [[4 - dijkstra]]
