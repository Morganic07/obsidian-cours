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
  - intervalle de Wald
  - Wald interval
  - intervalle de Wilson
  - Wilson score interval
  - intervalle de Clopper-Pearson
matieres:
  - Statistics
  - Data analysis (Thanos)
sources:
  - "[[4 - Inferential statistics 2|Chp4 Part2 - Inferential statistics]]"
  - "[[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]]"
  - "[[4 - Estimation|Cours 4 - Estimation]]"
maj: 2026-11-08
---

Un intervalle de confiance de niveau $100(1-\alpha)\,\%$ encadre un paramètre : estimation ponctuelle $\pm$ marge d'erreur. Sur de nombreux échantillons, une proportion $1 - \alpha$ des intervalles contient le paramètre : c'est l'intervalle qui varie, $\mu$ est fixe.

**Moyenne, $\sigma$ connu** : $\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$, avec $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$. [[Erreurs du cours#^e-intervalle-de-confiance|✎]] Valeurs : $z_{\alpha/2} = 1{,}645$ (90 %), $1{,}96$ (95 %), $2{,}58$ (99 %). Valable approximativement pour une loi quelconque si $n$ est grand ([[Théorème central limite]]).

**Méthode du pivot** : trouver $g(X; \theta)$ dépendant de $\theta$ dont la loi n'en dépend pas, encadrer $g$ par $C_L$, $C_U$, puis isoler $\theta$.

**Moyenne, $\sigma$ inconnu** (échantillon normal) : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$ ([[Loi de Student]]). **Variance** (moyenne $\mu$ inconnue) : $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2,n-1}},\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,n-1}}\right]$ ([[Loi du khi-deux]]). [[Erreurs du cours#^e-intervalle-de-confiance|✎]] **Proportion** : $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$.

**Taille d'échantillon** pour une erreur $E$ : $n = (z_{\alpha/2}\sigma/E)^2$ pour une moyenne ; $n = (z_{\alpha/2}/E)^2p(1-p)$ pour une proportion, avec $p(1-p) \le 0{,}25$.

**Intervalles unilatéraux**, $\sigma$ connu : $(-\infty, \bar{X} + z_\alpha\sigma/\sqrt{n})$ et $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$. [[Erreurs du cours#^e-intervalle-de-confiance|✎]]

**En Data analysis** : les mêmes intervalles (moyenne, proportion, variance) servent avec les tests Z, t et du khi-deux ([[Test d'hypothèse]], [[Quantile]]). En régression, l'intervalle de la réponse moyenne est $\hat{y} \pm t_{\alpha/2}\,s\sqrt{1/n + (x_p - \bar{x})^2/SS_{xx}}$ ([[11 - Multiple Linear Regression and F-statistic]]).

Liens : [[Estimateur]], [[Loi normale]], [[Distribution d'échantillonnage]]

## Compléments (complément, hors du cours)

**Intervalle d'une proportion : Wald, Wilson, Clopper-Pearson.** L'intervalle $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$ du cours s'appelle l'**intervalle de Wald**. Il repose sur l'approximation normale de la loi binomiale et n'est fiable que si $n\hat{p} \ge 5$ et $n(1-\hat{p}) \ge 5$ (seuil de 10 selon les manuels). Pour une proportion proche de 0 ou de 1, ou un petit échantillon, son niveau réel est nettement inférieur au niveau annoncé. On utilise alors :
- l'**intervalle de Wilson** (*score interval*), obtenu en inversant le test Z sans remplacer $p$ par $\hat{p}$ sous la racine :
$$\frac{\hat{p} + \dfrac{z^2}{2n} \pm z\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n} + \dfrac{z^2}{4n^2}}}{1 + \dfrac{z^2}{n}}, \qquad z = z_{\alpha/2} ;$$
- l'**intervalle de Clopper-Pearson**, dit « exact », calculé directement à partir de la loi binomiale ; il est conservateur (niveau réel au moins égal au niveau annoncé).

**Marge d'erreur d'un sondage.** À 95 %, dans le cas le plus défavorable $p = 0{,}5$ : $E = 1{,}96\sqrt{0{,}25/n} \approx 1/\sqrt{n}$. Pour $n = 1\,000$, $E \approx 0{,}031$, soit environ $\pm 3$ points. Cette marge ne dépend pas de la taille $N$ de la population tant que celle-ci est grande devant l'échantillon : le facteur de correction $\sqrt{(N-n)/(N-1)}$ est alors proche de 1. Un sondage de 1 000 personnes est aussi précis pour une ville que pour un pays.

**Taille d'échantillon.** Le $n$ obtenu par la formule s'arrondit toujours à l'entier **supérieur**, pour garantir la marge voulue. Comme $n$ varie en $1/E^2$, diviser la marge par 2 demande un échantillon 4 fois plus grand. Sans estimation préalable de $p$, on prend $p = 0{,}5$, qui maximise $p(1-p)$.

**Grand échantillon, $\sigma$ inconnu.** Pour $n$ grand (règle usuelle : $n \ge 30$), on remplace $\sigma$ par $s$ et on garde le quantile normal : $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$. Les quantiles de Student se rapprochent alors de ceux de la loi normale ($t_{0{,}025;\,30} \approx 2{,}04$ contre $1{,}96$).

**Intervalle de la variance.** Il n'est pas symétrique autour de $s^2$, parce que la [[Loi du khi-deux]] ne l'est pas. Il repose sur la normalité de l'échantillon et y reste sensible même pour $n$ grand, contrairement à l'intervalle de la moyenne, que le [[Théorème central limite]] rend robuste.

Résumés : [[4 - Inferential statistics 2]], [[4 - Inferential statistics 3]], [[0 - proba&stats utilitaire]], [[4 - Estimation]], [[6 - T-Test]], [[7 - Z-Test]], [[8 - Chi²-Test]], [[11 - Multiple Linear Regression and F-statistic]]
