---
type: concept
aliases: [inverse cdf method, méthode de l'inverse, simulation par inversion, inverse transform sampling]
matieres: [Statistics, Probability]
sources: ["[[Chp3 - More on probability]]"]
maj: 2026-11-05
---

Soit une loi de densité $f$ et de [[Fonction de répartition]] $F$. Si $U \sim \mathrm{Unif}[0, 1)$, la variable $X = F^{-1}(U)$ a pour densité $f$.

**Simulation** de $n$ valeurs : répéter $n$ fois (1) tirer $u$ dans $[0, 1)$ avec un générateur aléatoire, (2) poser $x = F^{-1}(u)$. Les $x_i$ simulent une variable de densité $f$.

Liens : [[Variable aléatoire]], [[Loi exponentielle]]

Résumé : [[Chp3 - More on probability (résumé)]]
