---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0b - Matrix algebra.docx|Chp 0b - Matrix algebra]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0b - Matrix algebra.docx|Chp 0b - Matrix algebra]] (« Chapter 0b - Matrix Algebra »), dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

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

La somme et le produit par un scalaire se calculent coefficient par coefficient : $(A + B)_{ij} = a_{ij} + b_{ij}$ et $(rA)_{ij} = r\,a_{ij}$. On n'additionne que deux matrices de même taille ; $0$ désigne la **matrice nulle**, dont tous les coefficients sont nuls. [[Complément hors du cours|ⓘ]]

> **Théorème** : $A$, $B$, $C$ de même taille, $r$, $s$ scalaires :
> a. $A + B = B + A$ ; b. $(A + B) + C = A + (B + C)$ ; c. $A + 0 = A$ ; d. $r(A + B) = rA + rB$ ; e. $(r + s)A = rA + sA$ ; f. $r(sA) = (rs)A$.

> **Définition ([[Produit matriciel]])** : si $A$ est $m \times n$ et $B$ est $n \times p$ de colonnes $\mathbf b_1, \ldots, \mathbf b_p$, alors $AB$ est la matrice $m \times p$ de colonnes $A\mathbf b_1, \ldots, A\mathbf b_p$ :
> $$AB = A[\mathbf b_1\ \mathbf b_2\ \cdots\ \mathbf b_p] = [A\mathbf b_1\ A\mathbf b_2\ \cdots\ A\mathbf b_p]$$

Chaque colonne $A\mathbf b_j$ est une [[Combinaison linéaire|combinaison linéaire]] des colonnes de $A$, de coefficients les composantes de $\mathbf b_j$ : $A\mathbf x = x_1\mathbf a_1 + \cdots + x_n\mathbf a_n$. Le produit n'existe que si le nombre de colonnes de $A$ égale le nombre de lignes de $B$. [[Complément hors du cours|ⓘ]]

**Règle ligne-colonne** : le coefficient $(i, j)$ de $AB$ est le produit de la ligne $i$ de $A$ par la colonne $j$ de $B$,
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj}.$$
Par exemple, $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 1\cdot 5 + 2\cdot 6 \\ 3\cdot 5 + 4\cdot 6 \end{bmatrix} = \begin{bmatrix} 17 \\ 39 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

Le produit est défini ainsi pour représenter la **composition** : si $\mathbf x \mapsto B\mathbf x$ puis $\mathbf y \mapsto A\mathbf y$, alors $A(B\mathbf x) = (AB)\mathbf x$. Appliquer $AB$, c'est appliquer d'abord $B$, puis $A$ ; c'est aussi pourquoi le produit est associatif mais pas commutatif, comme la composition des fonctions. [[Complément hors du cours|ⓘ]]

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

Contre-exemple pour les trois points : avec $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ et $B = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$, on a $AB = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ mais $BA = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ : $AB \neq BA$ ; $BA = 0$ sans que $A$ ni $B$ soit nulle ; et $BA = B \cdot 0$ sans que $A = 0$, donc on ne peut pas « simplifier par $B$ ». En revanche, si $A$ est [[Matrice inversible|inversible]], $AB = AC$ entraîne $B = C$ (multiplier à gauche par $A^{-1}$). [[Complément hors du cours|ⓘ]]

Les **puissances** d'une matrice carrée se définissent par $A^k = A \cdots A$ ($k$ facteurs) et $A^0 = I_n$. Une matrice peut être non nulle avec une puissance nulle : $B^2 = 0$ pour la matrice $B$ ci-dessus (matrice dite **nilpotente**). [[Complément hors du cours|ⓘ]]

> **Définition ([[Transposée]])** : pour $A$ de taille $m \times n$, la transposée $A^T$ est la matrice $n \times m$ dont les colonnes sont les lignes correspondantes de $A$.

> **Théorème (transposée)** : pour des tailles compatibles :
> a. $(A^T)^T = A$ ; b. $(A + B)^T = A^T + B^T$ ; c. $(rA)^T = rA^T$ ; d. $(AB)^T = B^TA^T$ ; e. $(ABC)^T = C^TB^TA^T$.

Coefficient par coefficient, $(A^T)_{ij} = a_{ji}$ : la transposition échange lignes et colonnes, comme une symétrie par rapport à la diagonale principale. Une matrice carrée égale à sa transposée ($A^T = A$, soit $a_{ij} = a_{ji}$) est une [[Matrice symétrique]] ; pour toute matrice $A$, $A^TA$ et $AA^T$ sont symétriques, d'après d. [[Complément hors du cours|ⓘ]]

## 2. Inverse d'une matrice (*inverse of a matrix*)

> **Définition ([[Matrice inversible]])** : une matrice carrée $A$ est inversible $\iff \exists!\, A^{-1}$, $A^{-1}A = I_n$ et $AA^{-1} = I_n$. L'inverse est **unique**.

Vocabulaire : une matrice non inversible est **singulière** (*singular*) ; une matrice inversible est **non singulière** (*nonsingular*).

> **Inverse d'une matrice $2 \times 2$** : soit $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. Si $ad - bc \neq 0$, $A$ est inversible et
> $$A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.$$
> Si $ad - bc = 0$, $A$ n'est pas inversible. On note $\det A = ad - bc$ (voir [[Déterminant]]).

Vérification de la formule : $\begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \begin{bmatrix} ad - bc & 0 \\ 0 & ad - bc \end{bmatrix} = (ad - bc)\,I_2$, d'où l'inverse en divisant par $ad - bc$. Moyen mnémotechnique : échanger les deux coefficients de la diagonale, changer le signe des deux autres, diviser par le déterminant. [[Complément hors du cours|ⓘ]]

> **Théorème** : si $A$ est $n \times n$ inversible, pour tout $\mathbf b \in \mathbb R^n$, $A\mathbf x = \mathbf b$ a l'unique solution $\mathbf x = A^{-1}\mathbf b$ :
> $$A\mathbf x = \mathbf b \iff A^{-1}A\mathbf x = A^{-1}\mathbf b \iff \mathbf x = A^{-1}\mathbf b.$$

> **Théorème** :
> a. si $A$ est inversible, $A^{-1}$ l'est aussi et $(A^{-1})^{-1} = A$ ;
> b. si $A$ et $B$ sont $n \times n$ inversibles, $AB$ l'est aussi et $(AB)^{-1} = B^{-1}A^{-1}$ (produit des inverses dans l'ordre inverse) ;
> c. si $A$ est inversible, $A^T$ l'est aussi et $(A^T)^{-1} = (A^{-1})^T$.

Démonstration de b : $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$, et de même $(B^{-1}A^{-1})(AB) = I$. L'ordre s'inverse comme pour des chaussettes et des chaussures : on met d'abord les chaussettes, mais on les retire en dernier. Pour c, il suffit de transposer $AA^{-1} = I$ : $(A^{-1})^TA^T = I^T = I$. [[Complément hors du cours|ⓘ]]

L'ensemble des matrices $n \times n$ inversibles, stable par produit et par passage à l'inverse, forme un groupe noté $GL_n(\mathbb R)$ ([[Groupe linéaire]]). [[Complément hors du cours|ⓘ]]

> **Théorème** : une matrice $n \times n$ est inversible si et seulement si elle est [[Opérations élémentaires sur les lignes|équivalente par lignes]] à $I_n$ ; dans ce cas, toute suite d'opérations élémentaires qui réduit $A$ à $I_n$ transforme aussi $I_n$ en $A^{-1}$.

### Algorithme de calcul de $A^{-1}$

1. Écrire la [[Matrice augmentée|matrice augmentée]] $[A\ \ I]$.
2. La réduire par opérations élémentaires sur les lignes.
3. Si $A$ est équivalente par lignes à $I$, on obtient $[I\ \ A^{-1}]$ ; sinon, $A$ n'a pas d'inverse.

Pourquoi l'algorithme marche : chaque opération élémentaire sur les lignes revient à multiplier à gauche par une [[Matrice élémentaire|matrice élémentaire]] $E$, obtenue en appliquant cette opération à $I$. Si $E_k \cdots E_1 A = I$, alors $E_k \cdots E_1 = A^{-1}$, et ce même produit appliqué à $I$ donne $E_k \cdots E_1 I = A^{-1}$ : c'est ce que fait la partie droite de $[A\ \ I]$. [[Complément hors du cours|ⓘ]]

Exemple avec $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$ :
$$\left[\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{array}\right] \xrightarrow{L_1 \leftrightarrow L_2} \left[\begin{array}{cc|cc} 1 & 1 & 0 & 1 \\ 2 & 1 & 1 & 0 \end{array}\right] \xrightarrow{L_2 \leftarrow L_2 - 2L_1} \left[\begin{array}{cc|cc} 1 & 1 & 0 & 1 \\ 0 & -1 & 1 & -2 \end{array}\right] \xrightarrow[L_1 \leftarrow L_1 - L_2]{L_2 \leftarrow -L_2} \left[\begin{array}{cc|cc} 1 & 0 & 1 & -1 \\ 0 & 1 & -1 & 2 \end{array}\right]$$
d'où $A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$, ce que confirme la formule $2 \times 2$ ($\det A = 2 - 1 = 1$). [[Complément hors du cours|ⓘ]]

En pratique, pour résoudre $A\mathbf x = \mathbf b$, on ne calcule pas $A^{-1}$ : réduire directement $[A\ \ \mathbf b]$ demande environ trois fois moins d'opérations et accumule moins d'erreurs d'arrondi (voir [[Conditionnement d'une matrice]]). $A^{-1}$ sert surtout en théorie, ou quand on doit résoudre le système pour de nombreux seconds membres. [[Complément hors du cours|ⓘ]]

### Théorème de la matrice inversible (*The Invertible Matrix Theorem*)

Soit $A$ carrée $n \times n$. Les énoncés suivants sont équivalents (tous vrais ou tous faux) ; voir [[3 - Invertible matrix theorem|Invertible matrix theorem]] et [[Théorème de la matrice inversible]] :
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

À cette liste s'ajoute un critère vu dans [[0 - Determinants|Determinants]] ([[Déterminant]]) : $A$ est inversible si et seulement si $\det A \neq 0$, ce qui généralise la condition $ad - bc \neq 0$ du cas $2 \times 2$. [[Complément hors du cours|ⓘ]]

Le théorème ne vaut que pour une matrice **carrée**. Il a une conséquence pratique : pour une matrice carrée, un inverse d'un seul côté suffit ; si $CA = I$, alors automatiquement $AC = I$ et $C = A^{-1}$ (énoncés j et k). [[Complément hors du cours|ⓘ]]

### Transformation linéaire inversible

> **Définition** : $T : \mathbb R^n \to \mathbb R^n$ linéaire est **inversible** s'il existe $S : \mathbb R^n \to \mathbb R^n$ telle que
> $$S(T(\mathbf x)) = \mathbf x \quad (1) \qquad T(S(\mathbf x)) = \mathbf x \quad (2) \qquad \text{pour tout } \mathbf x \in \mathbb R^n.$$

Exemples du cours : $e^x$ et $\ln(x)$ ; $A$ et $A^{-1}$.

**Théorème** : soit $T : \mathbb R^n \to \mathbb R^n$ linéaire, de matrice standard $A$ ([[Matrice d'une application linéaire]]). $T$ est inversible si et seulement si $A$ est inversible ; alors $S$ est unique, linéaire, et donnée par $S(\mathbf x) = A^{-1}\mathbf x$. Les fonctions $e^x$ et $\ln(x)$ illustrent l'idée de réciproque mais ne sont pas linéaires. [[Complément hors du cours|ⓘ]]

![[Chp 0b - Matrix algebra - image4.png]]
*Figure : la multiplication par $A$ envoie $\mathbf x$ sur $A\mathbf x$, la multiplication par $A^{-1}$ ramène $A\mathbf x$ à $\mathbf x$.*
