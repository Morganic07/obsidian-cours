---
type: matiere
sources: ["[[Cours/Year 3/Data analysis (Thanos)/Cours 1|Cours 1 (Data analysis)]]", "[[Cours 2 - Introduction statistics]]", "[[Cours 3 - Paradoxe de Simpson]]", "[[Cours 4 - Estimation]]", "[[Cours 5 - Hypothesis Testing]]", "[[Cours 6 - T-Test]]", "[[Cours 7 - Z-Test]]", "[[Cours 8 - Chi²-Test]]", "[[Cours 9 - Covariance and Correlation]]", "[[Cours 10 - linear regression]]", "[[Cours 11 - Multiple Linear Regression and F-statistic]]", "[[Cours 12 - ANOVA and F-statistic]]", "[[Cours 13 - Principal Components Analysis]]", "[[Cours 13 - PCA in R]]", "[[Summary functions in RStudio]]"]
maj: 2026-11-05
---

Analyse de données avec R : rappels de statistique, tests d'hypothèse, corrélation, régression simple et multiple, ANOVA et analyse en composantes principales. Les 15 notes sont à intégrer ; 14 résumés sont écrits (voir plus bas pour la quinzième).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Cours/Year 3/Data analysis (Thanos)/Cours 1\|Cours 1]] | R : structures, fonctions, opérateurs | [[Sources/Year 3/Data analysis (Thanos)/Cours 1 (résumé)\|Résumé]] |
| [[Cours 2 - Introduction statistics]] | Descriptif et inférentiel, niveaux de mesure | [[Cours 2 - Introduction statistics (résumé)\|Résumé]] |
| [[Cours 3 - Paradoxe de Simpson]] | Variable cachée | [[Cours 3 - Paradoxe de Simpson (résumé)\|Résumé]] |
| [[Cours 4 - Estimation]] | Intervalle de confiance | [[Cours 4 - Estimation (résumé)\|Résumé]] |
| [[Cours 5 - Hypothesis Testing]] | Hypothèses, erreurs, procédure | [[Cours 5 - Hypothesis Testing (résumé)\|Résumé]] |
| [[Cours 6 - T-Test]] | Loi de Student, test t | [[Cours 6 - T-Test (résumé)\|Résumé]] |
| [[Cours 7 - Z-Test]] | Tests Z, proportions | [[Cours 7 - Z-Test (résumé)\|Résumé]] |
| [[Cours 8 - Chi²-Test]] | χ², variance, indépendance | [[Cours 8 - Chi²-Test (résumé)\|Résumé]] |
| [[Cours 9 - Covariance and Correlation]] | Covariance, Pearson, Spearman, Kendall | [[Cours 9 - Covariance and Correlation (résumé)\|Résumé]] |
| [[Cours 10 - linear regression]] | Régression simple, résidus | [[Cours 10 - linear regression (résumé)\|Résumé]] |
| [[Cours 11 - Multiple Linear Regression and F-statistic]] | Prédiction, régression multiple, F | [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)\|Résumé]] |
| [[Cours 12 - ANOVA and F-statistic]] | ANOVA | [[Cours 12 - ANOVA and F-statistic (résumé)\|Résumé]] |
| [[Cours 13 - Principal Components Analysis]] | ACP | [[Cours 13 - Principal Components Analysis (résumé)\|Résumé]] |
| [[Cours 13 - PCA in R]] | ACP en R | [[Cours 13 - PCA in R (résumé)\|Résumé]] |
| [[Summary functions in RStudio]] | Aide-mémoire R | [[Summary functions in RStudio (résumé)\|Résumé]] |

## Concepts

- **Tests** : [[Test du χ²]], [[Statistique F]], [[ANOVA]]
- **Régression** : [[Régression linéaire]], [[Moindres carrés]], [[Intervalle de prédiction]]
- **Réduction de dimension** : [[Analyse en composantes principales]]
- **Méthode** : [[Paradoxe de Simpson]]

Les notions de base (test d'hypothèse, intervalle de confiance, loi normale, loi de Student, covariance, corrélation) n'ont pas de concept propre ici : elles dépendent des matières de probabilités et de statistique.

## À revoir en priorité avant un examen

- [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)]] : une diapositive écrit F à l'envers (non expliquée sur expliquée), et l'intervalle de prédiction de l'exemple a ses bornes inversées.
- [[Cours 12 - ANOVA and F-statistic (résumé)]] : « F = 22,59, p > 0,05 » est faux (rejet), et les sommes des carrés affichées ne correspondent pas aux données.
- [[Cours 7 - Z-Test (résumé)]] : des mesures avant et après traitement relèvent du test $t$ apparié, pas d'un « two-sample t-test ».
- [[Cours 8 - Chi²-Test (résumé)]] : l'introduction de la loi du χ² confond $n$ et $n-1$ degrés ; le tableau récapitulatif des intervalles a un signe faux ; la colonne 0,005 de la table est douteuse.

## Liens avec les autres matières

- **[[Year 2 - Bilinear Algebra]]** : la régression est un problème de [[Moindres carrés]] ([[Projection orthogonale]]), et l'ACP repose sur la [[Valeur propre]], le [[Vecteur propre]], la [[Matrice symétrique]] et la [[Décomposition en valeurs singulières]].
- **[[Year 2 - Analyse dans Rn]]** : la minimisation de la somme des carrés (Cours 10) emploie les dérivées partielles et un critère de minimum local du calcul différentiel (voir [[Dérivée partielle]]).
- **[[Year 4 - data mining]]** : arbres de décision, k-means et validation d'un classifieur utilisent les mêmes outils d'évaluation d'erreur ; l'ACP et la régression y servent à explorer et prédire.
- **Probability** et **Statistics** (Year 2) : base des lois et des tests utilisés ici.
