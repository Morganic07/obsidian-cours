---
type: concept
aliases: [eigenvalue, eigenvalues, valeurs propres]
sources: ["[[Chp 0e - Eigenvalues and eigenvectors]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp7|chp7 (Algèbre)]]"]
maj: 2026-11-05
---

Scalaire $\lambda$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ a une solution non triviale, c'est-à-dire tel que $(A - \lambda I)\mathbf{x} = \mathbf{0}$ en a une. Les valeurs propres sont les solutions de l'équation caractéristique $\det(A - \lambda I) = 0$, polynôme de degré $n$ dont les racines peuvent être complexes.

- Une valeur propre peut être nulle : 0 est valeur propre si et seulement si $A$ n'est pas inversible.
- Les valeurs propres d'une matrice triangulaire sont sur sa diagonale.
- Trouver les valeurs propres à la main est difficile au-delà de la taille 3.
- Pour un endomorphisme $f$, $\lambda$ est valeur propre si et seulement si Ker$(f - \lambda \text{Id}) \neq \{0\}$, c'est-à-dire si $f - \lambda \text{Id}$ n'est pas injective. Leur ensemble est le spectre Sp$(f)$.

> [!warning] Écart dans le cours
> La réduction par lignes ne donne pas les valeurs propres : une forme échelonnée ne les montre généralement pas. Une note de [[Chp 0e - Eigenvalues and eigenvectors]] dit le contraire, mais l'avertissement du même chapitre l'exclut.

Liens : [[Vecteur propre]], [[Espace propre]], [[Diagonalisation]], [[Déterminant]], [[Matrice inversible]], [[Forme quadratique]]

Résumés : [[Chp 0e - Eigenvalues and eigenvectors (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp7 (résumé)|chp7 (résumé)]]
