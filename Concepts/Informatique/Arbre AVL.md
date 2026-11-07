---
type: concept
tags: [year2]
aliases: [AVL, arbres AVL, arbre binaire de recherche équilibré, rotation droite, rotation gauche, double rotation, facteur d'équilibrage, Adelson-Velsky et Landis, rotation simple, double rotation droite-gauche, double rotation gauche-droite, rééquilibrage, equilibrer, rebalance]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]", "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]", "[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]", "[[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2.pdf]]"]
maj: 2026-11-07
---

Un arbre AVL est un arbre binaire de recherche équilibré : AVL = arbre binaire de recherche + rééquilibrage. Pour chaque nœud, les hauteurs des deux sous-arbres diffèrent d'au plus 1.

**Facteur d'équilibrage** : hauteur du sous-arbre droit moins hauteur du gauche dans le cours (l'usage est gauche moins droite). L'arbre est équilibré si le facteur vaut $-1$, $0$ ou $1$ en chaque nœud. À $\pm 2$, il y a déséquilibre.

**Hauteur** ([[Hauteur d'un arbre]]) : $h = 1 + \max(h_{gauche}, h_{droite})$, avec $h = -1$ pour un sous-arbre vide. Si l'arbre est équilibré, $h$ est en $O(\log n)$. Propriété de l'amphi : $\log_2(1+n) \le 1 + h \le 1{,}44 \log_2(2+n)$ (plus précisément $\le \alpha\log_2(2+n)$ avec $\alpha \le 1{,}44$, d'après [[6 - AVL]]).

**Rotations** : la rotation droite autour de $y$ fait descendre $y$ et remonter son fils gauche $x$, sans changer l'ordre des éléments. La rotation gauche est l'inverse.
- Facteur $-2$ en $y$, $x$ son fils gauche : si $eq(x)$ vaut $-1$ ou $0$, rotation droite. Si $eq(x)$ vaut 1, rotation gauche autour de $x$ puis rotation droite autour de $y$. Le cas $+2$ est symétrique.
- Après un ajout, une rotation (simple ou double) suffit. Après une suppression, il peut en falloir jusqu'à $h$.

**Ajout et suppression** : comme dans un arbre binaire de recherche, puis calcul des facteurs et rotations. Suppression d'un nœud à deux fils : on le remplace par le plus petit du sous-arbre droit.

> [!warning] Écart dans le cours
> Le coût de `equilibrer` est donné en $O(1)$ dans [[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]] et en $O(\log n)$ dans [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]. Avec le code du cours, qui recalcule la hauteur à chaque appel, il est en $O(n)$ (complément). Voir [[Calcul de complexité et théorème de résolution]].

Attention aux conventions : la fiche AVL pose la hauteur d'un arbre vide à 0, alors que le chapitre 3 la pose à $-1$.

Notion parente : [[Arbre binaire de recherche]]. Liens : [[Hauteur d'un arbre]], [[Complexité algorithmique]], [[Calcul de complexité et théorème de résolution]], [[Récursivité]]

## Erreurs du cours

- [[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]] (page 5, `equilibreAprèsInsertion`) écrit « tantque pere(p)!=NIL et eq!=2 et eq!=2 faire » ; il faut « eq!=2 et eq!=-2 », comme le test « si eq==2 ou eq==-2 » qui suit.
- [[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]] (image de la propriété) donne « si n = 100000, 17 ≤ h ≤ 25 » ; la formule $\log_2(1+n) \le 1 + h \le 1{,}44\log_2(2+n)$ donne $15{,}6 \le h \le 22{,}9$, soit $16 \le h \le 22$.

Résumés : [[6 - AVL]]
