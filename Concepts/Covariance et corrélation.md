---
type: concept
aliases: [covariance, correlation coefficient, coefficient de corrélation, variables non corrélées, uncorrelated, combinaison linéaire de variables aléatoires, linear combination of rvs]
matieres: [Probability, Statistics]
sources: ["[[Chp 6 - Joint probability distributions]]", "[[Chp3 - More on probability]]"]
maj: 2026-11-05
---

$\mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E(XY) - \mu_X\mu_Y$ ; symétrique, avec $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$.

**Corrélation** : $\rho = \mathrm{Cov}(X, Y)/(\sigma_X\sigma_Y)$. Si $X$ et $Y$ sont indépendantes, $\rho = 0$, mais $\rho = 0$ n'entraîne pas l'indépendance. $\rho = \pm 1$ si et seulement si $Y = aX + b$, $a \ne 0$. Non corrélées signifie $E[XY] = \mu_X\mu_Y$. Corrélation n'est pas causalité.

**Combinaison linéaire** $a_1X_1 + \dots + a_nX_n + b$ : $E = \sum a_i\mu_i + b$ sans condition ; $\mathrm{Var} = \sum_i\sum_j a_ia_j\mathrm{Cov}(X_i, X_j)$, qui devient $\sum a_i^2\sigma_i^2$ si les $X_i$ sont indépendantes. Pour une moyenne empirique, voir [[Théorème central limite]].

Liens : [[Loi conjointe]], [[Espérance et variance]]

Résumés : [[Chp 6 - Joint probability distributions (résumé)]], [[Chp3 - More on probability (résumé)]]
