---
type: concept
tags:
  - year3
aliases:
  - Student distribution
  - t distribution
  - loi t
  - loi de Student à n degrés de liberté
  - théorème de Gosset
  - Gosset's theorem
matieres:
  - Statistics
  - Data analysis (Thanos)
sources:
  - "[[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]]"
  - "[[6 - T-Test|Cours 6 - T-Test]]"
  - "[[Raw/Year 3/Statistics/Chp4 Part3 : Inferential statistics.docx|Chp4 Part3 - Inferential statistics]]"
maj: 2026-11-08
---

Si $Z$ est normale centrée réduite et $Y \sim \chi^2_v$ lui est indépendante, $T = Z/\sqrt{Y/v}$ suit la loi de Student à $v$ degrés de liberté, $t_v$ ([[Loi du khi-deux]]). Plus $v$ est grand, plus la courbe est proche de celle de $Z$ ; à bas degré, les queues sont plus épaisses.

**Théorème de Gosset** : pour un échantillon $N(\mu, \sigma)$, $(\bar{X} - \mu)/(S/\sqrt{n}) \sim t_{n-1}$ (preuve laissée en devoir). Cette loi ne dépend d'aucun paramètre inconnu : la statistique est un pivot. [[Complément hors du cours|ⓘ]] Valeur critique $t_{\alpha,\nu}$ : aire $\alpha$ à sa droite.

**Idée de la preuve** : on écrit [[Complément hors du cours|ⓘ]]
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\dfrac{(n-1)S^2/\sigma^2}{n-1}}} = \frac{Z}{\sqrt{Y/(n-1)}},$$
avec $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ et $Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ ([[Loi du khi-deux]]). $Z$ et $Y$ sont indépendantes, car $\bar{X}$ et $S^2$ le sont dans le cas gaussien. C'est exactement la définition de $t_{n-1}$. Le $\sigma$ inconnu se simplifie entre numérateur et dénominateur : d'où le pivot.

**Propriétés** : [[Complément hors du cours|ⓘ]]
- symétrique autour de 0 ;
- espérance $0$ pour $v > 1$ ;
- variance $\dfrac{v}{v-2}$ pour $v > 2$, toujours supérieure à 1 (celle de $Z$) : c'est l'effet de l'incertitude supplémentaire due à l'estimation de $\sigma$ par $S$ ; elle est infinie pour $v \in \,]1, 2]$ ;
- pour $v = 1$, c'est la loi de Cauchy, dont l'espérance n'existe pas ;
- quand $v \to \infty$, $t_v$ tend vers $N(0, 1)$.

**Ordre de grandeur** : les valeurs critiques à 95 % bilatéral sont $t_{0{,}025;\,9} = 2{,}262$ ($n = 10$) et $t_{0{,}025;\,29} = 2{,}045$ ($n = 30$), contre $z_{0{,}025} = 1{,}96$ pour la loi normale. Avec un petit échantillon, l'intervalle de confiance est donc nettement plus large. [[Complément hors du cours|ⓘ]]

**Histoire** : la loi a été publiée en 1908 par William Sealy Gosset, chimiste de la brasserie Guinness à Dublin, qui travaillait sur de petits échantillons ; il a signé sous le pseudonyme « Student », son employeur ne permettant pas à ses salariés de publier sous leur nom. [[Complément hors du cours|ⓘ]]

Elle donne l'[[Intervalle de confiance]] de la moyenne quand $\sigma$ est inconnu : $\bar{x} \pm t_{\alpha/2,n-1}\,s/\sqrt{n}$.

En Data analysis, c'est une famille de lois, une par nombre de degrés de liberté : symétrique, de la forme de la normale mais plus étalée, et qui tend vers elle. Elle sert au [[Test t]] ([[6 - T-Test]]).

Liens : [[Loi normale]], [[Distribution d'échantillonnage]], [[Loi du khi-deux]], [[Degrés de liberté]]

Résumés : [[4 - Inferential statistics 3]], [[6 - T-Test]]
