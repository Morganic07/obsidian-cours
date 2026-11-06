---
type: concept
tags: [year2, year3]
aliases: [linear regression, simple linear regression, multiple linear regression, régressions linéaires, least square line, least-squares line, least squares line, line of regression, droite de régression, droite des moindres carrés, design matrix, matrice de plan, parameter vector, observation vector, linear model, linear models, régression linéaire multiple, modèle linéaire simple, ordonnée à l'origine]
sources: ["[[chp 1 - Orthogonality]]", "[[Cours 10 - linear regression]]", "[[Cours 11 - Multiple Linear Regression and F-statistic]]", "[[Cours 12 - ANOVA and F-statistic]]", "[[probabilité statistiques utilitaire]]"]
maj: 2026-11-06
---

Trouver la droite $y = \beta_0 + \beta_1x$ la plus proche de points $(x_j, y_j)$, c'est-à-dire celle qui minimise la somme des carrés des [[Résidu (régression)|résidus]] (les écarts verticaux entre les points et la droite). $\beta_0$ (l'ordonnée à l'origine) et $\beta_1$ sont les coefficients de régression.

En algèbre linéaire, le problème s'écrit $X\boldsymbol{\beta} = \mathbf{y}$ au lieu de $A\mathbf{x} = \mathbf{b}$, avec $X$ la design matrix (matrice de plan), $\boldsymbol{\beta}$ le parameter vector (vecteur des paramètres) et $\mathbf{y}$ l'observation vector (vecteur des observations). C'est un problème de [[Moindres carrés]] avec d'autres notations.

**En statistique** (Data analysis (Thanos)) : le modèle simple $y = \beta_0 + \beta_1x + \varepsilon$ est estimé par les moindres carrés, $\hat\beta_1 = SS_{xy}/SS_{xx}$ et $\hat\beta_0 = \bar y - \hat\beta_1 \bar x$. Il suppose une erreur de moyenne nulle, de variance constante, normale et indépendante, ce qui se vérifie sur les résidus. Le [[Test de la pente]] porte sur $H_0 : \beta_1 = 0$, avec $n - 2$ degrés de liberté. $R^2$ ([[Coefficient de détermination]]) est la part de variation expliquée, avec $SST = SSR + SSE$.

**Régression multiple** : $y = \beta_0 + \beta_1X_1 + \dots + \beta_kX_k + \varepsilon$, où $\beta_j$ est l'effet moyen de $X_j$ toutes les autres variables fixées, avec $n-(k+1)$ degrés de liberté ([[Cours 11 - Multiple Linear Regression and F-statistic]]). [[Séance 3 - Paradoxe de Simpson (résumé)|Le cours 3]] note que la régression multivariée « ajuste » les résultats en tenant compte des variables cachées.

[[Cours 12 - ANOVA and F-statistic]] présente la régression simple comme un cas particulier d'[[ANOVA]], à partir de $y_i - \bar{y} = (y_i - \hat{y}_i) + (\hat{y}_i - \bar{y})$.

L'aide-mémoire de Statistics ([[probabilité statistiques utilitaire (résumé)|probabilité statistiques utilitaire]]) écrit la droite $\hat{Y} = a + bX$ avec $b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2}$ et $a = \bar Y - b\bar X$.

Notion parente : [[Moindres carrés]]. Voir aussi : [[Projection orthogonale]], [[Statistique F]], [[Intervalle de prédiction]], [[Résidu (régression)]], [[Test de la pente]], [[Coefficient de détermination]], [[ANOVA]]

## À vérifier

- [[chp 1 - Orthogonality]] écrit « determine β1 and β1 », à lire $\beta_0$ et $\beta_1$.
- « matrice de plan » : traduction de design matrix qui n'est pas donnée par le cours.

Résumés : [[chp 1 - Orthogonality (résumé)]], [[Séance 10 - linear regression (résumé)]], [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Séance 12 - ANOVA and F-statistic (résumé)]], [[Séance 3 - Paradoxe de Simpson (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
