---
type: concept
tags: [year2, year3]
aliases: [joint distribution, joint pmf, joint pdf, loi marginale, marginal pmf, marginal pdf, convolution, joint probability distribution, lois marginales, densité conjointe, joint density]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[6 - Joint probability distributions (résumé)|Chp 6 - Joint probability distributions]]", "[[9 - Covariance and Correlation (résumé)|Cours 9 - Covariance and Correlation]]", "[[3 - More on probability (résumé)|Chp3 - More on probability]]"]
maj: 2026-11-06
---

**Loi conjointe** de deux variables : $p(x, y) = P(X = x \text{ et } Y = y)$ (discret), avec $p \ge 0$, $\sum p = 1$ et $P((X, Y) \in A) = \sum_A p$ ; ou densité conjointe $f(x, y)$ avec $P((X, Y) \in A) = \iint_A f$ (continu, [[Intégrale multiple]]). Elle s'étend à $n$ variables. Espérance : $E[h(X, Y)] = \sum\sum h\,p$ ou $\iint h\,f$.

**Lois marginales** : $p_X(x) = \sum_y p(x, y)$, $f_X(x) = \int f(x, y)\,dy$, et de même pour $Y$.

**Indépendance** ([[Indépendance de variables aléatoires]]) : $X$ et $Y$ sont indépendantes si $p(x, y) = p_X(x)p_Y(y)$ (ou $f = f_Xf_Y$) pour tout couple. Alors $E[g_1(X)g_2(Y)] = E[g_1(X)]E[g_2(Y)]$.

**Somme** : si $X$ et $Y$ sont indépendantes et continues, la densité de $W = X + Y$ est la convolution $f_W(w) = \int f_X(x)f_Y(w - x)\,dx$.

En Data analysis et en Statistics (3e année), le cours reprend ces définitions et ajoute que la convolution de lois normales est normale ([[9 - Covariance and Correlation (résumé)]], [[3 - More on probability (résumé)]]).

Notion parente : [[Variable aléatoire]].

Liens : [[Covariance et corrélation]], [[Probabilité conditionnelle]]

## À vérifier

- [[6 - Joint probability distributions (résumé)|Chp 6 - Joint probability distributions]] : la mention d'un événement « de $S \times S$ » est à vérifier sur l'image.

Résumés : [[6 - Joint probability distributions (résumé)]], [[9 - Covariance and Correlation (résumé)]], [[3 - More on probability (résumé)]]
