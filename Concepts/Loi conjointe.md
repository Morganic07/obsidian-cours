---
type: concept
aliases: [joint distribution, joint pmf, joint pdf, loi marginale, marginal pmf, marginal pdf, indépendance de variables aléatoires, convolution]
matieres: [Probability, Statistics]
sources: ["[[Chp 6 - Joint probability distributions]]"]
maj: 2026-11-05
---

**Loi conjointe** de deux variables : $p(x, y) = P(X = x \text{ et } Y = y)$ (discret), ou densité $f(x, y)$ avec $P((X, Y) \in A) = \iint_A f$ (continu). Elle s'étend à $n$ variables.

**Lois marginales** : $p_X(x) = \sum_y p(x, y)$, $f_X(x) = \int f(x, y)\,dy$, et de même pour $Y$.

**Indépendance** : $X$ et $Y$ sont indépendantes si $p(x, y) = p_X(x)p_Y(y)$ (ou $f = f_Xf_Y$) pour tout couple. Alors $E[g_1(X)g_2(Y)] = E[g_1(X)]E[g_2(Y)]$.

**Somme** : si $X$ et $Y$ sont indépendantes et continues, la densité de $W = X + Y$ est la convolution $f_W(w) = \int f_X(x)f_Y(w - x)\,dx$.

Liens : [[Covariance et corrélation]], [[Variable aléatoire]], [[Probabilité conditionnelle]]

Résumé : [[Chp 6 - Joint probability distributions (résumé)]]
