---
type: concept
tags:
  - year2
  - year3
aliases:
  - linear regression
  - simple linear regression
  - multiple linear regression
  - régressions linéaires
  - least square line
  - least-squares line
  - least squares line
  - line of regression
  - droite de régression
  - droite des moindres carrés
  - design matrix
  - matrice de plan
  - parameter vector
  - observation vector
  - linear model
  - linear models
  - régression linéaire multiple
  - modèle linéaire simple
  - ordonnée à l'origine
sources:
  - "[[1 - Orthogonality|chp 1 - Orthogonality]]"
  - "[[10 - linear regression|Cours 10 - linear regression]]"
  - "[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]"
  - "[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
maj: 2026-11-08
---

Trouver la droite $y = \beta_0 + \beta_1x$ la plus proche de points $(x_j, y_j)$, c'est-à-dire celle qui minimise la somme des carrés des [[Résidu (régression)|résidus]] (les écarts verticaux entre les points et la droite). $\beta_0$ (l'ordonnée à l'origine) et $\beta_1$ (la pente) sont les coefficients de régression à déterminer. [[Erreurs du cours#^e-regression-lineaire|✎]]

En algèbre linéaire, le problème s'écrit $X\boldsymbol{\beta} = \mathbf{y}$ au lieu de $A\mathbf{x} = \mathbf{b}$, avec $X$ la design matrix (matrice de plan), $\boldsymbol{\beta}$ le parameter vector (vecteur des paramètres) et $\mathbf{y}$ l'observation vector (vecteur des observations). C'est un problème de [[Moindres carrés]] avec d'autres notations.

**En statistique** (Data analysis (Thanos)) : le modèle simple $y = \beta_0 + \beta_1x + \varepsilon$ est estimé par les moindres carrés, $\hat\beta_1 = SS_{xy}/SS_{xx}$ et $\hat\beta_0 = \bar y - \hat\beta_1 \bar x$. Il suppose une erreur de moyenne nulle, de variance constante, normale et indépendante, ce qui se vérifie sur les résidus. Le [[Test de la pente]] porte sur $H_0 : \beta_1 = 0$, avec $n - 2$ degrés de liberté. $R^2$ ([[Coefficient de détermination]]) est la part de variation expliquée, avec $SST = SSR + SSE$.

**Régression multiple** : $y = \beta_0 + \beta_1X_1 + \dots + \beta_kX_k + \varepsilon$, où $\beta_j$ est l'effet moyen de $X_j$ toutes les autres variables fixées, avec $n-(k+1)$ degrés de liberté ([[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]). [[3 - Paradoxe de Simpson|Le cours 3]] note que la régression multivariée « ajuste » les résultats en tenant compte des variables cachées.

[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]] présente la régression simple comme un cas particulier d'[[ANOVA]], à partir de $y_i - \bar{y} = (y_i - \hat{y}_i) + (\hat{y}_i - \bar{y})$.

L'aide-mémoire de Statistics ([[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]) écrit la droite $\hat{Y} = a + bX$ avec $b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2}$ et $a = \bar Y - b\bar X$.

## Compléments

- **Équations normales** de la régression simple, obtenues en annulant les dérivées partielles de $SSE$ par rapport à $\beta_0$ et $\beta_1$ : $\sum y = n\hat\beta_0 + \hat\beta_1 \sum x$ et $\sum xy = \hat\beta_0 \sum x + \hat\beta_1 \sum x^2$. La première, divisée par $n$, donne $\bar y = \hat\beta_0 + \hat\beta_1 \bar x$ : la droite des moindres carrés passe toujours par le point moyen $(\bar x, \bar y)$, et la somme des résidus est nulle. [[Complément hors du cours|ⓘ]]
- **Formes équivalentes de la pente** : $\hat\beta_1 = \dfrac{SS_{xy}}{SS_{xx}} = \dfrac{\sum (x - \bar x)(y - \bar y)}{\sum (x - \bar x)^2} = r\,\dfrac{s_y}{s_x}$, où $r$ est le coefficient de corrélation ([[Covariance et corrélation]]) : la pente a toujours le signe de la corrélation, et elle est nulle exactement quand $r = 0$. La formule de l'aide-mémoire de Statistics en est la version développée. [[Complément hors du cours|ⓘ]]
- **Estimation de $\sigma^2$** : $s^2 = \dfrac{SSE}{n-2}$ estime $\sigma^2$ sans biais ; on divise par $n - 2$ car deux paramètres ($\beta_0$, $\beta_1$) ont été estimés. En régression multiple à $p$ paramètres (constante comprise), $s^2 = \dfrac{RSS}{n-p}$. Voir [[Erreur standard de la régression]]. Exemple des jouets : $s^2 = 1{,}1/3$, $s \approx 0{,}6055$. [[Complément hors du cours|ⓘ]]
- **Extrapolation** : interpréter $\hat\beta_0$ quand $x = 0$ est hors de la plage observée, ou prédire en dehors de cette plage, est risqué : rien ne garantit que la relation reste linéaire au-delà des données. [[Complément hors du cours|ⓘ]]
- **« Toutes choses égales par ailleurs »** : en régression multiple, $\beta_j$ mesure l'effet de $X_j$ à autres variables fixées. Il peut donc différer nettement, voire changer de signe, par rapport à la pente de la régression simple de $y$ sur $X_j$ seule, quand $X_j$ est corrélée à une autre variable explicative (voir [[Paradoxe de Simpson]]). Si les variables explicatives sont trop corrélées entre elles, les coefficients deviennent instables ([[Multicolinéarité]]). [[Complément hors du cours|ⓘ]]
- **Linéaire en les paramètres** : le modèle reste « linéaire » avec des termes $X^2$, $\ln X$ ou des [[Variable indicatrice|variables indicatrices]], car il est linéaire en les $\beta_j$, pas forcément en $x$. [[Complément hors du cours|ⓘ]]
- **Hypothèses et ce qu'elles donnent** : les $\varepsilon_i$ indépendantes de même loi $N(0, \sigma^2)$, plus la linéarité de $E(y)$ en $x$. Moyenne nulle, variance constante ([[Homoscédasticité]]) et non-corrélation suffisent pour que les moindres carrés soient sans biais et de variance minimale parmi les estimateurs linéaires sans biais ([[Théorème de Gauss-Markov]]) ; la normalité ne sert qu'aux tests $t$ et $F$ et aux intervalles. [[Complément hors du cours|ⓘ]]
- **En R** : `m <- lm(y ~ x)` (ou `lm(y ~ x1 + x2)`), `summary(m)` pour les coefficients, erreurs standard, tests $t$, $R^2$ et test F global, `confint(m)` pour les intervalles de confiance des coefficients, `predict(m, newdata, interval = "prediction")` pour une prédiction, `plot(m)` pour les diagnostics des résidus. [[Complément hors du cours|ⓘ]]

Notion parente : [[Moindres carrés]]. Voir aussi : [[Projection orthogonale]], [[Statistique F]], [[Intervalle de prédiction]], [[Résidu (régression)]], [[Test de la pente]], [[Coefficient de détermination]], [[ANOVA]], [[Théorème de Gauss-Markov]], [[Multicolinéarité]], [[Paradoxe de Simpson]], [[Erreur standard de la régression]], [[Homoscédasticité]]

Résumés : [[1 - Orthogonality]], [[10 - linear regression]], [[11 - Multiple Linear Regression and F-statistic]], [[12 - ANOVA and F-statistic]], [[3 - Paradoxe de Simpson]], [[0 - proba&stats utilitaire]]
