---
type: concept
tags: [year3]
aliases: [quartile, quartiles, écart interquartile, interquartile range, iqr, IQR, valeur aberrante, outlier, outliers, boîte à moustaches, box plot, boxplot, percentile d'un échantillon]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[Chp2 - Descriptive statistics (résumé)|Chp2 - Descriptive statistics]]", "[[Séance 4 - Estimation (résumé)|Cours 4 - Estimation]]"]
maj: 2026-11-06
---

**Quartiles** : $q_1$ est la médiane de la moitié inférieure des données triées, $q_3$ celle de la moitié supérieure (la médiane est dans les deux moitiés si $n$ est impair). **Écart interquartile** : $\mathrm{iqr} = q_3 - q_1$, résistant aux valeurs aberrantes.

**Valeur aberrante** : $x < q_1 - 1{,}5\,\mathrm{iqr}$ ou $x > q_3 + 1{,}5\,\mathrm{iqr}$ ; extrême au-delà de $3\,\mathrm{iqr}$ d'un quartile, modérée sinon.

**Boîte à moustaches** : rectangle de $q_1$ à $q_3$, trait à la médiane, valeurs aberrantes marquées, moustaches jusqu'aux observations extrêmes non aberrantes.

**Percentile** : $x_p$ avec au moins $100p\,\%$ des données en dessous ou égales, et au moins $100(1-p)\,\%$ au-dessus ou égales. La valeur ordonnée $x_{(i)}$ est celle de $p = (i - 1/2)/n$. Pour une loi, voir [[Quantile]].

**En Data analysis (Thanos)**, [[Séance 4 - Estimation (résumé)|Cours 4 - Estimation]] définit le percentile comme la valeur sous laquelle se trouve un certain pourcentage de la population, et donne pour une loi normale $X = \mu + Z\sigma$. L'aide-mémoire R ([[Summary functions in RStudio (résumé)]]) cite `quantile` et `boxplot`, et la fiche [[probabilité statistiques utilitaire (résumé)|probabilité statistiques utilitaire]] rappelle l'écart interquartile.

Voir aussi : [[Statistique descriptive]], [[Quantile]], [[Variance et écart-type d'échantillon]], [[Fonction de répartition]]

## À vérifier

- [[Chp2 - Descriptive statistics (résumé)|Chp2 - Descriptive statistics]] donne deux définitions des quartiles : médianes des moitiés inférieure et supérieure, puis $x_{0.25}$ et $x_{0.75}$ comme percentiles.
- La phrase sur le quartile supérieur ($x_{0.75}$) est coupée dans le cours.

Résumés : [[Chp2 - Descriptive statistics (résumé)]], [[Séance 4 - Estimation (résumé)]], [[Summary functions in RStudio (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
