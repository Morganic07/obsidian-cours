---
type: source
tags: [year2]
sources: ["[[Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp 0e - Eigenvalues and eigenvectors]], dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une matrice agit sur certains vecteurs par simple multiplication. Ces directions permettent de la diagonaliser, donc de calculer facilement ses puissances.

## 1. Valeurs propres et vecteurs propres

> **Définition** : un **vecteur propre** (*eigenvector*, [[Vecteur propre]]) d'une matrice $A$ de taille $n \times n$ est un vecteur **non nul** $\mathbf x$ tel que $A\mathbf x = \lambda\mathbf x$ pour un scalaire $\lambda$. Un scalaire $\lambda$ est une **valeur propre** (*eigenvalue*, [[Valeur propre]]) de $A$ s'il existe une solution non triviale $\mathbf x$ de $A\mathbf x = \lambda\mathbf x$ ; un tel $\mathbf x$ est un *vecteur propre associé à $\lambda$*.

- Un vecteur propre doit être $\neq \mathbf 0$.
- Une valeur propre peut être $= 0$.

> $\lambda$ est valeur propre $\iff$ $(A - \lambda I)\mathbf x = \mathbf 0$ a une solution **non triviale**.

- Les solutions d'un [[Système linéaire homogène|système homogène]] sont les solutions de base et leurs [[Combinaison linéaire|combinaisons linéaires]] ; le cours en tire que « toute combinaison linéaire de vecteurs propres de base est un vecteur propre » (voir « Points à vérifier »).
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

La note de cours ajoute : « très pratique si on réduit une matrice sous forme échelonnée, la matrice sera souvent triangulaire, on repère direct les eigenvalues ». C'est **contraire** à l'avertissement ci-dessus (voir « Points à vérifier ») : le théorème ne vaut que pour une matrice déjà triangulaire.

> **Théorème** : si $\mathbf v_1, \ldots, \mathbf v_r$ sont des vecteurs propres associés à des valeurs propres **distinctes** $\lambda_1, \ldots, \lambda_r$ d'une matrice $n \times n$, alors $\{\mathbf v_1, \ldots, \mathbf v_r\}$ est [[Indépendance linéaire|linéairement indépendante]].

**Puissances** : si $A\mathbf x = \lambda\mathbf x$, alors $A^n\mathbf x = \lambda^n\mathbf x$.
Preuve par [[Récurrence|récurrence]] :
$$A^n\mathbf x = \lambda^n\mathbf x \Rightarrow AA^n\mathbf x = A\lambda^n\mathbf x \iff A^{n+1}\mathbf x = \lambda^n A\mathbf x \iff A^{n+1}\mathbf x = \lambda^n\lambda\mathbf x \iff A^{n+1}\mathbf x = \lambda^{n+1}\mathbf x.$$

## 2. Équation caractéristique (*characteristic equation*)

> **Théorème** : un scalaire $\lambda$ est valeur propre d'une matrice $n \times n$ si et seulement si $\lambda$ vérifie l'[[Équation caractéristique|équation caractéristique]]
> $$\det(A - \lambda I) = 0.$$

- C'est une équation polynomiale de degré $n$, de la forme $a\lambda^n + b\lambda^{n-1} + \cdots + \text{cst}$.
- Elle a donc $n$ racines (comptées avec multiplicité), et les racines complexes sont admises.
- Trouver à la main les valeurs propres d'une matrice plus grande que $2 \times 2$ ou $3 \times 3$ est compliqué.

> **Théorème de la matrice inversible (suite)** : $A$ ($n \times n$) est inversible si et seulement si :
> s. le nombre $0$ n'est **pas** valeur propre de $A$ ;
> t. le déterminant de $A$ n'est **pas** nul.
>
> Voir [[Invertible matrix theorem]], [[Matrice inversible]].

## 3. Diagonalisation (*diagonalization*)

Dans beaucoup de cas, l'information sur les valeurs et vecteurs propres de $A$ s'exprime par une factorisation utile
$$A = PDP^{-1},$$
où $D$ est une [[Matrice diagonale|matrice diagonale]]. Elle sert à calculer les puissances : $A^n = PD^nP^{-1}$.

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Contradiction sur la forme échelonnée** : ta note dit que réduire une matrice sous forme échelonnée permet de « repérer direct les eigenvalues ». Or l'avertissement du même chapitre dit le contraire : la réduction par lignes ne sert pas à trouver les valeurs propres, car une forme échelonnée ne les montre généralement pas. Le théorème ne vaut que pour la matrice triangulaire de départ. Le wiki suit l'avertissement. **À corriger avant un examen.**
2. **« Any linear combination of basic eigenvectors is an eigenvector »** : ce n'est vrai que pour des vecteurs d'une même valeur propre, et si la combinaison n'est pas nulle. Le chapitre le dit lui-même : un vecteur propre est non nul, et l'espace propre contient en plus $\mathbf{0}$.
3. **Multiplicité** : « la valeur de la puissance de chaque λ » est imprécis. C'est l'exposant du facteur $(\lambda - \lambda_i)$ dans le polynôme (complément).
4. **Étape 6** : la variante « vérifier $AP = PD$ » est un complément, le cours dit seulement « vérifier que $A = PDP^{-1}$ ».
