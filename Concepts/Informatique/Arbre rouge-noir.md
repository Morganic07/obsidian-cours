---
type: concept
tags: [year2]
aliases: [arbres rouge-noir, arbre bicolore, red-black tree, RB-tree]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un arbre rouge-noir est un [[Arbre binaire de recherche]] équilibré dont chaque nœud porte une couleur, rouge ou noir, et qui respecte quatre règles :
1. la racine est noire ;
2. les feuilles vides (NIL) sont noires ;
3. un nœud rouge n'a que des fils noirs (pas deux rouges à la suite) ;
4. tous les chemins d'un nœud vers les feuilles vides qui le suivent contiennent le même nombre de nœuds noirs (la *hauteur noire* du nœud).

**Conséquence** : sur une branche, les nœuds rouges sont au plus aussi nombreux que les noirs, donc la plus longue branche fait au plus deux fois la plus courte. On en déduit que la [[Hauteur d'un arbre|hauteur]] d'un arbre rouge-noir de $n$ nœuds vérifie
$$h \le 2 \log_2(n + 1),$$
d'où recherche, insertion et suppression en $O(\log n)$.

**Rééquilibrage** : après une insertion (le nouveau nœud est rouge) ou une suppression, on rétablit les règles par des **recolorations** et des **rotations**, les mêmes que pour l'[[Arbre AVL]]. Il faut au plus deux rotations par insertion et trois par suppression, les recolorations pouvant remonter jusqu'à la racine.

## Comparaison avec l'AVL

| | AVL | Rouge-noir |
|---|---|---|
| Équilibre | différence de hauteur $\le 1$ en chaque nœud | plus longue branche $\le$ 2 × plus courte |
| Hauteur maximale | $\approx 1{,}44 \log_2 n$ | $2 \log_2(n+1)$ |
| Recherche | un peu plus rapide | un peu plus lente |
| Rotations | 1 par insertion, jusqu'à $O(\log n)$ par suppression | au plus 2 par insertion, 3 par suppression |

L'arbre rouge-noir est donc préféré quand les modifications sont fréquentes. Exemples d'usage : la classe `TreeMap` de [[Langage Java|Java]], `std::map` dans les implémentations courantes de la bibliothèque standard C++, l'ordonnanceur CFS du noyau Linux.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[6 - AVL]], comme autre arbre binaire de recherche équilibré.

Voir aussi : [[Arbre AVL]], [[Arbre binaire de recherche]], [[B-arbre]], [[Hauteur d'un arbre]], [[Complexité algorithmique]].

Résumés : [[6 - AVL]]
