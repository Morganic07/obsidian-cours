---
type: concept
tags: [year2, year3]
aliases: [inverse cdf method, méthode de l'inverse, simulation par inversion, inverse transform sampling]
matieres: [Statistics, Probability]
sources: ["[[3 - More on probability|Chp3 - More on probability]]", "[[5 - Continuous random variable|Chp 5 - Continuous random variable]]"]
maj: 2026-11-06
---

Soit une loi de densité $f$ et de [[Fonction de répartition]] $F$. Si $U \sim \mathrm{Unif}[0, 1)$, la variable $X = F^{-1}(U)$ a pour densité $f$.

**Simulation** de $n$ valeurs : répéter $n$ fois (1) tirer $u$ dans $[0, 1)$ avec un générateur aléatoire, (2) poser $x = F^{-1}(u)$. Les $x_i$ simulent une variable de densité $f$.

En Probability, [[5 - Continuous random variable|Chp 5 - Continuous random variable]] note seulement $\eta_p = F^{-1}(p)$, le percentile d'ordre $p$, quand l'inverse de $F$ existe (voir [[Quantile]]) ; il ne présente pas la méthode de simulation elle-même.

Notion parente : [[Fonction de répartition]]. Voir aussi : [[Variable aléatoire]], [[Loi exponentielle]], [[Loi uniforme]], [[Quantile]], [[Théorème de transformation]]

Résumés : [[3 - More on probability]], [[5 - Continuous random variable]]
