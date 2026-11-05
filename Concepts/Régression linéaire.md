---
type: concept
aliases: [linear regression, simple linear regression, multiple linear regression, régressions linéaires, least square line, least-squares line, least squares line, line of regression, droite de régression, droite des moindres carrés]
sources: ["[[chp 1 - Orthogonality]]"]
maj: 2026-11-05
---

Trouver la droite $y = \beta_0 + \beta_1x$ la plus proche de points $(x_j, y_j)$, c'est-à-dire celle qui minimise la somme des carrés des résidus (les écarts verticaux entre les points et la droite). $\beta_0$ et $\beta_1$ sont les coefficients de régression.

En algèbre linéaire, le problème s'écrit $X\boldsymbol{\beta} = \mathbf{y}$, avec $X$ la design matrix, $\boldsymbol{\beta}$ le parameter vector et $\mathbf{y}$ l'observation vector. C'est un problème de [[Moindres carrés]] avec d'autres notations.

Le point de vue statistique reste à intégrer depuis [[Cours 10 - linear regression]] et [[Cours 11 - Multiple Linear Regression and F-statistic]].

Liens : [[Moindres carrés]], [[Projection orthogonale]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
