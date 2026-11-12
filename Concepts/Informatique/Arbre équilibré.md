---
type: concept
tags: [year4]
aliases: [arbres équilibrés, balanced tree, arbre auto-équilibré, self-balancing tree, arbre de recherche équilibré]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un arbre est **équilibré** quand sa [[Hauteur d'un arbre|hauteur]] reste de l'ordre du [[Logarithme|logarithme]] de sa taille, $h = O(\log n)$ : ses branches ont des longueurs voisines, chaque niveau est presque rempli avant le suivant. Le terme n'a pas de définition unique ; chaque famille d'arbres en fixe une précise : différence de hauteur d'au plus 1 entre les deux sous-arbres de chaque nœud pour l'[[Arbre AVL]], même nombre de nœuds noirs sur toutes les branches pour l'[[Arbre rouge-noir]], toutes les feuilles à la même profondeur pour le [[B-arbre]]. Un arbre **auto-équilibré** rétablit sa condition après chaque insertion ou suppression (rotations, recolorations, éclatements), ce qui garantit des opérations en $O(\log n)$ dans le pire des cas. L'opposé est l'[[Arbre dégénéré|arbre dégénéré]].

Ordre de grandeur : un [[Arbre binaire de recherche|arbre binaire de recherche]] équilibré d'un million de clés a une hauteur d'une vingtaine, contre un million pour un arbre dégénéré.

## Dans le cours

[[2 - tree revisions années précédentes]] donne la complexité de la recherche dans un ABR : $O(\log n)$ « si l'arbre est équilibré », $O(n)$ s'il est dégénéré.

Voir aussi : [[Arbre AVL]], [[Arbre rouge-noir]], [[B-arbre]], [[Tas binaire]], [[Complexité algorithmique]].

Résumés : [[2 - tree revisions années précédentes]]
