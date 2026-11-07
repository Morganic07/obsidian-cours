---
type: concept
tags: [year3]
aliases: [confidence interval, intervalles de confiance, niveau de confiance, confidence level, quantité pivot, pivotal quantity, marge d'erreur, taille d'échantillon pour un intervalle, confidence interval estimator, CIE, intervalle de confiance d'une variance, intervalle de confiance d'une proportion]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[Chp4 Part2 - Inferential statistics (résumé)|Chp4 Part2 - Inferential statistics]]", "[[Chp4 Part3 - Inferential statistics (résumé)|Chp4 Part3 - Inferential statistics]]", "[[Séance 4 - Estimation (résumé)|Cours 4 - Estimation]]"]
maj: 2026-11-06
---

Un intervalle de confiance de niveau $100(1-\alpha)\,\%$ encadre un paramètre : estimation ponctuelle $\pm$ marge d'erreur. Sur de nombreux échantillons, une proportion $1 - \alpha$ des intervalles contient le paramètre : c'est l'intervalle qui varie, $\mu$ est fixe.

**Moyenne, $\sigma$ connu** : $\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$, avec $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$. Valeurs : $z_{\alpha/2} = 1{,}645$ (90 %), $1{,}96$ (95 %), $2{,}58$ (99 %). Valable approximativement pour une loi quelconque si $n$ est grand ([[Théorème central limite]]).

**Méthode du pivot** : trouver $g(X; \theta)$ dépendant de $\theta$ dont la loi n'en dépend pas, encadrer $g$ par $C_L$, $C_U$, puis isoler $\theta$.

**Moyenne, $\sigma$ inconnu** (échantillon normal) : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$ ([[Loi de Student]]). **Variance** : $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}},\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}\right]$ ([[Loi du khi-deux]]). **Proportion** : $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.

**Taille d'échantillon** pour une erreur $E$ : $n = (z_{\alpha/2}\sigma/E)^2$ pour une moyenne ; $n = (z_{\alpha/2}/E)^2p(1-p)$ pour une proportion, avec $p(1-p) \le 0{,}25$.

> [!warning] Écart dans le cours
> Le tableau récapitulatif de [[Chp4 Part3 - Inferential statistics (résumé)|Chp4 Part3 - Inferential statistics]] porte $\bar{X} + z_\alpha\sigma/\sqrt{n}$ dans les deux colonnes unilatérales pour $\sigma$ connu. L'intervalle supérieur devrait être $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$ (complément).

**En Data analysis** : les mêmes intervalles (moyenne, proportion, variance) servent avec les tests Z, t et du khi-deux ([[Test d'hypothèse]], [[Quantile]]). En régression, l'intervalle de la réponse moyenne est $\hat{y} \pm t_{\alpha/2}\,s\sqrt{1/n + (x_p - \bar{x})^2/SS_{xx}}$ ([[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]]).

Liens : [[Estimateur]], [[Loi normale]], [[Distribution d'échantillonnage]]

## À vérifier

- Le même tableau récapitulatif figure aussi dans [[Séance 8 - Chi²-Test (résumé)|Cours 8 - Chi²-Test]], avec le même $+$ au lieu d'un $-$ pour l'intervalle supérieur à $\sigma$ connu : à corriger avant un examen.
- Le titre « mean known » est faux pour l'intervalle de la variance.
- [[Séance 4 - Estimation (résumé)|Cours 4 - Estimation]] et l'aide-mémoire ([[probabilité statistiques utilitaire (résumé)]]) notent $Z_\alpha$ là où il faut $z_{\alpha/2}$.

Résumés : [[Chp4 Part2 - Inferential statistics (résumé)]], [[Chp4 Part3 - Inferential statistics (résumé)]], [[probabilité statistiques utilitaire (résumé)]], [[Séance 4 - Estimation (résumé)]], [[Séance 6 - T-Test (résumé)]], [[Séance 7 - Z-Test (résumé)]], [[Séance 8 - Chi²-Test (résumé)]], [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]]
