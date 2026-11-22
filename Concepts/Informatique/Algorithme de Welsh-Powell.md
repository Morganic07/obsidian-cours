---
type: concept
tags: [year4]
aliases: [Welsh-Powell, Welsh et Powell, Welsh-Powell algorithm]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition** (d'après [[5 - colorier graph]]) : [[Algorithme glouton|algorithme glouton]] itératif de [[Coloration de graphe|coloration de graphe]] :
1. trier les sommets par [[Degré d'un sommet|degré]] décroissant dans une liste $V$ ;
2. ranger les couleurs dans une liste $C$ ;
3. colorier le premier sommet non colorié de $V$ avec la première couleur pas encore utilisée ;
4. parcourir le reste de $V$ et donner cette couleur à chaque sommet non colorié dont aucun voisin ne l'a déjà ;
5. répéter 3 et 4 jusqu'à ce que tous les sommets soient coloriés.

Publié par Dominic Welsh et Martin Powell en 1967 (*The Computer Journal*, 10(1)) pour construire des emplois du temps d'examens. La coloration obtenue est toujours propre, mais pas toujours optimale : c'est une [[Heuristique (algorithmique)|heuristique]], qui donne un majorant du [[Nombre chromatique|nombre chromatique]], à savoir $\chi(G) \leq \max_i \min(d_i + 1, i)$ pour des degrés triés $d_1 \geq \ldots \geq d_n$. Le résultat dépend de l'ordre entre sommets de même degré. Variante souvent meilleure : l'[[Algorithme DSATUR|algorithme DSATUR]]. [[Complément hors du cours|ⓘ]]

## Dans le cours

Chapitre 5 de Graph theory : description en cinq étapes, application à un graphe à 8 sommets (4 couleurs, ici optimales), et exercice où il utilise 4 couleurs alors que $\chi(G) = 3$ ([[5 - colorier graph]]).

Voir aussi : [[Algorithme de Kruskal]] (autre algorithme glouton du cours, optimal lui).

Résumés : [[5 - colorier graph]]
