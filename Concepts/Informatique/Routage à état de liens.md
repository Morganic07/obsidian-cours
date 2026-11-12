---
type: concept
tags: [year3, year4]
aliases: [état de liens, link-state, link state, link-state routing, protocole à état de liens, LSA, link-state advertisement]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : famille de protocoles de [[Routage dynamique|routage dynamique]] dans laquelle chaque [[Routeur|routeur]] diffuse à tous les routeurs de sa zone l'état de ses liens (voisins et coûts), dans des annonces d'état de liens (LSA). Chaque routeur dispose ainsi de la carte complète de la zone, un [[Graphe pondéré|graphe pondéré]], et y lance l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] (dit SPF, *Shortest Path First*) en se prenant pour source ; l'[[Arbre des plus courts chemins|arbre des plus courts chemins]] obtenu donne le prochain saut vers chaque destination. Exemples : [[OSPF]] et IS-IS. Ces protocoles convergent plus vite que le [[Routage à vecteur de distances|routage à vecteur de distances]] et sans [[Comptage à l'infini|comptage à l'infini]], au prix de plus de mémoire et de calcul.

## Dans le cours

- [[3 - Dynamic Routing]] (Computer Network, année 3) : famille présentée en complément, avec OSPF.
- [[4 - bellman ford]] (Graph theory, année 4) : le « fonctionnement global » de Dijkstra, qui choisit le sommet le plus proche parmi tous les sommets, donc a besoin de tout le graphe.
- [[4 - dijkstra]] (Graph theory) : application de Dijkstra au routage, en complément.

Voir aussi : [[Convergence d'un protocole de routage]].

Résumés : [[3 - Dynamic Routing]], [[4 - bellman ford]], [[4 - dijkstra]]
