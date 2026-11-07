---
type: concept
tags: [year2, year3]
aliases: [binomial distribution, binomial random variable, loi de Bernoulli, Bernoulli random variable, expérience binomiale, Bernoulli rv, variable de Bernoulli]
matieres: [Probability, Statistics]
sources: ["[[3 - Important discrete distributions|Chp 3 - Important discrete distributions]]", "[[3 - More on probability|Chp3 - More on probability]]"]
maj: 2026-11-07
---

**Expérience binomiale** : $n$ essais fixés à l'avance, deux issues (succès avec probabilité $p$, échec avec $1 - p$), essais indépendants. Un essai seul suit la loi de Bernoulli ($X = 1$ avec probabilité $p$, 0 sinon) : $E(X) = E(X^n) = p$ (pour $n \ge 1$), $V(X) = p(1-p)$.

Le nombre de succès $X$ suit la loi binomiale $(n, p)$ : $P(X = i) = \binom{n}{i}p^i(1-p)^{n-i}$ ($i = 0, \dots, n$), $E(X) = np$, $V(X) = np(1-p)$. Ces moments viennent de $X = \sum X_i$ avec $X_i$ de Bernoulli indépendantes (voir [[Espérance et variance]]). Les coefficients sont décrits dans [[Dénombrement]].

**Approximations** : Poisson quand $n$ est grand et $p$ petit ([[Loi de Poisson]]) ; normale quand $np \ge 10$ et $n(1-p) \ge 10$ ([[Théorème central limite]]). En Data analysis, le test $Z$ sur une proportion repose sur cette approximation, applicable quand $nP$ et $n(1-P)$ valent au moins 5 ([[7 - Z-Test]]).

**Somme** : une somme de binomiales indépendantes de même $p$ est une binomiale ([[4 - Inferential statistics 1]]). La fiche [[0 - proba&stats utilitaire|utilitaire de Statistics]] rappelle la moyenne et la variance.

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Loi de Poisson]], [[Combinaison (dénombrement)]], [[Loi binomiale négative]], [[Approximation normale]], [[Stabilité des lois par somme]].

## Erreurs du cours

- [[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]] écrit, pour $X_i \sim \mathrm{Bin}(n_i, p)$ indépendantes, « Y ∼ Bin(n_j , q) » ; il faut $Y \sim \mathrm{Bin}\left(\sum n_i, p\right)$.

Résumés : [[3 - Important discrete distributions]], [[4 - Discrete random variables]], [[3 - More on probability]], [[4 - Inferential statistics 1]], [[0 - proba&stats utilitaire]], [[7 - Z-Test]]
