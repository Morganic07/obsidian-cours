---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp2 - Symmetric matrices and quadratic forms.docx|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp2 - Symmetric matrices and quadratic forms.docx|Chp2 - Symmetric matrices and quadratic forms]], dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Idée générale

Les matrices symétriques se diagonalisent dans une base orthonormale. Ce résultat permet de simplifier et de classer les formes quadratiques, d'optimiser sous contrainte, puis, via $A^TA$, de factoriser n'importe quelle matrice.

## 1. Application linéaire (*linear function / map*)

> $T : V \to W$ est une [[Transformation linéaire|application linéaire]] (*linear map*) si :
> - $T(\mathbf u + \mathbf v) = T(\mathbf u) + T(\mathbf v)$ pour tous $\mathbf u, \mathbf v \in V$ ;
> - $T(\lambda\mathbf v) = \lambda T(\mathbf v)$ pour tout $\lambda \in F$ et tout $\mathbf v \in V$, où $F$ est un corps (*field*, [[Corps (algèbre)]]), par exemple $F = \mathbb R$ ou $F = \mathbb C$ ($\mathbb N$ n'est pas un corps). [[Erreurs du cours#^e-2-symmetric-matrices-and-quadratic-forms|✎]]
>
> L'ensemble des applications linéaires de $V$ dans $W$ se note $L(V, W)$.

**Le déterminant est linéaire par rapport à une colonne.** Si toutes les colonnes de $A$ sont fixées sauf une, $\mathbf x$ :
$$A = [\mathbf a_1\ \cdots\ \mathbf a_{j-1}\ \mathbf x\ \mathbf a_{j+1}\ \cdots\ \mathbf a_n], \qquad T(\mathbf x) = \det[\mathbf a_1\ \cdots\ \mathbf a_{j-1}\ \mathbf x\ \mathbf a_{j+1}\ \cdots\ \mathbf a_n],$$
alors $T$ est linéaire : $T(c\mathbf x) = cT(\mathbf x)$ et $T(\mathbf u + \mathbf v) = T(\mathbf u) + T(\mathbf v)$ pour tous scalaires et vecteurs de $\mathbb R^n$ (voir [[Déterminant]], [[Forme multilinéaire alternée]]).

## 2. Formes bilinéaires (*bilinear forms*)

> **Définition** : une [[Forme bilinéaire|forme bilinéaire]] sur un [[Espace vectoriel|espace vectoriel]] réel $V$ est une fonction $f : V \times V \to \mathbb R$ qui associe un nombre à chaque couple d'éléments de $V$, de façon que $f$ soit **linéaire en chaque variable**.

- Exemple type : le [[Produit scalaire|produit scalaire]] (*dot product*) sur $\mathbb R^n$.
- On écrit souvent $\langle \mathbf x, \mathbf y \rangle$ au lieu de $f(\mathbf x, \mathbf y)$, et l'on identifie une matrice $1 \times 1$ à son unique coefficient.

> **Théorème** : pour une certaine matrice $A$ de taille $n \times n$, une forme bilinéaire sur $\mathbb R^n$ s'écrit
> $$f(\mathbf x, \mathbf y) = \langle \mathbf x, \mathbf y \rangle = \mathbf x^TA\mathbf y = \sum_{i,j} x_i a_{ij} y_j,$$
> avec $\mathbf x = [x_1 \cdots x_n]^T$, $\mathbf y = [y_1 \cdots y_n]^T$.
>
> Exemples du cours : $f(\mathbf x, \mathbf y) = \mathbf x \cdot \mathbf y$ (produit scalaire, **forme bilinéaire**), tandis que $f(\mathbf x, \mathbf y) = \mathbf x + \mathbf y$ n'est pas une forme bilinéaire : c'est une application **linéaire** de $V \times V$ dans $V$, et pas une forme ([[Forme linéaire]]), puisqu'elle donne un vecteur et non un scalaire. [[Erreurs du cours#^e-2-symmetric-matrices-and-quadratic-forms|✎]]

Le coefficient $a_{ij}$ de cette matrice se lit sur la base canonique : $a_{ij} = f(\mathbf e_i, \mathbf e_j)$. La forme est dite **symétrique** quand $f(\mathbf x, \mathbf y) = f(\mathbf y, \mathbf x)$ pour tous $\mathbf x, \mathbf y$, ce qui équivaut à $A^T = A$ : c'est le pont entre formes bilinéaires et matrices symétriques. Le produit scalaire usuel correspond à $A = I$ ; plus généralement, un produit scalaire est une forme bilinéaire symétrique **définie positive** (section 4). [[Complément hors du cours|ⓘ]]

## 3. Diagonalisation des matrices symétriques

> **Définition** : une matrice **symétrique** ([[Matrice symétrique]]) est une matrice $A$ telle que $A^T = A$. Elle est nécessairement **carrée**. Ses coefficients diagonaux sont quelconques, les autres vont par paires, de part et d'autre de la diagonale.

> **Théorème** : une matrice $n \times n$ est **orthogonalement diagonalisable** ([[Diagonalisation]]) si et seulement si elle est symétrique.
>
> Preuve (sens direct) : si $A = PDP^T$ avec $P$ orthogonale, alors $A^T = (PDP^T)^T = P^{TT}D^TP^T = PDP^T = A$.

> **Théorème** : si $A$ est symétrique, deux [[Vecteur propre|vecteurs propres]] de deux [[Espace propre|espaces propres]] différents sont [[Orthogonalité|orthogonaux]].

Preuve : si $A\mathbf v_1 = \lambda_1\mathbf v_1$ et $A\mathbf v_2 = \lambda_2\mathbf v_2$ avec $\lambda_1 \neq \lambda_2$, alors $\lambda_1\,\mathbf v_1\cdot\mathbf v_2 = (A\mathbf v_1)^T\mathbf v_2 = \mathbf v_1^TA^T\mathbf v_2 = \mathbf v_1^TA\mathbf v_2 = \lambda_2\,\mathbf v_1\cdot\mathbf v_2$ ; donc $(\lambda_1 - \lambda_2)\,\mathbf v_1\cdot\mathbf v_2 = 0$, et $\mathbf v_1\cdot\mathbf v_2 = 0$. La symétrie sert à l'étape $A^T = A$. [[Complément hors du cours|ⓘ]]

L'ensemble des [[Valeur propre|valeurs propres]] d'une matrice $A$ s'appelle le **spectre** de $A$ ([[Spectre (algèbre linéaire)]]).

> **[[Théorème spectral]] pour les matrices symétriques** (*The Spectral Theorem for Symmetric Matrices*) : une matrice symétrique $A$ de taille $n \times n$ vérifie :
> a. $A$ a $n$ valeurs propres **réelles**, comptées avec multiplicité ;
> b. la [[Dimension (algèbre linéaire)|dimension]] de l'espace propre de chaque $\lambda$ est égale à la [[Multiplicité d'une valeur propre|multiplicité]] de $\lambda$ comme racine de l'[[Équation caractéristique|équation caractéristique]] ;
> c. les espaces propres sont orthogonaux entre eux : des vecteurs propres de valeurs propres différentes sont orthogonaux ;
> d. $A$ est orthogonalement diagonalisable.

Le point a n'est pas acquis pour une matrice quelconque : la rotation d'un quart de tour $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ a pour équation caractéristique $\lambda^2 + 1 = 0$, sans racine réelle. [[Complément hors du cours|ⓘ]]

**Méthode pour diagonaliser orthogonalement** une matrice symétrique $A$ : [[Complément hors du cours|ⓘ]]
1. trouver les valeurs propres, racines de $\det(A - \lambda I) = 0$ ;
2. pour chacune, trouver une base de l'espace propre (résoudre $(A - \lambda I)\mathbf x = \mathbf 0$) ;
3. si un espace propre est de dimension 2 ou plus, rendre sa base orthogonale par le [[Procédé de Gram-Schmidt]] ; des vecteurs d'espaces propres différents sont déjà orthogonaux ;
4. normaliser chaque vecteur, les ranger en colonnes de $P$, et placer les valeurs propres dans le même ordre sur la diagonale de $D$.

Exemple : $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$. $\det(A - \lambda I) = (3 - \lambda)^2 - 1 = 0$ donne $\lambda_1 = 4$ et $\lambda_2 = 2$, de vecteurs propres unitaires $\mathbf u_1 = \frac{1}{\sqrt 2}(1, 1)$ et $\mathbf u_2 = \frac{1}{\sqrt 2}(1, -1)$. Donc $P = \frac{1}{\sqrt 2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$, $D = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}$ et $A = PDP^T$. [[Complément hors du cours|ⓘ]]

### Décomposition spectrale (*spectral decomposition*)

Soit $A = PDP^{-1}$, où les colonnes de $P$ sont des vecteurs propres **orthonormés** $\mathbf u_1, \ldots, \mathbf u_n$ et $D$ la [[Matrice diagonale|matrice diagonale]] des valeurs propres $\lambda_1, \ldots, \lambda_n$. Comme $P^{-1} = P^T$ :
$$A = PDP^T = [\mathbf u_1\ \cdots\ \mathbf u_n]\begin{bmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{bmatrix}\begin{bmatrix} \mathbf u_1^T \\ \vdots \\ \mathbf u_n^T \end{bmatrix} = [\lambda_1\mathbf u_1\ \cdots\ \lambda_n\mathbf u_n]\begin{bmatrix} \mathbf u_1^T \\ \vdots \\ \mathbf u_n^T \end{bmatrix}$$

**[[Développement colonnes-lignes]]** (*column-row expansion*) : si $A$ est $m \times n$ et $B$ est $n \times p$,
$$AB = [\text{col}_1(A)\ \cdots\ \text{col}_n(A)]\begin{bmatrix} \text{row}_1(B) \\ \vdots \\ \text{row}_n(B) \end{bmatrix} = \text{col}_1(A)\,\text{row}_1(B) + \cdots + \text{col}_n(A)\,\text{row}_n(B).$$

D'où la **[[Décomposition spectrale]]** :
$$A = \lambda_1\mathbf u_1\mathbf u_1^T + \lambda_2\mathbf u_2\mathbf u_2^T + \cdots + \lambda_n\mathbf u_n\mathbf u_n^T.$$
- Chaque colonne de $\lambda_1\mathbf u_1\mathbf u_1^T$ est un multiple de $\mathbf u_1$.
- Chaque matrice $\mathbf u_j\mathbf u_j^T$ est une **matrice de projection** : pour tout $\mathbf x \in \mathbb R^n$, $(\mathbf u_j\mathbf u_j^T)\mathbf x$ est la [[Projection orthogonale|projection orthogonale]] de $\mathbf x$ sur le sous-espace [[Espace engendré|engendré]] par $\mathbf u_j$.

Lecture : $A$ agit sur $\mathbf x$ en le projetant sur chaque axe propre, puis en multipliant chaque projection par sa valeur propre. On en tire aussitôt $A^k = \lambda_1^k\mathbf u_1\mathbf u_1^T + \cdots + \lambda_n^k\mathbf u_n\mathbf u_n^T$. Sur l'exemple ci-dessus : $4 \cdot \frac12\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + 2 \cdot \frac12\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

## 4. Formes quadratiques (*quadratic forms*)

### Écrire une forme quadratique avec une matrice

Une [[Forme quadratique]] dans $\mathbb R^2$ : $ax^2 + bxy + cy^2$, qu'on réécrit $ax^2 + 2b'xy + cy^2$ avec $2b' = b$. Elle s'écrit alors (en notant à nouveau $b$ le coefficient $b'$) :
$$[x\ \ y]\begin{bmatrix} a & b \\ b & c \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \mathbf x^TM\mathbf x,$$
où $M$ est une matrice **symétrique**. On fait de même dans $\mathbb R^n$.

Règle de lecture dans $\mathbb R^n$ : le coefficient diagonal $a_{ii}$ est le coefficient de $x_i^2$, et $a_{ij} = a_{ji}$ vaut la **moitié** du coefficient de $x_ix_j$. Exemple : $Q(\mathbf x) = 5x_1^2 + 3x_2^2 + 2x_3^2 - x_1x_2 + 8x_2x_3$ a pour matrice $\begin{bmatrix} 5 & -1/2 & 0 \\ -1/2 & 3 & 4 \\ 0 & 4 & 2 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

> **Définition** : une forme quadratique sur $\mathbb R^n$ est une fonction $Q$ dont la valeur en $\mathbf x \in \mathbb R^n$ s'écrit $Q(\mathbf x) = \mathbf x^TA\mathbf x$, où $A$ est une matrice $n \times n$ symétrique, appelée **matrice de la forme quadratique**.
>
> Exemple le plus simple de forme quadratique non nulle : $Q(\mathbf x) = \mathbf x^TI\mathbf x = \|\mathbf x\|^2$.

Pourquoi exiger $A$ symétrique : $\mathbf x^TA\mathbf x$ ne change pas si l'on remplace $A$ par $\frac12(A + A^T)$, donc plusieurs matrices donnent la même forme, et seule la symétrique est unique. Une forme quadratique et sa forme bilinéaire symétrique $f(\mathbf x, \mathbf y) = \mathbf x^TA\mathbf y$ se déterminent l'une l'autre : $Q(\mathbf x) = f(\mathbf x, \mathbf x)$ et, en sens inverse, par l'**identité de polarisation** $f(\mathbf x, \mathbf y) = \frac12\big[Q(\mathbf x + \mathbf y) - Q(\mathbf x) - Q(\mathbf y)\big]$. [[Complément hors du cours|ⓘ]]

### Changement de variable (*change of variable*)

- Une forme quadratique est plus simple à utiliser **sans termes croisés** (*cross-product terms*), c'est-à-dire quand sa matrice est diagonale.
- On élimine les termes croisés par un changement de variable.

> Un **changement de variable** est une équation $\mathbf x = P\mathbf y$, ou $\mathbf y = P^{-1}\mathbf x$ (1), où $P$ est [[Matrice inversible|inversible]] et $\mathbf y$ est le vecteur des [[Coordonnées dans une base|coordonnées]] de $\mathbf x$ dans la [[Base (algèbre linéaire)|base]] formée par les colonnes de $P$ ([[Changement de base]]). Alors
> $$\mathbf x^TA\mathbf x = (P\mathbf y)^TA(P\mathbf y) = \mathbf y^TP^TAP\mathbf y = \mathbf y^T(P^TAP)\mathbf y \quad (2)$$
> est une nouvelle forme quadratique, de matrice $P^TAP$. Comme $A$ est symétrique, il existe $P$ **orthogonale** ($P^TP = I$, [[Matrice orthogonale]]) telle que $P^TAP = D$ diagonale ; (2) devient $\mathbf y^TD\mathbf y$.

Calcul : $A = PDP^T = PDP^{-1}$, donc
$$A = PDP^T \iff P^TA = P^TPDP^T \iff P^TA = DP^T \iff P^TAP = DP^TP \iff P^TAP = D.$$

> **[[Théorème des axes principaux]]** (*The Principal Axes Theorem*) : soit $A$ symétrique $n \times n$. Il existe un changement de variable orthogonal $\mathbf x = P\mathbf y$ qui transforme $\mathbf x^TA\mathbf x$ en $\mathbf y^TD\mathbf y$, sans terme croisé.
>
> Les colonnes de $P$ sont les **axes principaux** (*principal axes*) de la forme. $\mathbf y$ est le vecteur des coordonnées de $\mathbf x$ dans la [[Famille orthogonale|base orthonormée]] de $\mathbb R^n$ formée par ces axes.

### Vision géométrique des axes principaux

Soit $Q(\mathbf x) = \mathbf x^TA\mathbf x$, $A$ symétrique $2 \times 2$ inversible, $c$ constante. L'ensemble des $\mathbf x \in \mathbb R^2$ tels que $\mathbf x^TA\mathbf x = c$ est :
- une [[Ellipse|ellipse]] (ou un cercle) ;
- une hyperbole ;
- deux droites sécantes ;
- un point unique ;
- ou ne contient aucun point.

Si $A$ est diagonale, le graphe est en **position standard** :

![[Chp2 - Symmetric matrices and quadratic forms - image26.png]]
*Figure : ellipse $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} = 1$ et hyperbole $\frac{x_1^2}{a^2} - \frac{x_2^2}{b^2} = 1$ ($a > b > 0$), centrées à l'origine, avec les asymptotes de l'hyperbole en pointillés.*

Si $A$ n'est **pas** diagonale, le graphe est **tourné** (*rotated*) par rapport à la position standard :

![[Chp2 - Symmetric matrices and quadratic forms - image20.png]]
*Figure : (a) ellipse $5x_1^2 - 4x_1x_2 + 5x_2^2 = 48$ ; (b) hyperbole $x_1^2 - 8x_1x_2 - 5x_2^2 = 16$, avec les nouveaux axes $y_1$, $y_2$ dans les directions principales.*

Trouver les axes principaux (déterminés par les vecteurs propres de $A$) revient à trouver un nouveau système de coordonnées dans lequel le graphe est en position standard : avec les coordonnées $\mathbf x$, les axes sont $x_1$, $x_2$ ; avec les nouvelles coordonnées $\mathbf y$, ce sont $y_1$, $y_2$.

Exemple, l'ellipse (a) : $5x_1^2 - 4x_1x_2 + 5x_2^2$ a pour matrice $A = \begin{bmatrix} 5 & -2 \\ -2 & 5 \end{bmatrix}$, de valeurs propres $3$ et $7$, de vecteurs propres unitaires $\mathbf u_1 = \frac{1}{\sqrt 2}(1, 1)$ et $\mathbf u_2 = \frac{1}{\sqrt 2}(-1, 1)$. Avec $\mathbf x = P\mathbf y$, $P = [\mathbf u_1\ \mathbf u_2]$, la forme devient $3y_1^2 + 7y_2^2$, et l'équation $= 48$ s'écrit $\frac{y_1^2}{16} + \frac{y_2^2}{48/7} = 1$ : une ellipse de demi-axes $4$ et $\sqrt{48/7} \approx 2{,}62$, tournée de 45°. Prendre $\det P = 1$ fait de $P$ une rotation plutôt qu'une symétrie. [[Complément hors du cours|ⓘ]]

### Classer les formes quadratiques (*classifying quadratic forms*)

Si $A$ est $n \times n$, $Q(\mathbf x) = \mathbf x^TA\mathbf x$ est une fonction sur $\mathbb R^n$ qu'on peut représenter : pour chaque $\mathbf x = (x_1, x_2)$, le graphe montre les points $(x_1, x_2, z)$ avec $z = Q(\mathbf x)$.

![[Chp2 - Symmetric matrices and quadratic forms - image30.png]]
*Figure : (a) $z = 3x_1^2 + 7x_2^2$, cuvette ; (b) $z = 3x_1^2$, gouttière ; (c) $z = 3x_1^2 - 7x_2^2$, selle de cheval ; (d) $z = -3x_1^2 - 7x_2^2$, dôme.*

Les coupes horizontales (coupe 2D parallèle au plan $(x_1, x_2)$) sont : ellipse (graphes 1 et 4), deux droites parallèles (2, car $3x_1^2 = c$ donne $x_1 = \pm\sqrt{c/3}$ ; la parabole en est une coupe verticale), hyperbole (3). [[Erreurs du cours#^e-2-symmetric-matrices-and-quadratic-forms|✎]]

> **Définition** : une forme quadratique $Q$ est
> - **définie positive** (*positive definite*, [[Forme quadratique définie positive]]) : $Q(\mathbf x) > 0$ pour tout $\mathbf x \neq \mathbf 0$ ;
> - **semi-définie positive** (*positive semidefinite*) : $Q(\mathbf x) \ge 0$ ;
> - **définie négative** (*negative definite*) : $Q(\mathbf x) < 0$ pour tout $\mathbf x \neq \mathbf 0$ ; [[Erreurs du cours#^e-2-symmetric-matrices-and-quadratic-forms|✎]]
> - **semi-définie négative** (*negative semidefinite*) : $Q(\mathbf x) \le 0$.
>
> Le cours utilise aussi **indéfinie** (*indefinite*) : $Q$ prend des valeurs positives et négatives, définition déduite de la figure en selle et du théorème c. [[Complément hors du cours|ⓘ]]

![[Chp2 - Symmetric matrices and quadratic forms - image42.png]]
*Figure : définie positive, surface en cuvette au-dessus du plan $x_1x_2$, touchant l'origine.*

![[Chp2 - Symmetric matrices and quadratic forms - image16.png]]
*Figure : définie négative, surface en dôme sous le plan $x_1x_2$, de sommet l'origine.*

![[Chp2 - Symmetric matrices and quadratic forms - image19.png]]
*Figure : indéfinie, surface en selle de cheval passant par l'origine.*

> **Théorème (formes quadratiques et valeurs propres)** : soit $A$ symétrique $n \times n$. La forme $\mathbf x^TA\mathbf x$ est :
> a. définie positive $\iff$ les valeurs propres de $A$ sont toutes positives ;
> b. définie négative $\iff$ elles sont toutes négatives ;
> c. indéfinie $\iff$ $A$ a des valeurs propres positives et négatives.

Pourquoi : dans les axes principaux, $Q = \lambda_1y_1^2 + \cdots + \lambda_ny_n^2$, et $\mathbf y = P^T\mathbf x$ parcourt tous les vecteurs non nuls quand $\mathbf x$ le fait ; le signe de $Q$ se lit donc sur celui des $\lambda_i$. De même, semi-définie positive $\iff$ toutes les valeurs propres sont $\ge 0$, semi-définie négative $\iff$ toutes sont $\le 0$. [[Complément hors du cours|ⓘ]]

En dimension 2, inutile de calculer les valeurs propres : pour $A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$, $\det A = \lambda_1\lambda_2$ et $\text{tr}\,A = \lambda_1 + \lambda_2$ ([[Trace d'une matrice]]). Si $\det A > 0$, les deux valeurs propres ont le même signe, celui de $a$ : définie positive si $a > 0$, définie négative si $a < 0$. Si $\det A < 0$ : indéfinie. Si $\det A = 0$ : semi-définie, du signe de la trace. [[Complément hors du cours|ⓘ]]

**Critère de Sylvester** : une matrice symétrique $A$ est définie positive si et seulement si tous ses **mineurs principaux dominants** $\Delta_k$ (déterminant du bloc $k \times k$ en haut à gauche, $k = 1, \ldots, n$) sont strictement positifs ; elle est définie négative si et seulement si $(-1)^k\Delta_k > 0$ pour tout $k$ (signes alternés, $\Delta_1 < 0$). [[Complément hors du cours|ⓘ]]

**Signature et loi d'inertie de Sylvester** : on peut aussi supprimer les termes croisés par un changement de variable inversible non orthogonal (par exemple en complétant les carrés, méthode de Gauss). Les coefficients obtenus changent, mais le nombre $p$ de coefficients positifs et le nombre $q$ de coefficients négatifs restent toujours les mêmes ; le couple $(p, q)$ est la **signature** de la forme. Avec le changement orthogonal, $p$ et $q$ sont les nombres de valeurs propres positives et négatives. [[Complément hors du cours|ⓘ]]

**Usage en analyse** : en un point critique d'une fonction $C^2$ de $n$ variables, la matrice hessienne des dérivées partielles secondes est symétrique ([[Théorème de Schwarz]]). Définie positive, le point est un minimum local ; définie négative, un maximum local ; indéfinie, un point selle (les surfaces cuvette, dôme et selle ci-dessus) ; semi-définie, on ne peut pas conclure à l'ordre 2 (voir [[Extremum local d'une fonction de deux variables]]). [[Complément hors du cours|ⓘ]]

Toute matrice $A^TA$ est semi-définie positive, car $\mathbf x^TA^TA\mathbf x = \|A\mathbf x\|^2 \ge 0$, et définie positive quand les colonnes de $A$ sont linéairement indépendantes : c'est ce qui fonde la section 6. Réciproquement, toute matrice définie positive s'écrit $A = R^TR$ avec $R$ triangulaire supérieure à diagonale strictement positive (**décomposition de Cholesky**), très utilisée pour résoudre les systèmes $A\mathbf x = \mathbf b$ correspondants. [[Complément hors du cours|ⓘ]]

Le classement d'une forme se transpose à sa matrice : une **matrice définie positive** est une matrice *symétrique* dont la forme $\mathbf x^TA\mathbf x$ est définie positive ; de même pour « matrice semi-définie positive », etc.

## 5. Optimisation sous contrainte (*constrained optimization*)

Voir [[Optimisation sous contrainte]].
- Pour trouver le minimum ou le maximum de $Q(\mathbf x)$, on fait varier $\mathbf x$ parmi les [[Vecteur unitaire|vecteurs unitaires]].
- « $\mathbf x$ unitaire » s'écrit : $\|\mathbf x\| = 1$, $\|\mathbf x\|^2 = 1$, $\mathbf x^T\mathbf x = 1$, ou $x_1^2 + x_2^2 + \cdots + x_n^2 = 1$.
- Sans termes croisés, le minimum et le maximum de $Q(\mathbf x)$ sous $\mathbf x^T\mathbf x = 1$ sont faciles à trouver.

On pose
$$m = \min\{\mathbf x^TA\mathbf x : \|\mathbf x\| = 1\}, \qquad M = \max\{\mathbf x^TA\mathbf x : \|\mathbf x\| = 1\} \quad (2)$$

> **Théorème** : $A$ symétrique, $m$ et $M$ comme en (2). Alors $M$ est la plus grande valeur propre $\lambda_1$ de $A$ et $m$ la plus petite. $\mathbf x^TA\mathbf x$ vaut $M$ quand $\mathbf x$ est un vecteur propre unitaire $\mathbf u_1$ associé à $M$, et vaut $m$ quand $\mathbf x$ est un vecteur propre unitaire associé à $m$.

Pourquoi : avec $\mathbf x = P\mathbf y$, $P$ orthogonale, $\|\mathbf y\| = \|\mathbf x\| = 1$ et $Q = \lambda_1y_1^2 + \cdots + \lambda_ny_n^2 \le \lambda_1(y_1^2 + \cdots + y_n^2) = \lambda_1$, avec égalité pour $\mathbf y = \mathbf e_1$, c'est-à-dire $\mathbf x = \mathbf u_1$ ; même raisonnement pour le minimum. Exemple : sur le cercle unité, $5x_1^2 - 4x_1x_2 + 5x_2^2$ (section 4) a pour maximum $7$, atteint en $\pm\frac{1}{\sqrt 2}(-1, 1)$, et pour minimum $3$, atteint en $\pm\frac{1}{\sqrt 2}(1, 1)$. [[Complément hors du cours|ⓘ]]

Sans contrainte de norme, on étudie le **quotient de Rayleigh** $R(\mathbf x) = \dfrac{\mathbf x^TA\mathbf x}{\mathbf x^T\mathbf x}$ ($\mathbf x \neq \mathbf 0$), qui ne dépend que de la direction de $\mathbf x$ : le théorème s'écrit $\lambda_n \le R(\mathbf x) \le \lambda_1$. [[Complément hors du cours|ⓘ]]

> **Théorème** (contraintes supplémentaires) : avec $A$, $\lambda_1$, $\mathbf u_1$ comme ci-dessus, le maximum de $\mathbf x^TA\mathbf x$ sous les contraintes
> $$\mathbf x^T\mathbf x = 1, \quad \mathbf x^T\mathbf u_1 = 0$$
> est la deuxième plus grande valeur propre $\lambda_2$, atteint en un vecteur propre $\mathbf u_2$ associé à $\lambda_2$.

> **Théorème** (cas général) : $A$ symétrique $n \times n$, diagonalisée orthogonalement $A = PDP^{-1}$ avec $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$ sur la diagonale de $D$ et les vecteurs propres unitaires correspondants $\mathbf u_1, \ldots, \mathbf u_n$ en colonnes de $P$. Pour $k = 2, \ldots, n$, le maximum de $\mathbf x^TA\mathbf x$ sous les contraintes
> $$\mathbf x^T\mathbf x = 1, \quad \mathbf x^T\mathbf u_1 = 0, \quad \ldots, \quad \mathbf x^T\mathbf u_{k-1} = 0$$
> est $\lambda_k$, atteint en $\mathbf x = \mathbf u_k$.

Application : l'[[Analyse en composantes principales]] cherche la direction unitaire $\mathbf u$ qui maximise la variance $\mathbf u^TS\mathbf u$ des données projetées, $S$ étant la matrice de covariance (symétrique). Par ces théorèmes, la première composante principale est le vecteur propre de la plus grande valeur propre de $S$, la deuxième celui de $\lambda_2$ (orthogonale à la première), etc. ; chaque $\lambda_k$ est la variance expliquée par la $k$-ième composante. [[Complément hors du cours|ⓘ]]

## 6. Décomposition en valeurs singulières (*singular value decomposition, SVD*)

- Toutes les matrices ne se factorisent pas en $PDP^{-1}$ avec $D$ diagonale.
- Mais **toute** matrice $A$ de taille $m \times n$ se factorise en $A = U\Sigma V^T$ : c'est la [[Décomposition en valeurs singulières|décomposition en valeurs singulières]]. [[Erreurs du cours#^e-2-symmetric-matrices-and-quadratic-forms|✎]]

**Propriété de départ** : la [[Valeur absolue|valeur absolue]] des valeurs propres d'une matrice symétrique mesure de combien $A$ étire ou contracte certains vecteurs (ses vecteurs propres). Si $A\mathbf x = \lambda\mathbf x$ et $\|\mathbf x\| = 1$ :
$$\|A\mathbf x\| = \|\lambda\mathbf x\| = |\lambda|\,\|\mathbf x\| = |\lambda| \quad (1)$$
- Si $\lambda_1$ est la valeur propre de plus grand module, un vecteur propre **unitaire** associé $\mathbf v_1$ donne la direction où l'**effet d'étirement** de $A$ est le plus grand.
- La longueur de $A\mathbf x$ est maximale pour $\mathbf x = \mathbf v_1$, et $\|A\mathbf v_1\| = |\lambda_1|$ par (1).
- Cette description a un analogue pour les matrices rectangulaires, qui mène à la SVD.

### Valeurs singulières d'une matrice $m \times n$

Soit $A$ de taille $m \times n$. $A^TA$ est symétrique, donc orthogonalement diagonalisable. Soit $\{\mathbf v_1, \ldots, \mathbf v_n\}$ une base orthonormée de $\mathbb R^n$ formée de vecteurs propres de $A^TA$, de valeurs propres $\lambda_1, \ldots, \lambda_n$. Pour $1 \le i \le n$ :
$$\|A\mathbf v_i\|^2 = (A\mathbf v_i)^TA\mathbf v_i = \mathbf v_i^TA^TA\mathbf v_i = \mathbf v_i^T(\lambda_i\mathbf v_i) = \lambda_i$$
(car $\mathbf v_i$ est vecteur propre de $A^TA$, puis unitaire). Les valeurs propres de $A^TA$ sont donc toutes positives ou nulles ; on les renumérote : $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n \ge 0$.

> **Définition** : les **valeurs singulières** (*singular values*) de $A$ sont les racines carrées des valeurs propres de $A^TA$, notées $\sigma_1, \ldots, \sigma_n$, rangées par ordre décroissant : $\sigma_i = \sqrt{\lambda_i}$. Ce sont les longueurs des vecteurs $A\mathbf v_1, \ldots, A\mathbf v_n$.

> **Théorème** : soit $\{\mathbf v_1, \ldots, \mathbf v_n\}$ une base orthonormée de $\mathbb R^n$ de vecteurs propres de $A^TA$, avec $\lambda_1 \ge \cdots \ge \lambda_n$, et supposons que $A$ a $r$ valeurs singulières non nulles. Alors $\{A\mathbf v_1, \ldots, A\mathbf v_r\}$ est une base orthogonale de $\text{Col}\,A$, et $\text{rank}\,A = r$ ([[Rang d'une matrice|rang]] = dimension de l'[[Espace des colonnes|espace des colonnes]]).

Preuve : pour $i \neq j$, $(A\mathbf v_i)\cdot(A\mathbf v_j) = \mathbf v_i^TA^TA\mathbf v_j = \lambda_j\,\mathbf v_i\cdot\mathbf v_j = 0$ ; les $A\mathbf v_i$ sont non nuls pour $i \le r$ et nuls pour $i > r$ ($\|A\mathbf v_i\| = \sigma_i$). Tout $\mathbf y = A\mathbf x$, avec $\mathbf x = c_1\mathbf v_1 + \cdots + c_n\mathbf v_n$, s'écrit $c_1A\mathbf v_1 + \cdots + c_rA\mathbf v_r$ : ces $r$ vecteurs orthogonaux non nuls engendrent donc $\text{Col}\,A$. [[Complément hors du cours|ⓘ]]

> **Théorème (SVD)** : soit $A$ de taille $m \times n$ et de rang $r$. Il existe une matrice $\Sigma$ ($m \times n$) de la forme
> $$\Sigma = \begin{bmatrix} D & 0 \\ 0 & 0 \end{bmatrix} \quad (3)$$
> ($m - r$ lignes nulles en bas, $n - r$ colonnes nulles à droite), où $D$ est diagonale $r \times r$ de coefficients les $r$ premières valeurs singulières $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$, et il existe $U$ orthogonale $m \times m$ et $V$ orthogonale $n \times n$ telles que
> $$A = U\Sigma V^T, \qquad A_{m \times n} = U_{m \times m}\,\Sigma_{m \times n}\,V^T_{n \times n}.$$
> ($r$ ne dépasse pas $\min(m, n)$ ; si $r = m$ ou $r = n$, certains blocs nuls disparaissent.)

Toute factorisation $A = U\Sigma V^T$ avec $U$, $V$ [[Matrice orthogonale|orthogonales]], $\Sigma$ comme en (3) et coefficients diagonaux de $D$ positifs est **une** SVD de $A$. $U$ et $V$ ne sont pas uniques, mais les coefficients diagonaux de $\Sigma$ sont nécessairement les valeurs singulières de $A$.
- Les colonnes de $U$ sont les **vecteurs singuliers à gauche** (*left singular vectors*).
- Les colonnes de $V$ sont les **vecteurs singuliers à droite** (*right singular vectors*).

**Construire une SVD** : [[Complément hors du cours|ⓘ]]
1. diagonaliser orthogonalement $A^TA$, valeurs propres rangées par ordre décroissant : leurs vecteurs propres unitaires forment $V$ ;
2. prendre $\sigma_i = \sqrt{\lambda_i}$ et former $\Sigma$ ;
3. pour $i \le r$, poser $\mathbf u_i = \dfrac{A\mathbf v_i}{\sigma_i}$ (orthonormés d'après le théorème précédent) ;
4. si $r < m$, compléter $\mathbf u_1, \ldots, \mathbf u_r$ en une base orthonormée de $\mathbb R^m$ (vecteurs de $\text{Nul}\,A^T$, rendus orthonormés par [[Procédé de Gram-Schmidt|Gram-Schmidt]]) : on obtient $U$.

Exemple : $A = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$. $A^TA = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ a pour valeurs propres $2$ et $0$, de vecteurs propres $\mathbf v_1 = \frac{1}{\sqrt 2}(1, 1)$, $\mathbf v_2 = \frac{1}{\sqrt 2}(1, -1)$ ; $\sigma_1 = \sqrt 2$, $r = 1$, $\mathbf u_1 = A\mathbf v_1/\sqrt 2 = (1, 0)$, complété par $\mathbf u_2 = (0, 1)$. D'où $A = I\begin{bmatrix} \sqrt 2 & 0 \\ 0 & 0 \end{bmatrix}V^T$. [[Complément hors du cours|ⓘ]]

**SVD réduite** : seules les $r$ premières colonnes de $U$ et de $V$ servent, d'où $A = U_rDV_r^T = \sigma_1\mathbf u_1\mathbf v_1^T + \cdots + \sigma_r\mathbf u_r\mathbf v_r^T$, somme de $r$ matrices de rang 1, analogue de la décomposition spectrale. [[Complément hors du cours|ⓘ]]

**Approximation de rang faible** : garder les $k$ premiers termes, $A_k = \sigma_1\mathbf u_1\mathbf v_1^T + \cdots + \sigma_k\mathbf u_k\mathbf v_k^T$, donne la meilleure approximation de $A$ par une matrice de rang $k$ (théorème d'Eckart-Young, 1936), avec une erreur $\|A - A_k\|_2 = \sigma_{k+1}$ en norme spectrale ($\|A\|_2 = \sigma_1$, le plus grand étirement). C'est le principe de la compression d'images, du débruitage et de l'ACP, qui revient à une SVD de la matrice des données centrées. [[Complément hors du cours|ⓘ]]

### Application

- Si $A$ est $n \times n$ inversible, le rapport $\sigma_1/\sigma_n$ de la plus grande à la plus petite valeur singulière est le **conditionnement** (*condition number*, [[Conditionnement d'une matrice]]) de $A$.
- Il vaut au moins $1$, et exactement $1$ pour une matrice orthogonale. Plus il est grand, plus $A$ est **mal conditionnée** : une petite erreur relative sur $\mathbf b$ peut produire, sur la solution de $A\mathbf x = \mathbf b$, une erreur relative jusqu'à $\sigma_1/\sigma_n$ fois plus grande. [[Complément hors du cours|ⓘ]]
- **[[Pseudo-inverse]]** : $A^+ = V_rD^{-1}U_r^T$. Pour tout $\mathbf b$, $\hat{\mathbf x} = A^+\mathbf b$ est une solution de [[Moindres carrés|moindres carrés]] de $A\mathbf x = \mathbf b$, celle de plus petite norme ; si $A$ est inversible, $A^+ = A^{-1}$. [[Complément hors du cours|ⓘ]]
- $U$ et $V$, orthogonales, ne changent ni les longueurs ni les angles.
- Les instabilités possibles des calculs numériques se lisent dans $\Sigma$.
- Si les valeurs singulières sont extrêmement grandes ou petites, les erreurs d'arrondi sont presque inévitables, mais l'analyse d'erreur est facilitée par la connaissance de $\Sigma$ et $V$.

### Résumé de la SVD

- Les colonnes de $U$ sont les vecteurs propres de $AA^T$.
- Les colonnes de $V$ sont les vecteurs propres de $A^TA$.
- Les coefficients diagonaux de $\Sigma$ sont les valeurs singulières $\sigma_i = \sqrt{\lambda_i}$.
- Relations (avec normalisation) : $A\mathbf v_i = \sigma_i\mathbf u_i$ et $A^T\mathbf u_i = \sigma_i\mathbf v_i$ ; le facteur vient de $\|A\mathbf v_i\| = \sigma_i = \|A^T\mathbf u_i\|$.
- Pour une matrice symétrique, les valeurs singulières sont les valeurs absolues des valeurs propres ; pour une matrice symétrique définie positive, la SVD et la décomposition spectrale $PDP^T$ coïncident. [[Complément hors du cours|ⓘ]]

![[Chp2 - Symmetric matrices and quadratic forms - image39.png]]
*Figure : schéma $A_{m \times n} = U_{m \times m}\Sigma_{m \times n}V^T_{n \times n}$, avec la diagonale $\sigma_1, \ldots, \sigma_r$ puis des zéros dans $\Sigma$.*

### La SVD et les quatre sous-espaces

Si les colonnes de $V$ sont rangées par valeur singulière décroissante et $\text{rank}\,A = r$ (voir [[Sous-espaces fondamentaux]]) :
- $\text{Null}(A) = \text{span}\{\mathbf v_{r+1}, \ldots, \mathbf v_n\}$ : base orthonormée de l'[[Espace nul|espace nul]] de $A^TA$, donc de $A$ (l'espace propre $E_0$ de $A^TA$ est le null space de $A$) ;
- $\text{Row}(A) = \text{span}\{\mathbf v_1, \ldots, \mathbf v_r\}$ ;
- $\text{Col}(A) = \text{span}\{\mathbf u_1, \ldots, \mathbf u_r\}$, de dimension $r$ ;
- $\text{Null}(A^T) = \text{span}\{\mathbf u_{r+1}, \ldots, \mathbf u_m\}$.
