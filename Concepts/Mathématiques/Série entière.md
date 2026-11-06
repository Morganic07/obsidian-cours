---
type: concept
tags: [year3]
aliases: [séries entières, power series, rayon de convergence, radius of convergence, intervalle de convergence, série de Taylor, série de Maclaurin, Taylor series, Maclaurin series, série binomiale, polynôme de Taylor, Taylor polynomial]
matieres: [Séries]
sources: ["[[Chp5 - power series]]"]
maj: 2026-11-06
---

Série de fonctions $\sum a_n(x - \alpha)^n$. Trois cas : convergence en $\alpha$ seulement ($R = 0$), partout ($R = +\infty$), ou rayon $0 < R < +\infty$ avec convergence absolue pour $|x - \alpha| < R$ et divergence pour $|x - \alpha| > R$. Le rayon est unique. Aux bords, tout peut arriver, y compris une [[Convergence conditionnelle|convergence conditionnelle]] (série binomiale en 1 pour $-1 < a < 0$). Le rayon se calcule avec $\lim \frac{|a_{n+1}|}{|a_n|}$ ou $\lim \sqrt[n]{|a_n|}$ égale à $\ell$ : $R = 1/\ell$ ([[Critère de d'Alembert et de Cauchy]]).

**Propriétés** : convergence normale sur tout $[\alpha - r, \alpha + r]$ avec $r < R$, somme continue et indéfiniment dérivable sur $]\alpha - R, \alpha + R[$, dérivation et intégration terme à terme avec le même rayon (voir [[Interversion de limites]]).

**Taylor** : si $f = \sum a_n(x - \alpha)^n$, alors $a_n = \frac{f^{(n)}(\alpha)}{n!}$ (série de Maclaurin en $\alpha = 0$). Le polynôme de Taylor d'ordre $n$ est $T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(\alpha)}{k!}(x-\alpha)^k$. [[Reste de Taylor]] sous forme intégrale, de Lagrange, ou par inégalité de Taylor. Séries usuelles : $e^x$, $\sin$, $\cos$, $\sinh$, $\cosh$ ([[Fonctions hyperboliques]]) sur $\mathbb{R}$ ; $\frac{1}{1-x}$, $\ln(1+x)$, $\arctan$, $(1+x)^a$ sur $]-1, 1[$. Applications : somme d'une série numérique ($\ln(3/2)$), approximation de $\pi$ et de $e$.

Voir aussi : [[Développement limité]], [[Convergence uniforme]], [[Série numérique]], [[Reste de Taylor]], [[Critère de d'Alembert et de Cauchy]], [[Interversion de limites]], [[Fonctions hyperboliques]], [[Convergence conditionnelle]]

## À vérifier

- [[Chp5 - power series]] annonce une précision de $10^{-2}$ sur $\pi$ pour $n \ge 49$ : c'est sur $\pi/4$, il faut $n \ge 199$ pour $\pi$ (à corriger avant un examen).
- « $R_{\lambda a} = R_a$ » est faux pour $\lambda = 0$ (série nulle, $R = +\infty$).

Résumé : [[Chp5 - power series (résumé)]]
