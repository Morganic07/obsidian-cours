---
type: concept
tags:
  - year2
aliases:
  - diagonalizable
  - diagonalization
  - orthogonally diagonalizable
  - diagonalisable
  - étapes pour diagonaliser
sources:
  - "[[0 - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[2 - Symmetric matrices and quadratic forms (résumé)|Chp2 - Symmetric matrices and quadratic forms]]"
maj: 2026-11-06
---

$A$ est diagonalisable si $A = PDP^{-1}$ avec $D$ [[Matrice diagonale|diagonale]]. Cette écriture sert notamment à calculer $A^n = PD^nP^{-1}$.

- **Théorème** : $A$ est diagonalisable si et seulement si elle a $n$ vecteurs propres indépendants, qui forment alors les colonnes de $P$ et une base de vecteurs propres de $\mathbb{R}^n$. La diagonale de $D$ porte les valeurs propres correspondantes, dans le même ordre.
- **Condition suffisante** : $n$ valeurs propres distinctes suffisent, mais ne sont pas nécessaires.
- **Condition générale** : la somme des dimensions des [[Espace propre|espaces propres]] vaut $n$. Autrement dit, le polynôme caractéristique se factorise entièrement, et chaque espace propre a pour dimension la [[Multiplicité d'une valeur propre|multiplicité]] de sa valeur propre.
- **Orthogonalement diagonalisable** : $A = PDP^T$ avec $P$ orthogonale, ce qui équivaut à $A$ symétrique ([[Théorème spectral]]).

Méthode en six étapes : trouver les valeurs propres, puis les vecteurs propres, vérifier qu'il y en a $n$ indépendants, construire $P$ puis $D$ dans le même ordre, calculer $P^{-1}$ par $[P \mid I] \sim [I \mid P^{-1}]$, et vérifier.

Notion parente : [[Valeur propre]]. Voir aussi : [[Vecteur propre]], [[Espace propre]], [[Matrice diagonale]], [[Multiplicité d'une valeur propre]], [[Théorème spectral]], [[Matrice symétrique]], [[Décomposition en valeurs singulières]]

Résumés : [[0 - Eigenvalues and eigenvectors (résumé)]], [[2 - Symmetric matrices and quadratic forms (résumé)]]
