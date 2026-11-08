---
type: concept
tags:
  - year1
  - year2
aliases:
  - characteristic equation
  - polynôme caractéristique
  - characteristic polynomial
sources:
  - "[[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]]"
  - "[[Raw/Year 2/Bilinear Algebra/Chp 0e - Eigenvalues and eigenvectors.docx|Chp 0e - Eigenvalues and eigenvectors]]"
maj: 2026-11-08
---

$$\det(A-\lambda I)=0$$

C'est une équation polynomiale de degré $n$ en $\lambda$, dont les racines (éventuellement complexes) sont les valeurs propres de $A$.

Le cours de 1re année énonce le même critère : $\lambda$ est valeur propre de $A$ si et seulement si $\det(A - \lambda\,\text{Id}) = 0$ ([[7 - Algèbre linéaire]]).

## Polynôme caractéristique (complément, hors du cours)

- **Notation** : $\chi_A(\lambda) = \det(A - \lambda I_n)$, un [[Polynôme|polynôme]] de degré $n$ (de coefficient dominant $(-1)^n$). Ses racines sont exactement les valeurs propres de $A$ : il y en a donc **au plus $n$**.
- **Taille 2** : pour $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$,
$$\chi_A(\lambda) = (a - \lambda)(d - \lambda) - bc = \lambda^2 - \text{tr}(A)\,\lambda + \det A.$$
- **Somme et produit des racines** : en comptant les racines complexes avec leur [[Multiplicité d'une valeur propre|multiplicité]], leur somme vaut $\text{tr}(A)$ ([[Trace d'une matrice]]) et leur produit vaut $\det A$.
- **Matrice triangulaire** : $\chi_A(\lambda) = \prod_{i=1}^{n}(a_{ii} - \lambda)$, donc les valeurs propres d'une [[Matrice triangulaire|matrice triangulaire]] sont ses coefficients diagonaux.
- **Invariance** : deux [[Matrices semblables|matrices semblables]] ($A' = P^{-1}AP$) ont le même polynôme caractéristique, car $\det(P^{-1}(A - \lambda I_n)P) = \det(A - \lambda I_n)$. Les valeurs propres d'un endomorphisme ne dépendent donc pas de la base ([[Changement de base]]).
- **Pas toujours de racine réelle** : la rotation d'angle $\frac{\pi}{2}$, de matrice $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, donne $\chi(\lambda) = \lambda^2 + 1$, de racines $\pm i$ : aucune valeur propre réelle.
- **Cayley-Hamilton** : toute matrice annule son polynôme caractéristique, $\chi_A(A) = 0$ ([[Théorème de Cayley-Hamilton]]).

**Exemple** : $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$, $\text{tr}(A) = 7$, $\det A = 12 - 2 = 10$, donc
$$\chi_A(\lambda) = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2),$$
et les valeurs propres sont $5$ et $2$ (on vérifie $5 + 2 = 7$ et $5 \times 2 = 10$).

Notion parente : [[Valeur propre]]. Voir aussi : [[Déterminant]], [[Multiplicité d'une valeur propre]], [[Trace d'une matrice]], [[Théorème de Cayley-Hamilton]], [[Matrices semblables]], [[Diagonalisation]].

Résumés : [[0 - Eigenvalues and eigenvectors]], [[7 - Algèbre linéaire]]
