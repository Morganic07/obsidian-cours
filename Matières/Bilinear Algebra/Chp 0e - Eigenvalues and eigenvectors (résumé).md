---
type: source
tags: [year2]
sources: ["[[Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-05
---

Résumé de [[Chp 0e - Eigenvalues and eigenvectors]], dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une matrice agit sur certains vecteurs par simple multiplication. Ces directions permettent de la diagonaliser, donc de calculer facilement ses puissances.

## Contenu, dans l'ordre du cours

- **[[Valeur propre]] et [[Vecteur propre]]** : $A\mathbf{x} = \lambda\mathbf{x}$ avec $\mathbf{x} \neq \mathbf{0}$. Une valeur propre peut être nulle, et 0 est valeur propre si et seulement si $A$ n'est pas inversible.
- **[[Espace propre]]** : Nul$(A - \lambda I)$, formé de $\mathbf{0}$ et des vecteurs propres associés à $\lambda$.
- **Propriétés** : les valeurs propres d'une matrice triangulaire sont sur sa diagonale. Des vecteurs propres de valeurs propres distinctes sont indépendants. $A^n\mathbf{x} = \lambda^n\mathbf{x}$, par récurrence.
- **Équation caractéristique** : $\det(A - \lambda I) = 0$, polynôme de degré $n$, avec des racines éventuellement complexes.
- **Théorème de la matrice inversible** : énoncés s et t, voir [[Invertible matrix theorem]].
- **[[Diagonalisation]]** : $A = PDP^{-1}$ si et seulement si les colonnes de $P$ sont $n$ vecteurs propres indépendants. Alors $A^n = PD^nP^{-1}$. Avoir $n$ valeurs propres distinctes suffit, sans être nécessaire.
- **Méthode en 6 étapes** : valeurs propres, vecteurs propres, $P$, $D$ dans le même ordre, $P^{-1}$, vérification.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Contradiction sur la forme échelonnée** : ta note dit que réduire une matrice sous forme échelonnée permet de « repérer direct les eigenvalues ». Or l'avertissement du même chapitre dit le contraire : la réduction par lignes ne sert pas à trouver les valeurs propres, car une forme échelonnée ne les montre généralement pas. Le théorème ne vaut que pour la matrice triangulaire de départ. Le wiki suit l'avertissement. **À corriger avant un examen.**
2. **« Any linear combination of basic eigenvectors is an eigenvector »** : ce n'est vrai que pour des vecteurs d'une même valeur propre, et si la combinaison n'est pas nulle. Le chapitre le dit lui-même : un vecteur propre est non nul, et l'espace propre contient en plus $\mathbf{0}$.
3. **Multiplicité** : « la valeur de la puissance de chaque λ » est imprécis. C'est l'exposant du facteur $(\lambda - \lambda_i)$ dans le polynôme (complément).
