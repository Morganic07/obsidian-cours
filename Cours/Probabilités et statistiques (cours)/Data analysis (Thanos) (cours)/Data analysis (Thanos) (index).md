---
type: matiere
tags:
  - year3
sources:
  - "[[Séance 1 - Data analysis (Thanos) (résumé)|Cours 1 (Data analysis)]]"
  - "[[Séance 2 - Introduction statistics (résumé)|Cours 2 - Introduction statistics]]"
  - "[[Séance 3 - Paradoxe de Simpson (résumé)|Cours 3 - Paradoxe de Simpson]]"
  - "[[Séance 4 - Estimation (résumé)|Cours 4 - Estimation]]"
  - "[[Séance 5 - Hypothesis Testing (résumé)|Cours 5 - Hypothesis Testing]]"
  - "[[Séance 6 - T-Test (résumé)|Cours 6 - T-Test]]"
  - "[[Séance 7 - Z-Test (résumé)|Cours 7 - Z-Test]]"
  - "[[Séance 8 - Chi²-Test (résumé)|Cours 8 - Chi²-Test]]"
  - "[[Séance 9 - Covariance and Correlation (résumé)|Cours 9 - Covariance and Correlation]]"
  - "[[Séance 10 - linear regression (résumé)|Cours 10 - linear regression]]"
  - "[[Séance 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11 - Multiple Linear Regression and F-statistic]]"
  - "[[Séance 12 - ANOVA and F-statistic (résumé)|Cours 12 - ANOVA and F-statistic]]"
  - "[[Séance 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]"
  - "[[Séance 13 - PCA in R (résumé)|Cours 13 - PCA in R]]"
  - "[[Summary functions in RStudio (résumé)|Summary functions in RStudio]]"
maj: 2026-11-06
---

Analyse de données avec R : rappels de statistique, tests d'hypothèse, corrélation, régression simple et multiple, ANOVA et analyse en composantes principales. Les 15 notes sont à intégrer ; 14 résumés sont écrits (voir plus bas pour la quinzième).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Séance 1 - Data analysis (Thanos) (résumé)\|Cours 1]] | R : structures, fonctions, opérateurs | [[Séance 1 - Data analysis (Thanos) (résumé)\|Résumé]] |
| [[Séance 2 - Introduction statistics (résumé)\|Cours 2 - Introduction statistics]] | Descriptif et inférentiel, niveaux de mesure | [[Séance 2 - Introduction statistics (résumé)\|Résumé]] |
| [[Séance 3 - Paradoxe de Simpson (résumé)\|Cours 3 - Paradoxe de Simpson]] | Variable cachée | [[Séance 3 - Paradoxe de Simpson (résumé)\|Résumé]] |
| [[Séance 4 - Estimation (résumé)\|Cours 4 - Estimation]] | Intervalle de confiance | [[Séance 4 - Estimation (résumé)\|Résumé]] |
| [[Séance 5 - Hypothesis Testing (résumé)\|Cours 5 - Hypothesis Testing]] | Hypothèses, erreurs, procédure | [[Séance 5 - Hypothesis Testing (résumé)\|Résumé]] |
| [[Séance 6 - T-Test (résumé)\|Cours 6 - T-Test]] | Loi de Student, test t | [[Séance 6 - T-Test (résumé)\|Résumé]] |
| [[Séance 7 - Z-Test (résumé)\|Cours 7 - Z-Test]] | Tests Z, proportions | [[Séance 7 - Z-Test (résumé)\|Résumé]] |
| [[Séance 8 - Chi²-Test (résumé)\|Cours 8 - Chi²-Test]] | χ², variance, indépendance | [[Séance 8 - Chi²-Test (résumé)\|Résumé]] |
| [[Séance 9 - Covariance and Correlation (résumé)\|Cours 9 - Covariance and Correlation]] | Covariance, Pearson, Spearman, Kendall | [[Séance 9 - Covariance and Correlation (résumé)\|Résumé]] |
| [[Séance 10 - linear regression (résumé)\|Cours 10 - linear regression]] | Régression simple, résidus | [[Séance 10 - linear regression (résumé)\|Résumé]] |
| [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)\|Cours 11 - Multiple Linear Regression and F-statistic]] | Prédiction, régression multiple, F | [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)\|Résumé]] |
| [[Séance 12 - ANOVA and F-statistic (résumé)\|Cours 12 - ANOVA and F-statistic]] | ANOVA | [[Séance 12 - ANOVA and F-statistic (résumé)\|Résumé]] |
| [[Séance 13 - Principal Components Analysis (résumé)\|Cours 13 - Principal Components Analysis]] | ACP | [[Séance 13 - Principal Components Analysis (résumé)\|Résumé]] |
| [[Séance 13 - PCA in R (résumé)\|Cours 13 - PCA in R]] | ACP en R | [[Séance 13 - PCA in R (résumé)\|Résumé]] |
| [[Summary functions in RStudio (résumé)\|Summary functions in RStudio]] | Aide-mémoire R | [[Summary functions in RStudio (résumé)\|Résumé]] |

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

- [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]] : une diapositive écrit F à l'envers (non expliquée sur expliquée), et l'intervalle de prédiction de l'exemple a ses bornes inversées.
- [[Séance 12 - ANOVA and F-statistic (résumé)]] : « F = 22,59, p > 0,05 » est faux (rejet), et les sommes des carrés affichées ne correspondent pas aux données.
- [[Séance 7 - Z-Test (résumé)]] : des mesures avant et après traitement relèvent du test $t$ apparié, pas d'un « two-sample t-test ».
- [[Séance 8 - Chi²-Test (résumé)]] : l'introduction de la loi du χ² confond $n$ et $n-1$ degrés ; le tableau récapitulatif des intervalles a un signe faux ; la colonne 0,005 de la table est douteuse.

## Liens avec les autres matières

- **[[Bilinear Algebra (index)]]** : la régression est un problème de [[Moindres carrés]] ([[Projection orthogonale]]), et l'ACP repose sur la [[Valeur propre]], le [[Vecteur propre]], la [[Matrice symétrique]] et la [[Décomposition en valeurs singulières]].
- **[[Analyse dans Rn (index)]]** : la minimisation de la somme des carrés (Cours 10) emploie les dérivées partielles et un critère de minimum local du calcul différentiel (voir [[Dérivée partielle]]).
- **[[Data mining (index)]]** : arbres de décision, k-means et validation d'un classifieur utilisent les mêmes outils d'évaluation d'erreur ; l'ACP et la régression y servent à explorer et prédire.
- **Probability** et **Statistics** (Year 2) : base des lois et des tests utilisés ici.
- **[[Statistics (index)]]** : beaucoup de concepts sont communs, notamment [[Estimateur]], [[Intervalle de confiance]], [[Loi de Student]], [[Loi du khi-deux]], [[Test t]], [[Test Z]], [[Test du χ²]] et la statistique descriptive ([[Histogramme]], [[Quartiles et valeurs aberrantes]]).
- **[[Probability (index)]]** : [[Espérance et variance]], [[Loi conjointe]], [[Loi normale]] et [[Covariance et corrélation]] y sont définies.
- **[[Data mining (index)]]** : l'[[Erreur de type I et de type II]] revient dans l'introduction au data mining.
