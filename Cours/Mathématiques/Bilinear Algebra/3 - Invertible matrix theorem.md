---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Invertible matrix theorem .docx|Invertible matrix theorem]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Invertible matrix theorem .docx|Invertible matrix theorem]], dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

Cette note rassemble les 20 énoncés (a à t) du théorème, tous équivalents pour une matrice carrée : ils sont tous vrais, ou tous faux. Ils sont classés par thème dans [[Matrice inversible]] (voir aussi [[Théorème de la matrice inversible]]).

Les énoncés a à l viennent de [[0 - Matrix algebra|Chp 0b - Matrix algebra]], m à r de [[0 - Vector Space|Chp 0d - Vector Space]], s et t de [[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]].

## Le théorème de la matrice inversible (*The Invertible Matrix Theorem*)

Soit $A$ une matrice carrée $n \times n$. Les énoncés suivants sont équivalents : pour une matrice $A$ donnée, ils sont tous vrais ou tous faux.

Rappel : $A$ est **inversible** s'il existe $A^{-1}$ telle que $AA^{-1} = A^{-1}A = I_n$ ; une matrice non inversible est dite **singulière**. Les matrices inversibles $n \times n$ forment le [[Groupe linéaire|groupe linéaire]] $GL_n(\mathbb R)$. [[Complément hors du cours|ⓘ]]

Le théorème ne vaut que pour les matrices **carrées**. Pour une matrice $m \times n$ avec $m \neq n$, les énoncés se séparent : la matrice $2 \times 3$ $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ a des colonnes qui engendrent $\mathbb R^2$ (g, h, i vrais) mais liées (d, e, f faux). [[Complément hors du cours|ⓘ]]

### Énoncés a à l (réduction, systèmes, transformation)

- a. $A$ est inversible.
- b. $A$ est [[Opérations élémentaires sur les lignes|équivalente par lignes]] à la matrice identité $I_n$.
- c. $A$ a $n$ positions pivots.
- d. L'équation $A\mathbf x = \mathbf 0$ n'a que la [[Système linéaire homogène|solution triviale]].
- e. Les colonnes de $A$ forment une famille [[Indépendance linéaire|linéairement indépendante]].
- f. La [[Transformation linéaire|transformation linéaire]] $\mathbf x \mapsto A\mathbf x$ est [[Injectivité et surjectivité|injective]] (*one-to-one*).
- g. L'équation $A\mathbf x = \mathbf b$ a au moins une solution pour tout $\mathbf b \in \mathbb R^n$.
- h. Les colonnes de $A$ [[Espace engendré|engendrent]] $\mathbb R^n$.
- i. La transformation $\mathbf x \mapsto A\mathbf x$ envoie $\mathbb R^n$ **sur** $\mathbb R^n$ (surjective, *onto*).
- j. Il existe une matrice $C$ ($n \times n$) telle que $CA = I$.
- k. Il existe une matrice $D$ ($n \times n$) telle que $AD = I$.
- l. $A^T$ est inversible.

Le cœur du théorème est l'équivalence entre **injectivité** (d, e, f) et **surjectivité** (g, h, i), propre aux matrices carrées : $A$ a $n$ pivots (c) si et seulement si chaque colonne contient un pivot (pas de variable libre, donc solution triviale seule) si et seulement si chaque ligne en contient un (pas de ligne $[0 \cdots 0 \mid b]$ impossible, donc une solution pour tout $\mathbf b$). [[Complément hors du cours|ⓘ]]

Pour j et k : avec une matrice carrée, un inverse d'un seul côté suffit. Si $CA = I$ et $AD = I$, alors $C = C(AD) = (CA)D = D = A^{-1}$. Par l, tout ce qui est dit des colonnes vaut aussi pour les **lignes** : lignes linéairement indépendantes, lignes qui engendrent $\mathbb R^n$. Quand $A$ est inversible, l'unique solution de $A\mathbf x = \mathbf b$ est $\mathbf x = A^{-1}\mathbf b$. [[Complément hors du cours|ⓘ]]

**Calculer l'inverse.** On réduit la matrice augmentée $[A \mid I]$ ([[Matrice augmentée]]) : si $A$ est équivalente par lignes à $I$ (énoncé b), on obtient $[I \mid A^{-1}]$ (méthode de Gauss-Jordan) ; sinon, $A$ n'est pas inversible. En taille 2 : $\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \dfrac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ si $ad - bc \neq 0$. En général, $A^{-1} = \dfrac{1}{\det A}\,{}^t\text{com}(A)$ ([[Comatrice]]), formule surtout théorique. [[Complément hors du cours|ⓘ]]

**Propriétés** : si $A$ et $B$ sont inversibles, $(AB)^{-1} = B^{-1}A^{-1}$ (ordre inversé), $(A^T)^{-1} = (A^{-1})^T$, $(A^{-1})^{-1} = A$ ; pour des matrices carrées, $AB$ est inversible si et seulement si $A$ et $B$ le sont. Équivalent de b : $A$ est un produit de matrices élémentaires (celles des [[Opérations élémentaires sur les lignes|opérations élémentaires]]). [[Complément hors du cours|ⓘ]]

### Énoncés m à r (base, sous-espaces, rang)

Chacun équivaut à « $A$ est inversible » :
- m. Les colonnes de $A$ forment une [[Base (algèbre linéaire)|base]] de $\mathbb R^n$.
- n. $\text{Col}\,A = \mathbb R^n$ ([[Espace des colonnes]]).
- o. $\dim \text{Col}\,A = n$.
- p. $\text{rank}\,A = n$ ([[Rang d'une matrice]]).
- q. $\text{Nul}\,A = \{\mathbf 0\}$ ([[Espace nul]]).
- r. $\dim \text{Nul}\,A = 0$.

Ces énoncés sont reliés par le [[Théorème du rang|théorème du rang]] : $\text{rank}\,A + \dim \text{Nul}\,A = n$. Dire $\text{rank}\,A = n$ (p, surjectivité) revient donc à dire $\dim \text{Nul}\,A = 0$ (r, injectivité). [[Complément hors du cours|ⓘ]]

### Énoncés s et t (valeurs propres, déterminant)

$A$ est inversible si et seulement si :
- s. le nombre $0$ n'est **pas** une [[Valeur propre|valeur propre]] de $A$ ;
- t. le [[Déterminant|déterminant]] de $A$ n'est **pas** nul.

Lien entre s et t : $0$ est valeur propre si et seulement si $\det(A - 0I) = \det A = 0$, et $\det A$ est le produit des valeurs propres (comptées avec multiplicité, complexes comprises). Quand $A$ est inversible, $\det(A^{-1}) = \dfrac{1}{\det A}$, et les valeurs propres de $A^{-1}$ sont les $1/\lambda$. [[Complément hors du cours|ⓘ]]

Énoncé de plus, vu avec la SVD dans [[2 - Symmetric matrices and quadratic forms]] : $A$ est inversible si et seulement si sa plus petite valeur singulière $\sigma_n$ est non nulle. En calcul numérique, c'est le [[Conditionnement d'une matrice|conditionnement]] $\sigma_1/\sigma_n$, et non la petitesse de $\det A$, qui dit si $A$ est « presque singulière » : $\det(0{,}1\,I_{10}) = 10^{-10}$ alors que cette matrice est parfaitement conditionnée. [[Complément hors du cours|ⓘ]]

Exemple d'une matrice **non** inversible, où tous les énoncés échouent ensemble : $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$. La deuxième colonne vaut deux fois la première (e faux), $\det A = 4 - 4 = 0$ (t faux), $A\begin{bmatrix} 2 \\ -1 \end{bmatrix} = \mathbf 0$ donc $\text{Nul}\,A \neq \{\mathbf 0\}$ et $0$ est valeur propre (q, s faux), $\text{rank}\,A = 1$ (p faux), et $A\mathbf x = \mathbf b$ n'a de solution que si $\mathbf b$ est multiple de $(1, 2)$ (g faux). [[Complément hors du cours|ⓘ]]
