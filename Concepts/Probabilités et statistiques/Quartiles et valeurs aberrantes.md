---
type: concept
tags: [year3]
aliases: [quartile, quartiles, écart interquartile, interquartile range, iqr, IQR, valeur aberrante, outlier, outliers, boîte à moustaches, box plot, boxplot, percentile d'un échantillon, résumé en cinq nombres, five-number summary]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[2 - Descriptive statistics|Chp2 - Descriptive statistics]]", "[[4 - Estimation|Cours 4 - Estimation]]"]
maj: 2026-11-08
---

**Quartiles** : $q_1$ est la médiane de la moitié inférieure des données triées, $q_3$ celle de la moitié supérieure (la médiane est dans les deux moitiés si $n$ est impair). **Écart interquartile** : $\mathrm{iqr} = q_3 - q_1$, résistant aux valeurs aberrantes.

**Valeur aberrante** : $x < q_1 - 1{,}5\,\mathrm{iqr}$ ou $x > q_3 + 1{,}5\,\mathrm{iqr}$ ; extrême au-delà de $3\,\mathrm{iqr}$ d'un quartile, modérée sinon.

**Boîte à moustaches** : rectangle de $q_1$ à $q_3$, trait à la médiane, valeurs aberrantes marquées, moustaches jusqu'aux observations extrêmes non aberrantes.

**Compléments (hors du cours)** :
- **Résumé en cinq nombres** (*five-number summary*) : minimum, $q_1$, médiane, $q_3$, maximum, c'est-à-dire ce que dessine la boîte à moustaches. Celle-ci sert surtout à comparer plusieurs distributions côte à côte.
- Pour une [[Loi normale]], $q_1 - 1{,}5\,\mathrm{iqr}$ et $q_3 + 1{,}5\,\mathrm{iqr}$ tombent à environ $\pm 2{,}7\sigma$ de la moyenne : environ 0,7 % des valeurs sont signalées comme aberrantes.
- L'iqr étant résistant, on l'associe à la médiane pour une distribution asymétrique ; pour une distribution à peu près symétrique, on garde moyenne et écart-type ([[Forme d'une distribution]]).

**Percentile** : $x_p$ avec au moins $100p\,\%$ des données en dessous ou égales, et au moins $100(1-p)\,\%$ au-dessus ou égales. La valeur ordonnée $x_{(i)}$ est celle de $p = (i - 1/2)/n$. Le même chapitre présente aussi les quartiles comme percentiles : quartile inférieur $x_{0.25}$, quartile supérieur $x_{0.75}$ (la phrase du cours sur $x_{0.75}$ s'arrête en cours de route). Pour une loi, voir [[Quantile]].

**En Data analysis (Thanos)**, [[4 - Estimation|Cours 4 - Estimation]] définit le percentile comme la valeur sous laquelle se trouve un certain pourcentage de la population, et donne pour une loi normale $X = \mu + Z\sigma$. L'aide-mémoire R ([[14 - functions in RStudio]]) cite `quantile` et `boxplot`, et la fiche [[0 - proba&stats utilitaire|probabilité statistiques utilitaire]] rappelle l'écart interquartile.

Voir aussi : [[Statistique descriptive]], [[Quantile]], [[Variance et écart-type d'échantillon]], [[Fonction de répartition]]

Résumés : [[2 - Descriptive statistics]], [[4 - Estimation]], [[14 - functions in RStudio]], [[0 - proba&stats utilitaire]]
