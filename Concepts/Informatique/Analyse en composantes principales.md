---
type: concept
tags: [year3]
aliases: [PCA, principal component analysis, principal components analysis, composantes principales, composante principale, principal component, ACP, scree plot, biplot, Dim 1, PC1, PC2, éboulis des valeurs propres, critère de Kaiser, ACP normée]
matieres: [Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]", "[[13 - PCA in R|Cours 13 - PCA in R]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 13 : Principal Components Analysis.docx|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Méthode qui compresse $d$ variables en quelques composantes qui gardent le maximum de variance, pour visualiser les données ou limiter le surapprentissage.

**Construction** : on centre les données, puis on cherche la droite par l'origine qui minimise les distances aux points, ce qui revient à maximiser la variance des projections ([[Moindres carrés]], [[Projection orthogonale]]). C'est PC1 ; PC2 est orthogonale à PC1, et ainsi de suite. Il faut mettre les variables à la même échelle, en divisant par l'écart-type.

**Algèbre** : les composantes sont les [[Vecteur propre|vecteurs propres]] de la matrice de covariance $\dfrac{X^TX}{n-1}$ (données centrées), qui est [[Matrice symétrique|symétrique]], donc de vecteurs orthogonaux. Chaque [[Valeur propre]] mesure la variance le long de sa composante, et la part de variance expliquée est la valeur propre divisée par la somme. Le **scree plot** trace ces parts. Via la [[Décomposition en valeurs singulières]] : $V$ contient les **loadings** (poids des variables), les **scores** sont les coordonnées des échantillons dans les nouveaux axes. Le **biplot** superpose loadings et scores.

**Lecture d'un cercle des corrélations** (cours) : angle fermé, corrélation positive ; angle droit, corrélation nulle ; angle ouvert, corrélation négative.

**Précisions du cours** : PC1 est la droite par l'origine qui maximise la somme des carrés des distances des projections à l'origine, et cette somme $SS$ est la valeur propre de PC1. Cette « valeur propre » est celle de $X^TX$ ; celle de la matrice de covariance $\dfrac{X^TX}{n-1}$, qui mesure la variance, vaut $\dfrac{SS}{n-1}$ (le cours emploie les deux conventions ; les parts de variance expliquée sont les mêmes). Le but algébrique est une matrice orthogonale $P$ avec $X = PY$, où les variables $y$ ne sont pas corrélées et sont rangées par variance décroissante.

La première composante principale est le vecteur propre associé à la plus grande valeur propre (`e$vectors[,1]` en R). [[Erreurs du cours#^e-analyse-en-composantes-principales|✎]] Le nombre de composantes utiles est le plus petit entre le nombre de variables $d$ et le nombre d'échantillons moins un, $\min(d, n-1)$ : une fois les données centrées, $n$ échantillons n'engendrent qu'un espace de dimension $n-1$ au plus. [[Erreurs du cours#^e-analyse-en-composantes-principales|✎]]

## Compléments (hors du cours)

**Pourquoi les vecteurs propres** : pour un vecteur unitaire $v$ ($v^Tv = 1$), la variance des données centrées projetées sur $v$ vaut $v^T \Sigma v$, où $\Sigma$ est la [[Matrice de covariance|matrice de covariance]]. Maximiser $v^T\Sigma v$ sous la contrainte $\|v\| = 1$ (multiplicateur de Lagrange) donne $\Sigma v = \lambda v$ : l'optimum est le premier [[Vecteur propre|vecteur propre]], et la variance maximale vaut $\lambda_1$, la plus grande [[Valeur propre|valeur propre]]. La somme des valeurs propres est la [[Trace d'une matrice|trace]] de $\Sigma$, c'est-à-dire la variance totale. Le signe d'un vecteur propre est arbitraire ($v$ et $-v$ conviennent) : deux logiciels peuvent donner des axes de sens opposés sans que l'analyse change.

**ACP normée** : on centre et réduit chaque variable, $z = \dfrac{x - \bar{x}}{s}$ ([[Centrage et réduction]]). La matrice de covariance des données réduites est alors la matrice de corrélation, et la variance totale vaut $d$, le nombre de variables (chaque variable réduite a une variance 1). C'est l'ACP par défaut quand les variables n'ont pas la même unité.

**Choisir le nombre de composantes** :
- **coude** du scree plot (éboulis des valeurs propres) : on garde les composantes avant la cassure où la courbe s'aplatit ;
- **part de variance cumulée** : on garde assez de composantes pour atteindre un seuil, souvent entre 70 et 90 % ;
- **critère de Kaiser** (ACP normée) : on garde les valeurs propres supérieures à 1, c'est-à-dire les composantes qui résument plus qu'une variable d'origine.

**ACP et régression** : PC1 minimise les distances **perpendiculaires** des points à la droite, et traite les variables à égalité ; la [[Régression linéaire|régression]] minimise les écarts **verticaux** et explique une variable par l'autre. Les deux droites passent par le centre du nuage mais n'ont en général pas la même pente.

**Limites** : l'ACP ne capte que les relations linéaires ; elle est sensible aux valeurs aberrantes ([[Quartiles et valeurs aberrantes]]), qui pèsent lourd dans la variance ; les composantes, combinaisons de toutes les variables, sont parfois difficiles à interpréter ; une forte variance ne garantit pas un pouvoir prédictif (une composante de faible variance peut être la plus utile pour prédire une cible). Pour des variables qualitatives, on utilise l'analyse factorielle des correspondances (AFC, deux variables) ou l'analyse des correspondances multiples (ACM, plusieurs).

**Histoire** : Karl Pearson (1901) cherchait la droite et le plan les plus proches d'un nuage de points ; Harold Hotelling (1933) lui a donné son nom et sa formulation par les vecteurs propres.

Voir aussi : [[Matrice de covariance]], [[Loadings et scores (ACP)]], [[Cercle des corrélations]], [[Centrage et réduction]], [[Réduction de dimension]].

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]]
