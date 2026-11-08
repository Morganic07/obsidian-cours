---
type: concept
tags: [year3]
aliases: [multicollinearity, colinéarité, collinearity, VIF, variance inflation factor, facteur d'inflation de la variance]
matieres: [Data analysis (Thanos)]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 11 : Multiple Linear Regression and F-statistic.docx|Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : en [[Régression linéaire|régression linéaire multiple]], il y a multicolinéarité quand des variables explicatives sont fortement corrélées entre elles, ou que l'une est presque une combinaison linéaire des autres. Le modèle sépare alors mal leurs effets respectifs : si $X_1$ et $X_2$ varient presque toujours ensemble, les données ne disent pas laquelle des deux fait varier $y$.

**Conséquences.**
- Les erreurs standard des $\hat{\beta}_j$ gonflent : les intervalles de confiance s'élargissent et les tests $t$ perdent leur puissance.
- Les coefficients deviennent instables : un petit changement des données (une observation ajoutée ou retirée) les modifie fortement, et ils peuvent prendre un signe contraire à l'intuition.
- Le test F global ([[Statistique F]]) peut être significatif alors qu'aucun test $t$ individuel ne l'est : le groupe de variables explique $y$, sans qu'on puisse attribuer l'effet à l'une d'elles.
- Les prédictions, elles, restent bonnes tant qu'on reste dans des données de même structure ; c'est l'interprétation des coefficients qui souffre. Les estimateurs restent sans biais.

**Cas extrême : colinéarité exacte.** Si une colonne de $X$ est une combinaison linéaire exacte des autres, $X$ n'est pas de rang plein, $X^\top X$ n'est pas inversible et les coefficients ne sont pas définis de façon unique (voir [[Rang d'une matrice]], [[Matrice inversible]]). C'est pourquoi un facteur à $k$ modalités se code par $k - 1$ [[Variable indicatrice|indicatrices]] quand le modèle a une constante : les $k$ indicatrices ensemble ont pour somme la colonne de 1 (piège des variables indicatrices, *dummy variable trap*).

**Mesure : facteur d'inflation de la variance.**
$$VIF_j = \frac{1}{1 - R_j^2},$$
où $R_j^2$ est le [[Coefficient de détermination|coefficient de détermination]] de la régression de $X_j$ sur les autres variables explicatives. La variance de $\hat{\beta}_j$ est multipliée par $VIF_j$ par rapport au cas où $X_j$ serait non corrélée aux autres. $VIF_j = 1$ signifie aucune corrélation ; un VIF au-delà de 5 à 10 est le seuil d'alerte habituel. Un premier repérage se fait sur la matrice des corrélations entre variables explicatives ([[Covariance et corrélation]]), mais elle ne voit que les liaisons deux à deux. En R : `vif(m)` du paquet `car`.

**Remèdes.**
- Retirer une des variables redondantes, ou les regrouper en un indice.
- Remplacer les variables par des composantes non corrélées ([[Analyse en composantes principales]], régression sur composantes principales).
- Utiliser une régression pénalisée comme la régression ridge, qui accepte un léger biais pour réduire la variance.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[11 - Multiple Linear Regression and F-statistic]], à propos de l'interprétation des coefficients de la régression multiple.

Voir aussi : [[Régression linéaire]], [[Coefficient de détermination]], [[Variable indicatrice]], [[Analyse en composantes principales]], [[Statistique F]], [[Théorème de Gauss-Markov]], [[Covariance et corrélation]]

Résumés : [[11 - Multiple Linear Regression and F-statistic]]
