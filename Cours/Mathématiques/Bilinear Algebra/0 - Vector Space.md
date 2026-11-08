---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0d - Vector Space.docx|Chp 0d - Vector Space]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0d - Vector Space.docx|Chp 0d - Vector Space]] (« Chapter 0d - Vectors »), dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Idée générale

Le chapitre généralise les vecteurs de $\mathbb{R}^n$, puis décrit une matrice par ses quatre sous-espaces, sa dimension et son rang.

## 1. Espace vectoriel (*vector space*)

> **Définition** : un [[Espace vectoriel]] est un ensemble non vide $V$ d'objets appelés *vecteurs*, muni de deux opérations, l'*addition* et la *multiplication par un scalaire* (réel), soumises à dix axiomes valables pour tous $\mathbf u, \mathbf v, \mathbf w \in V$ et tous scalaires $c, d$ :
> 1. $\mathbf u + \mathbf v \in V$ ;
> 2. $\mathbf u + \mathbf v = \mathbf v + \mathbf u$ ;
> 3. $(\mathbf u + \mathbf v) + \mathbf w = \mathbf u + (\mathbf v + \mathbf w)$ ;
> 4. il existe un vecteur **nul** $\mathbf 0 \in V$ tel que $\mathbf u + \mathbf 0 = \mathbf u$ ;
> 5. pour tout $\mathbf u$, il existe $-\mathbf u \in V$ tel que $\mathbf u + (-\mathbf u) = \mathbf 0$ ;
> 6. $c\mathbf u \in V$ ;
> 7. $c(\mathbf u + \mathbf v) = c\mathbf u + c\mathbf v$ ;
> 8. $(c + d)\mathbf u = c\mathbf u + d\mathbf u$ ;
> 9. $c(d\mathbf u) = (cd)\mathbf u$ ;
> 10. (coupé sur l'image : l'image s'arrête à l'axiome 9).

Le dixième axiome est $1\mathbf u = \mathbf u$ : il figure dans les propriétés de $\mathbb R^n$ de [[0 - Linear combination|Linear combination]] (voir [[Espace vectoriel]]).

Des axiomes découlent des règles qu'on utilise sans y penser : $0\mathbf u = \mathbf 0$, $c\mathbf 0 = \mathbf 0$ et $-\mathbf u = (-1)\mathbf u$. Par exemple, $0\mathbf u = (0 + 0)\mathbf u = 0\mathbf u + 0\mathbf u$, puis on ajoute $-0\mathbf u$ des deux côtés. Le vecteur nul et l'opposé de chaque vecteur sont uniques. [[Complément hors du cours|ⓘ]]

L'intérêt de la définition abstraite est que des objets très différents de $\mathbb R^n$ vérifient les mêmes axiomes, et héritent donc des mêmes théorèmes : les matrices $m \times n$ (avec l'addition et le produit par un scalaire coefficient par coefficient), les polynômes de degré au plus $n$, noté $\mathbb P_n$, ou les fonctions réelles définies sur un même ensemble, additionnées point par point. [[Complément hors du cours|ⓘ]]

## 2. Sous-espaces (*subspaces*)

> **Définition** : un [[Sous-espace vectoriel|sous-espace]] d'un espace vectoriel $V$ est une partie $H$ de $V$ qui vérifie :
> a. le vecteur nul de $V$ est dans $H$ ;
> b. $H$ est stable par addition : $\mathbf u, \mathbf v \in H \Rightarrow \mathbf u + \mathbf v \in H$ ;
> c. $H$ est stable par multiplication par un scalaire : $\mathbf u \in H \Rightarrow c\mathbf u \in H$.

![[Chp 0d - Vector Space - image6.png]]
*Figure : trois sous-espaces de $\mathbb R^3$, un plan $\mathbf P$, une droite $\mathbf L$ et le point $\mathbf Z$ (origine) ; $\mathbf L$ est contenue dans $\mathbf P$, et tous passent par $(0,0,0)$.*

Remarques du cours :
- chaque propriété est vérifiée pour chaque sous-espace ;
- un plan de l'espace à trois dimensions n'est pas $\mathbb R^2$ : ses vecteurs ont 3 composantes et appartiennent à $\mathbb R^3$ ;
- une droite qui ne passe pas par l'origine n'est pas un sous-espace ;
- tout sous-espace est un espace vectoriel ;
- tout espace vectoriel est un sous-espace (de lui-même ou d'un espace plus grand) ;
- dans tout espace, $\{\mathbf 0\}$ est un sous-espace ;
- $\mathbb R^2$ n'est pas un sous-espace de $\mathbb R^3$ : ses vecteurs ont 2 composantes, ceux de $\mathbb R^3$ en ont 3.

**Méthode pour montrer qu'une partie $H$ est un sous-espace** : vérifier que $\mathbf 0 \in H$, puis que pour tous $\mathbf u, \mathbf v \in H$ et tout scalaire $c$, $\mathbf u + c\mathbf v \in H$ (ce qui regroupe b et c). Pour montrer que $H$ **n'en est pas** un, un seul contre-exemple suffit : $\mathbf 0 \notin H$, ou deux vecteurs de $H$ dont la somme sort de $H$. [[Complément hors du cours|ⓘ]]

Exemples : le plan $\{(x, y, z) : x + y - z = 0\}$ est un sous-espace de $\mathbb R^3$ (c'est l'ensemble des solutions d'une équation homogène) ; le plan $x + y - z = 1$ n'en est pas un, car il ne contient pas $(0,0,0)$. La réunion de deux droites distinctes passant par l'origine n'est pas un sous-espace non plus : $(1, 0)$ et $(0, 1)$ sont sur les deux axes de $\mathbb R^2$, mais leur somme $(1, 1)$ n'est sur aucun. [[Complément hors du cours|ⓘ]]

> **Théorème** : si $\mathbf v_1, \ldots, \mathbf v_p \in V$, alors $\text{Span}\{\mathbf v_1, \ldots, \mathbf v_p\}$ est un sous-espace de $V$ (voir [[Espace engendré]]).

## 3. Sous-espaces importants (*important subspaces*)

Pour une matrice $A$ ([[Sous-espaces fondamentaux]]) :
- **Row space** (espace des lignes) : ensemble des [[Combinaison linéaire|combinaisons linéaires]] des lignes ;
- **[[Espace nul|Null space]]** : solutions de l'équation homogène $A\mathbf x = \mathbf 0$ (le *ker* de $A$) ;
- **[[Espace des colonnes|Column space]]** : ensemble des combinaisons linéaires des colonnes ;
- **Left null space** : $\text{Nul}\,A^T$, solutions de $A^T\mathbf w = \mathbf 0$.

![[Chp 0d - Vector Space - image26.png]]
*Figure : pour $A$ de lignes $r_1 = (1,2,3)$ et $r_2 = (4,5,6)$, le row space est un plan 2D engendré par $r_1$, $r_2$ ; le vecteur $\mathbf x = (1,-2,1)$, perpendiculaire à ce plan, engendre une droite 1D (le null space) ; le left null space est réduit à l'origine (image coupée).*

![[Chp 0d - Vector Space - image1.png]]
*Figure : les colonnes $a_1 = (1,4)$, $a_2 = (2,5)$, $a_3 = (3,6)$ engendrent tout le plan : c'est le column space.*

**Les quatre sous-espaces fondamentaux.** Une matrice $A$ de taille $m \times n$ définit une [[Transformation linéaire|transformation linéaire]] de $\mathbb R^n$ dans $\mathbb R^m$. Ce qui se passe dans $A\mathbf x = \mathbf b$ s'exprime avec 4 sous-espaces, deux de $\mathbb R^n$ et deux de $\mathbb R^m$ :

| Sous-espace | Notation | Notation de certains livres | Dans |
|---|---|---|---|
| Column space | $\text{Col}\,A$ | $C(A)$ | $\mathbb R^m$ |
| Row space | $\text{Col}\,A^T$ | $C(A^T)$ | $\mathbb R^n$ |
| Null space | $\text{Nul}\,A$ | $N(A)$ | $\mathbb R^n$ |
| Left null space | $\text{Nul}\,A^T$ | $N(A^T)$ | $\mathbb R^m$ |

- Le column space d'une matrice est l'**image** (*range*) de la transformation matricielle associée.
- $\text{Row}\,A = \text{Col}\,A^T$, donc $\text{Row}\,A^T = \text{Col}\,A$.

Pourquoi le null space est perpendiculaire au row space, comme sur la figure : la $i$-ème composante de $A\mathbf x$ est le [[Produit scalaire|produit scalaire]] de la ligne $i$ de $A$ avec $\mathbf x$. Donc $A\mathbf x = \mathbf 0$ signifie exactement que $\mathbf x$ est orthogonal à chaque ligne, donc à toute combinaison des lignes : $\text{Nul}\,A = (\text{Row}\,A)^\perp$. De même, $\text{Nul}\,A^T = (\text{Col}\,A)^\perp$ ([[Complément orthogonal]], vu dans [[1 - Orthogonality|Orthogonality]]). Sur l'exemple, $(1,2,3)\cdot(1,-2,1) = 1 - 4 + 3 = 0$ et $(4,5,6)\cdot(1,-2,1) = 4 - 10 + 6 = 0$. [[Complément hors du cours|ⓘ]]

## 4. Column space

> **Définition** : le column space de $A$ ($m \times n$), noté $\text{Col}\,A$, est l'ensemble des combinaisons linéaires des colonnes de $A$. Si $A = [\mathbf a_1 \cdots \mathbf a_n]$,
> $$\text{Col}\,A = \text{Span}\{\mathbf a_1, \ldots, \mathbf a_n\} = \{\mathbf b : \mathbf b = A\mathbf x \text{ pour un } \mathbf x \in \mathbb R^n\}.$$

> **Théorème** : le column space d'une matrice $m \times n$ est un sous-espace de $\mathbb R^m$.

- Quand un système s'écrit $A\mathbf x = \mathbf b$, $\text{Col}\,A$ est l'ensemble des $\mathbf b$ pour lesquels le système a une solution.
- $\text{Col}\,A = \mathbb R^m$ si et seulement si $A\mathbf x = \mathbf b$ a une solution pour tout $\mathbf b \in \mathbb R^m$.

## 5. Row space

- Si $A$ est $m \times n$, chaque ligne a $n$ coordonnées et s'identifie à un vecteur de $\mathbb R^n$.
- L'ensemble des combinaisons linéaires des lignes, $\text{Row}\,A$, est un sous-espace de $\mathbb R^n$.
- $\text{Row}\,A = \text{Col}\,A^T$.

## 6. Null space

> **Définition** : le null space de $A$ ($m \times n$), noté $\text{Nul}\,A$, est l'ensemble des solutions de l'équation homogène $A\mathbf x = \mathbf 0$ :
> $$\text{Nul}\,A = \{\mathbf x : \mathbf x \in \mathbb R^n \text{ et } A\mathbf x = \mathbf 0\}.$$
> Description plus dynamique : l'ensemble des $\mathbf x \in \mathbb R^n$ envoyés sur le vecteur nul de $\mathbb R^m$ par $\mathbf x \mapsto A\mathbf x$.

![[Chp 0d - Vector Space - image7.png]]
*Figure : la droite $\text{Nul}\,A$ de $\mathbb R^n$, passant par $\mathbf 0$, est envoyée tout entière sur le point $\mathbf 0$ de $\mathbb R^m$.*

> **Théorème** : le null space d'une matrice $m \times n$ est un sous-espace de $\mathbb R^n$. De façon équivalente, l'ensemble des solutions d'un système $A\mathbf x = \mathbf 0$ de $m$ équations homogènes à $n$ inconnues est un sous-espace de $\mathbb R^n$.

> **Propriété** : quand $\text{Nul}\,A$ contient des vecteurs non nuls, le nombre de vecteurs de la famille génératrice de $\text{Nul}\,A$ est égal au nombre de [[Variable libre|variables libres]] de $A\mathbf x = \mathbf 0$.

**Méthode pour trouver une famille génératrice de $\text{Nul}\,A$** : réduire $A$ à sa [[Forme échelonnée|forme échelonnée réduite]], exprimer les variables de base en fonction des variables libres, puis écrire la solution générale comme combinaison linéaire de vecteurs, un par variable libre. Exemple avec $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ :
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \xrightarrow{L_2 \leftarrow L_2 - 4L_1} \begin{bmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \end{bmatrix} \xrightarrow{L_2 \leftarrow -L_2/3} \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \end{bmatrix} \xrightarrow{L_1 \leftarrow L_1 - 2L_2} \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \end{bmatrix}$$
d'où $x_1 = x_3$, $x_2 = -2x_3$, $x_3$ libre, et $\mathbf x = x_3\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$ : on retrouve la droite de la figure, engendrée par $(1,-2,1)$. La famille obtenue ainsi est toujours linéairement indépendante, donc c'est une base de $\text{Nul}\,A$. [[Complément hors du cours|ⓘ]]

### Comparaison de $\text{Nul}\,A$ et $\text{Col}\,A$ (pour $A$ de taille $m \times n$)

| | $\text{Nul}\,A$ | $\text{Col}\,A$ |
|---|---|---|
| 1 | Sous-espace de $\mathbb R^n$. | Sous-espace de $\mathbb R^m$. |
| 2 | Défini **implicitement** : on ne donne qu'une condition ($A\mathbf x = \mathbf 0$) que ses vecteurs doivent vérifier. | Défini **explicitement** : on dit comment construire ses vecteurs. |
| 3 | Trouver des vecteurs de $\text{Nul}\,A$ prend du temps : il faut des [[Opérations élémentaires sur les lignes\|opérations sur les lignes]] de $[A\ \ \mathbf 0]$. | Facile : les colonnes de $A$ sont données, les autres s'en déduisent. |
| 4 | Pas de relation évidente avec les coefficients de $A$. | Relation évidente : chaque colonne de $A$ est dans $\text{Col}\,A$. |
| 5 | Un vecteur typique $\mathbf v$ vérifie $A\mathbf v = \mathbf 0$. | Un vecteur typique $\mathbf v$ est tel que $A\mathbf x = \mathbf v$ est compatible. |
| 6 | Tester si $\mathbf v \in \text{Nul}\,A$ est facile : calculer $A\mathbf v$. | Tester si $\mathbf v \in \text{Col}\,A$ peut prendre du temps : réduire $[A\ \ \mathbf v]$. |
| 7 | $\text{Nul}\,A = \{\mathbf 0\}$ $\iff$ $A\mathbf x = \mathbf 0$ n'a que la [[Système linéaire homogène\|solution triviale]]. | $\text{Col}\,A = \mathbb R^m$ $\iff$ $A\mathbf x = \mathbf b$ a une solution pour tout $\mathbf b \in \mathbb R^m$. |
| 8 | $\text{Nul}\,A = \{\mathbf 0\}$ $\iff$ $\mathbf x \mapsto A\mathbf x$ est [[Injectivité et surjectivité\|injective]]. | $\text{Col}\,A = \mathbb R^m$ $\iff$ $\mathbf x \mapsto A\mathbf x$ envoie $\mathbb R^n$ **sur** $\mathbb R^m$. |

### Dimensions des quatre sous-espaces

| Espace | Sous-espace | Description | Dimension |
|---|---|---|---|
| $\mathbb R^n$ | Row space $C(A^T)$ | tous les $A^T\mathbf y$ | $r$ ([[Rang d'une matrice\|rang]]) |
| $\mathbb R^n$ | Nullspace $N(A)$ | $A\mathbf x = \mathbf 0$ | $n - r$ |
| $\mathbb R^m$ | Column space $C(A)$ | tous les $A\mathbf x$ | $r$ |
| $\mathbb R^m$ | Left nullspace $N(A^T)$ | $A^T\mathbf y = \mathbf 0$ | $m - r$ |

![[Chp 0d - Vector Space - image21.png]]
*Figure : schéma des quatre sous-espaces fondamentaux, row space et nullspace dans $\mathbb R^n$, column space et left nullspace dans $\mathbb R^m$, avec leurs dimensions.*

## 7. Base d'un sous-espace (*basis of a subspace*)

> **Définition** : une [[Base (algèbre linéaire)|base]] d'un sous-espace $H$ de $\mathbb R^n$ est une famille [[Indépendance linéaire|linéairement indépendante]] de $H$ qui engendre $H$.

> **Propriété** :
> - les colonnes d'une matrice $n \times n$ **inversible** forment une base de $\mathbb R^n$, car elles sont linéairement indépendantes et engendrent $\mathbb R^n$ (théorème de la [[Matrice inversible|matrice inversible]]) ;
> - c'est le cas de la matrice identité $I_n$ ; ses colonnes $\mathbf e_i$ forment la **base standard** (canonique) $\{\mathbf e_1, \ldots, \mathbf e_n\}$ de $\mathbb R^n$ :
> $$\mathbf e_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix},\ \mathbf e_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix},\ \ldots,\ \mathbf e_n = \begin{bmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$

Une base est à la fois une famille génératrice **minimale** (en retirer un vecteur, elle n'engendre plus $H$) et une famille libre **maximale** (en ajouter un, elle devient liée). Son intérêt : tout vecteur de $H$ s'écrit d'une **seule** façon comme combinaison linéaire des vecteurs de la base, ce qui définit ses [[Coordonnées dans une base|coordonnées]]. [[Complément hors du cours|ⓘ]]

**Base de $\text{Col}\,A$** : les colonnes **pivots de $A$** forment une base de $\text{Col}\,A$. On repère les pivots sur une forme échelonnée, mais on prend les colonnes correspondantes de la matrice $A$ d'origine : les opérations sur les lignes changent le column space. Dans l'exemple ci-dessus, les colonnes 1 et 2 sont pivots, donc $\{(1,4), (2,5)\}$ est une base de $\text{Col}\,A$, qui est tout $\mathbb R^2$. [[Complément hors du cours|ⓘ]]

## 8. Dimension et rang d'une matrice

> **Définition** : la [[Dimension (algèbre linéaire)|dimension]] d'un sous-espace non nul $H$, notée $\dim H$, est le nombre de vecteurs de n'importe quelle base de $H$. La dimension du sous-espace nul $\{\mathbf 0\}$ est définie comme 0 (il n'a **pas** de base, car le vecteur nul seul forme une famille liée).
>
> $\mathbb R^n$ est de dimension $n$ et toute base de $\mathbb R^n$ a $n$ vecteurs. Un plan passant par $\mathbf 0$ dans $\mathbb R^3$ est de dimension 2, une droite passant par $\mathbf 0$ de dimension 1.

> **Propriété ([[Rang d'une matrice]])** : le rang d'une matrice est le nombre de colonnes de la matrice identité dans sa forme échelonnée réduite ([[Forme échelonnée]]). Autrement dit, c'est le nombre de colonnes linéairement indépendantes.
>
> Exemple : $\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ a 3 colonnes de l'identité, donc $\text{rank}\,A = 3$.

> **Théorème du rang** ([[Théorème du rang|rank theorem]]) : si $A$ a $n$ colonnes,
> $$\text{rank}\,A + \dim \text{Nul}\,A = n.$$

Le théorème se lit en comptant les colonnes : chacune correspond soit à une variable de base (une colonne pivot, comptée dans le rang), soit à une [[Variable libre|variable libre]] (un vecteur de la base de $\text{Nul}\,A$). Sur l'exemple $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ : $\text{rank}\,A = 2$, $\dim \text{Nul}\,A = 1$, et $2 + 1 = 3$ colonnes ; le left null space a pour dimension $m - r = 2 - 2 = 0$, ce qui explique qu'il soit réduit à l'origine. [[Complément hors du cours|ⓘ]]

Le rang est le même vu par les lignes ou par les colonnes : $\dim \text{Row}\,A = \dim \text{Col}\,A$, soit $\text{rank}\,A = \text{rank}\,A^T$. Il est donc au plus égal au plus petit des deux nombres $m$ et $n$ : $\text{rank}\,A \leq \min(m, n)$. [[Complément hors du cours|ⓘ]]

> **Théorème de la matrice inversible (suite)** : $A$ de taille $n \times n$. Chacun des énoncés suivants équivaut à « $A$ est inversible » (voir [[3 - Invertible matrix theorem|Invertible matrix theorem]]) :
> m. les colonnes de $A$ forment une base de $\mathbb R^n$ ;
> n. $\text{Col}\,A = \mathbb R^n$ ;
> o. $\dim \text{Col}\,A = n$ ;
> p. $\text{rank}\,A = n$ ;
> q. $\text{Nul}\,A = \{\mathbf 0\}$ ;
> r. $\dim \text{Nul}\,A = 0$.

## 9. Noyau et image (*kernel and image*)

> **Définition (noyau)** : soit $T : V \to W$ une transformation linéaire entre espaces vectoriels. Le **noyau** (*kernel*, aussi *null space* de $T$) est l'image réciproque du vecteur nul de $W$ :
> $$\ker(T) = T^{-1}(\mathbf 0) = \{\mathbf v \in V \mid T\mathbf v = \mathbf 0\},$$
> parfois noté $N(T)$.

> **Définition (image)** : l'**image** (*range*) de $T$ est l'ensemble de ses valeurs :
> $$T(V) = \{T(\mathbf v) \in W \mid \mathbf v \in V\},$$
> aussi notée $\text{im}(T)$ ou $R(T)$. Voir [[Transformation linéaire]], [[Image d'une application linéaire]].

Le noyau est un sous-espace de $V$, l'image un sous-espace de $W$. Quand $T(\mathbf x) = A\mathbf x$, on retrouve $\ker T = \text{Nul}\,A$ et $\text{im}\,T = \text{Col}\,A$ : ces deux définitions généralisent le null space et le column space à n'importe quelle transformation linéaire. [[Complément hors du cours|ⓘ]]

$T$ est [[Injectivité et surjectivité|injective]] si et seulement si $\ker T = \{\mathbf 0\}$ : si $T\mathbf u = T\mathbf v$, alors $T(\mathbf u - \mathbf v) = \mathbf 0$, donc $\mathbf u - \mathbf v \in \ker T$. Et si $V$ est de dimension finie, le [[Théorème du rang|théorème du rang]] s'écrit $\dim V = \dim \ker T + \dim \text{im}\,T$. [[Complément hors du cours|ⓘ]]
