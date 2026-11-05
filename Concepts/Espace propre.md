---
type: concept
aliases: [eigenspace, eigenspaces, espaces propres]
sources: ["[[Chp 0e - Eigenvalues and eigenvectors]]", "[[Chp2 - Symmetric matrices and quadratic forms]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp7|chp7 (Algèbre)]]"]
maj: 2026-11-05
---

L'espace propre de $A$ associé à $\lambda$ est l'ensemble des solutions de $(A - \lambda I)\mathbf{x} = \mathbf{0}$, soit Nul$(A - \lambda I)$. C'est un sous-espace de $\mathbb{R}^n$, formé du vecteur nul et de tous les vecteurs propres associés à $\lambda$.

- Sa dimension est inférieure ou égale à la multiplicité de $\lambda$.
- $A$ est diagonalisable si et seulement si la somme des dimensions des espaces propres vaut $n$.
- Pour une matrice symétrique, chaque dimension égale la multiplicité, et les espaces propres sont orthogonaux entre eux.
- Pour un endomorphisme $f$, on note $E_\lambda = \text{Ker}(f - \lambda \text{Id})$. Les espaces propres de valeurs propres distinctes sont en [[Somme directe]].

Liens : [[Valeur propre]], [[Vecteur propre]], [[Espace nul]], [[Diagonalisation]], [[Matrice symétrique]], [[Somme directe]]

Résumés : [[Chp 0e - Eigenvalues and eigenvectors (résumé)]], [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp7 (résumé)|chp7 (résumé)]]
