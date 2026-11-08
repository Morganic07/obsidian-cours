---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/chp 1 - Orthogonality.docx|chp 1 - Orthogonality]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/chp 1 - Orthogonality.docx|chp 1 - Orthogonality]], dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Idée générale

Le chapitre part du [[Produit scalaire]] pour mesurer longueurs, distances et angles droits. Il en tire un outil central, la [[Projection orthogonale]], puis trois applications : le [[Procédé de Gram-Schmidt]], la [[Factorisation QR]] et les [[Moindres carrés]], qui mènent à la [[Régression linéaire]].

## 1. Produit intérieur et produit scalaire (*inner product and dot product*)

Pour $\mathbf u$ et $\mathbf v$ vecteurs (donc matrices colonnes) :
- $\langle \mathbf u, \mathbf v \rangle$ est le produit intérieur (*inner product*) ;
- $\mathbf u^T\mathbf v$ est la même chose que $\mathbf u \cdot \mathbf v$ (*dot product*) ;
- un dot product est un inner product, mais un inner product n'est pas forcément un dot product.

Un **inner product** sur un espace vectoriel réel $V$ est toute application $(\mathbf u, \mathbf v) \mapsto \langle \mathbf u, \mathbf v \rangle \in \mathbb R$ symétrique, linéaire par rapport à chaque argument et **définie positive** ($\langle \mathbf u, \mathbf u \rangle > 0$ pour $\mathbf u \neq \mathbf 0$) : ce sont exactement les propriétés a à d ci-dessous, prises comme axiomes. Le dot product n'en est qu'un exemple. Autres exemples classiques : le produit pondéré $\langle \mathbf u, \mathbf v \rangle = w_1u_1v_1 + \cdots + w_nu_nv_n$ avec des poids $w_i > 0$, ou, sur les fonctions continues sur $[a, b]$, $\langle f, g \rangle = \int_a^b f(t)g(t)\,dt$. Tout ce chapitre (norme, distance, orthogonalité, projection, Gram-Schmidt) reste valable avec n'importe quel inner product. [[Complément hors du cours|ⓘ]]

> **Définition (dot product)** : pour $\mathbf x = (x_1, \ldots, x_n)$ et $\mathbf y = (y_1, \ldots, y_n)$ de $\mathbb R^n$,
> $$\mathbf x \cdot \mathbf y = x_1y_1 + \cdots + x_ny_n.$$

Interprétation géométrique : $\mathbf u \cdot \mathbf v = \|\mathbf u\|\,\|\mathbf v\|\cos\theta$. Le résultat est un **scalaire**.

Lue à l'envers, cette formule donne l'angle entre deux vecteurs non nuls : $\cos\theta = \dfrac{\mathbf u \cdot \mathbf v}{\|\mathbf u\|\,\|\mathbf v\|}$. Le signe du dot product dit donc si l'angle est aigu ($> 0$), droit ($= 0$) ou obtus ($< 0$). Dans $\mathbb R^n$ avec $n > 3$, c'est cette formule qui **définit** l'angle ; elle a un sens grâce à l'[[Inégalité de Cauchy-Schwarz]] $|\mathbf u \cdot \mathbf v| \le \|\mathbf u\|\,\|\mathbf v\|$, qui garantit que le quotient est entre $-1$ et $1$. C'est aussi le **cosinus de similarité** utilisé en fouille de textes et en recherche d'information. [[Complément hors du cours|ⓘ]]

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

Dans $\mathbb C^n$, on contourne le problème en conjuguant l'une des coordonnées : $\langle \mathbf u, \mathbf v \rangle = u_1\bar v_1 + \cdots + u_n\bar v_n$ (**produit hermitien**). Alors $\langle \mathbf v, \mathbf v \rangle = |v_1|^2 + \cdots + |v_n|^2 \ge 0$ et la norme se définit comme dans $\mathbb R^n$. C'est ce conjugué qui apparaît dans la propriété (e) ci-dessus. [[Complément hors du cours|ⓘ]]

> $\|c\mathbf v\| = |c|\,\|\mathbf v\|$.

Justification : $\|c\mathbf v\|^2 = (c\mathbf v) \cdot (c\mathbf v) = c^2(\mathbf v \cdot \mathbf v) = c^2\|\mathbf v\|^2$, puis on prend la racine, avec $\sqrt{c^2} = |c|$. [[Complément hors du cours|ⓘ]]

## 3. Vecteur unitaire et normalisation

- Si $\|\mathbf u\| = 1$, $\mathbf u$ est un [[Vecteur unitaire|vecteur unitaire]] (*unit vector*).
- Pour obtenir un vecteur unitaire à partir de $\mathbf v \neq \mathbf 0$ : $\mathbf u = \frac{1}{\|\mathbf v\|}\mathbf v$. [[Erreurs du cours#^e-1-orthogonality|✎]]
- Exemple : $\mathbf v = (1, -2, 2, 0)$ a pour norme $\sqrt{1 + 4 + 4 + 0} = 3$, d'où $\mathbf u = \frac13\mathbf v = \left(\frac13, -\frac23, \frac23, 0\right)$, qui a la même direction et le même sens que $\mathbf v$ et vérifie $\|\mathbf u\| = 1$ d'après $\|c\mathbf v\| = |c|\,\|\mathbf v\|$. [[Complément hors du cours|ⓘ]]

## 4. Distance dans $\mathbb R^n$

> Pour $\mathbf u, \mathbf v \in \mathbb R^n$, la [[Distance|distance]] entre $\mathbf u$ et $\mathbf v$ est la longueur de $\mathbf u - \mathbf v$ :
> $$\text{dist}(\mathbf u, \mathbf v) = \|\mathbf u - \mathbf v\|.$$

![[chp 1 - Orthogonality - image31.png]]
*Figure : la distance entre $\mathbf u$ et $\mathbf v$ est la longueur de $\mathbf u - \mathbf v$ ; parallélogramme formé avec $-\mathbf v$ et $\mathbf u - \mathbf v$.*

- Dans $\mathbb R^2$ et $\mathbb R^3$, cette définition coïncide avec la distance euclidienne usuelle.
- La distance de $\mathbf u$ à $\mathbf v$ est la même que celle de $\mathbf u - \mathbf v$ à $\mathbf 0$ (parallélogramme).
- La norme vérifie l'[[Inégalité triangulaire]] $\|\mathbf u + \mathbf v\| \le \|\mathbf u\| + \|\mathbf v\|$ (conséquence de Cauchy-Schwarz) ; pour la distance, elle s'écrit $\text{dist}(\mathbf u, \mathbf w) \le \text{dist}(\mathbf u, \mathbf v) + \text{dist}(\mathbf v, \mathbf w)$ : le chemin direct est le plus court. [[Complément hors du cours|ⓘ]]

## 5. Orthogonalité

Deux droites (en bleu sur la figure) sont géométriquement perpendiculaires si et seulement si la distance de $\mathbf u$ à $\mathbf v$ est égale à la distance de $\mathbf u$ à $-\mathbf v$, ce qui revient à égaler les carrés de ces distances.

Le calcul sauté : en développant avec les propriétés du dot product, $\|\mathbf u - \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2 - 2\,\mathbf u \cdot \mathbf v$ et $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2 + 2\,\mathbf u \cdot \mathbf v$. Les deux sont égaux si et seulement si $-2\,\mathbf u \cdot \mathbf v = 2\,\mathbf u \cdot \mathbf v$, c'est-à-dire $\mathbf u \cdot \mathbf v = 0$ : d'où la définition qui suit. [[Complément hors du cours|ⓘ]]

![[chp 1 - Orthogonality - image9.png]]
*Figure : deux droites sécantes en $\mathbf 0$, l'une par $\mathbf u$, l'autre par $\mathbf v$ et $-\mathbf v$ ; distances $\|\mathbf u - \mathbf v\|$ et $\|\mathbf u - (-\mathbf v)\|$.*

> $\mathbf u$ est [[Orthogonalité|orthogonal]] à $\mathbf v$ $\iff \mathbf u \cdot \mathbf v = 0$.
> - Le vecteur nul est orthogonal à tout vecteur, car $\mathbf 0^T\mathbf v = 0$.
> - $\mathbf 0$ est le seul vecteur orthogonal à lui-même.

![[chp 1 - Orthogonality - image2.png]]
*Figure : triangle de sommets $\mathbf 0$, $\mathbf u$, $\mathbf u + \mathbf v$, de côtés $\|\mathbf u\|$, $\|\mathbf v\|$, $\|\mathbf u + \mathbf v\|$.*

> **Théorème 2 ([[Théorème de Pythagore]])** : $\mathbf u$ et $\mathbf v$ sont orthogonaux si et seulement si $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2$.

Preuve en une ligne : $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2 + 2\,\mathbf u \cdot \mathbf v$ (calcul ci-dessus), qui vaut $\|\mathbf u\|^2 + \|\mathbf v\|^2$ si et seulement si $\mathbf u \cdot \mathbf v = 0$. [[Complément hors du cours|ⓘ]]

## 6. Compléments orthogonaux (*orthogonal complements*)

- Si $\mathbf u$ est orthogonal à **tout** vecteur d'un [[Sous-espace vectoriel|sous-espace]] $W$ de $\mathbb R^n$, $\mathbf u$ est orthogonal à $W$.
- L'ensemble des vecteurs orthogonaux à $W$ est le [[Complément orthogonal|complément orthogonal]] $W^\perp$.
- $W^\perp$ est un sous-espace de $\mathbb R^n$.
- En pratique, $\mathbf x \in W^\perp$ si et seulement si $\mathbf x$ est orthogonal à chacun des vecteurs d'une famille qui engendre $W$ : par linéarité, il est alors orthogonal à toutes leurs combinaisons linéaires. [[Complément hors du cours|ⓘ]]
- Propriétés classiques : $W \cap W^\perp = \{\mathbf 0\}$ (un vecteur des deux est orthogonal à lui-même), $\dim W + \dim W^\perp = n$, $(W^\perp)^\perp = W$, et $\mathbb R^n = W \oplus W^\perp$ ([[Somme directe]]), ce que le théorème de décomposition orthogonale (section 9) rend explicite. [[Complément hors du cours|ⓘ]]

**Exemple** : soit $W$ un plan passant par l'origine dans $\mathbb R^3$ et $L$ la droite passant par l'origine et perpendiculaire à $W$. Si $\mathbf z \in L$ et $\mathbf w \in W$ sont non nuls, le segment de $\mathbf 0$ à $\mathbf z$ est perpendiculaire au segment de $\mathbf 0$ à $\mathbf w$ : $\mathbf z \cdot \mathbf w = 0$. Chaque vecteur de $L$ est orthogonal à tout $\mathbf w$ de $W$. En fait $L$ est formée de **tous** les vecteurs orthogonaux aux $\mathbf w$ de $W$, et inversement : $L = W^\perp$ et $W = L^\perp$.

![[chp 1 - Orthogonality - image7.png]]
*Figure : un plan et une droite passant par $\mathbf 0$, compléments orthogonaux l'un de l'autre.*

> **Théorème 3** : soit $A$ de taille $m \times n$. Le complément orthogonal du [[Sous-espaces fondamentaux|row space]] de $A$ est le [[Espace nul|null space]] de $A$, et le complément orthogonal du [[Espace des colonnes|column space]] de $A$ est le null space de $A^T$ :
> $$(\text{Row}\,A)^\perp = \text{Nul}\,A \qquad (\text{Col}\,A)^\perp = \text{Nul}\,A^T.$$

Pourquoi : la $i$-ème coordonnée de $A\mathbf x$ est le dot product de la $i$-ème ligne de $A$ avec $\mathbf x$. Donc $A\mathbf x = \mathbf 0$ signifie que $\mathbf x$ est orthogonal à chaque ligne, donc (par le critère ci-dessus) à Row $A$. La seconde égalité s'obtient en appliquant la première à $A^T$, dont les lignes sont les colonnes de $A$. Combiné au [[Théorème du rang]], cela donne $\dim \text{Row}\,A + \dim \text{Nul}\,A = n$, cohérent avec $\dim W + \dim W^\perp = n$. [[Complément hors du cours|ⓘ]]

![[chp 1 - Orthogonality - image4.png]]
*Figure : les sous-espaces fondamentaux d'une matrice $m \times n$ : Row $A$ et Nul $A$ perpendiculaires en $\mathbf 0$ (à gauche), Col $A$ et Nul $A^T$ perpendiculaires (à droite), reliés par $A$.*

**Exemple** : $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$.
- Row space : plan 2D de $\mathbb R^3$ engendré par $r_1 = (1,2,3)$ et $r_2 = (4,5,6)$.
- Null space ($A\mathbf x = \mathbf 0$) : la droite engendrée par $\mathbf x = (1,-2,1)$, perpendiculaire au row space.
- Column space : $a_1 = (1,4)$, $a_2 = (2,5)$, $a_3 = (3,6)$ engendrent tout le plan $\mathbb R^2$.
- Left null space : $A^T\mathbf w = w_1(1,2,3) + w_2(4,5,6) = \mathbf 0 \Rightarrow (w_1, w_2) = (0,0)$ : $\text{Nul}\,A^T$ est le sous-espace nul.
- Vérification : $(1,-2,1) \cdot (1,2,3) = 1 - 4 + 3 = 0$ et $(1,-2,1) \cdot (4,5,6) = 4 - 10 + 6 = 0$. Les dimensions concordent : $A$ est de rang 2, donc $\dim \text{Row}\,A + \dim \text{Nul}\,A = 2 + 1 = 3$ et $\dim \text{Col}\,A + \dim \text{Nul}\,A^T = 2 + 0 = 2$. [[Complément hors du cours|ⓘ]]

![[chp 1 - Orthogonality - image30.png]]
*Figure : le row space (plan engendré par $r_1$, $r_2$) et le vecteur $\mathbf x = (1,-2,1)$ qui lui est perpendiculaire.*

![[chp 1 - Orthogonality - image28.png]]
*Figure : les colonnes $a_1$, $a_2$, $a_3$ engendrent le plan entier, le column space.*

## 7. Familles orthogonales (*orthogonal set*)

$\{\mathbf u_1, \ldots, \mathbf u_p\} \subset \mathbb R^n$ est une [[Famille orthogonale|famille orthogonale]] si ses vecteurs sont deux à deux orthogonaux.

> **Théorème** : si $S = \{\mathbf u_1, \ldots, \mathbf u_p\}$ est une famille orthogonale de vecteurs **non nuls**, alors $S$ est [[Indépendance linéaire|linéairement indépendante]], donc une [[Base (algèbre linéaire)|base]] du sous-espace [[Espace engendré|engendré]] par $S$.

Idée de la preuve : si $c_1\mathbf u_1 + \cdots + c_p\mathbf u_p = \mathbf 0$, on fait le dot product avec $\mathbf u_j$. Tous les termes $\mathbf u_i \cdot \mathbf u_j$ avec $i \neq j$ sont nuls, il reste $c_j(\mathbf u_j \cdot \mathbf u_j) = 0$ ; comme $\mathbf u_j \neq \mathbf 0$, $\mathbf u_j \cdot \mathbf u_j > 0$, donc $c_j = 0$, pour chaque $j$. [[Complément hors du cours|ⓘ]]

> **Théorème** : soit $\{\mathbf u_1, \ldots, \mathbf u_p\}$ une base orthogonale d'un sous-espace $W$ de $\mathbb R^n$. Pour tout $\mathbf y \in W$, les poids de la [[Combinaison linéaire|combinaison linéaire]] $\mathbf y = c_1\mathbf u_1 + \cdots + c_p\mathbf u_p$ sont
> $$c_j = \frac{\mathbf y \cdot \mathbf u_j}{\mathbf u_j \cdot \mathbf u_j} \quad (j = 1, \ldots, p).$$

Même calcul : en faisant le dot product de $\mathbf y = c_1\mathbf u_1 + \cdots + c_p\mathbf u_p$ avec $\mathbf u_j$, il reste $\mathbf y \cdot \mathbf u_j = c_j(\mathbf u_j \cdot \mathbf u_j)$. C'est tout l'intérêt d'une base orthogonale : chaque coordonnée se calcule seule, par un quotient, sans résoudre de système linéaire. [[Complément hors du cours|ⓘ]]

Cas $W = \mathbb R^2 = \text{Span}\{\mathbf u_1, \mathbf u_2\}$ avec $\mathbf u_1 \perp \mathbf u_2$ :
$$\mathbf y = \frac{\mathbf y \cdot \mathbf u_1}{\mathbf u_1 \cdot \mathbf u_1}\mathbf u_1 + \frac{\mathbf y \cdot \mathbf u_2}{\mathbf u_2 \cdot \mathbf u_2}\mathbf u_2 \quad (3)$$
Le théorème décompose chaque $\mathbf y$ de $\text{Span}\{\mathbf u_1, \ldots, \mathbf u_p\}$ en somme de $p$ projections sur des sous-espaces de dimension 1, deux à deux orthogonaux.

![[chp 1 - Orthogonality - image3.png]]
*Figure : $\mathbf y$ décomposé en $\hat{\mathbf y}_1$ (projection sur $\mathbf u_1$) plus $\hat{\mathbf y}_2$ (projection sur $\mathbf u_2$).*

## 8. Familles orthonormées (*orthonormal set*)

- Famille orthonormée = famille orthogonale de vecteurs normés, $\|\mathbf u_i\| = 1$.

> Une matrice $U$ de taille $m \times n$ a des colonnes orthonormées $\iff U^TU = I$.

Pourquoi : le coefficient $(i, j)$ de $U^TU$ est $\mathbf u_i^T\mathbf u_j = \mathbf u_i \cdot \mathbf u_j$. Il vaut 1 sur la diagonale (vecteurs normés) et 0 ailleurs (vecteurs orthogonaux). En revanche, si $m > n$, $UU^T$ (de taille $m \times m$) n'est **pas** l'identité : c'est la matrice de la projection orthogonale sur Col $U$ (formule (5), section 9). [[Complément hors du cours|ⓘ]]

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

D'où vient $\alpha$ : on impose $\mathbf z = \mathbf y - \alpha\mathbf u$ orthogonal à $\mathbf u$, soit $(\mathbf y - \alpha\mathbf u) \cdot \mathbf u = \mathbf y \cdot \mathbf u - \alpha(\mathbf u \cdot \mathbf u) = 0$, d'où la valeur de $\alpha$ (définie car $\mathbf u \neq \mathbf 0$). [[Complément hors du cours|ⓘ]]

Exemple : $\mathbf y = (7, 6)$, $\mathbf u = (4, 2)$. $\mathbf y \cdot \mathbf u = 40$, $\mathbf u \cdot \mathbf u = 20$, donc $\hat{\mathbf y} = 2\mathbf u = (8, 4)$ et $\mathbf z = (-1, 2)$. Vérification : $\mathbf z \cdot \mathbf u = -4 + 4 = 0$. La distance de $\mathbf y$ à la droite engendrée par $\mathbf u$ est $\|\mathbf z\| = \sqrt 5$. [[Complément hors du cours|ⓘ]]

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

La matrice $P = UU^T$ est la **matrice de projection** sur $W$. Elle vérifie $P^2 = P$ (projeter deux fois revient à projeter une fois, car $U^TU = I$) et $P^T = P$ ([[Matrice symétrique|symétrique]]) ; réciproquement, toute matrice symétrique telle que $P^2 = P$ est la matrice d'une projection orthogonale. $I - P$ est la projection sur $W^\perp$ : elle donne $\mathbf z$. [[Complément hors du cours|ⓘ]]

**Interprétation géométrique.** Quand $W$ est de dimension 1, (2) n'a qu'un terme. Quand $\dim W > 1$, chaque terme de (2) est la projection orthogonale de $\mathbf y$ sur la droite engendrée par un des $\mathbf u_j$. Ainsi $\hat{\mathbf y} = \hat{\mathbf y}_1 + \hat{\mathbf y}_2$ pour $W$ engendré par $\mathbf u_1$, $\mathbf u_2$ dans $\mathbb R^3$ : **la projection orthogonale de $\mathbf y$ est la somme de ses projections sur des sous-espaces de dimension 1 deux à deux orthogonaux.**

![[chp 1 - Orthogonality - image37.png]]
*Figure : dans $\mathbb R^3$, $\mathbf y$ projeté sur le plan engendré par $\mathbf u_1$ et $\mathbf u_2$ ; les projections $\hat{\mathbf y}_1$ et $\hat{\mathbf y}_2$ sur les deux droites s'additionnent en $\hat{\mathbf y}$.*

> **Théorème de la meilleure approximation** (*the best approximation*) : $W$ sous-espace de $\mathbb R^n$, $\mathbf y \in \mathbb R^n$. $\hat{\mathbf y}$ est le point de $W$ le plus proche de $\mathbf y$ :
> $$\|\mathbf y - \hat{\mathbf y}\| < \|\mathbf y - \mathbf v\| \quad \text{pour tout } \mathbf v \in W,\ \mathbf v \neq \hat{\mathbf y}.$$
> $\hat{\mathbf y}$ est la meilleure approximation de $\mathbf y$ par des éléments de $W$.

Pourquoi : pour $\mathbf v \in W$, on écrit $\mathbf y - \mathbf v = (\mathbf y - \hat{\mathbf y}) + (\hat{\mathbf y} - \mathbf v)$. Le premier terme est dans $W^\perp$, le second dans $W$ : ils sont orthogonaux, et le [[Théorème de Pythagore]] donne $\|\mathbf y - \mathbf v\|^2 = \|\mathbf y - \hat{\mathbf y}\|^2 + \|\hat{\mathbf y} - \mathbf v\|^2$, strictement plus grand que $\|\mathbf y - \hat{\mathbf y}\|^2$ dès que $\mathbf v \neq \hat{\mathbf y}$. La distance de $\mathbf y$ à $W$ est donc $\|\mathbf y - \hat{\mathbf y}\| = \|\mathbf z\|$. C'est ce théorème qui fonde les moindres carrés (section 12). [[Complément hors du cours|ⓘ]]

## 10. Matrice orthogonale

- Toute matrice **carrée** à colonnes ortho**normées** est une matrice ortho**gonale** ([[Matrice orthogonale]]).
- Une matrice orthogonale a aussi des lignes orthonormées.
- Une matrice orthogonale est inversible et $U^{-1} = U^T$.
- Son [[Déterminant|déterminant]] vaut $1$ ou $-1$, car $\det(U^T)\det(U) = \det(I) = 1$ et $\det U^T = \det U$. Comme elle conserve longueurs et angles (section 8), elle représente une **isométrie** : une rotation si $\det U = 1$, une rotation composée avec une réflexion si $\det U = -1$. [[Complément hors du cours|ⓘ]]
- Exemples dans $\mathbb R^2$ : la rotation d'angle $\theta$, $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ (déterminant 1), et la symétrie par rapport à l'axe des abscisses, $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ (déterminant $-1$). Les matrices de permutation sont aussi orthogonales. [[Complément hors du cours|ⓘ]]

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

Le mécanisme : chaque $\mathbf v_k$ est $\mathbf x_k$ **moins sa projection orthogonale** sur $W_{k-1} = \text{Span}\{\mathbf v_1, \ldots, \mathbf v_{k-1}\}$ (formule (2) de la section 9, appliquée avec la base orthogonale déjà construite). Par le théorème de décomposition orthogonale, $\mathbf v_k$ est donc dans $W_{k-1}^\perp$, orthogonal à tous les précédents. Il n'est pas nul, car $\mathbf x_k$ n'est pas dans $W_{k-1} = \text{Span}\{\mathbf x_1, \ldots, \mathbf x_{k-1}\}$ (famille libre). Pour une base orthonormée, on normalise chaque $\mathbf v_k$ à la fin. [[Complément hors du cours|ⓘ]]

Exemple : $\mathbf x_1 = (3, 6, 0)$, $\mathbf x_2 = (1, 2, 2)$. On pose $\mathbf v_1 = \mathbf x_1$ ; $\mathbf x_2 \cdot \mathbf v_1 = 15$ et $\mathbf v_1 \cdot \mathbf v_1 = 45$, donc $\mathbf v_2 = (1, 2, 2) - \frac13(3, 6, 0) = (0, 0, 2)$. On vérifie $\mathbf v_1 \cdot \mathbf v_2 = 0$. Base orthonormée : $\left(\frac{1}{\sqrt5}, \frac{2}{\sqrt5}, 0\right)$ et $(0, 0, 1)$. [[Complément hors du cours|ⓘ]]

Si $A$ ($m \times n$) a des colonnes linéairement indépendantes $\mathbf x_1, \ldots, \mathbf x_n$, appliquer Gram-Schmidt (avec **normalisation**) revient à factoriser $A$.

> **[[Factorisation QR]]** : si $A$ ($m \times n$) a des colonnes linéairement indépendantes, $A = QR$, où
> - $Q$ est $m \times n$ et ses colonnes forment une base orthonormée de $\text{Col}\,A$ ;
> - $R$ est $n \times n$, triangulaire supérieure, [[Matrice inversible|inversible]], à coefficients diagonaux positifs.

Schéma du cours pour $A = [\mathbf a_1\ \mathbf a_2\ \mathbf a_3]$ et $Q = [\mathbf e_1\ \mathbf e_2\ \mathbf e_3]$ (vecteurs unitaires orthogonaux) :
$$R = \begin{bmatrix} \mathbf e_1^T\mathbf a_1 & \mathbf e_1^T\mathbf a_2 & \mathbf e_1^T\mathbf a_3 \\ 0 & \mathbf e_2^T\mathbf a_2 & \mathbf e_2^T\mathbf a_3 \\ 0 & 0 & \mathbf e_3^T\mathbf a_3 \end{bmatrix}$$

![[chp 1 - Orthogonality - image12.png]]
*Figure : schéma $A = QR$, avec $Q$ formée des vecteurs unitaires orthogonaux $\mathbf e_i$ et $R$ triangulaire supérieure (légendée « upper diagonal matrix »).*

D'où vient ce $R$ : comme $Q^TQ = I$ (colonnes orthonormées), multiplier $A = QR$ à gauche par $Q^T$ donne $R = Q^TA$, dont le coefficient $(i, j)$ est $\mathbf e_i^T\mathbf a_j$. Les zéros sous la diagonale viennent de (1) : $\mathbf a_j$ est dans $\text{Span}\{\mathbf e_1, \ldots, \mathbf e_j\}$, donc orthogonal à $\mathbf e_i$ pour $i > j$. Dans l'exemple ci-dessus, $A = \begin{bmatrix} 3 & 1 \\ 6 & 2 \\ 0 & 2 \end{bmatrix}$ donne $R = \begin{bmatrix} 3\sqrt5 & \sqrt5 \\ 0 & 2 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

En calcul numérique, le Gram-Schmidt classique perd vite l'orthogonalité à cause des erreurs d'arrondi : on lui préfère le **Gram-Schmidt modifié** (on retire les projections une à une, sur le vecteur déjà corrigé) ou les réflexions de Householder, méthode qu'utilisent les bibliothèques courantes (LAPACK, d'où `numpy.linalg.qr`). [[Complément hors du cours|ⓘ]]

## 12. Problème des moindres carrés (*least square problem*)

- Parfois $A\mathbf x = \mathbf b$ n'a pas de solution ; le mieux est alors de trouver un $\mathbf x$ qui rend $A\mathbf x$ aussi proche que possible de $\mathbf b$.
- Le problème des [[Moindres carrés|moindres carrés]] consiste à trouver $\mathbf x$ qui rend $\|\mathbf b - A\mathbf x\|$ aussi petit que possible : la plus petite distance est $\|\mathbf b - A\hat{\mathbf x}\|$, atteinte pour la solution des moindres carrés $\hat{\mathbf x}$. [[Erreurs du cours#^e-1-orthogonality|✎]]

> **Définition** : si $A$ est $m \times n$ et $\mathbf b \in \mathbb R^m$, une **solution au sens des moindres carrés** (*least-squares solution*) de $A\mathbf x = \mathbf b$ est un $\hat{\mathbf x} \in \mathbb R^n$ tel que
> $$\|\mathbf b - A\hat{\mathbf x}\| \le \|\mathbf b - A\mathbf x\| \quad \text{pour tout } \mathbf x \in \mathbb R^n.$$

![[chp 1 - Orthogonality - image15.png]]
*Figure : le plan $\text{Col}\,A$ contient $\mathbf 0$, $A\hat{\mathbf x}$, $A\mathbf x_1$, $A\mathbf x_2$ ; $\mathbf b$ est hors du plan et $A\hat{\mathbf x}$ en est la projection orthogonale.*

- $A\hat{\mathbf x}$ est le projeté orthogonal de $\mathbf b$ sur Col $A$ (c'est bien $A\hat{\mathbf x}$, et non $\hat{\mathbf x} \in \mathbb R^n$, qui est dans Col $A \subset \mathbb R^m$). [[Erreurs du cours#^e-1-orthogonality|✎]]
- Quel que soit $\mathbf x$, $A\mathbf x$ est forcément dans $\text{Col}\,A$.
- Si $\mathbf b$ est dans $\text{Col}\,A$, alors $\mathbf b = A\mathbf x$ pour un $\mathbf x$, et ce $\mathbf x$ est une solution des moindres carrés.
- $\|\mathbf b - A\hat{\mathbf x}\|$ est l'**erreur des moindres carrés** (*least-square error*).

> **Théorème (équations normales)** : l'ensemble des solutions des moindres carrés de $A\mathbf x = \mathbf b$ coïncide avec l'ensemble (non vide) des solutions des **équations normales**
> $$A^TA\mathbf x = A^T\mathbf b.$$
> (Annotation : « Read it by yourselves ».)

D'où viennent les équations normales : par le théorème de la meilleure approximation, $A\hat{\mathbf x}$ est la projection de $\mathbf b$ sur Col $A$, donc $\mathbf b - A\hat{\mathbf x}$ est dans $(\text{Col}\,A)^\perp = \text{Nul}\,A^T$ (Théorème 3). Cela s'écrit $A^T(\mathbf b - A\hat{\mathbf x}) = \mathbf 0$, soit $A^TA\hat{\mathbf x} = A^T\mathbf b$. Le nom vient de là : le résidu $\mathbf b - A\hat{\mathbf x}$ est **normal** (perpendiculaire) à Col $A$. [[Complément hors du cours|ⓘ]]

> **Théorème** : $A$ de taille $m \times n$. Sont équivalents :
> a. $A\mathbf x = \mathbf b$ a une **unique** solution des moindres carrés pour tout $\mathbf b \in \mathbb R^m$ ;
> b. les colonnes de $A$ sont linéairement indépendantes ;
> c. $A^TA$ est inversible.
>
> Dans ce cas,
> $$\hat{\mathbf x} = (A^TA)^{-1}A^T\mathbf b. \quad (4)$$

Avec la factorisation $A = QR$, les équations normales se simplifient : $A^TA = R^TQ^TQR = R^TR$ et $A^T\mathbf b = R^TQ^T\mathbf b$, d'où $R\hat{\mathbf x} = Q^T\mathbf b$, système triangulaire qui se résout par remontée : $\hat{\mathbf x} = R^{-1}Q^T\mathbf b$. C'est la méthode préférée en pratique, car former $A^TA$ élève au carré le [[Conditionnement d'une matrice|conditionnement]] et amplifie les erreurs d'arrondi. [[Complément hors du cours|ⓘ]]

## 13. Application aux modèles linéaires (*application to linear models*)

En statistique, au lieu de $A\mathbf x = \mathbf b$ on écrit $X\boldsymbol\beta = \mathbf y$ (voir [[Régression linéaire]]) :
- $X$ est la **matrice du plan d'expérience** (*design matrix*) ;
- $\boldsymbol\beta$ est le **vecteur des paramètres** (*parameter vector*) ;
- $\mathbf y$ est le **vecteur des observations** (*observation vector*).

La relation la plus simple entre $x$ et $y$ est $y = \beta_0 + \beta_1 x$ (au lieu de $y = mx + b$). Des données expérimentales $(x_1, y_1), \ldots, (x_n, y_n)$ semblent souvent proches d'une droite ; on veut déterminer $\beta_0$ et $\beta_1$ [[Erreurs du cours#^e-1-orthogonality|✎]] pour que la droite soit aussi « proche » que possible des points.

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

Le cours ne donne pas ici la forme explicite de $X$ ; avec le modèle $y = \beta_0 + \beta_1 x$, elle a une première colonne de 1 et une seconde colonne des $x_j$. [[Complément hors du cours|ⓘ]]

$$X = \begin{bmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{bmatrix}, \qquad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}, \qquad \mathbf y = \begin{bmatrix} y_1 \\ \vdots \\ y_n \end{bmatrix}.$$

Résoudre les équations normales $X^TX\boldsymbol\beta = X^T\mathbf y$ donne les formules de la régression simple : $\hat\beta_1 = \dfrac{\sum_j (x_j - \bar x)(y_j - \bar y)}{\sum_j (x_j - \bar x)^2}$ (covariance sur variance, voir [[Covariance et corrélation]]) et $\hat\beta_0 = \bar y - \hat\beta_1\bar x$, où $\bar x$ et $\bar y$ sont les [[Moyenne empirique|moyennes]]. La droite passe donc toujours par le point moyen $(\bar x, \bar y)$, et la première équation normale dit que la somme des résidus est nulle. [[Complément hors du cours|ⓘ]]

Exemple : points $(0, 0)$, $(1, 1)$, $(2, 1)$. $X^TX = \begin{bmatrix} 3 & 3 \\ 3 & 5 \end{bmatrix}$ et $X^T\mathbf y = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$ ; le système $3\beta_0 + 3\beta_1 = 2$, $3\beta_0 + 5\beta_1 = 3$ donne $\beta_1 = \frac12$, $\beta_0 = \frac16$, soit la droite $y = \frac16 + \frac12 x$. Résidus : $-\frac16$, $\frac13$, $-\frac16$, de somme nulle. [[Complément hors du cours|ⓘ]]

Le même cadre couvre des modèles plus riches, tant qu'ils restent **linéaires en $\boldsymbol\beta$** : régression multiple ($y = \beta_0 + \beta_1 x_1 + \beta_2 x_2$, une colonne de $X$ par variable) ou ajustement d'une parabole ($y = \beta_0 + \beta_1 x + \beta_2 x^2$, colonnes $1$, $x_j$, $x_j^2$). [[Complément hors du cours|ⓘ]]
