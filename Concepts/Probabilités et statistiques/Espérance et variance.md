---
type: concept
tags: [year2, year3]
aliases: [expected value, expectation, espérance, espérance mathématique, standard deviation, écart-type, inégalité de Tchebychev, Chebyshev's inequality, linearity of expectation, "linéarité de l'espérance", variance shortcut formula, formule raccourcie de la variance, formule de König-Huygens, inégalité de Markov, Markov's inequality]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[4 - Discrete random variables|Chp 4 - Discrete random variables]]", "[[5 - Continuous random variable|Chp 5 - Continuous random variable]]", "[[3 - More on probability|Chp3 - More on probability]]", "[[Raw/Year 2/Probability/Chp 4 : Discrete random variables.docx|Chp 4 - Discrete random variables]]"]
maj: 2026-11-08
---

**Espérance** : $E(X) = \sum x\,p(x)$ (discret) ou $\int x f(x)\,dx$ (continu). Pour une fonction, $E[h(X)] = \sum h(x)p(x)$ ou $\int h f$. Pour deux variables, $E[h(X, Y)] = \sum h(x, y)\,p(x, y)$, lui aussi linéaire.

**Linéarité** : $E(a_1h_1(X) + a_2h_2(X) + b) = a_1E(h_1(X)) + a_2E(h_2(X)) + b$. En particulier $E(aX + b) = aE(X) + b$.

**Variance** : $\mathrm{Var}(X) = E[(X - \mu)^2] = E(X^2) - \mu^2$ (*shortcut formula*, formule raccourcie). Écart-type $\sigma = \sqrt{\mathrm{Var}(X)}$. $\mathrm{Var}(aX + b) = a^2\sigma^2$ et $\sigma_{aX+b} = |a|\sigma$.

**Tchebychev** (cours de continu) : $P(|X - \mu| \ge k\sigma) \le 1/k^2$ pour $k \ge 1$.

**Combinaison linéaire et échantillon** (Statistics, Data analysis) : pour $Y = \sum a_iX_i + b$, $E(Y) = \sum a_i\mu_i + b$, et $\mathrm{Var}(Y) = \sum a_i^2\sigma_i^2$ si les $X_i$ sont indépendantes. Pour le total $T$ d'un échantillon de taille $n$ et sa moyenne : $E(T) = n\mu$, $\mathrm{Var}(T) = n\sigma^2$, $\mathrm{Var}(\bar X) = \sigma^2/n$ ([[Distribution d'échantillonnage]]).

## Compléments (hors du cours)

- **Interprétation de l'espérance** : moyenne des valeurs pondérée par leurs probabilités ; centre de gravité de la distribution (les masses $p(x)$ placées aux points $x$) ; valeur vers laquelle tend la moyenne d'un grand nombre de répétitions indépendantes ([[Loi des grands nombres]]).
- **Existence** : dans le cas discret, $E(X)$ n'existe que si $\sum |x|\,p(x)$ converge (de même $\int |x| f(x)\,dx$ dans le cas continu).
- **Piège** : en général $E(h(X)) \ne h(E(X))$. Dans l'exemple du diagnostic automobile de [[4 - Discrete random variables]], $E(h(X)) = 52$ alors que $h(E(X)) = h(5{,}4) = 50{,}78$. L'égalité n'est garantie que pour $h$ affine.
- **Démonstration de la formule raccourcie** : par linéarité, $E[(X - \mu)^2] = E(X^2) - 2\mu E(X) + \mu^2 = E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2$.
- **Inégalité de Markov** : pour $Y \ge 0$ et $a > 0$, $P(Y \ge a) \le \dfrac{E(Y)}{a}$. Tchebychev s'en déduit en prenant $Y = (X - \mu)^2$ et $a = k^2\sigma^2$ : $P(|X - \mu| \ge k\sigma) = P\big((X-\mu)^2 \ge k^2\sigma^2\big) \le \dfrac{\sigma^2}{k^2\sigma^2} = \dfrac{1}{k^2}$.
- **Portée de Tchebychev** : elle vaut pour toute loi ayant une variance, d'où sa généralité mais aussi sa grossièreté. Pour $k = 2$, au plus 25 % des valeurs sont à $2\sigma$ ou plus de la moyenne, alors que pour une [[Loi normale]] c'est environ 5 %.

Pour plusieurs variables, voir [[Covariance et corrélation]]. Pour le calcul sur un échantillon, voir [[Variance et écart-type d'échantillon]].

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Fonction génératrice des moments]], [[Covariance et corrélation]], [[Distribution d'échantillonnage]]

Résumés : [[4 - Discrete random variables]], [[5 - Continuous random variable]], [[6 - Joint probability distributions]], [[3 - More on probability]], [[9 - Covariance and Correlation]]
