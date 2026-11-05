---
type: concept
aliases: [binomial distribution, binomial random variable, loi de Bernoulli, Bernoulli random variable, expérience binomiale]
matieres: [Probability, Statistics]
sources: ["[[Chp 3 - Important discrete distributions]]", "[[Chp3 - More on probability]]"]
maj: 2026-11-05
---

**Expérience binomiale** : $n$ essais fixés à l'avance, deux issues (succès avec probabilité $p$, échec avec $1 - p$), essais indépendants. Un essai seul suit la loi de Bernoulli : $E(X) = p$, $V(X) = p(1-p)$.

Le nombre de succès $X$ suit la loi binomiale $(n, p)$ : $P(X = i) = \binom{n}{i}p^i(1-p)^{n-i}$ ($i = 0, \dots, n$), $E(X) = np$, $V(X) = np(1-p)$. Ces moments viennent de $X = \sum X_i$ avec $X_i$ de Bernoulli indépendantes (voir [[Espérance et variance]]). Les coefficients sont décrits dans [[Dénombrement]].

**Approximations** : Poisson quand $n$ est grand et $p$ petit ([[Loi de Poisson]]) ; normale quand $np \ge 10$ et $n(1-p) \ge 10$ ([[Théorème central limite]]).

Liens : [[Variable aléatoire]]

Résumés : [[Chp 3 - Important discrete distributions (résumé)]], [[Chp3 - More on probability (résumé)]]
