---
type: concept
tags: [year4]
aliases: [DSATUR, DSatur, algorithme de Brélaz]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition (complément, hors du cours)** : DSATUR (*degree of saturation*) est un [[Algorithme glouton|algorithme glouton]] de [[Coloration de graphe|coloration de graphe]] publié par Daniel Brélaz en 1979. Le **degré de saturation** d'un sommet est le nombre de couleurs différentes déjà portées par ses voisins. À chaque étape, l'algorithme colorie, avec la plus petite couleur possible, le sommet non colorié de plus grand degré de saturation (en départageant par le [[Degré d'un sommet|degré]]). Contrairement à l'[[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]], dont l'ordre est fixé une fois pour toutes, l'ordre s'adapte aux couleurs déjà posées ; DSATUR colorie optimalement les [[Graphe biparti|graphes bipartis]], mais reste une [[Heuristique (algorithmique)|heuristique]] en général.

## Dans le cours

Pas nommé : cité en complément dans [[5 - colorier graph]] (Graph theory), comme variante de Welsh et Powell.

Résumés : [[5 - colorier graph]]
