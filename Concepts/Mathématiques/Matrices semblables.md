---
type: concept
tags: [year1, year2]
aliases: [matrice semblable, similar matrices, similar matrix, matrices similaires, similitude de matrices]
sources: ["[[Raw/Year 1/Algèbre Linéaire/Cours /chp5 .docx|chp5 (Algèbre)]]", "[[Raw/Year 2/Bilinear Algebra/Chp 0e - Eigenvalues and eigenvectors.docx|Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : deux matrices carrées $A$ et $A'$ de $\mathcal{M}_n(K)$ sont **semblables** s'il existe une matrice inversible $P \in \mathcal{M}_n(K)$ telle que
$$A' = P^{-1} A P.$$
La relation est symétrique : on peut aussi écrire $A = P A' P^{-1}$, forme employée en Bilinear Algebra ($A = PBP^{-1}$).

**Interprétation.** Deux matrices semblables représentent le même endomorphisme $f$ de $E$ dans deux bases $\mathcal{B}$ et $\mathcal{B}'$, $P$ étant la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$ : c'est la formule de [[Changement de base]] $A' = P^{-1}AP$.

**Invariants.** Deux matrices semblables ont :
- le même déterminant : $\det A' = \det(P^{-1}) \det A \det P = \det A$ ;
- la même trace, puisque $\operatorname{tr}(P^{-1}AP) = \operatorname{tr}(APP^{-1}) = \operatorname{tr} A$ ;
- le même rang ;
- le même polynôme caractéristique, $\det(A' - \lambda I) = \det(P^{-1}(A - \lambda I)P) = \det(A - \lambda I)$, donc les mêmes valeurs propres avec les mêmes multiplicités.

Les vecteurs propres, eux, changent : si $A\mathbf{v} = \lambda\mathbf{v}$, alors $A'(P^{-1}\mathbf{v}) = \lambda P^{-1}\mathbf{v}$.

**La réciproque est fausse.** Avoir la même trace, le même déterminant, et même le même polynôme caractéristique ne suffit pas : $I_2$ et $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ ont toutes deux trace $2$, déterminant $1$ et polynôme caractéristique $(\lambda - 1)^2$, mais ne sont pas semblables, car la seule matrice semblable à $I_2$ est $I_2$ elle-même ($P^{-1} I_2 P = I_2$).

**Lien avec la diagonalisation.** Une matrice est diagonalisable si et seulement si elle est semblable à une [[Matrice diagonale|matrice diagonale]] : diagonaliser $A$, c'est trouver $P$ inversible et $D$ diagonale telles que $A = PDP^{-1}$ (voir [[Diagonalisation]]).

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[5 - Algèbre linéaire]], à propos de la formule de changement de base, et de [[0 - Eigenvalues and eigenvectors]], à propos de la diagonalisation.

Voir aussi : [[Diagonalisation]], [[Changement de base]], [[Valeur propre]], [[Trace d'une matrice]], [[Déterminant]], [[Rang d'une matrice]], [[Matrice inversible]], [[Matrice d'une application linéaire]]

Résumés : [[5 - Algèbre linéaire]], [[0 - Eigenvalues and eigenvectors]], [[0 - Determinants]]
