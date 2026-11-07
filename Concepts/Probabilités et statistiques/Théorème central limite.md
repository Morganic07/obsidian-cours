---
type: concept
tags:
  - year3
aliases:
  - central limit theorem
  - CLT
  - TCL
  - asymptotiquement normale
  - asymptotically normal
matieres:
  - Statistics
  - Probability
sources:
  - "[[3 - More on probability|Chp3 - More on probability]]"
  - "[[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]]"
maj: 2026-11-06
---

Soit un échantillon de loi de moyenne $\mu$ et d'écart-type $\sigma$. Pour $\bar{X}$ et le total $T = \sum X_i$ :
$E(\bar{X}) = \mu$, $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$, $E(T) = n\mu$, $\mathrm{SD}(T) = \sqrt{n}\,\sigma$.

**Théorème** : $P\!\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z\right) \to \Phi(z)$ quand $n \to \infty$, de même pour $(T - n\mu)/(\sqrt{n}\sigma)$. Pour $n$ grand, $\bar{X}$ et $T$ sont approximativement normales, quelle que soit la loi de départ. Si les $X_i$ sont normales, $\bar{X}$ et $T$ le sont exactement ([[Loi normale]]).

**Applications** : approximation normale de la [[Loi binomiale]], de la [[Loi de Poisson]] ($\mu$ grand), de la binomiale négative ($r$ grand) et de la gamma ($\alpha$ grand). Pour $\hat{P} = X/n$ : $E = p$, $\mathrm{SD} = \sqrt{p(1-p)/n}$, normale si $np \ge 10$ et $n(1-p) \ge 10$. Il justifie aussi les [[Intervalle de confiance|intervalles de confiance]] approchés.

Liens : [[Approximation normale]], [[Loi des grands nombres]], [[Échantillonnage]], [[Distribution d'échantillonnage]]

Résumés : [[3 - More on probability]], [[4 - Inferential statistics 1]], [[4 - Inferential statistics 3]]
