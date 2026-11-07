---
type: concept
tags: [year3]
aliases: [t-test, t test, test de Student, test t de Student, two-sample t-test, test t à deux échantillons, paired t-test, paired t test, test t apparié, variance poolée, pooled variance, two-group t test]
matieres: [Data analysis (Thanos), Statistics]
sources: ["[[6 - T-Test|Cours 6 - T-Test]]", "[[7 - Z-Test|Cours 7 - Z-Test]]"]
maj: 2026-11-07
---

Remplace le [[Test Z]] quand $\sigma$ est inconnu et que l'échantillon est petit ([[6 - T-Test|Cours 6 - T-Test]]). La statistique suit une [[Loi de Student]].

- **Un échantillon** : $t_{n-1} = \dfrac{\bar X - \mu_0}{s/\sqrt n}$.
- **Deux échantillons indépendants**, populations normales : $t_{n_1+n_2-2} = \dfrac{\bar X_1 - \bar X_2}{\sqrt{s^2_{pooled}\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$, avec la variance poolée $s^2_{pooled} = \dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$.

Exemple du cours : $t = -2{,}50$ comparé à $\pm 2{,}1315$, donc rejet de $H_0$.

Le test t compare deux moyennes ; l'[[ANOVA]] en compare plus de deux ([[12 - ANOVA and F-statistic]]). Pour des données appariées, l'organigramme de [[7 - Z-Test|Cours 7 - Z-Test]] donne le test t apparié ([[Échantillons appariés et indépendants]]).

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Loi de Student]], [[Test Z]], [[Échantillons appariés et indépendants]], [[ANOVA]], [[Test de la pente]].

## Erreurs du cours

- [[7 - Z-Test|Cours 7 - Z-Test]] écrit, pour des mesures avant/après sur les mêmes patients, « An appropriate test to use here would be a two-sample t-test » ; il faut le test t apparié (paired t test), que donne l'organigramme du même cours.

Résumés : [[6 - T-Test]], [[7 - Z-Test]], [[12 - ANOVA and F-statistic]], [[0 - proba&stats utilitaire]]
