---
type: concept
tags: [year3]
aliases: [coefficient of determination, R², R carré, R-squared, adjusted R², R² ajusté]
matieres: [Data analysis (Thanos)]
sources: ["[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]", "[[10 - linear regression|Cours 10 - linear regression]]", "[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-08
---

**Définition** (d'après [[9 - Covariance and Correlation]]) :

$$R^2 = r^2 = \frac{SS_{yy} - SSE}{SS_{yy}}$$

L'égalité $R^2 = r^2$ vaut en régression simple (complément, hors du cours). Proportion de la variation de $Y$ expliquée par $X$, comprise entre 0 et 1 : $r = 0{,}30$ donne 9 %, $r = 0{,}90$ donne 81 %.

$R^2$ dit combien est expliqué, la [[Statistique F]] dit si c'est significatif. Relation donnée par le cours : $R^2 = 1 - \left(1 + F\frac{p-1}{n-p}\right)^{-1}$.

## Compléments

- **Deux écritures** : comme $SST = SSR + SSE$ ([[Somme des carrés (SST, SSR, SSE)]]), $R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$ (notations de la séance 10, où $SS_{yy} = SST$) ; en séance 11, $R^2 = 1 - \frac{RSS}{TSS}$, avec $RSS = SSE$ et $TSS = SST$. [[Complément hors du cours|ⓘ]]
- **D'où vient la relation du cours** : $F = \frac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$, donc $F\frac{p-1}{n-p} = \frac{TSS - RSS}{RSS} = \frac{TSS}{RSS} - 1$. Ainsi $1 + F\frac{p-1}{n-p} = \frac{TSS}{RSS}$, dont l'inverse est $\frac{RSS}{TSS} = 1 - R^2$. Formule inverse : $F = \dfrac{R^2/(p-1)}{(1 - R^2)/(n-p)}$ ; à $R^2$ égal, $F$ croît avec $n$, si bien qu'un $R^2$ modeste peut être très significatif sur un grand échantillon. [[Complément hors du cours|ⓘ]]
- **$R^2$ ajusté** : $\bar{R}^2 = 1 - (1 - R^2)\dfrac{n-1}{n-p}$ ($p$ paramètres, constante comprise). Le $R^2$ augmente toujours (ou reste égal) quand on ajoute une variable, même sans rapport avec $y$ ; le $R^2$ ajusté pénalise le nombre de paramètres et peut baisser. Il sert à comparer des modèles de tailles différentes ; il peut être négatif, et n'est plus une proportion de variation expliquée. [[Complément hors du cours|ⓘ]]
- **Exemple des jouets** ($n = 5$, $p = 2$, séances 10 et 11) : $SST = 26 - \frac{10^2}{5} = 6$, $SSE = 1{,}1$, $SSR = 4{,}9$, d'où $R^2 = \frac{4{,}9}{6} \approx 0{,}82$ et $\bar{R}^2 = 1 - 0{,}183 \times \frac{4}{3} \approx 0{,}76$. [[Complément hors du cours|ⓘ]]
- **Ce que $R^2$ ne dit pas** : un $R^2$ élevé ne prouve ni que le modèle linéaire est adapté (voir [[Quatuor d'Anscombe]] et l'examen des [[Résidu (régression)|résidus]]), ni une relation de cause à effet ([[Corrélation et causalité]]). [[Complément hors du cours|ⓘ]]

Notion parente : [[Régression linéaire]]. Voir aussi : [[Covariance et corrélation]], [[Somme des carrés (SST, SSR, SSE)]], [[Statistique F]], [[Multicolinéarité]], [[Quatuor d'Anscombe]].

Résumés : [[9 - Covariance and Correlation]], [[10 - linear regression]], [[11 - Multiple Linear Regression and F-statistic]]
