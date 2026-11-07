---
type: concept
tags:
  - year3
aliases:
  - confidence interval
  - intervalles de confiance
  - niveau de confiance
  - confidence level
  - quantité pivot
  - pivotal quantity
  - marge d'erreur
  - taille d'échantillon pour un intervalle
  - confidence interval estimator
  - CIE
  - intervalle de confiance d'une variance
  - intervalle de confiance d'une proportion
matieres:
  - Statistics
  - Data analysis (Thanos)
sources:
  - "[[4 - Inferential statistics 2|Chp4 Part2 - Inferential statistics]]"
  - "[[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]]"
  - "[[4 - Estimation|Cours 4 - Estimation]]"
maj: 2026-11-07
---

Un intervalle de confiance de niveau $100(1-\alpha)\,\%$ encadre un paramètre : estimation ponctuelle $\pm$ marge d'erreur. Sur de nombreux échantillons, une proportion $1 - \alpha$ des intervalles contient le paramètre : c'est l'intervalle qui varie, $\mu$ est fixe.

**Moyenne, $\sigma$ connu** : $\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$, avec $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$. Valeurs : $z_{\alpha/2} = 1{,}645$ (90 %), $1{,}96$ (95 %), $2{,}58$ (99 %). Valable approximativement pour une loi quelconque si $n$ est grand ([[Théorème central limite]]).

**Méthode du pivot** : trouver $g(X; \theta)$ dépendant de $\theta$ dont la loi n'en dépend pas, encadrer $g$ par $C_L$, $C_U$, puis isoler $\theta$.

**Moyenne, $\sigma$ inconnu** (échantillon normal) : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$ ([[Loi de Student]]). **Variance** : $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}},\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}\right]$ ([[Loi du khi-deux]]). **Proportion** : $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.

**Taille d'échantillon** pour une erreur $E$ : $n = (z_{\alpha/2}\sigma/E)^2$ pour une moyenne ; $n = (z_{\alpha/2}/E)^2p(1-p)$ pour une proportion, avec $p(1-p) \le 0{,}25$.

**Intervalles unilatéraux**, $\sigma$ connu : $(-\infty, \bar{X} + z_\alpha\sigma/\sqrt{n})$ et $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$ ; le tableau du cours porte une erreur de signe sur le second (voir « Erreurs du cours »).

**En Data analysis** : les mêmes intervalles (moyenne, proportion, variance) servent avec les tests Z, t et du khi-deux ([[Test d'hypothèse]], [[Quantile]]). En régression, l'intervalle de la réponse moyenne est $\hat{y} \pm t_{\alpha/2}\,s\sqrt{1/n + (x_p - \bar{x})^2/SS_{xx}}$ ([[11 - Multiple Linear Regression and F-statistic]]).

Liens : [[Estimateur]], [[Loi normale]], [[Distribution d'échantillonnage]]

## Erreurs du cours

- [[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]] et [[8 - Chi²-Test|Cours 8 - Chi²-Test]] (même tableau « Table 7.1 », vérifié sur l'image) écrivent, pour $\sigma^2$ connu, l'intervalle supérieur « $(\overline{X} + z_\alpha\sigma/\sqrt{n}, \infty)$ » ; il faut $(\overline{X} - z_\alpha\sigma/\sqrt{n}, \infty)$, comme la ligne $\sigma^2$ inconnu du même tableau ($\overline{X} - t_{\alpha,n-1}S/\sqrt{n}$).
- [[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]] titre l'intervalle de la variance « the case of Gaussian distributed rv, mean known » ; il faut « mean unknown » : la formule utilise $s^2$ et $n-1$ degrés de liberté, et le tableau récapitulatif la range sous « μ unknown ».
- [[4 - Estimation|Cours 4 - Estimation]] et l'aide-mémoire ([[0 - proba&stats utilitaire]]) écrivent « $\overline{X} \pm Z_\alpha\,\sigma/\sqrt{n}$ » ; il faut $z_{\alpha/2}$ pour un intervalle bilatéral de niveau $1-\alpha$. Aucun des deux ne définit $Z_\alpha$.

Résumés : [[4 - Inferential statistics 2]], [[4 - Inferential statistics 3]], [[0 - proba&stats utilitaire]], [[4 - Estimation]], [[6 - T-Test]], [[7 - Z-Test]], [[8 - Chi²-Test]], [[11 - Multiple Linear Regression and F-statistic]]
