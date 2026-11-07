---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0a - Linear combination .docx|Chp 0a - Linear combination]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0a - Linear combination .docx|Chp 0a - Linear combination]] (« Chapter 0a - Linear equation in linear algebra »), dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre montre qu'une même question s'écrit de trois façons équivalentes : un système, une équation vectorielle et une équation matricielle. Il en tire les notions de base : engendrer, être indépendant, transformer.

## 1. Systèmes d'équations linéaires (*systems of linear equations*)

Une équation linéaire s'écrit
$$a_1x_1 + a_2x_2 + \cdots + a_nx_n = b.$$

Deux [[Système linéaire|systèmes linéaires]] sont **équivalents** s'ils ont le même ensemble de solutions (*same solution set*).

Visualisation géométrique pour 2 et 3 inconnues (donc 2 et 3 [[Dimension (algèbre linéaire)|dimensions]]) : un système a **0, 1 ou une infinité** de solutions.

| Nombre de solutions | Statut | Dans le plan | Dans l'espace |
|---|---|---|---|
| 1 solution | *Consistent* (compatible) | ![[Chp 0a - Linear combination - image21.png]] | ![[Chp 0a - Linear combination - image12.png]] |
| Infinité | *Consistent* | ![[Chp 0a - Linear combination - image27.png]] | |
| Aucune | *Inconsistent* (incompatible) | ![[Chp 0a - Linear combination - image19.png]] | ![[Chp 0a - Linear combination - image2.png]] |

*Figure : une solution = deux droites sécantes en $(3,2)$, ou trois plans sécants en $(1,0,-1)$ ; infinité = droites confondues ($\ell_1$ seule) ; aucune = droites parallèles, ou trois plans sans point commun (« no point lies on all three planes »).*

## 2. Matrice des coefficients et matrice augmentée

Exemple du cours :
$$\begin{aligned} x_1 - 2x_2 + x_3 &= 0 \\ 2x_2 - 8x_3 &= 8 \\ 5x_1 - 5x_3 &= 10 \end{aligned}
\qquad
\text{coefficient matrix } \begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{bmatrix}
\qquad
\text{augmented matrix } \left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array}\right]$$
(voir [[Matrice augmentée]]).

### Méthode de résolution

- Stratégie : remplacer le système par un système **équivalent** plus facile à résoudre.
- Utiliser le terme en $x_1$ de la première équation pour éliminer $x_1$ des autres, puis le terme en $x_2$ de la deuxième pour éliminer $x_2$ des autres, etc.

Les trois [[Opérations élémentaires sur les lignes|opérations élémentaires]] (*elementary row operations*) :
1. **Remplacement** : remplacer une équation par la somme d'elle-même et d'un multiple d'une autre ;
2. **Échange** : échanger deux équations ;
3. **Mise à l'échelle** : multiplier tous les termes d'une équation par une constante non nulle.

Deux matrices sont **équivalentes par lignes** (*row equivalent*) si l'on passe de l'une à l'autre par des opérations élémentaires. Ces opérations sont réversibles, et deux matrices équivalentes par lignes ont le même ensemble de solutions.

Avant de résoudre, savoir si le système est compatible, puis chercher le nombre de solutions : observer le coin inférieur droit de la matrice augmentée.

**Théorème d'existence et d'unicité** (*Existence and Uniqueness Theorem*). Un système linéaire est compatible si et seulement si la dernière colonne de la matrice augmentée n'est **pas** une colonne pivot, c'est-à-dire si et seulement si une forme échelonnée de la matrice augmentée n'a **aucune** ligne de la forme
$$[0\ \cdots\ 0\ b] \quad \text{avec } b \neq 0.$$
S'il est compatible, l'ensemble des solutions contient soit (i) une **unique** solution s'il n'y a pas de [[Variable libre|variable libre]], soit (ii) une **infinité** de solutions s'il y a au moins une variable libre.

Exemple : $\begin{bmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & 0 & 0 & 15 \end{bmatrix}$ : la dernière ligne s'écrit $0x_3 = 15$, impossible.

## 3. Réduction et forme échelonnée (*row reduction and echelon form*)

**Forme échelonnée** (*echelon form*, *row echelon form*) d'une matrice $n \times p$ (voir [[Forme échelonnée]]) :
1. s'il existe des lignes de zéros, elles sont toutes en bas ;
2. si deux lignes successives sont non nulles, la seconde a plus de zéros à gauche que la première. (Le poly ajoute que le premier coefficient non nul de chaque ligne vaut 1, ce qui n'est pas obligatoire.)

**Forme totalement échelonnée** (*reduced echelon form*) :
1. elle est échelonnée ;
2. le premier coefficient non nul de chaque ligne vaut 1 ;
3. tous les éléments de la colonne au-dessus de ce 1 sont nuls.

- **Pivot** : premier terme non nul d'une ligne d'une matrice échelonnée.
- **Colonne pivot** (*pivot column*) : colonne qui contient un pivot.
- Si une colonne n'est pas une colonne pivot, la variable $x_i$ associée est **libre**.

> **Théorème (unicité de la forme réduite)** : chaque matrice est équivalente par lignes à une et une seule matrice totalement échelonnée.

> **Théorème** : un système linéaire est incompatible $\iff$ la dernière colonne de sa matrice **augmentée** est une colonne pivot.

**Exemple (système homogène)** : réduire la matrice augmentée, entourer les pivots. Si une colonne de la matrice des **coefficients** n'est pas pivot, la variable est libre et le système a une solution non triviale ; sinon il n'a **que** la [[Système linéaire homogène|solution triviale]].
$$\begin{bmatrix} 2 & -5 & 8 & 0 \\ -2 & -7 & 1 & 0 \\ 4 & 2 & 7 & 0 \end{bmatrix} \sim \begin{bmatrix} 2 & -5 & 8 & 0 \\ 0 & -12 & 9 & 0 \\ 0 & 12 & -9 & 0 \end{bmatrix} \sim \begin{bmatrix} 2 & -5 & 8 & 0 \\ 0 & -12 & 9 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
Pivots $2$ et $-12$ ; $x_3$ est libre, donc il existe une solution non triviale.

## 4. Équations vectorielles (*vector equations*)

Propriétés algébriques de $\mathbb R^n$ : pour tous $\mathbf u, \mathbf v, \mathbf w \in \mathbb R^n$ et scalaires $c, d$ :
1. $\mathbf u + \mathbf v = \mathbf v + \mathbf u$
2. $(\mathbf u + \mathbf v) + \mathbf w = \mathbf u + (\mathbf v + \mathbf w)$
3. $\mathbf u + \mathbf 0 = \mathbf 0 + \mathbf u = \mathbf u$
4. $\mathbf u + (-\mathbf u) = -\mathbf u + \mathbf u = \mathbf 0$, où $-\mathbf u = (-1)\mathbf u$
5. $c(\mathbf u + \mathbf v) = c\mathbf u + c\mathbf v$
6. $(c + d)\mathbf u = c\mathbf u + d\mathbf u$
7. $c(d\mathbf u) = (cd)\mathbf u$
8. $1\mathbf u = \mathbf u$

**[[Combinaison linéaire]]** : $\mathbf y = c_1\mathbf v_1 + \cdots + c_n\mathbf v_n$ est une combinaison linéaire de $\mathbf v_1, \ldots, \mathbf v_n$ de poids (*weights*) $c_1, \ldots, c_n$.

> **Propriété clé** (« ça faut bien capter ») : l'équation vectorielle $x_1\mathbf a_1 + \cdots + x_n\mathbf a_n = \mathbf b$ a le même ensemble de solutions que le système de matrice augmentée $[\mathbf a_1\ \mathbf a_2\ \cdots\ \mathbf a_n\ \mathbf b]$. En particulier, $\mathbf b$ est combinaison linéaire de $\mathbf a_1, \ldots, \mathbf a_n$ si et seulement si ce système a une solution.

**[[Espace engendré]]** (*Span*) : $\text{Span}\{\mathbf v_1, \ldots, \mathbf v_n\}$, aussi noté $L(\mathbf v_1, \ldots, \mathbf v_n)$, est la partie de $\mathbb R^n$ engendrée par les $\mathbf v_i$ : l'ensemble de tous les vecteurs $c_1\mathbf v_1 + \cdots + c_n\mathbf v_n$.

![[Chp 0a - Linear combination - image26.png]]
*Figure : $\text{Span}\{\mathbf v\}$ est une droite passant par l'origine ; $\text{Span}\{\mathbf u, \mathbf v\}$ un plan passant par l'origine (contenant $\mathbf u$, $\mathbf v$, $\mathbf u + \mathbf v$).*

$$\mathbf b \in \text{Span}\{\mathbf v_1, \ldots, \mathbf v_n\} \iff c_1\mathbf v_1 + \cdots + c_n\mathbf v_n = \mathbf b \text{ a une solution} \iff [\mathbf v_1 \cdots \mathbf v_n \mid \mathbf b] \text{ a une solution}$$
et la solution est la même dans les trois cas. $\text{Span}\{\mathbf v_1, \ldots, \mathbf v_p\}$ contient tous les multiples $c\mathbf v_1 = c\mathbf v_1 + 0\mathbf v_2 + \cdots + 0\mathbf v_p$, et en particulier le vecteur nul.

## 5. Équation matricielle $A\mathbf x = \mathbf b$

Idée fondamentale : voir une combinaison linéaire comme le produit d'une matrice par un vecteur.

> **Définition** : si $A$ est $m \times n$, de colonnes $\mathbf a_1, \ldots, \mathbf a_n$, et $\mathbf x \in \mathbb R^n$,
> $$A\mathbf x = [\mathbf a_1\ \mathbf a_2\ \cdots\ \mathbf a_n]\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = x_1\mathbf a_1 + x_2\mathbf a_2 + \cdots + x_n\mathbf a_n.$$
> $A\mathbf x$ n'est défini que si le nombre de colonnes de $A$ égale le nombre de coordonnées de $\mathbf x$.

$A\mathbf x = \mathbf b$ a une solution $\iff$ $\mathbf b$ est combinaison linéaire des colonnes de $A$.

> **Théorème** : $A\mathbf x = \mathbf b$, $x_1\mathbf a_1 + \cdots + x_n\mathbf a_n = \mathbf b$ et $[\mathbf a_1\ \cdots\ \mathbf a_n \mid \mathbf b]$ : ces trois formes ont la même solution.

> **Théorème** (« Let $A$ be a $n \times m$ matrix ») : les propositions suivantes sont équivalentes (toutes vraies ou toutes fausses) :
> 1. pour tout $\mathbf b \in \mathbb R^n$, $A\mathbf x = \mathbf b$ a une solution ;
> 2. tout $\mathbf b \in \mathbb R^n$ est combinaison linéaire des colonnes de $A$ ;
> 3. les colonnes de $A$ engendrent $\mathbb R^m$ (sic, voir « Points à vérifier ») ;
> 4. $A$ a une position pivot dans **chaque ligne**.

**Calcul ligne par ligne** ([[Produit matriciel]]) : la $i$-ème coordonnée de $A\mathbf x$ est la somme des produits des entrées de la ligne $i$ de $A$ par celles de $\mathbf x$. Exemple :
$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} r \\ s \\ t \end{bmatrix} = \begin{bmatrix} 1 \cdot r + 0 \cdot s + 0 \cdot t \\ 0 \cdot r + 1 \cdot s + 0 \cdot t \\ 0 \cdot r + 0 \cdot s + 1 \cdot t \end{bmatrix} = \begin{bmatrix} r \\ s \\ t \end{bmatrix}$$

> **Théorème (linéarité)** : $A$ matrice $m \times n$, $\mathbf u, \mathbf v \in \mathbb R^n$, $c$ scalaire :
> (a) $A(\mathbf u + \mathbf v) = A\mathbf u + A\mathbf v$ ; (b) $A(c\mathbf u) = c(A\mathbf u)$.

**Preuve** (pour $n = 3$, $A = [\mathbf a_1\ \mathbf a_2\ \mathbf a_3]$) :
$$A(\mathbf u + \mathbf v) = (u_1 + v_1)\mathbf a_1 + (u_2 + v_2)\mathbf a_2 + (u_3 + v_3)\mathbf a_3 = (u_1\mathbf a_1 + u_2\mathbf a_2 + u_3\mathbf a_3) + (v_1\mathbf a_1 + v_2\mathbf a_2 + v_3\mathbf a_3) = A\mathbf u + A\mathbf v$$
$$A(c\mathbf u) = (cu_1)\mathbf a_1 + (cu_2)\mathbf a_2 + (cu_3)\mathbf a_3 = c(u_1\mathbf a_1 + u_2\mathbf a_2 + u_3\mathbf a_3) = c(A\mathbf u)$$

## 6. Ensembles de solutions (*solution sets of linear systems*)

- Un système est **homogène** s'il s'écrit $A\mathbf x = \mathbf 0$. Il a toujours au moins la **solution triviale** $\mathbf x = \mathbf 0$ ; la question est de savoir s'il existe une solution non triviale (voir [[Système linéaire homogène]]).
- **Systèmes non homogènes** : quand un système non homogène a plusieurs solutions, la solution générale s'écrit sous **forme vectorielle paramétrique** comme un vecteur **plus** une combinaison linéaire arbitraire de solutions du système homogène associé.

En gros : pour $A\mathbf x = \mathbf 0$, $\mathbf x = t\mathbf v$ ; pour $A\mathbf x = \mathbf b$, $\mathbf x = t\mathbf v + \mathbf p$, où $\mathbf p$ est une solution particulière.

> **Théorème** : si $A\mathbf x = \mathbf b$ est compatible et $\mathbf p$ en est une solution, l'ensemble des solutions de $A\mathbf x = \mathbf b$ est l'ensemble des vecteurs $\mathbf w = \mathbf p + \mathbf v_h$, où $\mathbf v_h$ est une solution quelconque de l'équation homogène $A\mathbf x = \mathbf 0$.

![[Chp 0a - Linear combination - image24.png]]
*Figure : la droite $A\mathbf x = \mathbf b$ (passant par $\mathbf p$, d'équation $\mathbf x = \mathbf p + t\mathbf v$) est parallèle à la droite $A\mathbf x = \mathbf 0$ (passant par l'origine) ; à droite, même chose avec deux plans parallèles.*

**Interprétation géométrique** : ajouter $\mathbf p$ revient à **translater** (*translate*). Si chaque point d'une droite $L$ est translaté de $\mathbf p$, on obtient une droite parallèle à $L$. L'ensemble des solutions de $A\mathbf x = \mathbf b$ est une droite passant par $\mathbf p$, parallèle à l'ensemble des solutions de $A\mathbf x = \mathbf 0$.

![[Chp 0a - Linear combination - image25.png]]
*Figure : parallélogramme $\mathbf 0, \mathbf p, \mathbf v, \mathbf v + \mathbf p$ ; droite $L$ et sa translatée $L + \mathbf p$ ; droites parallèles $A\mathbf x = \mathbf 0$ et $A\mathbf x = \mathbf b$.*

### Vision ligne et vision colonne (*row picture*, *column picture*)

Système $2x + 3y = 5$, $4x + 2y = 6$, soit $\left[\begin{array}{cc|c} 2 & 3 & 5 \\ 4 & 2 & 6 \end{array}\right]$ :
- **Row picture** : tracer les deux droites ; la réponse est leur intersection (en 3D, l'intersection de trois plans).
- **Column picture** : $x\begin{bmatrix} 2 \\ 4 \end{bmatrix} + y\begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ 6 \end{bmatrix}$ : la réponse est la « quantité » de chaque vecteur colonne pour atteindre $(5,6)$ : 1 fois le premier et 1 fois le second.

![[Chp 0a - Linear combination - image3.png]]
*Figure : à gauche, les droites $2x + 3y = 5$ et $4x + 2y = 6$ qui se croisent ; à droite, les vecteurs $(2,4)$ et $(3,2)$ dont la somme donne $(5,6)$.*

- **Infinité de solutions** : $2x + 4y = 6$, $4x + 8y = 12$. Row picture : la même droite. Column picture : $x(2,4) + y(4,8) = (6,12)$, vecteurs colinéaires dont le span n'est qu'une droite ; la cible est dans ce span, d'où une infinité de combinaisons.
- **Aucune solution** : $2x + 4y = 6$, $4x + 8y = 13$. Row picture : droites parallèles. Column picture : $(6,13)$ n'est pas dans le span (une droite) des colonnes colinéaires.

![[Chp 0a - Linear combination - image33.png]]
*Figure : vision ligne et vision colonne des cas « infinité de solutions » et « aucune solution ».*

## 7. Indépendance linéaire (*linear independence*)

> **Définition** : $\{\mathbf v_1, \ldots, \mathbf v_n\}$ est [[Indépendance linéaire|linéairement indépendant]] $\iff$ $x_1\mathbf v_1 + \cdots + x_n\mathbf v_n = \mathbf 0$ n'a que la solution triviale.

**Colonnes d'une matrice** : pour $A = [\mathbf a_1 \cdots \mathbf a_n]$, $A\mathbf x = \mathbf 0$ s'écrit $x_1\mathbf a_1 + \cdots + x_n\mathbf a_n = \mathbf 0$. Toute relation de dépendance entre les colonnes correspond à une solution non triviale de $A\mathbf x = \mathbf 0$. Donc :
$$\text{les colonnes de } A \text{ sont linéairement indépendantes} \iff A\mathbf x = \mathbf 0 \text{ n'a que la solution triviale.}$$

> **Théorème (caractérisation des familles liées)** : $\{\mathbf v_1, \ldots, \mathbf v_n\}$ est linéairement dépendant $\iff$ au moins un des vecteurs est combinaison linéaire des autres.

> **Théorème** : si une famille contient plus de vecteurs que de coordonnées, elle est liée : $\{\mathbf v_1, \ldots, \mathbf v_p\} \subset \mathbb R^n$ est dépendante si $p > n$. Si une matrice a plus de colonnes que de lignes, ses colonnes sont liées.

> **Théorème** : une famille qui contient le vecteur $\mathbf 0$ est liée.

Selon le cours, une colonne pivot est « linéairement indépendante » car le pivot montre qu'elle ne s'exprime pas comme combinaison des autres colonnes ; une colonne non pivot est « linéairement dépendante » (voir « Points à vérifier »).

## 8. Transformations linéaires (*linear transformations*)

$A\mathbf x = \mathbf b$ et $x_1\mathbf a_1 + \cdots + x_n\mathbf a_n = \mathbf b$ sont essentiellement la même chose. Mais $A\mathbf x = \mathbf b$ apparaît aussi (infographie, *computer graphics* ; traitement du signal, *signal processing*) quand on voit $A$ comme un **objet qui agit** (« opère ») sur $\mathbf x$ par multiplication pour produire $A\mathbf x$. Exemple :
$$\begin{bmatrix} 4 & -3 & 1 & 3 \\ 2 & 0 & 5 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 8 \end{bmatrix}, \qquad \begin{bmatrix} 4 & -3 & 1 & 3 \\ 2 & 0 & 5 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 4 \\ -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
La multiplication par $A$ transforme $\mathbf x$ en $\mathbf b$, et $\mathbf u$ en le vecteur nul.

![[Chp 0a - Linear combination - image23.png]]
*Figure : la multiplication par $A$ envoie $\mathbf x \in \mathbb R^4$ sur $\mathbf b \in \mathbb R^2$ et $\mathbf u$ sur $\mathbf 0$.*

**Définition** : une **transformation** (*function*, *mapping*, « application ») $T : \mathbb R^n \to \mathbb R^m$ associe à chaque $\mathbf x \in \mathbb R^n$ un vecteur $T(\mathbf x) \in \mathbb R^m$. $\mathbb R^n$ est le **domaine** (*domain*, [[Ensemble de définition|domaine de définition]]), $\mathbb R^m$ le **codomaine** (*codomain*, ensemble d'arrivée). $T(\mathbf x)$ est l'**image** de $\mathbf x$ ; l'ensemble des images est le **range** (image de $T$), partie du codomaine.

![[Chp 0a - Linear combination - image15.png]]
*Figure : $T$ envoie $\mathbf x$ du domaine $\mathbb R^n$ sur $T(\mathbf x)$ dans le codomaine $\mathbb R^m$ ; le range est une partie du codomaine.*

> **Définition** : $T$ est **linéaire** ([[Transformation linéaire]]) $\iff$
> - $T(\mathbf u + \mathbf v) = T(\mathbf u) + T(\mathbf v)$ ;
> - $T(c\mathbf u) = cT(\mathbf u)$.
>
> Toute transformation matricielle est linéaire. Conséquences : $T(\mathbf 0) = \mathbf 0$ et $T(c\mathbf u + d\mathbf v) = cT(\mathbf u) + dT(\mathbf v)$.

### Transformations linéaires géométriques de $\mathbb R^2$

Tableaux du cours ([[Transformations géométriques du plan]], [[Matrice d'une application linéaire|matrice standard]]) :

| Transformation | Matrice standard |
|---|---|
| Réflexion par rapport à l'axe $x_1$ (symétrie orthogonale d'axe $Ox_1$) | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ |
| Réflexion par rapport à l'axe $x_2$ (d'axe $Ox_2$) | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| Réflexion par rapport à la droite $x_2 = x_1$ | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ |
| Réflexion par rapport à la droite $x_2 = -x_1$ | $\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$ |
| Réflexion par rapport à l'origine (symétrie de centre $O$) | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ |
| Contraction / dilatation horizontale ($0<k<1$ / $k>1$) : $(1,0) \mapsto (k,0)$ | $\begin{bmatrix} k & 0 \\ 0 & 1 \end{bmatrix}$ |
| Contraction / dilatation verticale : $(0,1) \mapsto (0,k)$ | $\begin{bmatrix} 1 & 0 \\ 0 & k \end{bmatrix}$ |
| Cisaillement horizontal (*horizontal shear*, $k<0$ ou $k>0$) : $(0,1) \mapsto (k,1)$ | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ |
| Cisaillement vertical : $(1,0) \mapsto (1,k)$ | $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$ |
| Projection sur l'axe $Ox_1$ (carré unité écrasé sur $[(0,0),(1,0)]$) | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |
| Projection sur l'axe $Ox_2$ | $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ |

![[Chp 0a - Linear combination - image9.png]]
*Figure : Table 1, réflexions, avec l'image du carré unité et des libellés rouges en français (voir « Points à vérifier »).*

![[Chp 0a - Linear combination - image28.png]]
*Figure : Tables 2 et 3, contractions et dilatations, cisaillements.*

![[Chp 0a - Linear combination - image10.png]]
*Figure : Table 4, projections sur les axes.*

### Surjectivité et injectivité

> **Définition** : $T : \mathbb R^n \to \mathbb R^m$ est **surjective** (*onto* $\mathbb R^m$) si chaque $\mathbf b \in \mathbb R^m$ est l'image d'**au moins un** $\mathbf x \in \mathbb R^n$ (voir [[Injectivité et surjectivité]]).

![[Chp 0a - Linear combination - image16.png]]
*Figure : $T$ non surjective (le range n'est qu'une partie de $\mathbb R^m$) et $T$ surjective (le range est $\mathbb R^m$).*

> **Définition** : $T$ est **injective** (*one-to-one*) si chaque $\mathbf b \in \mathbb R^m$ est l'image d'**au plus un** $\mathbf x \in \mathbb R^n$.

![[Chp 0a - Linear combination - image6.png]]
*Figure : $T$ non injective (plusieurs points, dont un groupe contenant $\mathbf 0$, envoyés sur un même point) et $T$ injective.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Théorème « Let A be a nxm matrix »** : il mélange les dimensions, avec $\mathbf{b}$ dans $\mathbb{R}^n$ puis des colonnes qui engendrent $\mathbb{R}^m$. Avec $A$ de taille $n \times m$, les colonnes sont dans $\mathbb{R}^n$ : il faudrait lire $\mathbb{R}^n$ partout (complément, le cours ne le dit pas).
2. **Tableau des réflexions** : image lue directement, deux libellés rouges ne correspondent pas à leur ligne. « Reflection through the line $x_2 = x_1$ » apparaît deux fois, dont une avec le libellé « d'axe $x_2 = -x_1$ », et « Reflection through the line $x_2 = -x_1$ » porte le libellé « d'axe $Ox_2$ ». Les matrices et le texte anglais restent cohérents. Tu as déjà coché ce point dans ta liste, sans que je connaisse ta conclusion. (Le tableau de cette fiche suit le texte anglais et les matrices.)
3. **Colonnes pivots** : « une colonne pivot est linéairement indépendante » est imprécis, car l'indépendance concerne un ensemble de vecteurs. Plus juste : une colonne non pivot est combinaison des colonnes précédentes (complément).
4. **Théorème sur les solutions** : la phrase « **w** = **p** + **v_h** is any solution » a perdu un mot. Il faut lire « où **v_h** est une solution quelconque de $A\mathbf{x} = \mathbf{0}$ ». De même, $\mathbf{x} = t\mathbf{v}$ ne décrit que le cas d'une seule variable libre.
5. **Définition du pivot** : le cours écrit « premier terme non nul d'une matrice échelonnée » ; il s'agit du premier terme non nul de chaque **ligne** (complément).
