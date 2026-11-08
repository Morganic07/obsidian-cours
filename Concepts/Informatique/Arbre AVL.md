---
type: concept
tags: [year2]
aliases: [AVL, arbres AVL, arbre binaire de recherche équilibré, rotation droite, rotation gauche, double rotation, facteur d'équilibrage, Adelson-Velsky et Landis, rotation simple, double rotation droite-gauche, double rotation gauche-droite, rééquilibrage, equilibrer, rebalance]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]", "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]", "[[Raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL.pdf]]", "[[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2.pdf]]"]
maj: 2026-11-08
---

Un arbre AVL est un arbre binaire de recherche équilibré : AVL = arbre binaire de recherche + rééquilibrage. Pour chaque nœud, les hauteurs des deux sous-arbres diffèrent d'au plus 1.

**Facteur d'équilibrage** : hauteur du sous-arbre droit moins hauteur du gauche dans le cours (l'usage est gauche moins droite). L'arbre est équilibré si le facteur vaut $-1$, $0$ ou $1$ en chaque nœud. À $\pm 2$, il y a déséquilibre.

**Hauteur** ([[Hauteur d'un arbre]]) : $h = 1 + \max(h_{gauche}, h_{droite})$, avec $h = -1$ pour un sous-arbre vide. Si l'arbre est équilibré, $h$ est en $O(\log n)$. Propriété de l'amphi : $\log_2(1+n) \le 1 + h \le 1{,}44 \log_2(2+n)$ (plus précisément $\le \alpha\log_2(2+n)$ avec $\alpha \le 1{,}44$, d'après [[6 - AVL]]). Exemple : pour $n = 100\,000$, $16 \le h \le 22$. [[Erreurs du cours#^e-arbre-avl|✎]]

**Rotations** : la rotation droite autour de $y$ fait descendre $y$ et remonter son fils gauche $x$, sans changer l'ordre des éléments. La rotation gauche est l'inverse.
- Facteur $-2$ en $y$, $x$ son fils gauche : si $eq(x)$ vaut $-1$ ou $0$, rotation droite. Si $eq(x)$ vaut 1, rotation gauche autour de $x$ puis rotation droite autour de $y$. Le cas $+2$ est symétrique.
- Après un ajout, une rotation (simple ou double) suffit. Après une suppression, il peut en falloir jusqu'à $h$.

**Ajout et suppression** : comme dans un arbre binaire de recherche, puis calcul des facteurs et rotations. Suppression d'un nœud à deux fils : on le remplace par le plus petit du sous-arbre droit.

**Coût de `equilibrer`** : avec le code du cours, qui recalcule la hauteur à chaque appel, il est en $O(n)$ (une rotation seule coûte $O(1)$). [[Erreurs du cours#^e-arbre-avl|✎]] Voir [[Calcul de complexité et théorème de résolution]].

Attention aux conventions : la fiche AVL pose la hauteur d'un arbre vide à 0, alors que le chapitre 3 la pose à $-1$.

## Précisions (complément, hors du cours)

**D'où vient la borne 1,44.** Soit $N(h)$ le nombre minimal de nœuds d'un AVL de hauteur $h$ (une feuille a la hauteur 0). L'arbre le plus creux a un sous-arbre de hauteur $h-1$ et l'autre de hauteur $h-2$, tous deux eux-mêmes minimaux :
$$N(h) = 1 + N(h-1) + N(h-2), \qquad N(0) = 1,\ N(1) = 2.$$
On en tire $N(h) = F_{h+3} - 1$, où $F_k$ est la [[Suite de Fibonacci]] ($F_1 = F_2 = 1$) ; ces arbres minimaux s'appellent arbres de Fibonacci. Comme $F_k \approx \varphi^k/\sqrt5$ avec $\varphi = \frac{1+\sqrt5}{2}$, un AVL de $n$ nœuds vérifie $h \lesssim \log_\varphi n = \frac{\log_2 n}{\log_2 \varphi} \approx 1{,}44 \log_2 n$.

**Les quatre cas de déséquilibre**, nommés d'après le chemin qui mène de $y$ (le nœud déséquilibré) vers le sous-arbre trop haut :

| Cas | Sous-arbre trop haut | Correction |
|---|---|---|
| gauche-gauche | sous-arbre gauche du fils gauche | rotation droite autour de $y$ |
| gauche-droite | sous-arbre droit du fils gauche | rotation gauche autour du fils, puis rotation droite autour de $y$ |
| droite-droite | sous-arbre droit du fils droit | rotation gauche autour de $y$ |
| droite-gauche | sous-arbre gauche du fils droit | rotation droite autour du fils, puis rotation gauche autour de $y$ |

**Une rotation préserve l'ordre.** Avant la rotation droite, $y$ a pour fils gauche $x$ (de sous-arbres $\alpha$, $\beta$) et pour sous-arbre droit $\gamma$ ; après, $x$ est à la racine, avec $\alpha$ à gauche et $y$ à droite, $y$ recevant $\beta$ et $\gamma$. Le parcours infixe reste $\alpha, x, \beta, y, \gamma$ : c'est toujours un ABR. La rotation ne modifie que quelques pointeurs, d'où un coût $O(1)$.

**Pourquoi une rotation suffit après une insertion** : la rotation (simple ou double) rend au sous-arbre rééquilibré la hauteur qu'il avait avant l'insertion, donc les ancêtres ne voient aucun changement. Après une suppression, le sous-arbre peut au contraire perdre un niveau, et le déséquilibre remonter : jusqu'à $O(\log n)$ rotations.

Article original : G. M. Adelson-Velsky et E. M. Landis, « An algorithm for the organization of information », *Doklady Akademii Nauk SSSR*, 1962. [[Erreurs du cours#^e-arbre-avl|✎]] Variante moins strictement équilibrée : [[Arbre rouge-noir]].

Notion parente : [[Arbre binaire de recherche]]. Liens : [[Hauteur d'un arbre]], [[Complexité algorithmique]], [[Calcul de complexité et théorème de résolution]], [[Récursivité]], [[Arbre rouge-noir]], [[B-arbre]]

Résumés : [[6 - AVL]]
