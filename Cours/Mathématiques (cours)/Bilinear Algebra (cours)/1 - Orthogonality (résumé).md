---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/chp 1 - Orthogonality.docx|chp 1 - Orthogonality]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Bilinear Algebra/chp 1 - Orthogonality.docx|chp 1 - Orthogonality]], dans [[Bilinear Algebra (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre part du [[Produit scalaire]] pour mesurer longueurs, distances et angles droits. Il en tire un outil central, la [[Projection orthogonale]], puis trois applications : le [[Procédé de Gram-Schmidt]], la [[Factorisation QR]] et les [[Moindres carrés]], qui mènent à la [[Régression linéaire]].

## 1. Produit intérieur et produit scalaire (*inner product and dot product*)

Pour $\mathbf u$ et $\mathbf v$ vecteurs (donc matrices colonnes) :
- $\langle \mathbf u, \mathbf v \rangle$ est le produit intérieur (*inner product*) ;
- $\mathbf u^T\mathbf v$ est la même chose que $\mathbf u \cdot \mathbf v$ (*dot product*) ;
- un dot product est un inner product, mais un inner product n'est pas forcément un dot product.

> **Définition (dot product)** : pour $\mathbf x = (x_1, \ldots, x_n)$ et $\mathbf y = (y_1, \ldots, y_n)$ de $\mathbb R^n$,
> $$\mathbf x \cdot \mathbf y = x_1y_1 + \cdots + x_ny_n.$$

Interprétation géométrique : $\mathbf u \cdot \mathbf v = \|\mathbf u\|\,\|\mathbf v\|\cos\theta$. Le résultat est un **scalaire**.

![[chp 1 - Orthogonality - image32.png]]
*Figure : vecteurs $\mathbf u = (u_1,u_2)$ et $\mathbf v = (v_1,v_2)$ issus de l'origine, séparés par l'angle $\vartheta$ ; le troisième côté du triangle est $\mathbf u - \mathbf v$.*

**Propriétés** : pour $\mathbf u, \mathbf v, \mathbf w \in \mathbb R^n$ et $c$ scalaire :
- a. $\mathbf u \cdot \mathbf v = \mathbf v \cdot \mathbf u$ ;
- b. $(\mathbf u + \mathbf v) \cdot \mathbf w = \mathbf u \cdot \mathbf w + \mathbf v \cdot \mathbf w$ ;
- c. $(c\mathbf u) \cdot \mathbf v = c(\mathbf u \cdot \mathbf v) = \mathbf u \cdot (c\mathbf v)$ ;
- d. $\mathbf u \cdot \mathbf u \ge 0$, et $\mathbf u \cdot \mathbf u = 0 \iff \mathbf u = \mathbf 0$.

En combinant (b) et (c) : $(c_1\mathbf u_1 + \cdots + c_p\mathbf u_p) \cdot \mathbf w = c_1(\mathbf u_1 \cdot \mathbf w) + \cdots + c_p(\mathbf u_p \cdot \mathbf w)$.

**Propriétés de base d'un inner product** (extrait « 6.7 » d'un autre manuel, sur un corps $\mathbf F$) :
- (a) pour $u \in V$ fixé, $v \mapsto \langle v, u \rangle$ est une [[Transformation linéaire|application linéaire]] de $V$ dans $\mathbf F$ ;
- (b) $\langle 0, u \rangle = 0$ ; (c) $\langle u, 0 \rangle = 0$ pour tout $u$ ;
- (d) $\langle u, v + w \rangle = \langle u, v \rangle + \langle u, w \rangle$ ;
- (e) $\langle u, \lambda v \rangle = \bar\lambda\langle u, v \rangle$ (conjugué de $\lambda$, cas complexe).

## 2. Longueur d'un vecteur (*length*)

> La **longueur** ou [[Norme|norme]] de $\mathbf v$ est le scalaire positif
> $$\|\mathbf v\| = \sqrt{\mathbf v \cdot \mathbf v} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}, \qquad \|\mathbf v\|^2 = \mathbf v \cdot \mathbf v.$$

Remarque du cours : $\mathbf v \cdot \mathbf v$ n'est pas négatif car $\mathbf v$ est réel ; dans $\mathbb C$, $\mathbf v \cdot \mathbf v$ pourrait être négatif et la norme ne serait pas définie ainsi.

> $\|c\mathbf v\| = |c|\,\|\mathbf v\|$.

## 3. Vecteur unitaire et normalisation

- Si $\|\mathbf u\| = 1$, $\mathbf u$ est un [[Vecteur unitaire|vecteur unitaire]] (*unit vector*).
- Pour obtenir un vecteur unitaire à partir de $\mathbf v \neq \mathbf 0$ : $\mathbf u = \frac{1}{\|\mathbf v\|}\mathbf v$ (le cours écrit « $\frac{1}{\|\mathbf v\|}\|\mathbf v\|$ » et « $\mathbf u = x\mathbf v$ », voir « Points à vérifier »).

## 4. Distance dans $\mathbb R^n$

> Pour $\mathbf u, \mathbf v \in \mathbb R^n$, la [[Distance|distance]] entre $\mathbf u$ et $\mathbf v$ est la longueur de $\mathbf u - \mathbf v$ :
> $$\text{dist}(\mathbf u, \mathbf v) = \|\mathbf u - \mathbf v\|.$$

![[chp 1 - Orthogonality - image31.png]]
*Figure : la distance entre $\mathbf u$ et $\mathbf v$ est la longueur de $\mathbf u - \mathbf v$ ; parallélogramme formé avec $-\mathbf v$ et $\mathbf u - \mathbf v$.*

- Dans $\mathbb R^2$ et $\mathbb R^3$, cette définition coïncide avec la distance euclidienne usuelle.
- La distance de $\mathbf u$ à $\mathbf v$ est la même que celle de $\mathbf u - \mathbf v$ à $\mathbf 0$ (parallélogramme).

## 5. Orthogonalité

Deux droites (en bleu sur la figure) sont géométriquement perpendiculaires si et seulement si la distance de $\mathbf u$ à $\mathbf v$ est égale à la distance de $\mathbf u$ à $-\mathbf v$, ce qui revient à égaler les carrés de ces distances.

![[chp 1 - Orthogonality - image9.png]]
*Figure : deux droites sécantes en $\mathbf 0$, l'une par $\mathbf u$, l'autre par $\mathbf v$ et $-\mathbf v$ ; distances $\|\mathbf u - \mathbf v\|$ et $\|\mathbf u - (-\mathbf v)\|$.*

> $\mathbf u$ est [[Orthogonalité|orthogonal]] à $\mathbf v$ $\iff \mathbf u \cdot \mathbf v = 0$.
> - Le vecteur nul est orthogonal à tout vecteur, car $\mathbf 0^T\mathbf v = 0$.
> - $\mathbf 0$ est le seul vecteur orthogonal à lui-même.

![[chp 1 - Orthogonality - image2.png]]
*Figure : triangle de sommets $\mathbf 0$, $\mathbf u$, $\mathbf u + \mathbf v$, de côtés $\|\mathbf u\|$, $\|\mathbf v\|$, $\|\mathbf u + \mathbf v\|$.*

> **Théorème 2 ([[Théorème de Pythagore]])** : $\mathbf u$ et $\mathbf v$ sont orthogonaux si et seulement si $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2$.

## 6. Compléments orthogonaux (*orthogonal complements*)

- Si $\mathbf u$ est orthogonal à **tout** vecteur d'un [[Sous-espace vectoriel|sous-espace]] $W$ de $\mathbb R^n$, $\mathbf u$ est orthogonal à $W$.
- L'ensemble des vecteurs orthogonaux à $W$ est le [[Complément orthogonal|complément orthogonal]] $W^\perp$.
- $W^\perp$ est un sous-espace de $\mathbb R^n$.

**Exemple** : soit $W$ un plan passant par l'origine dans $\mathbb R^3$ et $L$ la droite passant par l'origine et perpendiculaire à $W$. Si $\mathbf z \in L$ et $\mathbf w \in W$ sont non nuls, le segment de $\mathbf 0$ à $\mathbf z$ est perpendiculaire au segment de $\mathbf 0$ à $\mathbf w$ : $\mathbf z \cdot \mathbf w = 0$. Chaque vecteur de $L$ est orthogonal à tout $\mathbf w$ de $W$. En fait $L$ est formée de **tous** les vecteurs orthogonaux aux $\mathbf w$ de $W$, et inversement : $L = W^\perp$ et $W = L^\perp$.

![[chp 1 - Orthogonality - image7.png]]
*Figure : un plan et une droite passant par $\mathbf 0$, compléments orthogonaux l'un de l'autre.*

> **Théorème 3** : soit $A$ de taille $m \times n$. Le complément orthogonal du [[Sous-espaces fondamentaux|row space]] de $A$ est le [[Espace nul|null space]] de $A$, et le complément orthogonal du [[Espace des colonnes|column space]] de $A$ est le null space de $A^T$ :
> $$(\text{Row}\,A)^\perp = \text{Nul}\,A \qquad (\text{Col}\,A)^\perp = \text{Nul}\,A^T.$$

![[chp 1 - Orthogonality - image4.png]]
*Figure : les sous-espaces fondamentaux d'une matrice $m \times n$ : Row $A$ et Nul $A$ perpendiculaires en $\mathbf 0$ (à gauche), Col $A$ et Nul $A^T$ perpendiculaires (à droite), reliés par $A$.*

**Exemple** : $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$.
- Row space : plan 2D de $\mathbb R^3$ engendré par $r_1 = (1,2,3)$ et $r_2 = (4,5,6)$.
- Null space ($A\mathbf x = \mathbf 0$) : la droite engendrée par $\mathbf x = (1,-2,1)$, perpendiculaire au row space.
- Column space : $a_1 = (1,4)$, $a_2 = (2,5)$, $a_3 = (3,6)$ engendrent tout le plan $\mathbb R^2$.
- Left null space : $A^T\mathbf w = w_1(1,2,3) + w_2(4,5,6) = \mathbf 0 \Rightarrow (w_1, w_2) = (0,0)$ : $\text{Nul}\,A^T$ est le sous-espace nul.

![[chp 1 - Orthogonality - image30.png]]
*Figure : le row space (plan engendré par $r_1$, $r_2$) et le vecteur $\mathbf x = (1,-2,1)$ qui lui est perpendiculaire.*

![[chp 1 - Orthogonality - image28.png]]
*Figure : les colonnes $a_1$, $a_2$, $a_3$ engendrent le plan entier, le column space.*

## 7. Familles orthogonales (*orthogonal set*)

$\{\mathbf u_1, \ldots, \mathbf u_p\} \subset \mathbb R^n$ est une [[Famille orthogonale|famille orthogonale]] si ses vecteurs sont deux à deux orthogonaux.

> **Théorème** : si $S = \{\mathbf u_1, \ldots, \mathbf u_p\}$ est une famille orthogonale de vecteurs **non nuls**, alors $S$ est [[Indépendance linéaire|linéairement indépendante]], donc une [[Base (algèbre linéaire)|base]] du sous-espace [[Espace engendré|engendré]] par $S$.

> **Théorème** : soit $\{\mathbf u_1, \ldots, \mathbf u_p\}$ une base orthogonale d'un sous-espace $W$ de $\mathbb R^n$. Pour tout $\mathbf y \in W$, les poids de la [[Combinaison linéaire|combinaison linéaire]] $\mathbf y = c_1\mathbf u_1 + \cdots + c_p\mathbf u_p$ sont
> $$c_j = \frac{\mathbf y \cdot \mathbf u_j}{\mathbf u_j \cdot \mathbf u_j} \quad (j = 1, \ldots, p).$$

Cas $W = \mathbb R^2 = \text{Span}\{\mathbf u_1, \mathbf u_2\}$ avec $\mathbf u_1 \perp \mathbf u_2$ :
$$\mathbf y = \frac{\mathbf y \cdot \mathbf u_1}{\mathbf u_1 \cdot \mathbf u_1}\mathbf u_1 + \frac{\mathbf y \cdot \mathbf u_2}{\mathbf u_2 \cdot \mathbf u_2}\mathbf u_2 \quad (3)$$
Le théorème décompose chaque $\mathbf y$ de $\text{Span}\{\mathbf u_1, \ldots, \mathbf u_p\}$ en somme de $p$ projections sur des sous-espaces de dimension 1, deux à deux orthogonaux.

![[chp 1 - Orthogonality - image3.png]]
*Figure : $\mathbf y$ décomposé en $\hat{\mathbf y}_1$ (projection sur $\mathbf u_1$) plus $\hat{\mathbf y}_2$ (projection sur $\mathbf u_2$).*

## 8. Familles orthonormées (*orthonormal set*)

- Famille orthonormée = famille orthogonale de vecteurs normés, $\|\mathbf u_i\| = 1$.

> Une matrice $U$ de taille $m \times n$ a des colonnes orthonormées $\iff U^TU = I$.

> Si $U$ ($m \times n$) a des colonnes orthonormées et $\mathbf x, \mathbf y \in \mathbb R^n$ :
> - $\|U\mathbf x\| = \|\mathbf x\|$ ;
> - $(U\mathbf x) \cdot (U\mathbf y) = \mathbf x \cdot \mathbf y$ ;
> - $(U\mathbf x) \cdot (U\mathbf y) = 0 \iff \mathbf x \cdot \mathbf y = 0$.
>
> L'application $\mathbf x \mapsto U\mathbf x$ conserve les longueurs et l'orthogonalité.

## 9. Projection orthogonale (*orthogonal projection*)

![[chp 1 - Orthogonality - image40.png]]
*Figure : un plan $W$ contenant $\mathbf 0$, $\mathbf u$ et $\alpha\mathbf u$ ; $\mathbf y$ au-dessus du plan, son projeté $\hat{\mathbf y} = \text{proj}_W\,\mathbf y$ et $\mathbf z = \mathbf y - \hat{\mathbf y}$ perpendiculaire au plan (texte de l'image coupé).*

**Projection sur un vecteur.** Soit $\mathbf u \neq \mathbf 0$ dans $\mathbb R^n$. On veut écrire $\mathbf y \in \mathbb R^n$ comme somme d'un multiple de $\mathbf u$ et d'un vecteur orthogonal à $\mathbf u$ : $\mathbf y = \hat{\mathbf y} + \mathbf z$, avec
- $\hat{\mathbf y} = \alpha\mathbf u$, la [[Projection orthogonale|projection orthogonale]] de $\mathbf y$ sur $\mathbf u$ ;
- $\mathbf z \perp \mathbf u$, la composante de $\mathbf y$ orthogonale à $\mathbf u$.

$$\alpha = \frac{\mathbf y \cdot \mathbf u}{\mathbf u \cdot \mathbf u}, \qquad \hat{\mathbf y} = \frac{\mathbf y \cdot \mathbf u}{\mathbf u \cdot \mathbf u}\mathbf u, \qquad \mathbf z = \mathbf y - \hat{\mathbf y}.$$

- On note $\hat{\mathbf y} = \text{proj}_W\,\mathbf y$.
- $\hat{\mathbf y}$ est l'**unique** vecteur de $W$ tel que $\mathbf y - \hat{\mathbf y}$ soit orthogonal à $W$.
- $\hat{\mathbf y}$ est l'**unique** vecteur de $W$ le plus proche de $\mathbf y$.
- La projection de $\mathbf y$ sur $\mathbf u$ est la même que sur $c\mathbf u$ : elle ne dépend que du sous-espace $L$ engendré par $\mathbf u$.

> **Théorème de décomposition orthogonale** (*The Orthogonal Decomposition Theorem*) : soit $W$ un sous-espace de $\mathbb R^n$. Tout $\mathbf y \in \mathbb R^n$ s'écrit de façon **unique**
> $$\mathbf y = \hat{\mathbf y} + \mathbf z \quad (1)$$
> avec $\hat{\mathbf y} \in W$ et $\mathbf z \in W^\perp$. Si $\{\mathbf u_1, \ldots, \mathbf u_p\}$ est **une** base orthogonale de $W$ :
> $$\hat{\mathbf y} = \frac{\mathbf y \cdot \mathbf u_1}{\mathbf u_1 \cdot \mathbf u_1}\mathbf u_1 + \cdots + \frac{\mathbf y \cdot \mathbf u_p}{\mathbf u_p \cdot \mathbf u_p}\mathbf u_p \quad (2)$$
> et $\mathbf z = \mathbf y - \hat{\mathbf y}$.
>
> Il n'est pas nécessaire d'avoir une base orthogonale de $\mathbb R^n$ : une base orthogonale de $W$ suffit. L'unicité de (1) montre que $\hat{\mathbf y}$ ne dépend que de $W$, pas de la base choisie.

Si $\mathbf y$ est déjà dans $W = \text{Span}\{\mathbf u_1, \ldots, \mathbf u_p\}$, alors $\text{proj}_W\,\mathbf y = \mathbf y$.

> **Théorème de décomposition orthonormée** (*Orthonormal Decomposition Theorem*) : si $\{\mathbf u_1, \ldots, \mathbf u_p\}$ est une **base orthonormée** de $W$,
> $$\text{proj}_W\,\mathbf y = (\mathbf y \cdot \mathbf u_1)\mathbf u_1 + (\mathbf y \cdot \mathbf u_2)\mathbf u_2 + \cdots + (\mathbf y \cdot \mathbf u_p)\mathbf u_p \quad (4)$$
> et, avec $U = [\mathbf u_1\ \mathbf u_2\ \cdots\ \mathbf u_p]$,
> $$\text{proj}_W\,\mathbf y = UU^T\mathbf y \quad \text{pour tout } \mathbf y \in \mathbb R^n. \quad (5)$$
>
> Preuve (« not in the exams ») : (4) découle de (2) ; (4) montre que $\text{proj}_W\,\mathbf y$ est combinaison des colonnes de $U$ avec les poids $\mathbf y \cdot \mathbf u_j = \mathbf u_j^T\mathbf y$, qui sont les coefficients de $U^T\mathbf y$, d'où (5).

**Interprétation géométrique.** Quand $W$ est de dimension 1, (2) n'a qu'un terme. Quand $\dim W > 1$, chaque terme de (2) est la projection orthogonale de $\mathbf y$ sur la droite engendrée par un des $\mathbf u_j$. Ainsi $\hat{\mathbf y} = \hat{\mathbf y}_1 + \hat{\mathbf y}_2$ pour $W$ engendré par $\mathbf u_1$, $\mathbf u_2$ dans $\mathbb R^3$ : **la projection orthogonale de $\mathbf y$ est la somme de ses projections sur des sous-espaces de dimension 1 deux à deux orthogonaux.**

![[chp 1 - Orthogonality - image37.png]]
*Figure : dans $\mathbb R^3$, $\mathbf y$ projeté sur le plan engendré par $\mathbf u_1$ et $\mathbf u_2$ ; les projections $\hat{\mathbf y}_1$ et $\hat{\mathbf y}_2$ sur les deux droites s'additionnent en $\hat{\mathbf y}$.*

> **Théorème de la meilleure approximation** (*the best approximation*) : $W$ sous-espace de $\mathbb R^n$, $\mathbf y \in \mathbb R^n$. $\hat{\mathbf y}$ est le point de $W$ le plus proche de $\mathbf y$ :
> $$\|\mathbf y - \hat{\mathbf y}\| < \|\mathbf y - \mathbf v\| \quad \text{pour tout } \mathbf v \in W,\ \mathbf v \neq \hat{\mathbf y}.$$
> $\hat{\mathbf y}$ est la meilleure approximation de $\mathbf y$ par des éléments de $W$.

## 10. Matrice orthogonale

- Toute matrice **carrée** à colonnes ortho**normées** est une matrice ortho**gonale** ([[Matrice orthogonale]]).
- Une matrice orthogonale a aussi des lignes orthonormées.
- Une matrice orthogonale est inversible et $U^{-1} = U^T$.

## 11. Procédé de Gram-Schmidt et factorisation QR

Si $V$ est un [[Espace vectoriel|espace vectoriel]] de dimension $p \ge 1$, toute famille libre de $p$ vecteurs de $V$ est automatiquement une base de $V$, car elle engendre $V$.

Le procédé transforme une famille de vecteurs linéairement **indépendants** en une famille orthogonale (ou orthonormée, si on normalise).

> **[[Procédé de Gram-Schmidt]]** : soit $\{\mathbf x_1, \ldots, \mathbf x_p\}$ une base d'un sous-espace non nul $W$ de $\mathbb R^n$. On pose
> $$\begin{aligned}
> \mathbf v_1 &= \mathbf x_1 \\
> \mathbf v_2 &= \mathbf x_2 - \frac{\mathbf x_2 \cdot \mathbf v_1}{\mathbf v_1 \cdot \mathbf v_1}\mathbf v_1 \\
> \mathbf v_3 &= \mathbf x_3 - \frac{\mathbf x_3 \cdot \mathbf v_1}{\mathbf v_1 \cdot \mathbf v_1}\mathbf v_1 - \frac{\mathbf x_3 \cdot \mathbf v_2}{\mathbf v_2 \cdot \mathbf v_2}\mathbf v_2 \\
> &\ \ \vdots \\
> \mathbf v_p &= \mathbf x_p - \frac{\mathbf x_p \cdot \mathbf v_1}{\mathbf v_1 \cdot \mathbf v_1}\mathbf v_1 - \cdots - \frac{\mathbf x_p \cdot \mathbf v_{p-1}}{\mathbf v_{p-1} \cdot \mathbf v_{p-1}}\mathbf v_{p-1}
> \end{aligned}$$
> Alors $\{\mathbf v_1, \ldots, \mathbf v_p\}$ est une base orthogonale de $W$, et
> $$\text{Span}\{\mathbf v_1, \ldots, \mathbf v_k\} = \text{Span}\{\mathbf x_1, \ldots, \mathbf x_k\} \quad \text{pour } 1 \le k \le p. \quad (1)$$

Si $A$ ($m \times n$) a des colonnes linéairement indépendantes $\mathbf x_1, \ldots, \mathbf x_n$, appliquer Gram-Schmidt (avec **normalisation**) revient à factoriser $A$.

> **[[Factorisation QR]]** : si $A$ ($m \times n$) a des colonnes linéairement indépendantes, $A = QR$, où
> - $Q$ est $m \times n$ et ses colonnes forment une base orthonormée de $\text{Col}\,A$ ;
> - $R$ est $n \times n$, triangulaire supérieure, [[Matrice inversible|inversible]], à coefficients diagonaux positifs.

Schéma du cours pour $A = [\mathbf a_1\ \mathbf a_2\ \mathbf a_3]$ et $Q = [\mathbf e_1\ \mathbf e_2\ \mathbf e_3]$ (vecteurs unitaires orthogonaux) :
$$R = \begin{bmatrix} \mathbf e_1^T\mathbf a_1 & \mathbf e_1^T\mathbf a_2 & \mathbf e_1^T\mathbf a_3 \\ 0 & \mathbf e_2^T\mathbf a_2 & \mathbf e_2^T\mathbf a_3 \\ 0 & 0 & \mathbf e_3^T\mathbf a_3 \end{bmatrix}$$

![[chp 1 - Orthogonality - image12.png]]
*Figure : schéma $A = QR$, avec $Q$ formée des vecteurs unitaires orthogonaux $\mathbf e_i$ et $R$ triangulaire supérieure (légendée « upper diagonal matrix », voir « Points à vérifier »).*

## 12. Problème des moindres carrés (*least square problem*)

- Parfois $A\mathbf x = \mathbf b$ n'a pas de solution ; le mieux est alors de trouver un $\mathbf x$ qui rend $A\mathbf x$ aussi proche que possible de $\mathbf b$.
- Le problème des [[Moindres carrés|moindres carrés]] consiste à trouver $\mathbf x$ qui rend $\|\mathbf b - A\mathbf x\|$ aussi petit que possible (le cours écrit « the smallest distance is $\|\mathbf b - A\mathbf x\|$ », voir « Points à vérifier »).

> **Définition** : si $A$ est $m \times n$ et $\mathbf b \in \mathbb R^m$, une **solution au sens des moindres carrés** (*least-squares solution*) de $A\mathbf x = \mathbf b$ est un $\hat{\mathbf x} \in \mathbb R^n$ tel que
> $$\|\mathbf b - A\hat{\mathbf x}\| \le \|\mathbf b - A\mathbf x\| \quad \text{pour tout } \mathbf x \in \mathbb R^n.$$

![[chp 1 - Orthogonality - image15.png]]
*Figure : le plan $\text{Col}\,A$ contient $\mathbf 0$, $A\hat{\mathbf x}$, $A\mathbf x_1$, $A\mathbf x_2$ ; $\mathbf b$ est hors du plan et $A\hat{\mathbf x}$ en est la projection orthogonale.*

- Le cours écrit : « $\hat{\mathbf x}$ est le projeté orthogonal de $\mathbf b$ sur Col $A$ » ; la figure montre que c'est $A\hat{\mathbf x}$ (voir « Points à vérifier »).
- Quel que soit $\mathbf x$, $A\mathbf x$ est forcément dans $\text{Col}\,A$.
- Si $\mathbf b$ est dans $\text{Col}\,A$, alors $\mathbf b = A\mathbf x$ pour un $\mathbf x$, et ce $\mathbf x$ est une solution des moindres carrés.
- $\|\mathbf b - A\hat{\mathbf x}\|$ est l'**erreur des moindres carrés** (*least-square error*).

> **Théorème (équations normales)** : l'ensemble des solutions des moindres carrés de $A\mathbf x = \mathbf b$ coïncide avec l'ensemble (non vide) des solutions des **équations normales**
> $$A^TA\mathbf x = A^T\mathbf b.$$
> (Annotation : « Read it by yourselves ».)

> **Théorème** : $A$ de taille $m \times n$. Sont équivalents :
> a. $A\mathbf x = \mathbf b$ a une **unique** solution des moindres carrés pour tout $\mathbf b \in \mathbb R^m$ ;
> b. les colonnes de $A$ sont linéairement indépendantes ;
> c. $A^TA$ est inversible.
>
> Dans ce cas,
> $$\hat{\mathbf x} = (A^TA)^{-1}A^T\mathbf b. \quad (4)$$

## 13. Application aux modèles linéaires (*application to linear models*)

En statistique, au lieu de $A\mathbf x = \mathbf b$ on écrit $X\boldsymbol\beta = \mathbf y$ (voir [[Régression linéaire]]) :
- $X$ est la **matrice du plan d'expérience** (*design matrix*) ;
- $\boldsymbol\beta$ est le **vecteur des paramètres** (*parameter vector*) ;
- $\mathbf y$ est le **vecteur des observations** (*observation vector*).

La relation la plus simple entre $x$ et $y$ est $y = \beta_0 + \beta_1 x$ (au lieu de $y = mx + b$). Des données expérimentales $(x_1, y_1), \ldots, (x_n, y_n)$ semblent souvent proches d'une droite ; on veut déterminer $\beta_0$ et $\beta_1$ pour que la droite soit aussi « proche » que possible des points.

Pour $\beta_0$, $\beta_1$ fixés et chaque point $(x_j, y_j)$, il y a un point $(x_j, \beta_0 + \beta_1 x_j)$ de la droite de même abscisse. $y_j$ est la valeur **observée**, $\beta_0 + \beta_1 x_j$ la valeur **prédite** ; leur différence est un **résidu** (*residual*, [[Résidu (régression)]]).

![[chp 1 - Orthogonality - image38.png]]
*Figure : ajustement d'une droite $y = \beta_0 + \beta_1 x$ à des données expérimentales ; les résidus sont les écarts verticaux entre « data point » $(x_j, y_j)$ et « point on line » $(x_j, \beta_0 + \beta_1 x_j)$.*

- Pour mesurer la proximité de la droite aux données, on additionne les carrés des résidus.
- La **droite des moindres carrés** (*least square line*) est celle qui minimise la somme des carrés des résidus.
- On l'appelle aussi **droite de régression de $y$ en $x$** (*line of regression of y on x*), car on suppose les erreurs uniquement sur les ordonnées.
- $\beta_0$ et $\beta_1$ sont les **coefficients de régression** (*regression coefficients*).

**Lien avec $X\boldsymbol\beta = \mathbf y$** : si les points ne sont pas alignés, aucun $(\beta_0, \beta_1)$ ne rend les valeurs prédites $X\boldsymbol\beta$ égales aux valeurs observées $\mathbf y$ : $X\boldsymbol\beta = \mathbf y$ n'a pas de solution. C'est un problème de moindres carrés $A\mathbf x = \mathbf b$ avec d'autres notations. Le carré de la distance entre $X\boldsymbol\beta$ et $\mathbf y$ est exactement la somme des carrés des résidus ; le $\boldsymbol\beta$ qui minimise cette somme minimise aussi cette distance. *Calculer la solution des moindres carrés de $X\boldsymbol\beta = \mathbf y$ revient à trouver la droite des moindres carrés.*

![[chp 1 - Orthogonality - image13.png]]
*Figure : texte du manuel reliant $X\boldsymbol\beta = \mathbf y$ aux moindres carrés, avec la figure 1 (droite ajustée et résidus).*

Le cours ne donne pas ici la forme explicite de $X$ ; avec le modèle $y = \beta_0 + \beta_1 x$, elle a une première colonne de 1 et une seconde colonne des $x_j$ (complément).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Ces remarques comparent son texte à ses images, ou à son propre raisonnement.

1. **Projeté de $\mathbf{b}$** : le texte dit que $\hat{\mathbf{x}}$ est le projeté orthogonal de $\mathbf{b}$ sur Col $A$. La figure du cours montre que c'est $A\hat{\mathbf{x}}$. D'ailleurs, $\hat{\mathbf{x}}$ est dans $\mathbb{R}^n$, alors que Col $A$ est dans $\mathbb{R}^m$. Le wiki suit la figure.
2. **Normalisation** : l'image donne $\frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\|$ et le texte écrit $\mathbf{u} = x\mathbf{v}$. Telle quelle, cette expression vaut 1, donc $\mathbf{u} = \mathbf{v}$. Le coefficient attendu est $\frac{1}{\|\mathbf{v}\|}$ (complément, le cours ne le dit pas sous cette forme). Le texte exact de l'image reste à interpréter.
3. **Application to linear models** : « determine β1 and β1 » doit se lire β0 et β1.
4. **Distance minimale** : « the smallest distance is $\|\mathbf{b} - A\mathbf{x}\|$ » ne vaut que pour $\mathbf{x} = \hat{\mathbf{x}}$, comme le dit plus loin le cours avec la least-square error.
5. **Figure QR** : sa légende dit « upper diagonal matrix », alors que le théorème et le contenu de la figure indiquent une matrice triangulaire supérieure.
6. **Images coupées** : la figure de la projection orthogonale (« Given any sca… », « That is, (1… ») et la figure de la distance (rectangle jaune illisible) sont coupées ; leurs mentions « À vérifier » sont reprises ici.
7. **Note de bas de page de la figure 1** : le manuel écrit « for for » (doublon) ; et la note de cours écrit $y = \beta_0 + \beta_1 x_1$ avec un indice inutile sur $x$.
8. **Propriétés « 6.7 » de l'inner product** : elles viennent d'un autre manuel, sur un corps $\mathbf F$ qui peut être $\mathbb C$ (d'où le conjugué $\bar\lambda$) ; le reste du chapitre est sur $\mathbb R$.
