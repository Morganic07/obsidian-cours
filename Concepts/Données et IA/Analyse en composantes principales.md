---
type: concept
tags: [year3]
aliases: [PCA, principal component analysis, principal components analysis, composantes principales, composante principale, principal component, ACP, scree plot, biplot, Dim 1, PC1, PC2]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 13 - Principal Components Analysis]]", "[[Cours 13 - PCA in R]]"]
maj: 2026-11-06
---

Méthode qui compresse $d$ variables en quelques composantes qui gardent le maximum de variance, pour visualiser les données ou limiter le surapprentissage.

**Construction** : on centre les données, puis on cherche la droite par l'origine qui minimise les distances aux points, ce qui revient à maximiser la variance des projections ([[Moindres carrés]], [[Projection orthogonale]]). C'est PC1 ; PC2 est orthogonale à PC1, et ainsi de suite. Il faut mettre les variables à la même échelle, en divisant par l'écart-type.

**Algèbre** : les composantes sont les [[Vecteur propre|vecteurs propres]] de la matrice de covariance $\dfrac{X^TX}{n-1}$ (données centrées), qui est [[Matrice symétrique|symétrique]], donc de vecteurs orthogonaux. Chaque [[Valeur propre]] mesure la variance le long de sa composante, et la part de variance expliquée est la valeur propre divisée par la somme. Le **scree plot** trace ces parts. Via la [[Décomposition en valeurs singulières]] : $V$ contient les **loadings** (poids des variables), les **scores** sont les coordonnées des échantillons dans les nouveaux axes. Le **biplot** superpose loadings et scores.

**Lecture d'un cercle des corrélations** (cours) : angle fermé, corrélation positive ; angle droit, corrélation nulle ; angle ouvert, corrélation négative.

**Précisions du cours** : PC1 est la droite par l'origine qui maximise la somme des carrés des distances des projections à l'origine, et cette somme $SS$ est la valeur propre de PC1. Le but algébrique est une matrice orthogonale $P$ avec $X = PY$, où les variables $y$ ne sont pas corrélées et sont rangées par variance décroissante.

Voir aussi : [[Matrice de covariance]], [[Loadings et scores (ACP)]], [[Cercle des corrélations]], [[Centrage et réduction]], [[Réduction de dimension]].

## À vérifier

Deux conventions de « valeur propre » (de $X^TX$ ou de la covariance) ; nombre de composantes $\min(d, n-1)$ plutôt que min(variables, échantillons) ; c'est le vecteur propre et non la valeur propre qui donne la composante.

Résumés : [[Séance 13 - Principal Components Analysis (résumé)]], [[Séance 13 - PCA in R (résumé)]]
