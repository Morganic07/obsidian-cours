---
type: concept
tags: [year3]
aliases: [p-valeur, valeur p, p value, p-values]
matieres: [Data analysis (Thanos)]
sources: ["[[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]", "[[6 - T-Test|Cours 6 - T-Test]]"]
maj: 2026-11-08
---

Probabilité d'obtenir les résultats observés, ou des résultats plus extrêmes, si $H_0$ est vraie. On rejette $H_0$ si elle est inférieure au [[Seuil de signification|seuil α]] ([[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]).

Pour une même valeur de $t$, elle dépend des degrés de liberté : $P(|X| \ge 2{,}05)$ vaut 0,289 à df = 1 et 0,043 à df = 100 ([[6 - T-Test|Cours 6 - T-Test]]).

Dans l'exemple d'ANOVA de [[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]], $F(2, 12) \approx 17{,}92$ dépasse la valeur critique 3,89 : $p < 0{,}05$, et l'on rejette $H_0$. [[Erreurs du cours#^e-p-value|✎]]

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Statistique de test]], [[Seuil de signification]], [[Vraisemblance]], [[Loi de Student]].

Résumés : [[5 - Hypothesis Testing]], [[6 - T-Test]], [[10 - linear regression]], [[11 - Multiple Linear Regression and F-statistic]], [[12 - ANOVA and F-statistic]]
