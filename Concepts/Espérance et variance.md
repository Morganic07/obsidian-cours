---
type: concept
aliases: [expected value, expectation, espérance, espérance mathématique, standard deviation, écart-type, inégalité de Tchebychev, Chebyshev's inequality]
matieres: [Probability, Statistics]
sources: ["[[Chp 4 - Discrete random variables]]", "[[Chp 5 - Continuous random variable]]"]
maj: 2026-11-05
---

**Espérance** : $E(X) = \sum x\,p(x)$ (discret) ou $\int x f(x)\,dx$ (continu). Pour une fonction, $E[h(X)] = \sum h(x)p(x)$ ou $\int h f$.

**Linéarité** : $E(a_1h_1(X) + a_2h_2(X) + b) = a_1E(h_1(X)) + a_2E(h_2(X)) + b$. En particulier $E(aX + b) = aE(X) + b$.

**Variance** : $\mathrm{Var}(X) = E[(X - \mu)^2] = E(X^2) - \mu^2$. Écart-type $\sigma = \sqrt{\mathrm{Var}(X)}$. $\mathrm{Var}(aX + b) = a^2\sigma^2$ et $\sigma_{aX+b} = |a|\sigma$.

**Tchebychev** (cours de continu) : $P(|X - \mu| \ge k\sigma) \le 1/k^2$ pour $k \ge 1$.

Pour plusieurs variables, voir [[Covariance et corrélation]]. Pour le calcul sur un échantillon, voir [[Variance et écart-type d'échantillon]].

Liens : [[Variable aléatoire]], [[Fonction génératrice des moments]]

Résumés : [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]]
