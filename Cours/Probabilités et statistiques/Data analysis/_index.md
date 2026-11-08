---
type: matiere
tags:
  - year3
sources:
  - "[[1 - Data analysis|Cours 1 (Data analysis)]]"
  - "[[2 - Introduction statistics|Cours 2 - Introduction statistics]]"
  - "[[3 - Paradoxe de Simpson|Cours 3 - Paradoxe de Simpson]]"
  - "[[4 - Estimation|Cours 4 - Estimation]]"
  - "[[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]"
  - "[[6 - T-Test|Cours 6 - T-Test]]"
  - "[[7 - Z-Test|Cours 7 - Z-Test]]"
  - "[[8 - Chi²-Test|Cours 8 - Chi²-Test]]"
  - "[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"
  - "[[10 - linear regression|Cours 10 - linear regression]]"
  - "[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]"
  - "[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]"
  - "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"
  - "[[13 - PCA in R|Cours 13 - PCA in R]]"
  - "[[14 - functions in RStudio|Summary functions in RStudio]]"
maj: 2026-11-08
---

Analyse de données avec R : rappels de statistique, tests d'hypothèse, corrélation, régression simple et multiple, ANOVA et analyse en composantes principales. Les 15 notes sont à intégrer ; 14 résumés sont écrits (voir plus bas pour la quinzième).

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - Data analysis\|Cours 1]] | R : structures, fonctions, opérateurs | [[1 - Data analysis\|Résumé]] |
| [[2 - Introduction statistics\|Cours 2 - Introduction statistics]] | Descriptif et inférentiel, niveaux de mesure | [[2 - Introduction statistics\|Résumé]] |
| [[3 - Paradoxe de Simpson\|Cours 3 - Paradoxe de Simpson]] | Variable cachée | [[3 - Paradoxe de Simpson\|Résumé]] |
| [[4 - Estimation\|Cours 4 - Estimation]] | Intervalle de confiance | [[4 - Estimation\|Résumé]] |
| [[5 - Hypothesis Testing\|Cours 5 - Hypothesis Testing]] | Hypothèses, erreurs, procédure | [[5 - Hypothesis Testing\|Résumé]] |
| [[6 - T-Test\|Cours 6 - T-Test]] | Loi de Student, test t | [[6 - T-Test\|Résumé]] |
| [[7 - Z-Test\|Cours 7 - Z-Test]] | Tests Z, proportions | [[7 - Z-Test\|Résumé]] |
| [[8 - Chi²-Test\|Cours 8 - Chi²-Test]] | χ², variance, indépendance | [[8 - Chi²-Test\|Résumé]] |
| [[9 - Covariance and Correlation\|Cours 9 - Covariance and Correlation]] | Covariance, Pearson, Spearman, Kendall | [[9 - Covariance and Correlation\|Résumé]] |
| [[10 - linear regression\|Cours 10 - linear regression]] | Régression simple, résidus | [[10 - linear regression\|Résumé]] |
| [[11 - Multiple Linear Regression and F-statistic\|Cours 11 - Multiple Linear Regression and F-statistic]] | Prédiction, régression multiple, F | [[11 - Multiple Linear Regression and F-statistic\|Résumé]] |
| [[12 - ANOVA and F-statistic\|Cours 12 - ANOVA and F-statistic]] | ANOVA | [[12 - ANOVA and F-statistic\|Résumé]] |
| [[13 - Principal Components Analysis\|Cours 13 - Principal Components Analysis]] | ACP | [[13 - Principal Components Analysis\|Résumé]] |
| [[13 - PCA in R\|Cours 13 - PCA in R]] | ACP en R | [[13 - PCA in R\|Résumé]] |
| [[14 - functions in RStudio\|Summary functions in RStudio]] | Aide-mémoire R | [[14 - functions in RStudio\|Résumé]] |

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
- **Ajoutés par l'enrichissement** : [[Théorème de Gauss-Markov]], [[Multicolinéarité]], [[Régression logistique]], [[Test de Kruskal-Wallis]], [[Comparaisons multiples]], [[Puissance d'un test]], [[Taille d'effet]], [[Test de Welch]], [[Essai contrôlé randomisé]], [[V de Cramér]], [[Test d'adéquation du χ²]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[11 - Multiple Linear Regression and F-statistic]] : F = variation expliquée / variation non expliquée (rapport de carrés moyens) ; lecture d'un intervalle de prédiction.
- [[12 - ANOVA and F-statistic]] : on rejette $H_0$ quand F dépasse la valeur critique (p-value inférieure à $\alpha$) ; refaire le calcul des sommes des carrés de l'exemple.
- [[7 - Z-Test]] : des mesures avant et après traitement sur les mêmes individus relèvent du test $t$ apparié.
- [[8 - Chi²-Test]] : la somme des carrés de $n$ normales centrées réduites indépendantes suit un χ² à $n$ degrés, celle des écarts à la moyenne d'échantillon un χ² à $n - 1$ degrés ; signes des bornes des intervalles unilatéraux.

## Liens avec les autres matières

- **[[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]]** : la régression est un problème de [[Moindres carrés]] ([[Projection orthogonale]]), et l'ACP repose sur la [[Valeur propre]], le [[Vecteur propre]], la [[Matrice symétrique]] et la [[Décomposition en valeurs singulières]].
- **[[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]]** : la minimisation de la somme des carrés (Cours 10) emploie les dérivées partielles et un critère de minimum local du calcul différentiel (voir [[Dérivée partielle]]).
- **[[Cours/Informatique/Data mining/_index|Data mining]]** : arbres de décision, k-means et validation d'un classifieur utilisent les mêmes outils d'évaluation d'erreur ; l'ACP et la régression y servent à explorer et prédire.
- **Probability** et **Statistics** (Year 2) : base des lois et des tests utilisés ici.
- **[[Cours/Probabilités et statistiques/Statistics/_index|Statistics]]** : beaucoup de concepts sont communs, notamment [[Estimateur]], [[Intervalle de confiance]], [[Loi de Student]], [[Loi du khi-deux]], [[Test t]], [[Test Z]], [[Test du χ²]] et la statistique descriptive ([[Histogramme]], [[Quartiles et valeurs aberrantes]]).
- **[[Cours/Probabilités et statistiques/Probability/_index|Probability]]** : [[Espérance et variance]], [[Loi conjointe]], [[Loi normale]] et [[Covariance et corrélation]] y sont définies.
- **[[Cours/Informatique/Data mining/_index|Data mining]]** : l'[[Erreur de type I et de type II]] revient dans l'introduction au data mining.
