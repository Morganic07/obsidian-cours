---
type: concept
tags:
  - year1
  - year2
  - year3
aliases:
  - eigenvalue
  - eigenvalues
  - valeurs propres
  - éléments propres
sources:
  - "[[Chp 0e - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[chp7 (résumé)|chp7 (Algèbre)]]"
  - "[[Séance 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]"
  - "[[Séance 13 - PCA in R (résumé)|Cours 13 - PCA in R]]"
maj: 2026-11-06
---

Scalaire $\lambda$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ a une solution non triviale ($\mathbf{x} \ne \mathbf{0}$), c'est-à-dire tel que $(A - \lambda I)\mathbf{x} = \mathbf{0}$ en a une. Les valeurs propres sont les solutions de l'[[Équation caractéristique|équation caractéristique]] $\det(A - \lambda I) = 0$, polynôme de degré $n$ dont les racines peuvent être complexes.

- Une valeur propre peut être nulle : 0 est valeur propre si et seulement si $A$ n'est pas inversible.
- Les valeurs propres d'une [[Matrice triangulaire|matrice triangulaire]] sont sur sa diagonale.
- Si $A\mathbf{x} = \lambda\mathbf{x}$, alors $A^n\mathbf{x} = \lambda^n\mathbf{x}$ (par récurrence).
- Trouver les valeurs propres à la main est difficile au-delà de la taille 3.

**En 1re année (endomorphismes)** : pour $f \in L(E)$ ([[Morphisme]]), $\lambda$ est valeur propre s'il existe $v$ non nul avec $f(v) = \lambda v$. Une valeur propre peut être nulle si $\mathrm{Ker} f \neq \{0\}$. $\lambda \in \mathrm{Sp}(f)$ ([[Spectre (algèbre linéaire)|spectre]]) $\iff E_\lambda \neq \{0\} \iff f - \lambda \mathrm{Id}$ non injective. Pour une matrice : $\lambda$ valeur propre de $A \iff \mathrm{Ker}(A - \lambda \mathrm{Id}) \neq \{0\}$ ([[Espace nul]]) $\iff \det(A - \lambda \mathrm{Id}) = 0$.

**En Data analysis (Thanos), ACP** : une valeur propre indique la variance dans la direction de son vecteur propre ; la somme des carrés des distances projetées sur PC1 est la valeur propre de PC1, et sa racine est la valeur singulière ([[Séance 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]). En R : `eigen(m)` ([[Séance 13 - PCA in R (résumé)|Cours 13 - PCA in R]]). Voir [[Analyse en composantes principales]] et [[Matrice de covariance]].

> [!warning] Écart dans le cours
> La réduction par lignes ne donne pas les valeurs propres : une forme échelonnée ne les montre généralement pas. Une note de [[Chp 0e - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]] dit le contraire, mais l'avertissement du même chapitre l'exclut.

Notion parente : [[Morphisme]]. Voir aussi : [[Vecteur propre]], [[Espace propre]], [[Spectre (algèbre linéaire)]], [[Équation caractéristique]], [[Matrice triangulaire]], [[Diagonalisation]], [[Déterminant]], [[Espace nul]], [[Matrice inversible]], [[Forme quadratique]], [[Analyse en composantes principales]], [[Matrice de covariance]]

## À vérifier

- [[chp7 (résumé)|chp7 (Algèbre)]] écrit « Ǝ un vecteur nul X tq A·X = λ·X » : il faut « non nul ».
- Même chapitre, coquilles : « non-injonctive », et « une valeur propre peut si Ker f ≠ {0} » (il manque « être nulle »).
- Dans [[Chp 0e - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]], une note personnelle dit que la forme échelonnée permet de « repérer direct les eigenvalues », ce que contredit l'avertissement du cours.
- Le cours d'ACP nomme « eigenvalue » deux grandeurs aux normalisations différentes.

Résumés : [[Chp 0e - Eigenvalues and eigenvectors (résumé)]], [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[chp7 (résumé)|chp7 (résumé)]], [[Séance 13 - Principal Components Analysis (résumé)]], [[Séance 13 - PCA in R (résumé)]]
