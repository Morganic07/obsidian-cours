---
type: concept
aliases: [séries entières, power series, rayon de convergence, radius of convergence, intervalle de convergence, série de Taylor, série de Maclaurin, Taylor series, Maclaurin series, série binomiale]
matieres: [Séries]
sources: ["[[Chp5 - power series]]"]
maj: 2026-11-05
---

Série de fonctions $\sum a_n(x - \alpha)^n$. Trois cas : convergence en $\alpha$ seulement ($R = 0$), partout ($R = +\infty$), ou rayon $0 < R < +\infty$ avec convergence absolue pour $|x - \alpha| < R$ et divergence pour $|x - \alpha| > R$. Aux bords, tout peut arriver. Le rayon se calcule avec $\lim \frac{|a_{n+1}|}{|a_n|}$ ou $\lim \sqrt[n]{|a_n|}$ égale à $\ell$ : $R = 1/\ell$ ([[Critère de d'Alembert et de Cauchy]]).

**Propriétés** : convergence normale sur tout $[\alpha - r, \alpha + r]$ avec $r < R$, somme continue et indéfiniment dérivable sur $]\alpha - R, \alpha + R[$, dérivation et intégration terme à terme avec le même rayon.

**Taylor** : si $f = \sum a_n(x - \alpha)^n$, alors $a_n = \frac{f^{(n)}(\alpha)}{n!}$. Reste de Taylor sous forme intégrale, de Lagrange, ou par inégalité de Taylor. Séries usuelles : $e^x$, $\sin$, $\cos$, $\sinh$, $\cosh$ sur $\mathbb{R}$ ; $\frac{1}{1-x}$, $\ln(1+x)$, $\arctan$, $(1+x)^a$ sur $]-1, 1[$. Applications : somme d'une série numérique, approximation de $\pi$ et de $e$.

Liens : [[Développement limité]], [[Convergence uniforme]], [[Série numérique]]

Résumé : [[Chp5 - power series (résumé)]]
