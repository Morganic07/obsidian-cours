---
type: concept
tags: [year3]
aliases: [PCA, principal component analysis, principal components analysis, composantes principales, composante principale, principal component, ACP, scree plot, biplot, Dim 1, PC1, PC2]
matieres: [Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]", "[[13 - PCA in R|Cours 13 - PCA in R]]"]
maj: 2026-11-07
---

Méthode qui compresse $d$ variables en quelques composantes qui gardent le maximum de variance, pour visualiser les données ou limiter le surapprentissage.

**Construction** : on centre les données, puis on cherche la droite par l'origine qui minimise les distances aux points, ce qui revient à maximiser la variance des projections ([[Moindres carrés]], [[Projection orthogonale]]). C'est PC1 ; PC2 est orthogonale à PC1, et ainsi de suite. Il faut mettre les variables à la même échelle, en divisant par l'écart-type.

**Algèbre** : les composantes sont les [[Vecteur propre|vecteurs propres]] de la matrice de covariance $\dfrac{X^TX}{n-1}$ (données centrées), qui est [[Matrice symétrique|symétrique]], donc de vecteurs orthogonaux. Chaque [[Valeur propre]] mesure la variance le long de sa composante, et la part de variance expliquée est la valeur propre divisée par la somme. Le **scree plot** trace ces parts. Via la [[Décomposition en valeurs singulières]] : $V$ contient les **loadings** (poids des variables), les **scores** sont les coordonnées des échantillons dans les nouveaux axes. Le **biplot** superpose loadings et scores.

**Lecture d'un cercle des corrélations** (cours) : angle fermé, corrélation positive ; angle droit, corrélation nulle ; angle ouvert, corrélation négative.

**Précisions du cours** : PC1 est la droite par l'origine qui maximise la somme des carrés des distances des projections à l'origine, et cette somme $SS$ est la valeur propre de PC1. Cette « valeur propre » est celle de $X^TX$ ; celle de la matrice de covariance $\dfrac{X^TX}{n-1}$, qui mesure la variance, vaut $\dfrac{SS}{n-1}$ (le cours emploie les deux conventions ; les parts de variance expliquée sont les mêmes). Le but algébrique est une matrice orthogonale $P$ avec $X = PY$, où les variables $y$ ne sont pas corrélées et sont rangées par variance décroissante.

Voir aussi : [[Matrice de covariance]], [[Loadings et scores (ACP)]], [[Cercle des corrélations]], [[Centrage et réduction]], [[Réduction de dimension]].

## Erreurs du cours

- [[Raw/Year 3/Data analysis (Thanos)/Cours 13 : Principal Components Analysis.docx|Cours 13 - Principal Components Analysis]] donne comme nombre de composantes « either the # of variables or the # of samples (whichever is smaller) » ; il faut $\min(d, n-1)$ : une fois les données centrées, $n$ échantillons n'engendrent qu'un espace de dimension $n-1$ au plus.
- [[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]] écrit « The largest eigenvalue is the first principal component » ; il faut « le vecteur propre associé à la plus grande valeur propre est la première composante principale » (la phrase suivante du cours utilise d'ailleurs `e$vectors[,1]`).

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]]
