---
type: concept
tags: [year2, year3]
aliases: [negative binomial distribution, negative binomial rv, binomiale négative]
sources: ["[[Chp 3 - Important discrete distributions (résumé)|Chp 3 - Important discrete distributions]]", "[[Chp4 Part 1 - Inferential statistics (résumé)|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-06
---

**Probability** : paramètres $r$ (nombre de succès voulus) et $p=P(S)$, essais indépendants.
$$nb(x;r,p)=\binom{x-1}{r-1}p^r(1-p)^{x-r},\qquad x=r,r+1,\dots$$
$E(X)=r/p$ et $\text{Var}(X)=r(1-p)/p^2$.

**Statistics** : citée parmi les lois additives que le théorème central limite permet d'approcher par une loi normale quand $r$ est grand.

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Loi binomiale]], [[Approximation normale]].

## À vérifier

Le cours dit « nombre d'essais avant d'obtenir $r$ succès », mais la formule compte les essais jusqu'au $r$-ième succès inclus.

Résumés : [[Chp 3 - Important discrete distributions (résumé)]], [[Chp4 Part 1 - Inferential statistics (résumé)]]
