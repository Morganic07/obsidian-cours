---
type: concept
tags: [year2, year4]
aliases: [nœud interne, noeud interne, nœud externe, descendants d'un nœud, ascendants d'un nœud, arité d'un nœud, arité d'un arbre, degré d'un nœud, degré d'un arbre]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]"]
maj: 2026-11-12
---

Termes de base sur les arbres, d'après les chapitres 3 et 4 :

- **racine** : nœud sans parent ;
- **feuille** ou **nœud externe** : nœud sans fils (arité 0) ;
- **nœud interne** : nœud ayant au moins un fils ;
- **arité** (ou degré) d'un nœud : nombre de ses fils ; d'un arbre : maximum de l'arité sur ses nœuds ;
- **[[Sous-arbre|sous-arbre]]** ;
- **branche** : suite de nœuds de la racine à une feuille ;
- **descendants** d'un nœud : nœuds de son sous-arbre ; **ascendants** : nœuds de la branche qui va de la racine à ce nœud ;
- **taille** : nombre de nœuds (0 pour l'arbre vide) ;
- **niveau** ou **profondeur** : la racine est au niveau 0, un fils au niveau de son père + 1.

## Graph theory (Year 4)

Le diaporama de révision [[2 - tree revisions années précédentes]] voit l'arbre enraciné comme un graphe orienté : une **feuille** (nœud externe) n'a pas d'arc sortant, un **nœud interne** n'est pas externe, le **degré** d'un nœud est son nombre d'arcs sortants, des nœuds **frères** (ou sœurs) ont le même parent ; $u$ est un **ancêtre** de $w$, et $w$ un **descendant** de $u$, si $w$ est dans l'arbre enraciné en $u$. Il définit aussi la **taille** (nombre de nœuds), la **profondeur** (distance de la racine au nœud), la [[Hauteur d'un arbre|hauteur]], l'[[Arbre ordonné|arbre ordonné]] et l'[[Arbre numéroté|arbre numéroté]].

Notion parente : [[Arbre (théorie des graphes)]]. Voir aussi : [[Hauteur d'un arbre]], [[Arbre binaire]], [[Sous-arbre]].

Résumés : [[3 - Arbres]], [[4 - Arbres binaires]], [[2 - tree revisions années précédentes]]
