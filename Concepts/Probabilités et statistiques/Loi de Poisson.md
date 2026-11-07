---
type: concept
tags:
  - year2
  - year3
aliases:
  - Poisson distribution
  - Poisson random variable
  - variable de Poisson
  - approximation de la binomiale par la loi de Poisson
matieres:
  - Probability
  - Statistics
sources:
  - "[[3 - Important discrete distributions|Chp 3 - Important discrete distributions]]"
  - "[[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]]"
maj: 2026-11-07
---

Pour $\lambda > 0$, $P(X = i) = e^{-\lambda}\lambda^i/i!$ pour $i = 0, 1, \dots$ ; $E(X) = \mathrm{Var}(X) = \lambda$.

Elle approche la [[Loi binomiale]] $(n, p)$ quand $n \to \infty$, $p \to 0$ et $np \to \mu > 0$ : la masse $b(x; n, p)$ tend vers $e^{-\mu}\mu^x/x!$.

La somme de Poisson indépendantes de moyennes $\mu_i$ est une Poisson de moyenne $\sum \mu_i$. Pour $\mu$ grand, elle est approximée par une normale ([[Théorème central limite]]).

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Loi binomiale]], [[Stabilité des lois par somme]], [[Approximation normale]].

Résumés : [[3 - Important discrete distributions]], [[4 - Inferential statistics 1]]
