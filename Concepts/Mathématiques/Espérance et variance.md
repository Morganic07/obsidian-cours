---
type: concept
tags: [year2, year3]
aliases: [expected value, expectation, espérance, espérance mathématique, standard deviation, écart-type, inégalité de Tchebychev, Chebyshev's inequality, linearity of expectation, "linéarité de l'espérance", variance shortcut formula, formule raccourcie de la variance, formule de König-Huygens]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[Chp 4 - Discrete random variables (résumé)|Chp 4 - Discrete random variables]]", "[[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]]", "[[Chp3 - More on probability (résumé)|Chp3 - More on probability]]"]
maj: 2026-11-06
---

**Espérance** : $E(X) = \sum x\,p(x)$ (discret) ou $\int x f(x)\,dx$ (continu). Pour une fonction, $E[h(X)] = \sum h(x)p(x)$ ou $\int h f$. Pour deux variables, $E[h(X, Y)] = \sum h(x, y)\,p(x, y)$, lui aussi linéaire.

**Linéarité** : $E(a_1h_1(X) + a_2h_2(X) + b) = a_1E(h_1(X)) + a_2E(h_2(X)) + b$. En particulier $E(aX + b) = aE(X) + b$.

**Variance** : $\mathrm{Var}(X) = E[(X - \mu)^2] = E(X^2) - \mu^2$ (*shortcut formula*, formule raccourcie). Écart-type $\sigma = \sqrt{\mathrm{Var}(X)}$. $\mathrm{Var}(aX + b) = a^2\sigma^2$ et $\sigma_{aX+b} = |a|\sigma$.

**Tchebychev** (cours de continu) : $P(|X - \mu| \ge k\sigma) \le 1/k^2$ pour $k \ge 1$.

**Combinaison linéaire et échantillon** (Statistics, Data analysis) : pour $Y = \sum a_iX_i + b$, $E(Y) = \sum a_i\mu_i + b$, et $\mathrm{Var}(Y) = \sum a_i^2\sigma_i^2$ si les $X_i$ sont indépendantes. Pour le total $T$ d'un échantillon de taille $n$ et sa moyenne : $E(T) = n\mu$, $\mathrm{Var}(T) = n\sigma^2$, $\mathrm{Var}(\bar X) = \sigma^2/n$ ([[Distribution d'échantillonnage]]).

Pour plusieurs variables, voir [[Covariance et corrélation]]. Pour le calcul sur un échantillon, voir [[Variance et écart-type d'échantillon]].

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Fonction génératrice des moments]], [[Covariance et corrélation]], [[Distribution d'échantillonnage]]

## À vérifier

- Le nom « formule de König-Huygens » n'est pas dans le cours, qui dit « shortcut formula ».

Résumés : [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]], [[Chp 6 - Joint probability distributions (résumé)]], [[Chp3 - More on probability (résumé)]], [[Séance 9 - Covariance and Correlation (résumé)]]
