---
type: concept
tags: [year3]
aliases: [séries entières, power series, rayon de convergence, radius of convergence, intervalle de convergence, série de Taylor, série de Maclaurin, Taylor series, Maclaurin series, série binomiale, polynôme de Taylor, Taylor polynomial]
matieres: [Séries]
sources: ["[[5 - power series|Chp5 - power series]]"]
maj: 2026-11-07
---

Série de fonctions $\sum a_n(x - \alpha)^n$. Trois cas : convergence en $\alpha$ seulement ($R = 0$), partout ($R = +\infty$), ou rayon $0 < R < +\infty$ avec convergence absolue pour $|x - \alpha| < R$ et divergence pour $|x - \alpha| > R$. Le rayon est unique. Aux bords, tout peut arriver, y compris une [[Convergence conditionnelle|convergence conditionnelle]] (série binomiale en 1 pour $-1 < a < 0$). Le rayon se calcule avec $\lim \frac{|a_{n+1}|}{|a_n|}$ ou $\lim \sqrt[n]{|a_n|}$ égale à $\ell$ : $R = 1/\ell$ ([[Critère de d'Alembert et de Cauchy]]).

**Propriétés** : convergence normale sur tout $[\alpha - r, \alpha + r]$ avec $r < R$, somme continue et indéfiniment dérivable sur $]\alpha - R, \alpha + R[$, dérivation et intégration terme à terme avec le même rayon (voir [[Interversion de limites]]).

**Taylor** : si $f = \sum a_n(x - \alpha)^n$, alors $a_n = \frac{f^{(n)}(\alpha)}{n!}$ (série de Maclaurin en $\alpha = 0$). Le polynôme de Taylor d'ordre $n$ est $T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(\alpha)}{k!}(x-\alpha)^k$. [[Reste de Taylor]] sous forme intégrale, de Lagrange, ou par inégalité de Taylor. Séries usuelles : $e^x$, $\sin$, $\cos$, $\sinh$, $\cosh$ ([[Fonctions hyperboliques]]) sur $\mathbb{R}$ ; $\frac{1}{1-x}$, $\ln(1+x)$, $\arctan$, $(1+x)^a$ sur $]-1, 1[$. Applications : somme d'une série numérique ($\ln(3/2)$), approximation de $\pi$ et de $e$.

Voir aussi : [[Développement limité]], [[Convergence uniforme]], [[Série numérique]], [[Reste de Taylor]], [[Critère de d'Alembert et de Cauchy]], [[Interversion de limites]], [[Fonctions hyperboliques]], [[Convergence conditionnelle]]

## Erreurs du cours

- [[5 - power series|Chp5 - power series]] (approximation de $\pi$, image vérifiée) écrit « if we want to have an accuracy of $10^{-2}$, we need to take $n \ge 49$ » pour $\pi$ ; il faut $n \ge 199$. La borne $|R_n(1)| \le \frac{1}{2n+3}$ porte sur la série de somme $\pi/4$ : l'erreur sur $\pi$ est $\frac{4}{2n+3}$, et $n \ge 49$ ne donne $10^{-2}$ que sur $\pi/4$.
- [[5 - power series|Chp5 - power series]] (opérations sur les séries entières, image vérifiée) écrit « $R_{\lambda a} = R_a$ » pour tout $\lambda \in \mathbb{R}$ ; il faut $\lambda \neq 0$ : pour $\lambda = 0$, la série est nulle et $R_{\lambda a} = +\infty$.

Résumé : [[5 - power series]]
