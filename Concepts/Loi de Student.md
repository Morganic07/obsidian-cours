---
type: concept
aliases: [Student distribution, t distribution, loi t, loi de Student à n degrés de liberté, théorème de Gosset, Gosset's theorem]
matieres: [Statistics]
sources: ["[[Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-05
---

Si $Z$ est normale centrée réduite et $Y \sim \chi^2_v$ lui est indépendante, $T = Z/\sqrt{Y/v}$ suit la loi de Student à $v$ degrés de liberté, $t_v$ ([[Loi du khi-deux]]). Plus $v$ est grand, plus la courbe est proche de celle de $Z$ ; à bas degré, les queues sont plus épaisses.

**Théorème de Gosset** : pour un échantillon $N(\mu, \sigma)$, $(\bar{X} - \mu)/(S/\sqrt{n}) \sim t_{n-1}$ (preuve laissée en devoir). Cette loi ne dépend d'aucun paramètre inconnu : la statistique est un pivot (complément). Valeur critique $t_{\alpha,\nu}$ : aire $\alpha$ à sa droite.

Elle donne l'[[Intervalle de confiance]] de la moyenne quand $\sigma$ est inconnu : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$.

Liens : [[Loi normale]], [[Distribution d'échantillonnage]]

Résumé : [[Chp4 Part3 - Inferential statistics (résumé)]]
