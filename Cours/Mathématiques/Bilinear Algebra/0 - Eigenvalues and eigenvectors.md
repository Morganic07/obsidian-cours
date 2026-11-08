---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0e - Eigenvalues and eigenvectors.docx|Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0e - Eigenvalues and eigenvectors.docx|Chp 0e - Eigenvalues and eigenvectors]], dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Idée générale

Une matrice agit sur certains vecteurs par simple multiplication. Ces directions permettent de la diagonaliser, donc de calculer facilement ses puissances.

## 1. Valeurs propres et vecteurs propres

> **Définition** : un **vecteur propre** (*eigenvector*, [[Vecteur propre]]) d'une matrice $A$ de taille $n \times n$ est un vecteur **non nul** $\mathbf x$ tel que $A\mathbf x = \lambda\mathbf x$ pour un scalaire $\lambda$. Un scalaire $\lambda$ est une **valeur propre** (*eigenvalue*, [[Valeur propre]]) de $A$ s'il existe une solution non triviale $\mathbf x$ de $A\mathbf x = \lambda\mathbf x$ ; un tel $\mathbf x$ est un *vecteur propre associé à $\lambda$*.

- Un vecteur propre doit être $\neq \mathbf 0$.
- Une valeur propre peut être $= 0$.

**Lecture géométrique.** En général, $A$ change la direction d'un vecteur. Un vecteur propre est un vecteur dont la direction est conservée : $A\mathbf x$ reste sur la droite de $\mathbf x$, étiré ($|\lambda| > 1$), raccourci ($|\lambda| < 1$), retourné ($\lambda < 0$) ou écrasé sur $\mathbf 0$ ($\lambda = 0$). Exemple : pour la réflexion d'axe $Ox_1$, $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$, les vecteurs de l'axe $Ox_1$ sont propres pour $\lambda = 1$ et ceux de l'axe $Ox_2$ pour $\lambda = -1$. [[Complément hors du cours|ⓘ]]

**Vérifier qu'un vecteur est propre** ne demande aucun calcul de valeur propre : on calcule $A\mathbf x$ et l'on regarde s'il est multiple de $\mathbf x$. Exemple : $\begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}\begin{bmatrix} 6 \\ -5 \end{bmatrix} = \begin{bmatrix} -24 \\ 20 \end{bmatrix} = -4\begin{bmatrix} 6 \\ -5 \end{bmatrix}$ : vecteur propre associé à $\lambda = -4$. [[Complément hors du cours|ⓘ]]

> $\lambda$ est valeur propre $\iff$ $(A - \lambda I)\mathbf x = \mathbf 0$ a une solution **non triviale**.

- Les solutions d'un [[Système linéaire homogène|système homogène]] sont les solutions de base et leurs [[Combinaison linéaire|combinaisons linéaires]] ; le cours en tire que toute combinaison linéaire **non nulle** de vecteurs propres de base associés à une **même** valeur propre est un vecteur propre (un vecteur propre est non nul). [[Erreurs du cours#^e-0-eigenvalues-and-eigenvectors|✎]]
- L'ensemble des solutions de cette équation est l'[[Espace nul|espace nul]] de $A - \lambda I$. C'est un [[Sous-espace vectoriel|sous-espace]] de $\mathbb R^n$, appelé **espace propre** (*eigenspace*, [[Espace propre]]) de $A$ associé à $\lambda$.
- **L'espace propre est formé du vecteur nul et de tous les vecteurs propres associés à $\lambda$.**

Pour une valeur propre $\lambda$ :
- $(\lambda I - A)^{-1}$ n'existe pas ;
- une matrice non inversible a un [[Déterminant|déterminant]] nul ;
- donc $\det(\lambda I - A) = 0 \iff \det(A - \lambda I) = 0$.

> **Avertissement** (*warning*) : la [[Opérations élémentaires sur les lignes|réduction par lignes]] sert à trouver les vecteurs propres (exemple 3 du manuel), mais **pas** les valeurs propres. Une [[Forme échelonnée|forme échelonnée]] de $A$ ne montre généralement **pas** les valeurs propres de $A$.

**Valeur propre nulle** : $0$ est valeur propre $\iff (A - 0I)\mathbf x = \mathbf 0$ a une solution non triviale $\iff A\mathbf x = \mathbf 0$ a une solution non triviale $\iff A$ n'est pas inversible. Donc :
$$0 \text{ est valeur propre de } A \iff A \text{ n'est pas inversible.}$$

> **Théorème** : les valeurs propres d'une [[Matrice triangulaire|matrice triangulaire]] sont les coefficients de sa diagonale principale.

Ce théorème ne vaut que pour une matrice **déjà** triangulaire : réduire $A$ sous forme échelonnée donne bien une matrice triangulaire, mais la réduction par lignes change les valeurs propres (voir l'avertissement ci-dessus), et la diagonale obtenue ne les montre pas. [[Erreurs du cours#^e-0-eigenvalues-and-eigenvectors|✎]]

> **Théorème** : si $\mathbf v_1, \ldots, \mathbf v_r$ sont des vecteurs propres associés à des valeurs propres **distinctes** $\lambda_1, \ldots, \lambda_r$ d'une matrice $n \times n$, alors $\{\mathbf v_1, \ldots, \mathbf v_r\}$ est [[Indépendance linéaire|linéairement indépendante]].

**Puissances** : si $A\mathbf x = \lambda\mathbf x$, alors $A^n\mathbf x = \lambda^n\mathbf x$.
Preuve par [[Récurrence|récurrence]] :
$$A^n\mathbf x = \lambda^n\mathbf x \Rightarrow AA^n\mathbf x = A\lambda^n\mathbf x \iff A^{n+1}\mathbf x = \lambda^n A\mathbf x \iff A^{n+1}\mathbf x = \lambda^n\lambda\mathbf x \iff A^{n+1}\mathbf x = \lambda^{n+1}\mathbf x.$$

De même, si $A$ est inversible (donc $\lambda \neq 0$), $A^{-1}\mathbf x = \dfrac{1}{\lambda}\mathbf x$ : on multiplie $A\mathbf x = \lambda\mathbf x$ par $A^{-1}$, ce qui donne $\mathbf x = \lambda A^{-1}\mathbf x$, puis on divise par $\lambda$. $A$ et $A^{-1}$ ont les mêmes vecteurs propres, de valeurs propres inverses. [[Complément hors du cours|ⓘ]]

## 2. Équation caractéristique (*characteristic equation*)

> **Théorème** : un scalaire $\lambda$ est valeur propre d'une matrice $n \times n$ si et seulement si $\lambda$ vérifie l'[[Équation caractéristique|équation caractéristique]]
> $$\det(A - \lambda I) = 0.$$

- C'est une équation polynomiale de degré $n$, de la forme $a\lambda^n + b\lambda^{n-1} + \cdots + \text{cst}$.
- Elle a donc $n$ racines (comptées avec multiplicité), et les racines complexes sont admises.
- Trouver à la main les valeurs propres d'une matrice plus grande que $2 \times 2$ ou $3 \times 3$ est compliqué.

Le membre de gauche, $\det(A - \lambda I)$, s'appelle le **polynôme caractéristique** de $A$. En taille $2$, pour $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ :
$$\det(A - \lambda I) = (a - \lambda)(d - \lambda) - bc = \lambda^2 - (a + d)\lambda + (ad - bc) = \lambda^2 - \text{tr}(A)\,\lambda + \det A,$$
où $\text{tr}(A) = a + d$ est la [[Trace d'une matrice|trace]] (somme de la diagonale). [[Complément hors du cours|ⓘ]]

**Trace, déterminant et valeurs propres.** Pour toute matrice $n \times n$ de valeurs propres $\lambda_1, \ldots, \lambda_n$ (complexes éventuellement, répétées selon leur multiplicité) :
$$\lambda_1 + \lambda_2 + \cdots + \lambda_n = \text{tr}(A), \qquad \lambda_1\lambda_2\cdots\lambda_n = \det A.$$
C'est un contrôle rapide d'un calcul de valeurs propres, et cela redonne le résultat de la section 1 : $0$ est valeur propre si et seulement si $\det A = 0$. [[Complément hors du cours|ⓘ]]

**Racines complexes : un exemple.** La rotation d'un quart de tour, $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, a pour polynôme caractéristique $\lambda^2 + 1$, sans racine réelle ($\lambda = \pm i$) : aucun vecteur non nul du plan ne garde sa direction quand on le fait tourner de $90°$. Une matrice réelle peut donc n'avoir aucune valeur propre réelle, et ne pas être diagonalisable sur $\mathbb R$. [[Complément hors du cours|ⓘ]]

> **Théorème de la matrice inversible (suite)** : $A$ ($n \times n$) est inversible si et seulement si :
> s. le nombre $0$ n'est **pas** valeur propre de $A$ ;
> t. le déterminant de $A$ n'est **pas** nul.
>
> Voir [[3 - Invertible matrix theorem|Invertible matrix theorem]], [[Matrice inversible]].

## 3. Diagonalisation (*diagonalization*)

Dans beaucoup de cas, l'information sur les valeurs et vecteurs propres de $A$ s'exprime par une factorisation utile
$$A = PDP^{-1},$$
où $D$ est une [[Matrice diagonale|matrice diagonale]]. Elle sert à calculer les puissances : $A^n = PD^nP^{-1}$.

Pourquoi : dans $A^2 = (PDP^{-1})(PDP^{-1}) = PD(P^{-1}P)DP^{-1} = PD^2P^{-1}$, les $P^{-1}P$ du milieu se simplifient, et de même pour toute puissance. Or $D^n$ s'obtient en élevant chaque coefficient diagonal à la puissance $n$, ce qui ne coûte presque rien. [[Complément hors du cours|ⓘ]]

Deux matrices $A$ et $B$ telles que $A = PBP^{-1}$ ($P$ inversible) sont dites **semblables** ([[Matrices semblables]]) : elles représentent la même [[Transformation linéaire|transformation]] dans deux bases différentes, et ont le même polynôme caractéristique, donc les mêmes valeurs propres avec les mêmes multiplicités, la même trace et le même déterminant. Diagonaliser, c'est trouver une matrice diagonale semblable à $A$, c'est-à-dire une base (celle des vecteurs propres) dans laquelle la transformation agit coordonnée par coordonnée. [[Complément hors du cours|ⓘ]]

> **Théorème de diagonalisation** ([[Diagonalisation]]) : une matrice $n \times n$ est diagonalisable si et seulement si elle a $n$ vecteurs propres linéairement indépendants. Plus précisément, $A = PDP^{-1}$ avec $D$ diagonale si et seulement si les colonnes de $P$ sont $n$ vecteurs propres linéairement indépendants de $A$. Les coefficients diagonaux de $D$ sont alors les valeurs propres associées, dans le même ordre, aux vecteurs propres de $P$.

Autrement dit, $A$ est diagonalisable $\iff$ il y a assez de vecteurs propres pour former une [[Base (algèbre linéaire)|base]] de $\mathbb R^n$, appelée **base de vecteurs propres** (*eigenvector basis*).

> **Théorème** : une matrice $n \times n$ ayant $n$ valeurs propres **distinctes** est diagonalisable.
> - Les valeurs propres doivent être distinctes pour appliquer ce théorème.
> - Mais avoir $n$ valeurs propres distinctes n'est **pas nécessaire** pour être diagonalisable (condition suffisante seulement).

> **Théorème** : $A$ de taille $n \times n$, de valeurs propres distinctes $\lambda_1, \ldots, \lambda_p$.
> a. Pour $1 \le k \le p$, la [[Dimension (algèbre linéaire)|dimension]] de l'espace propre de $\lambda_k$ est inférieure ou égale à la [[Multiplicité d'une valeur propre|multiplicité]] de $\lambda_k$.
> b. $A$ est diagonalisable si et seulement si la somme des dimensions des espaces propres vaut $n$, ce qui a lieu si et seulement si (i) le polynôme caractéristique se factorise entièrement en facteurs du premier degré et (ii) la dimension de l'espace propre de chaque $\lambda_k$ est égale à sa multiplicité.
> c. Si $A$ est diagonalisable et $\mathcal B_k$ une base de l'espace propre de $\lambda_k$ pour chaque $k$, la réunion des $\mathcal B_1, \ldots, \mathcal B_p$ forme une base de vecteurs propres de $\mathbb R^n$.

## 4. Méthode : diagonaliser une matrice $A$ de taille $n \times n$

1. **Trouver les valeurs propres de $A$** : écrire $\det(A - \lambda I) = 0$, ce qui donne l'équation caractéristique en $\lambda^n, \ldots$ ; la résoudre pour trouver chaque $\lambda$ avec sa multiplicité.
2. **Déterminer les vecteurs propres** : pour chaque $\lambda_i$, résoudre $(A - \lambda_i I)\mathbf x = \mathbf 0$. Vérifier qu'il y a bien $n$ vecteurs propres linéairement indépendants ; sinon, $A$ n'est pas diagonalisable.
3. **Construire $P$** : placer les vecteurs propres $\mathbf x_i$ en colonnes.
4. **Construire $D$** : placer les valeurs propres $\lambda_i$ sur la diagonale, **dans le même ordre** que les vecteurs propres de $P$.
5. **Calculer $P^{-1}$** : $P$ est formée de vecteurs indépendants, donc inversible par le théorème de la matrice inversible, et $[P \mid I] \sim [I \mid P^{-1}]$.
6. **Vérifier** que $A = PDP^{-1}$ (ou, plus simplement, $AP = PD$).

Le cours ne donne pas d'exemple chiffré de diagonalisation dans cette note.

**Exemple complet** avec $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$ : [[Complément hors du cours|ⓘ]]
1. $\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2)$ : valeurs propres $5$ et $2$, distinctes, donc $A$ est diagonalisable (contrôle : $5 + 2 = 7 = \text{tr}\,A$ et $5 \times 2 = 10 = \det A$). [[Complément hors du cours|ⓘ]]
2. $\lambda = 5$ : $A - 5I = \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix}$, d'où $x_1 = x_2$ et $\mathbf v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$. $\lambda = 2$ : $A - 2I = \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}$, d'où $x_2 = -2x_1$ et $\mathbf v_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]
3. $P = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}$ ($\mathbf v_1$ puis $\mathbf v_2$ en colonnes). [[Complément hors du cours|ⓘ]]
4. $D = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix}$ ($5$ puis $2$, dans le même ordre). [[Complément hors du cours|ⓘ]]
5. $\det P = -3$, donc $P^{-1} = \dfrac{1}{3}\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]
6. $A\mathbf v_1 = \begin{bmatrix} 5 \\ 5 \end{bmatrix} = 5\mathbf v_1$ et $A\mathbf v_2 = \begin{bmatrix} 2 \\ -4 \end{bmatrix} = 2\mathbf v_2$, donc $AP = PD$. [[Complément hors du cours|ⓘ]]

On en tire toutes les puissances d'un coup : $A^k = PD^kP^{-1} = \dfrac{1}{3}\begin{bmatrix} 2 \cdot 5^k + 2^k & 5^k - 2^k \\ 2 \cdot 5^k - 2 \cdot 2^k & 5^k + 2 \cdot 2^k \end{bmatrix}$ (pour $k = 1$, on retrouve bien $A$). [[Complément hors du cours|ⓘ]]

**Contre-exemple : une matrice non diagonalisable.** $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ (le cisaillement horizontal de [[0 - Linear combination]]) est triangulaire, de valeur propre unique $1$, de multiplicité $2$. Mais $A - I = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ impose seulement $x_2 = 0$ : l'espace propre est la droite engendrée par $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$, de dimension $1 < 2$. Il n'y a pas deux vecteurs propres indépendants, donc pas de diagonalisation possible. [[Complément hors du cours|ⓘ]]

**À quoi ça sert, au-delà du calcul de puissances.** Les valeurs et vecteurs propres sont partout : l'[[Analyse en composantes principales]] cherche les vecteurs propres de la matrice de covariance (les directions où les données varient le plus) ; le classement des pages web par les moteurs de recherche (PageRank) et la loi stationnaire d'une chaîne de Markov sont des vecteurs propres associés à la valeur propre $1$ ; en mécanique, les modes propres de vibration d'une structure sont les vecteurs propres de son modèle. Dans un système $\mathbf x_{k+1} = A\mathbf x_k$, les valeurs propres de module $> 1$ font exploser $\mathbf x_k$ dans leur direction, celles de module $< 1$ le font décroître. [[Complément hors du cours|ⓘ]]
