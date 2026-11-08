---
type: concept
tags: [year2, year3]
aliases: [covariance, correlation coefficient, coefficient de corrélation, variables non corrélées, uncorrelated, combinaison linéaire de variables aléatoires, linear combination of rvs, Covariance shortcut formula, distributive property of covariance, correlation versus causation, corrélation de Pearson, coefficient de corrélation de Pearson, Pearson correlation, "coefficient d'échantillon r"]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[6 - Joint probability distributions|Chp 6 - Joint probability distributions]]", "[[3 - More on probability|Chp3 - More on probability]]", "[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-08
---

$\mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E(XY) - \mu_X\mu_Y$ (formule raccourcie) ; symétrique, avec $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$. Distributivité : $\mathrm{Cov}(aX + bY + c, Z) = a\,\mathrm{Cov}(X, Z) + b\,\mathrm{Cov}(Y, Z)$. La covariance dépend des unités ; elle s'estime sur un échantillon par $\sum (x_i - \bar X)(y_i - \bar Y)/(n-1)$.

**Corrélation de Pearson** : $\rho = \mathrm{Cov}(X, Y)/(\sigma_X\sigma_Y)$, sans unité, entre $-1$ et $1$, bornes comprises [[Erreurs du cours#^e-covariance-et-correlation|✎]]. Si $X$ et $Y$ sont [[Indépendance de variables aléatoires|indépendantes]], $\rho = 0$, mais $\rho = 0$ n'entraîne pas l'indépendance. $\rho = \pm 1$ si et seulement si $Y = aX + b$, $a \ne 0$. Non corrélées signifie $E[XY] = \mu_X\mu_Y$. Corrélation n'est pas causalité : voir [[Corrélation et causalité]]. Coefficient d'échantillon : $r = SS_{xy}/\sqrt{SS_{xx}SS_{yy}}$.

**Changement d'unités (complément, hors du cours)** : $\mathrm{Cov}(aX + b, cY + d) = ac\,\mathrm{Cov}(X, Y)$, donc $\mathrm{Corr}(aX + b, cY + d) = \mathrm{Corr}(X, Y)$ si $ac > 0$ et $-\mathrm{Corr}(X, Y)$ si $ac < 0$ : la corrélation ne dépend pas des unités, seulement du sens des axes.

**Pourquoi $-1 \le \rho \le 1$ (complément, hors du cours)** : $\mathrm{Var}\!\left(\dfrac{X}{\sigma_X} \pm \dfrac{Y}{\sigma_Y}\right) = 2(1 \pm \rho) \ge 0$. C'est l'[[Inégalité de Cauchy-Schwarz]] appliquée aux variables centrées, $\lvert \mathrm{Cov}(X, Y) \rvert \le \sigma_X\sigma_Y$, avec égalité si et seulement si $Y = aX + b$. Géométriquement, le $r$ d'échantillon est le cosinus de l'angle entre les vecteurs centrés $(x_i - \bar x)$ et $(y_i - \bar y)$.

**Variance d'une somme (complément, hors du cours)** : $\mathrm{Var}(aX + bY) = a^2\,\mathrm{Var}(X) + b^2\,\mathrm{Var}(Y) + 2ab\,\mathrm{Cov}(X, Y)$ ; $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$ seulement si $X$ et $Y$ sont non corrélées. Forme matricielle : $\mathrm{Var}(a^\top X) = a^\top \Sigma a$, avec $\Sigma$ la [[Matrice de covariance]]. Pour la moyenne empirique d'un échantillon iid : $E(\bar X) = \mu$ et $\mathrm{Var}(\bar X) = \sigma^2/n$.

**Non corrélées sans être indépendantes (complément, hors du cours)** : $X$ uniforme sur $\{-1, 0, 1\}$ et $Y = X^2$. Alors $E(X) = 0$ et $E(XY) = E(X^3) = 0$, donc $\mathrm{Cov}(X, Y) = 0$, alors que $Y$ est une fonction de $X$. La corrélation ne mesure que la dépendance **linéaire**.

**Test de $H_0 : \rho = 0$ (complément, hors du cours)** : sous normalité bivariée, $t = \dfrac{r\sqrt{n-2}}{\sqrt{1 - r^2}}$ suit une [[Loi de Student]] à $n - 2$ degrés de liberté. La normalité ne sert qu'au test, pas au calcul de $r$. En R : `cor(x, y, method = "pearson")` (ou `"spearman"`, `"kendall"`) et `cor.test(x, y)`.

**Sensibilité aux points aberrants (complément, hors du cours)** : un seul point peut créer ou masquer une forte corrélation ; voir le [[Quatuor d'Anscombe]]. La **matrice de corrélation** est la [[Matrice de covariance]] normalisée ($\Sigma_{ij}/(\sigma_i\sigma_j)$), de diagonale 1.

En Data analysis, le cours rapproche Pearson du [[Coefficient de corrélation de Spearman]], du [[Tau de Kendall]] et du [[Coefficient de détermination]] ; la version multivariée est la [[Matrice de covariance]].

**Combinaison linéaire** $a_1X_1 + \dots + a_nX_n + b$, constantes $a_i$ et $b$ quelconques ($b = 0$ pour la moyenne empirique) [[Erreurs du cours#^e-covariance-et-correlation|✎]] : $E = \sum a_i\mu_i + b$ sans condition ; $\mathrm{Var} = \sum_i\sum_j a_ia_j\mathrm{Cov}(X_i, X_j)$, qui devient $\sum a_i^2\sigma_i^2$ si les $X_i$ sont indépendantes. Pour une moyenne empirique, voir [[Théorème central limite]].

Notion parente : [[Loi conjointe]]. Voir aussi : [[Espérance et variance]], [[Corrélation et causalité]], [[Indépendance de variables aléatoires]], [[Matrice de covariance]], [[Coefficient de corrélation de Spearman]], [[Tau de Kendall]], [[Coefficient de détermination]], [[Inégalité de Cauchy-Schwarz]], [[Quatuor d'Anscombe]], [[Loi de Student]]

Résumés : [[6 - Joint probability distributions]], [[3 - More on probability]], [[9 - Covariance and Correlation]], [[0 - proba&stats utilitaire]]
