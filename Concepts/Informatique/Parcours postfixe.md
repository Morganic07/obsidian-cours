---
type: concept
tags: [year2, year4]
aliases: [parcours suffixe, ordre postfixe, parcours GDR, postorder, postorder traversal, post-order traversal]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[2 - tree revisions années précédentes]]) : le parcours **postfixe** (ou suffixe) est un [[Parcours en profondeur|parcours en profondeur]] d'arbre où chaque nœud est visité **après** chacun de ses fils : on fait le parcours postfixe des [[Sous-arbre|sous-arbres]] de gauche à droite, puis on visite la racine. Dans un [[Arbre binaire|arbre binaire]], c'est le parcours G D R (gauche, droit, racine).

Exemple du cours (arbre 1 → 2, 8 ; 2 → 3, 6 ; 3 → 4, 5 ; 6 → 7 ; 8 → 9, 10) : 4, 5, 3, 7, 6, 2, 9, 10, 8, 1.

**Précisions (complément, hors du cours)** :
- la racine est toujours visitée en dernier, les feuilles d'abord ;
- coût $\Theta(n)$ pour $n$ nœuds ;
- usages : tout calcul où un nœud a besoin du résultat de ses fils : [[Hauteur d'un arbre|hauteur]] ($1 + \max$ des hauteurs des fils), taille, libération de la mémoire d'un arbre (libérer les fils avant le père), taille d'un répertoire dans un [[Système de fichiers|système de fichiers]] (commande `du`), évaluation d'un arbre d'expression, qui s'écrit alors en [[Notation polonaise|notation polonaise inverse]].

## Dans le cours

[[2 - tree revisions années précédentes]] le présente avec le [[Parcours préfixe|préfixe]] et l'[[Parcours infixe|infixe]]. Le cours d'Algo de Year 2 donne les trois parcours d'un arbre binaire dans [[Arbre binaire]].

Notion parente : [[Parcours en profondeur]]. Voir aussi : [[Parcours préfixe]], [[Parcours infixe]], [[Récursivité]].

Résumés : [[2 - tree revisions années précédentes]], [[4 - Arbres binaires]]
