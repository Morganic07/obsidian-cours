---
type: concept
aliases: [confidence interval, intervalles de confiance, niveau de confiance, confidence level, quantité pivot, pivotal quantity, marge d'erreur, taille d'échantillon pour un intervalle]
matieres: [Statistics]
sources: ["[[Chp4 Part2 - Inferential statistics]]", "[[Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-05
---

Un intervalle de confiance de niveau $100(1-\alpha)\,\%$ encadre un paramètre : estimation ponctuelle $\pm$ marge d'erreur. Sur de nombreux échantillons, une proportion $1 - \alpha$ des intervalles contient le paramètre.

**Moyenne, $\sigma$ connu** : $\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$, avec $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$. Valeurs : $z_{\alpha/2} = 1{,}645$ (90 %), $1{,}96$ (95 %), $2{,}58$ (99 %). Valable approximativement pour une loi quelconque si $n$ est grand ([[Théorème central limite]]).

**Méthode du pivot** : trouver $g(X; \theta)$ dépendant de $\theta$ dont la loi n'en dépend pas, encadrer $g$ par $C_L$, $C_U$, puis isoler $\theta$.

**Moyenne, $\sigma$ inconnu** (échantillon normal) : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$ ([[Loi de Student]]). **Variance** : $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}},\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}\right]$ ([[Loi du khi-deux]]). **Proportion** : $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.

**Taille d'échantillon** pour une erreur $E$ : $n = (z_{\alpha/2}\sigma/E)^2$ pour une moyenne ; $n = (z_{\alpha/2}/E)^2p(1-p)$ pour une proportion, avec $p(1-p) \le 0{,}25$.

> [!warning] Écart dans le cours
> Le tableau récapitulatif de [[Chp4 Part3 - Inferential statistics]] porte $\bar{X} + z_\alpha\sigma/\sqrt{n}$ dans les deux colonnes unilatérales pour $\sigma$ connu. L'intervalle supérieur devrait être $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$ (complément).

Liens : [[Estimateur]], [[Loi normale]], [[Distribution d'échantillonnage]]

Résumés : [[Chp4 Part2 - Inferential statistics (résumé)]], [[Chp4 Part3 - Inferential statistics (résumé)]]
