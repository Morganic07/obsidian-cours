---
type: concept
tags: [year2, year4]
aliases: [parcours symétrique, ordre infixe, parcours GRD, inorder, inorder traversal, in-order traversal]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[2 - tree revisions années précédentes]]) : le parcours **infixe** (ou symétrique) est un [[Parcours en profondeur|parcours en profondeur]] défini pour un [[Arbre binaire|arbre binaire]] seulement : chaque nœud est visité après son fils gauche et avant son fils droit. On fait le parcours infixe du [[Sous-arbre|sous-arbre]] gauche, on visite la racine, puis on fait le parcours infixe du sous-arbre droit : parcours G R D (gauche, racine, droit).

Exemple du cours (arbre 1 → 2, 8 ; 2 → 3, 6 ; 3 → 4, 5 ; 6 → 7, fils droit ; 8 → 9, 10) : 4, 3, 5, 2, 6, 7, 1, 9, 8, 10.

**Précisions (complément, hors du cours)** :
- propriété clé : le parcours infixe d'un [[Arbre binaire de recherche|arbre binaire de recherche]] donne ses valeurs dans l'ordre croissant, et un arbre binaire est un ABR si et seulement si son infixe est strictement croissant ;
- sur un arbre d'expression, il donne l'écriture usuelle, qui a besoin de parenthèses, contrairement à la [[Notation polonaise|notation polonaise]] ;
- coût $\Theta(n)$ ; avec l'ordre [[Parcours préfixe|préfixe]], il permet de reconstruire un arbre binaire aux étiquettes distinctes.

## Dans le cours

[[2 - tree revisions années précédentes]] le présente après le [[Parcours préfixe|préfixe]] et le [[Parcours postfixe|postfixe]]. Le cours d'Algo de Year 2 donne les trois parcours d'un arbre binaire dans [[Arbre binaire]] et la propriété des ABR dans [[Arbre binaire de recherche]].

Notion parente : [[Parcours en profondeur]]. Voir aussi : [[Parcours préfixe]], [[Parcours postfixe]].

Résumés : [[2 - tree revisions années précédentes]], [[4 - Arbres binaires]], [[5 - ABR]]
