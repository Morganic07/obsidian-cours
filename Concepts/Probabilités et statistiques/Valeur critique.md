---
type: concept
tags: [year3]
aliases: [critical value, valeurs critiques, région de rejet, rejection region, zone de rejet, region of rejection]
sources: ["[[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]", "[[6 - T-Test|Cours 6 - T-Test]]"]
maj: 2026-11-08
---

Seuil à partir duquel on rejette $H_0$ dans un test. La zone de rejet correspond toujours à $H_1$, et le cours conseille de dessiner la courbe pour la situer.

Notations : $\chi^2_{\alpha,\nu}$ et $t_{\alpha,\nu}$ désignent la valeur qui laisse une aire $\alpha$ à sa droite. Exemples du cours : $\pm 2{,}1315$ pour $t_{15}$ à 5 % (bilatéral), $3{,}841$ pour le $\chi^2$ à df = 1.

Pour un test F (régression, [[ANOVA]]), on rejette $H_0$ quand $F$ dépasse la valeur critique, ce qui équivaut à une p-value inférieure à $\alpha$ ; sinon, on ne la rejette pas ([[Statistique F]]). [[Erreurs du cours#^e-valeur-critique|✎]] Dans la table du $\chi^2$ de [[8 - Chi²-Test|Cours 8 - Chi²-Test]], la colonne 0,005 (aire à gauche) vaut 0,0100 pour df = 2, 0,072 pour df = 3, 2,16 pour df = 10 et 13,79 pour df = 30 ([[Loi du khi-deux]]). [[Erreurs du cours#^e-valeur-critique|✎]]

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Seuil de signification]], [[Test unilatéral et bilatéral]], [[Quantile]].

Résumés : [[5 - Hypothesis Testing]], [[6 - T-Test]], [[8 - Chi²-Test]], [[10 - linear regression]], [[12 - ANOVA and F-statistic]], [[4 - Inferential statistics 3]]
