---
type: concept
tags: [year3]
aliases: [covariance matrix, matrices de covariance, matrice de variance-covariance, variance totale]
sources: ["[[Cours 13 - Principal Components Analysis]]", "[[Cours 13 - PCA in R]]"]
maj: 2026-11-06
---

Matrice dont la diagonale porte les variances et dont les autres coefficients sont les covariances. Pour des données centrées $X$, échantillons en lignes : $\Sigma = \dfrac{X^TX}{n}$ pour une population, $\dfrac{X^TX}{n-1}$ pour un échantillon. La variance totale est sa [[Trace d'une matrice|trace]]. Elle est [[Matrice symétrique|symétrique]], donc ses vecteurs propres sont orthogonaux ([[Cours 13 - Principal Components Analysis]]).

En R : `cov()`, puis `matrix()` ([[Cours 13 - PCA in R]]).

Notion parente : [[Covariance et corrélation]]. Voir aussi : [[Analyse en composantes principales]], [[Matrice symétrique]], [[Trace d'une matrice]], [[Valeur propre]].

Résumés : [[Cours 13 - Principal Components Analysis (résumé)]], [[Cours 13 - PCA in R (résumé)]]
