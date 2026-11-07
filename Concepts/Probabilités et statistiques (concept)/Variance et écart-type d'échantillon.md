---
type: concept
tags: [year3]
aliases: [sample variance, sample standard deviation, variance d'échantillon, écart-type d'échantillon, correction de Bessel, degrés de liberté, degrees of freedom, moyenne d'échantillon, médiane d'échantillon, sample median]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[chp 2 - Descriptive statistics (résumé)|Chp2 - Descriptive statistics]]", "[[Séance 6 - T-Test (résumé)|Cours 6 - T-Test]]"]
maj: 2026-11-06
---

**Moyenne** $\bar{x} = \sum x_i/n$ (voir [[Moyenne empirique]]). **Médiane** : valeur d'ordre $(n+1)/2$ ($n$ impair), ou moyenne des valeurs d'ordre $n/2$ et $n/2 + 1$ ($n$ pair). La somme des écarts à la moyenne vaut 0.

**Variance et écart-type d'échantillon** : avec $S_{xx} = \sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2$, $s^2 = S_{xx}/(n-1)$ et $s = \sqrt{s^2}$. Le diviseur $n - 1$ (correction de Bessel) donne $n - 1$ degrés de liberté : les $n$ écarts sommant à 0, $n - 1$ suffisent à fixer le dernier. La moyenne $\bar{x}$ étant calculée sur les mêmes données, elle les « colle » et réduit artificiellement la variabilité.

**En Data analysis (Thanos)**, [[Séance 6 - T-Test (résumé)|Cours 6 - T-Test]] illustre les degrés de liberté : pour 3 observations de moyenne imposée, les deux premières valeurs sont libres et la troisième est forcée. L'écart-type $s$ y sert à l'erreur standard $s/\sqrt{n}$ du [[Test t]].

**Population finie** : $\mu = \sum x_i/N$, $\sigma^2 = \sum (x_i - \mu)^2/N$. Pour une population infinie, ce sont l'espérance et la variance de la variable ([[Espérance et variance]]). L'aide-mémoire de Statistics ([[probabilité statistiques utilitaire (résumé)|probabilité statistiques utilitaire]]) rappelle moyenne et variance de population et d'échantillon.

Voir aussi : [[Moyenne empirique]], [[Quartiles et valeurs aberrantes]], [[Estimateur]], [[Loi du khi-deux]], [[Test t]]

Résumés : [[chp 2 - Descriptive statistics (résumé)]], [[Séance 6 - T-Test (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
