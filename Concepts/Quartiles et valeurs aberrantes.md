---
type: concept
aliases: [quartile, quartiles, écart interquartile, interquartile range, iqr, IQR, valeur aberrante, outlier, outliers, boîte à moustaches, box plot, boxplot, percentile d'un échantillon]
matieres: [Statistics]
sources: ["[[Chp2 - Descriptive statistics]]"]
maj: 2026-11-05
---

**Quartiles** : $q_1$ est la médiane de la moitié inférieure des données triées, $q_3$ celle de la moitié supérieure (la médiane est dans les deux moitiés si $n$ est impair). **Écart interquartile** : $\mathrm{iqr} = q_3 - q_1$, résistant aux valeurs aberrantes.

**Valeur aberrante** : $x < q_1 - 1{,}5\,\mathrm{iqr}$ ou $x > q_3 + 1{,}5\,\mathrm{iqr}$ ; extrême au-delà de $3\,\mathrm{iqr}$ d'un quartile, modérée sinon.

**Boîte à moustaches** : rectangle de $q_1$ à $q_3$, trait à la médiane, valeurs aberrantes marquées, moustaches jusqu'aux observations extrêmes non aberrantes.

**Percentile** : $x_p$ avec au moins $100p\,\%$ des données en dessous ou égales, et au moins $100(1-p)\,\%$ au-dessus ou égales. La valeur ordonnée $x_{(i)}$ est celle de $p = (i - 1/2)/n$.

Liens : [[Variance et écart-type d'échantillon]], [[Fonction de répartition]]

Résumé : [[Chp2 - Descriptive statistics (résumé)]]
