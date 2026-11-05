---
type: concept
aliases: [sample variance, sample standard deviation, variance d'échantillon, écart-type d'échantillon, correction de Bessel, degrés de liberté, degrees of freedom, moyenne d'échantillon, sample mean, médiane d'échantillon, sample median]
matieres: [Statistics]
sources: ["[[Chp2 - Descriptive statistics]]"]
maj: 2026-11-05
---

**Moyenne** $\bar{x} = \sum x_i/n$. **Médiane** : valeur d'ordre $(n+1)/2$ ($n$ impair), ou moyenne des valeurs d'ordre $n/2$ et $n/2 + 1$ ($n$ pair). La somme des écarts à la moyenne vaut 0.

**Variance et écart-type d'échantillon** : avec $S_{xx} = \sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2$, $s^2 = S_{xx}/(n-1)$ et $s = \sqrt{s^2}$. Le diviseur $n - 1$ (correction de Bessel) donne $n - 1$ degrés de liberté : les $n$ écarts sommant à 0, $n - 1$ suffisent à fixer le dernier. La moyenne $\bar{x}$ étant calculée sur les mêmes données, elle les « colle » et réduit artificiellement la variabilité.

**Population finie** : $\mu = \sum x_i/N$, $\sigma^2 = \sum (x_i - \mu)^2/N$. Pour une population infinie, ce sont l'espérance et la variance de la variable ([[Espérance et variance]]).

Liens : [[Quartiles et valeurs aberrantes]], [[Estimateur]]

Résumé : [[Chp2 - Descriptive statistics (résumé)]]
