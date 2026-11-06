---
type: concept
tags: [year2]
aliases: [random variable, variable aléatoire discrète, variable aléatoire continue, discrete random variable, continuous random variable, fonction de masse, probability mass function, pmf, densité de probabilité, probability density function, pdf, loi de probabilité, distribution of probability]
matieres: [Probability, Statistics]
sources: ["[[Chp 4 - Discrete random variables]]", "[[Chp 5 - Continuous random variable]]"]
maj: 2026-11-06
---

Une variable aléatoire est une fonction de l'espace d'échantillonnage vers une partie de $\mathbb{R}$ ([[Espace probabilisé]]).

**Discrète** : ses valeurs forment un ensemble fini ou dénombrable. Sa loi est la fonction de masse (pmf) $p(x) = P(X = x) = P(\{s \in S : X(s) = x\})$, avec $p \ge 0$ et $\sum p = 1$. Une variable de Bernoulli prend 0 et 1.

**Continue** : sa loi est une densité (pdf) $f$ telle que $P(a \le X \le b) = \int_a^b f$, avec $f \ge 0$ et $\int f = 1$. Alors $P(X = c) = 0$, et les bornes de l'intervalle ne comptent pas.

**Changement de variable** : si $Y = g(X)$ avec $g$ strictement monotone d'inverse $h$ dérivable, $f_Y(y) = f_X(h(y))\,|h'(y)|$.

Liens : [[Fonction de répartition]], [[Espérance et variance]], [[Diagramme en bâtons et histogramme de probabilité]], [[Loi conjointe]], [[Loi binomiale]], [[Loi de Poisson]], [[Loi uniforme]], [[Loi normale]], [[Loi exponentielle]], [[Intégrale]]

## À vérifier

- [[Chp 4 - Discrete random variables]] écrit $p(x) > 0$ ; il faut $p(x) \ge 0$.
- La définition de variable continue donnée au chapitre 4 n'est qu'une propriété.

Résumés : [[Chp 4 - Discrete random variables (résumé)]], [[Chp 5 - Continuous random variable (résumé)]]
