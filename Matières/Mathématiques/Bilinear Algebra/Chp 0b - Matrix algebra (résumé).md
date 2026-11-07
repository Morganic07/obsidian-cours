---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0b - Matrix algebra.docx|Chp 0b - Matrix algebra]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0b - Matrix algebra.docx|Chp 0b - Matrix algebra]] (« Chapter 0b - Matrix Algebra »), dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre donne les règles de calcul sur les matrices, puis caractérise les matrices inversibles.

## 1. Opérations sur les matrices (*matrix operations*)

Une [[Matrice]] $m \times n$ s'écrit $A = [a_{ij}]$, ou par colonnes $A = [\mathbf a_1\ \mathbf a_2\ \cdots\ \mathbf a_n]$, chaque $\mathbf a_j$ étant un vecteur colonne :
$$A = \begin{bmatrix} a_{11} & \cdots & a_{1j} & \cdots & a_{1n} \\ \vdots & & \vdots & & \vdots \\ a_{i1} & \cdots & a_{ij} & \cdots & a_{in} \\ \vdots & & \vdots & & \vdots \\ a_{m1} & \cdots & a_{mj} & \cdots & a_{mn} \end{bmatrix}$$
($a_{ij}$ : ligne $i$, colonne $j$).

- **[[Matrice diagonale]]** (*diagonal matrix*) : matrice carrée dont tous les coefficients hors de la diagonale principale sont nuls.

![[Chp 0b - Matrix algebra - image15.png]]
*Figure : matrice diagonale, diagonale principale surlignée, des 0 partout ailleurs.*

- **Matrice identité** (*identity matrix*) :
$$I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$$

> **Théorème** : $A$, $B$, $C$ de même taille, $r$, $s$ scalaires :
> a. $A + B = B + A$ ; b. $(A + B) + C = A + (B + C)$ ; c. $A + 0 = A$ ; d. $r(A + B) = rA + rB$ ; e. $(r + s)A = rA + sA$ ; f. $r(sA) = (rs)A$.

> **Définition ([[Produit matriciel]])** : si $A$ est $m \times n$ et $B$ est $n \times p$ de colonnes $\mathbf b_1, \ldots, \mathbf b_p$, alors $AB$ est la matrice $m \times p$ de colonnes $A\mathbf b_1, \ldots, A\mathbf b_p$ :
> $$AB = A[\mathbf b_1\ \mathbf b_2\ \cdots\ \mathbf b_p] = [A\mathbf b_1\ A\mathbf b_2\ \cdots\ A\mathbf b_p]$$

> **Théorème (multiplication matricielle)** : $A$ de taille $m \times n$, $B$ et $C$ de tailles compatibles :
> a. $A(BC) = (AB)C$ (associativité) ;
> b. $A(B + C) = AB + AC$ (distributivité à gauche) ;
> c. $(B + C)A = BA + CA$ (distributivité à droite) ;
> d. $r(AB) = (rA)B = A(rB)$ pour tout scalaire $r$ ;
> e. $I_mA = A = AI_n$ (élément neutre).

En général (il peut y avoir des exceptions) :
- $AB \neq BA$ ;
- $AB = AC \not\Rightarrow B = C$ ;
- $AB = 0 \not\Rightarrow A = 0$ ou $B = 0$.

> **Définition ([[Transposée]])** : pour $A$ de taille $m \times n$, la transposée $A^T$ est la matrice $n \times m$ dont les colonnes sont les lignes correspondantes de $A$.

> **Théorème (transposée)** : pour des tailles compatibles :
> a. $(A^T)^T = A$ ; b. $(A + B)^T = A^T + B^T$ ; c. $(rA)^T = rA^T$ ; d. $(AB)^T = B^TA^T$ ; e. $(ABC)^T = C^TB^TA^T$.

## 2. Inverse d'une matrice (*inverse of a matrix*)

> **Définition ([[Matrice inversible]])** : une matrice carrée $A$ est inversible $\iff \exists!\, A^{-1}$, $A^{-1}A = I_n$ et $AA^{-1} = I_n$. L'inverse est **unique**.

Vocabulaire : une matrice non inversible est **singulière** (*singular*) ; une matrice inversible est **non singulière** (*nonsingular*).

> **Inverse d'une matrice $2 \times 2$** : soit $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. Si $ad - bc \neq 0$, $A$ est inversible et
> $$A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.$$
> Si $ad - bc = 0$, $A$ n'est pas inversible. On note $\det A = ad - bc$ (voir [[Déterminant]]).

> **Théorème** : si $A$ est $n \times n$ inversible, pour tout $\mathbf b \in \mathbb R^n$, $A\mathbf x = \mathbf b$ a l'unique solution $\mathbf x = A^{-1}\mathbf b$ :
> $$A\mathbf x = \mathbf b \iff A^{-1}A\mathbf x = A^{-1}\mathbf b \iff \mathbf x = A^{-1}\mathbf b.$$

> **Théorème** :
> a. si $A$ est inversible, $A^{-1}$ l'est aussi et $(A^{-1})^{-1} = A$ ;
> b. si $A$ et $B$ sont $n \times n$ inversibles, $AB$ l'est aussi et $(AB)^{-1} = B^{-1}A^{-1}$ (produit des inverses dans l'ordre inverse) ;
> c. si $A$ est inversible, $A^T$ l'est aussi et $(A^T)^{-1} = (A^{-1})^T$.

> **Théorème** : une matrice $n \times n$ est inversible si et seulement si elle est [[Opérations élémentaires sur les lignes|équivalente par lignes]] à $I_n$ ; dans ce cas, toute suite d'opérations élémentaires qui réduit $A$ à $I_n$ transforme aussi $I_n$ en $A^{-1}$.

### Algorithme de calcul de $A^{-1}$

1. Écrire la [[Matrice augmentée|matrice augmentée]] $[A\ \ I]$.
2. La réduire par opérations élémentaires sur les lignes.
3. Si $A$ est équivalente par lignes à $I$, on obtient $[I\ \ A^{-1}]$ ; sinon, $A$ n'a pas d'inverse.

### Théorème de la matrice inversible (*The Invertible Matrix Theorem*)

Soit $A$ carrée $n \times n$. Les énoncés suivants sont équivalents (tous vrais ou tous faux) ; voir [[Invertible matrix theorem (résumé)|Invertible matrix theorem]] et [[Théorème de la matrice inversible]] :
- a. $A$ est inversible ;
- b. $A$ est équivalente par lignes à $I_n$ ;
- c. $A$ a $n$ positions pivots ;
- d. $A\mathbf x = \mathbf 0$ n'a que la [[Système linéaire homogène|solution triviale]] ;
- e. les colonnes de $A$ forment une famille [[Indépendance linéaire|linéairement indépendante]] ;
- f. la [[Transformation linéaire|transformation linéaire]] $\mathbf x \mapsto A\mathbf x$ est [[Injectivité et surjectivité|injective]] (*one-to-one*) ;
- g. $A\mathbf x = \mathbf b$ a au moins une solution pour tout $\mathbf b \in \mathbb R^n$ ;
- h. les colonnes de $A$ [[Espace engendré|engendrent]] $\mathbb R^n$ ;
- i. $\mathbf x \mapsto A\mathbf x$ envoie $\mathbb R^n$ **sur** $\mathbb R^n$ (surjective, *onto*) ;
- j. il existe $C$ ($n \times n$) telle que $CA = I$ ;
- k. il existe $D$ ($n \times n$) telle que $AD = I$ ;
- l. $A^T$ est inversible.

### Transformation linéaire inversible

> **Définition** : $T : \mathbb R^n \to \mathbb R^n$ linéaire est **inversible** s'il existe $S : \mathbb R^n \to \mathbb R^n$ telle que
> $$S(T(\mathbf x)) = \mathbf x \quad (1) \qquad T(S(\mathbf x)) = \mathbf x \quad (2) \qquad \text{pour tout } \mathbf x \in \mathbb R^n.$$

Exemples du cours : $e^x$ et $\ln(x)$ (voir « Points à vérifier ») ; $A$ et $A^{-1}$.

![[Chp 0b - Matrix algebra - image4.png]]
*Figure : la multiplication par $A$ envoie $\mathbf x$ sur $A\mathbf x$, la multiplication par $A^{-1}$ ramène $A\mathbf x$ à $\mathbf x$.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Exemple $e^x$ et $\ln(x)$** : il illustre bien une fonction réciproque, mais il suit une définition portant sur des transformations **linéaires** de $\mathbb{R}^n$. Or ces deux fonctions ne sont pas linéaires, et $\ln$ n'est pas définie sur tout $\mathbb{R}$ (complément). L'exemple est donc seulement une analogie.
2. **Définition de l'inverse** : le cours écrit « inversible $\iff \exists!\, A^{-1}$ » ; l'unicité est une conséquence (énoncée juste après), pas une condition de la définition (complément).
