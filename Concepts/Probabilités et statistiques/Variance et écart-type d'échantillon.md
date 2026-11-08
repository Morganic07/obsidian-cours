---
type: concept
tags: [year3]
aliases: [sample variance, sample standard deviation, variance d'échantillon, écart-type d'échantillon, correction de Bessel, degrés de liberté, degrees of freedom, ddl, moyenne d'échantillon, médiane d'échantillon, sample median, règle empirique, empirical rule]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[2 - Descriptive statistics|Chp2 - Descriptive statistics]]", "[[6 - T-Test|Cours 6 - T-Test]]", "[[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-08
---

**Moyenne** $\bar{x} = \sum x_i/n$ (voir [[Moyenne empirique]]). **Médiane** : valeur d'ordre $(n+1)/2$ ($n$ impair), ou moyenne des valeurs d'ordre $n/2$ et $n/2 + 1$ ($n$ pair). La somme des écarts à la moyenne vaut 0.

**Variance et écart-type d'échantillon** : avec $S_{xx} = \sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2$, $s^2 = S_{xx}/(n-1)$ et $s = \sqrt{s^2}$. Le diviseur $n - 1$ (correction de Bessel) donne $n - 1$ degrés de liberté : les $n$ écarts sommant à 0, $n - 1$ suffisent à fixer le dernier. La moyenne $\bar{x}$ étant calculée sur les mêmes données, elle les « colle » et réduit artificiellement la variabilité.

**En Data analysis (Thanos)**, [[6 - T-Test|Cours 6 - T-Test]] illustre les degrés de liberté : pour 3 observations de moyenne imposée, les deux premières valeurs sont libres et la troisième est forcée. L'écart-type $s$ y sert à l'erreur standard $s/\sqrt{n}$ du [[Test t]].

**Compléments (hors du cours)** :
- **Biais** : pour des observations indépendantes de variance $\sigma^2$, $E(S^2) = \sigma^2$ : $S^2$ est sans biais, alors que $\frac{1}{n}\sum (X_i - \bar X)^2$ a pour espérance $\frac{n-1}{n}\sigma^2$. L'écart-type $S$ reste légèrement biaisé ($E(S) < \sigma$). La variance s'exprime dans l'unité des données au carré, $s$ dans l'unité des données.
- **Inégalité de Bienaymé-Tchebychev** appliquée aux données : au moins $1 - 1/k^2$ des valeurs sont à moins de $k$ écarts-types de la moyenne (75 % pour $k = 2$, environ 89 % pour $k = 3$), quelle que soit la distribution. **Règle empirique** pour une distribution en cloche : environ 68 %, 95 % et 99,7 % des valeurs à moins de 1, 2 et 3 écarts-types ([[Loi normale]]).
- **Exemple chiffré** (dix mesures du Chp2) : $\bar x = 2{,}47$, $S_{xx} = 0{,}521$, $s^2 \approx 0{,}0579$, $s \approx 0{,}241$ ([[2 - Descriptive statistics]]).

**Degrés de liberté (complément, hors du cours)** : c'est le paramètre $\nu$ des lois $\chi^2_\nu$, $t_\nu$ (et $F$). Il compte le nombre de termes indépendants qui entrent dans une statistique, moins le nombre de contraintes imposées par les paramètres estimés. Les $n$ écarts $X_i - \bar X$ vérifient $\sum (X_i - \bar X) = 0$, donc seuls $n - 1$ sont libres. D'où, pour un échantillon gaussien, $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$, alors qu'avec $\mu$ connu $\sum (X_i - \mu)^2/\sigma^2 \sim \chi^2_n$ ([[Loi du khi-deux]]) ; c'est aussi pourquoi $S^2$ divise par $n - 1$. Le théorème de Gosset donne $(\bar X - \mu)/(S/\sqrt n) \sim t_{n-1}$ ([[Loi de Student]]). Plus $\nu$ est grand, plus $t_\nu$ est proche de $N(0, 1)$ et plus $\chi^2_\nu$ est symétrique ([[4 - Inferential statistics 3]]).

**Population finie** : $\mu = \sum x_i/N$, $\sigma^2 = \sum (x_i - \mu)^2/N$. Pour une population infinie, ce sont l'espérance et la variance de la variable ([[Espérance et variance]]). L'aide-mémoire de Statistics ([[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]) rappelle moyenne et variance de population et d'échantillon.

Voir aussi : [[Moyenne empirique]], [[Quartiles et valeurs aberrantes]], [[Estimateur]], [[Loi du khi-deux]], [[Loi de Student]], [[Test t]], [[Loi normale]]

Résumés : [[2 - Descriptive statistics]], [[6 - T-Test]], [[0 - proba&stats utilitaire]], [[4 - Inferential statistics 3]]
