---
type: concept
aliases: [PCA, principal component analysis, principal components analysis, composantes principales, composante principale, principal component, ACP, scree plot, biplot]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 13 - Principal Components Analysis]]", "[[Cours 13 - PCA in R]]"]
maj: 2026-11-05
---

Méthode qui compresse $d$ variables en quelques composantes qui gardent le maximum de variance, pour visualiser les données ou limiter le surapprentissage.

**Construction** : on centre les données, puis on cherche la droite par l'origine qui minimise les distances aux points, ce qui revient à maximiser la variance des projections ([[Moindres carrés]], [[Projection orthogonale]]). C'est PC1 ; PC2 est orthogonale à PC1, et ainsi de suite. Il faut mettre les variables à la même échelle, en divisant par l'écart-type.

**Algèbre** : les composantes sont les [[Vecteur propre|vecteurs propres]] de la matrice de covariance $\dfrac{X^TX}{n-1}$ (données centrées), qui est [[Matrice symétrique|symétrique]], donc de vecteurs orthogonaux. Chaque [[Valeur propre]] mesure la variance le long de sa composante, et la part de variance expliquée est la valeur propre divisée par la somme. Le **scree plot** trace ces parts. Via la [[Décomposition en valeurs singulières]] : $V$ contient les **loadings** (poids des variables), les **scores** sont les coordonnées des échantillons dans les nouveaux axes. Le **biplot** superpose loadings et scores.

**Lecture d'un cercle des corrélations** (cours) : angle fermé, corrélation positive ; angle droit, corrélation nulle ; angle ouvert, corrélation négative.

Résumés : [[Cours 13 - Principal Components Analysis (résumé)]], [[Cours 13 - PCA in R (résumé)]]
