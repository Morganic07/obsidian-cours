---
type: concept
tags: [year4]
aliases: [arbres dégénérés, arbre filiforme, degenerate tree, peigne (arbre)]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un arbre **dégénéré** (ou filiforme) est un arbre dont chaque nœud interne n'a qu'un seul fils : il se réduit à une seule branche, comme une [[Liste chaînée|liste chaînée]]. Sa [[Hauteur d'un arbre|hauteur]] est maximale, $h = n - 1$ pour $n$ nœuds, et une recherche y coûte $O(n)$, comme une [[Recherche séquentielle|recherche séquentielle]]. Un [[Arbre binaire de recherche|arbre binaire de recherche]] dégénère quand on insère des valeurs déjà triées (1, 2, 3, … donne un « peigne » où chaque nœud est le fils droit du précédent). Les arbres [[Arbre équilibré|équilibrés]] ([[Arbre AVL|AVL]], [[Arbre rouge-noir|rouge-noir]]) existent pour éviter ce cas.

## Dans le cours

[[2 - tree revisions années précédentes]] l'invoque deux fois : c'est le pire cas du théorème de la hauteur ($h = n - 1$) et celui de la recherche dans un ABR ($O(n)$ « si l'arbre est dégénéré »).

Voir aussi : [[Arbre équilibré]], [[Complexité algorithmique]].

Résumés : [[2 - tree revisions années précédentes]]
