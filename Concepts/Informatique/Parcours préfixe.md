---
type: concept
tags: [year2, year4]
aliases: [ordre préfixe, parcours RGD, preorder, preorder traversal, pre-order traversal]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[2 - tree revisions années précédentes]]) : le parcours **préfixe** est un [[Parcours en profondeur|parcours en profondeur]] d'arbre où chaque nœud est visité **avant** ses fils : on visite la racine, puis on fait le parcours préfixe des [[Sous-arbre|sous-arbres]] de gauche à droite. Dans un [[Arbre binaire|arbre binaire]], c'est le parcours R G D (racine, gauche, droit).

Exemple du cours (arbre 1 → 2, 8 ; 2 → 3, 6 ; 3 → 4, 5 ; 6 → 7 ; 8 → 9, 10) : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

**Précisions (complément, hors du cours)** :
- version [[Récursivité|récursive]] : `visiter(racine(a))`, puis appel sur chaque fils ; version itérative avec une [[Pile et file|pile]] : dépiler un nœud, le visiter, empiler ses fils de droite à gauche ;
- coût $\Theta(n)$ pour $n$ nœuds, mémoire $O(h)$ ([[Hauteur d'un arbre|hauteur]]) ;
- usages : copier ou sérialiser un arbre (la racine vient avant ce qui en dépend), afficher une hiérarchie indentée (commande `tree`), écrire un arbre d'expression en [[Notation polonaise|notation polonaise]] ;
- avec l'ordre [[Parcours infixe|infixe]], il permet de reconstruire un arbre binaire aux étiquettes distinctes.

## Dans le cours

[[2 - tree revisions années précédentes]] le présente avec le [[Parcours postfixe|postfixe]] et l'[[Parcours infixe|infixe]], toujours de gauche à droite. Le cours d'Algo de Year 2 donne les trois parcours d'un arbre binaire dans [[Arbre binaire]].

Notion parente : [[Parcours en profondeur]]. Voir aussi : [[Parcours postfixe]], [[Parcours infixe]], [[Parcours en largeur]].

Résumés : [[2 - tree revisions années précédentes]], [[4 - Arbres binaires]]
