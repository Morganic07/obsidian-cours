---
type: concept
tags: [year3]
aliases: [critical value, valeurs critiques, région de rejet, rejection region, zone de rejet, region of rejection]
sources: ["[[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]", "[[6 - T-Test|Cours 6 - T-Test]]"]
maj: 2026-11-07
---

Seuil à partir duquel on rejette $H_0$ dans un test. La zone de rejet correspond toujours à $H_1$, et le cours conseille de dessiner la courbe pour la situer.

Notations : $\chi^2_{\alpha,\nu}$ et $t_{\alpha,\nu}$ désignent la valeur qui laisse une aire $\alpha$ à sa droite. Exemples du cours : $\pm 2{,}1315$ pour $t_{15}$ à 5 % (bilatéral), $3{,}841$ pour le $\chi^2$ à df = 1.

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Seuil de signification]], [[Test unilatéral et bilatéral]], [[Quantile]].

## Erreurs du cours

- [[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]] et [[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]] (vérifié sur l'image) écrivent « You should not reject the null if your critical f value is smaller than your F-value, unless you also have a small p-value » ; il faut : on rejette $H_0$ quand la statistique dépasse la valeur critique. Voir [[Statistique F]].
- [[8 - Chi²-Test|Cours 8 - Chi²-Test]] : la colonne 0.005 de l'extrait de table du $\chi^2$ est fausse à partir de df = 2 (vérifié sur l'image). Voir [[Loi du khi-deux]].

Résumés : [[5 - Hypothesis Testing]], [[6 - T-Test]], [[8 - Chi²-Test]], [[10 - linear regression]], [[12 - ANOVA and F-statistic]], [[4 - Inferential statistics 3]]
