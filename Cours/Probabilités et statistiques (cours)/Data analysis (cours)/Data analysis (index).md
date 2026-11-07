---
type: matiere
tags:
  - year3
sources:
  - "[[1 - Data analysis (résumé)|Cours 1 (Data analysis)]]"
  - "[[2 - Introduction statistics (résumé)|Cours 2 - Introduction statistics]]"
  - "[[3 - Paradoxe de Simpson (résumé)|Cours 3 - Paradoxe de Simpson]]"
  - "[[4 - Estimation (résumé)|Cours 4 - Estimation]]"
  - "[[5 - Hypothesis Testing (résumé)|Cours 5 - Hypothesis Testing]]"
  - "[[6 - T-Test (résumé)|Cours 6 - T-Test]]"
  - "[[7 - Z-Test (résumé)|Cours 7 - Z-Test]]"
  - "[[8 - Chi²-Test (résumé)|Cours 8 - Chi²-Test]]"
  - "[[9 - Covariance and Correlation (résumé)|Cours 9 - Covariance and Correlation]]"
  - "[[10 - linear regression (résumé)|Cours 10 - linear regression]]"
  - "[[11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11 - Multiple Linear Regression and F-statistic]]"
  - "[[12 - ANOVA and F-statistic (résumé)|Cours 12 - ANOVA and F-statistic]]"
  - "[[13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]"
  - "[[13 - PCA in R (résumé)|Cours 13 - PCA in R]]"
  - "[[14 - functions in RStudio (résumé)|Summary functions in RStudio]]"
maj: 2026-11-06
---

Analyse de données avec R : rappels de statistique, tests d'hypothèse, corrélation, régression simple et multiple, ANOVA et analyse en composantes principales. Les 15 notes sont à intégrer ; 14 résumés sont écrits (voir plus bas pour la quinzième).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - Data analysis (résumé)\|Cours 1]] | R : structures, fonctions, opérateurs | [[1 - Data analysis (résumé)\|Résumé]] |
| [[2 - Introduction statistics (résumé)\|Cours 2 - Introduction statistics]] | Descriptif et inférentiel, niveaux de mesure | [[2 - Introduction statistics (résumé)\|Résumé]] |
| [[3 - Paradoxe de Simpson (résumé)\|Cours 3 - Paradoxe de Simpson]] | Variable cachée | [[3 - Paradoxe de Simpson (résumé)\|Résumé]] |
| [[4 - Estimation (résumé)\|Cours 4 - Estimation]] | Intervalle de confiance | [[4 - Estimation (résumé)\|Résumé]] |
| [[5 - Hypothesis Testing (résumé)\|Cours 5 - Hypothesis Testing]] | Hypothèses, erreurs, procédure | [[5 - Hypothesis Testing (résumé)\|Résumé]] |
| [[6 - T-Test (résumé)\|Cours 6 - T-Test]] | Loi de Student, test t | [[6 - T-Test (résumé)\|Résumé]] |
| [[7 - Z-Test (résumé)\|Cours 7 - Z-Test]] | Tests Z, proportions | [[7 - Z-Test (résumé)\|Résumé]] |
| [[8 - Chi²-Test (résumé)\|Cours 8 - Chi²-Test]] | χ², variance, indépendance | [[8 - Chi²-Test (résumé)\|Résumé]] |
| [[9 - Covariance and Correlation (résumé)\|Cours 9 - Covariance and Correlation]] | Covariance, Pearson, Spearman, Kendall | [[9 - Covariance and Correlation (résumé)\|Résumé]] |
| [[10 - linear regression (résumé)\|Cours 10 - linear regression]] | Régression simple, résidus | [[10 - linear regression (résumé)\|Résumé]] |
| [[11 - Multiple Linear Regression and F-statistic (résumé)\|Cours 11 - Multiple Linear Regression and F-statistic]] | Prédiction, régression multiple, F | [[11 - Multiple Linear Regression and F-statistic (résumé)\|Résumé]] |
| [[12 - ANOVA and F-statistic (résumé)\|Cours 12 - ANOVA and F-statistic]] | ANOVA | [[12 - ANOVA and F-statistic (résumé)\|Résumé]] |
| [[13 - Principal Components Analysis (résumé)\|Cours 13 - Principal Components Analysis]] | ACP | [[13 - Principal Components Analysis (résumé)\|Résumé]] |
| [[13 - PCA in R (résumé)\|Cours 13 - PCA in R]] | ACP en R | [[13 - PCA in R (résumé)\|Résumé]] |
| [[14 - functions in RStudio (résumé)\|Summary functions in RStudio]] | Aide-mémoire R | [[14 - functions in RStudio (résumé)\|Résumé]] |

## Concepts

- **R (cours 1 et aide-mémoire)** : [[Langage R]], [[Module, paquet, bibliothèque et framework]], [[Bibliothèque ggplot2]], [[Data frame]], [[Facteur (variable catégorielle)]], [[Variable indicatrice]], [[Formule de modèle en R]], [[Fonction de répartition empirique]], [[Transposée]]
- **Introduction à la statistique (cours 2)** : [[Statistique descriptive]], [[Statistique inférentielle]], [[Population et échantillon]], [[Paramètre et statistique]], [[Type de variable statistique]], [[Mesures de tendance centrale]], [[Variance et écart-type d'échantillon]], [[Coefficient de variation]], [[Quartiles et valeurs aberrantes]], [[Quantile]], [[Histogramme]], [[Diagramme tige et feuilles]], [[Forme d'une distribution]]
- **Variable cachée (cours 3)** : [[Paradoxe de Simpson]], [[Corrélation et causalité]]
- **Estimation (cours 4)** : [[Échantillonnage]], [[Erreur d'échantillonnage]], [[Estimateur]], [[Intervalle de confiance]], [[Loi normale]], [[Approximation normale]], [[Loi binomiale]]
- **Tests d'hypothèse (cours 5)** : [[Test d'hypothèse]], [[Statistique de test]], [[Seuil de signification]], [[Valeur critique]], [[P-value]], [[Test unilatéral et bilatéral]], [[Erreur de type I et de type II]], [[Vraisemblance]]
- **Tests t, Z et χ² (cours 6 à 8)** : [[Loi de Student]], [[Test t]], [[Test Z]], [[Échantillons appariés et indépendants]], [[Test binomial]], [[Loi du khi-deux]], [[Fonction Gamma]], [[Test du χ²]], [[Tableau de contingence]]
- **Tests non paramétriques (organigramme du cours 7)** : [[Test paramétrique et non paramétrique]], [[Test du signe]], [[Test de Wilcoxon]], [[Test de Mann-Whitney]], [[Test de Kolmogorov-Smirnov]], [[Test de McNemar]], [[Test de la médiane]], [[Test des runs]]
- **Covariance et corrélation (cours 9)** : [[Modèle déterministe et probabiliste]], [[Espérance et variance]], [[Loi conjointe]], [[Covariance et corrélation]], [[Coefficient de corrélation de Spearman]], [[Tau de Kendall]], [[Coefficient de détermination]]
- **Régression (cours 10 et 11)** : [[Régression linéaire]], [[Moindres carrés]], [[Extremum local d'une fonction de deux variables]], [[Résidu (régression)]], [[Homoscédasticité]], [[Diagramme de probabilité]], [[Quatuor d'Anscombe]], [[Erreur standard de la régression]], [[Test de la pente]], [[Somme des carrés (SST, SSR, SSE)]], [[Statistique F]], [[Intervalle de prédiction]]
- **ANOVA (cours 12)** : [[ANOVA]], [[Carré moyen]]
- **Analyse en composantes principales (cours 13)** : [[Analyse en composantes principales]], [[Réduction de dimension]], [[Surapprentissage]], [[Centrage et réduction]], [[Matrice de covariance]], [[Matrice symétrique]], [[Valeur propre]], [[Vecteur propre]], [[Matrice orthogonale]], [[Projection orthogonale]], [[Théorème de Pythagore]], [[Trace d'une matrice]], [[Décomposition en valeurs singulières]], [[Loadings et scores (ACP)]], [[Cercle des corrélations]]

## À revoir en priorité avant un examen

- [[11 - Multiple Linear Regression and F-statistic (résumé)]] : une diapositive écrit F à l'envers (non expliquée sur expliquée), et l'intervalle de prédiction de l'exemple a ses bornes inversées.
- [[12 - ANOVA and F-statistic (résumé)]] : « F = 22,59, p > 0,05 » est faux (rejet), et les sommes des carrés affichées ne correspondent pas aux données.
- [[7 - Z-Test (résumé)]] : des mesures avant et après traitement relèvent du test $t$ apparié, pas d'un « two-sample t-test ».
- [[8 - Chi²-Test (résumé)]] : l'introduction de la loi du χ² confond $n$ et $n-1$ degrés ; le tableau récapitulatif des intervalles a un signe faux ; la colonne 0,005 de la table est douteuse.

## Liens avec les autres matières

- **[[Bilinear Algebra (index)]]** : la régression est un problème de [[Moindres carrés]] ([[Projection orthogonale]]), et l'ACP repose sur la [[Valeur propre]], le [[Vecteur propre]], la [[Matrice symétrique]] et la [[Décomposition en valeurs singulières]].
- **[[Analyse dans Rn (index)]]** : la minimisation de la somme des carrés (Cours 10) emploie les dérivées partielles et un critère de minimum local du calcul différentiel (voir [[Dérivée partielle]]).
- **[[Data mining (index)]]** : arbres de décision, k-means et validation d'un classifieur utilisent les mêmes outils d'évaluation d'erreur ; l'ACP et la régression y servent à explorer et prédire.
- **Probability** et **Statistics** (Year 2) : base des lois et des tests utilisés ici.
- **[[Statistics (index)]]** : beaucoup de concepts sont communs, notamment [[Estimateur]], [[Intervalle de confiance]], [[Loi de Student]], [[Loi du khi-deux]], [[Test t]], [[Test Z]], [[Test du χ²]] et la statistique descriptive ([[Histogramme]], [[Quartiles et valeurs aberrantes]]).
- **[[Probability (index)]]** : [[Espérance et variance]], [[Loi conjointe]], [[Loi normale]] et [[Covariance et corrélation]] y sont définies.
- **[[Data mining (index)]]** : l'[[Erreur de type I et de type II]] revient dans l'introduction au data mining.
