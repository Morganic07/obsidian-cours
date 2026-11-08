---
type: concept
tags: [year3]
aliases: [bootstrap statistique, rééchantillonnage bootstrap, bootstrapping, intervalle bootstrap, bootstrap percentile]
matieres: [Statistics]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le bootstrap est une méthode de rééchantillonnage qui approche la [[Distribution d'échantillonnage|distribution d'échantillonnage]] d'une statistique sans formule théorique. Proposée par Bradley Efron en 1979, elle repose sur une idée simple : faute de connaître la population, **les données observées en tiennent lieu**.

**Algorithme** : à partir de l'échantillon observé $x_1, \dots, x_n$ et d'une statistique $\hat\theta$ (moyenne, médiane, corrélation…) :
1. tirer $n$ valeurs **avec remise** parmi $x_1, \dots, x_n$ : c'est un échantillon bootstrap ([[Tirage avec et sans remise]]) ; certaines valeurs y figurent plusieurs fois, d'autres pas du tout ;
2. calculer la statistique sur cet échantillon, $\hat\theta^*_b$ ;
3. répéter $B$ fois (typiquement $B$ de l'ordre de 1 000 à 10 000) ;
4. utiliser la distribution des $B$ valeurs $\hat\theta^*_1, \dots, \hat\theta^*_B$ comme approximation de celle de $\hat\theta$.

**Ce qu'on en tire** :
- **Erreur type** : l'écart-type des $\hat\theta^*_b$, $\widehat{\mathrm{se}} = \sqrt{\frac{1}{B-1}\sum_b (\hat\theta^*_b - \bar\theta^*)^2}$, où $\bar\theta^*$ est leur moyenne ([[Estimateur]]).
- **Biais** : estimé par $\bar\theta^* - \hat\theta$.
- **[[Intervalle de confiance]] par percentiles** : les [[Quantile|quantiles]] 2,5 % et 97,5 % des $\hat\theta^*_b$ donnent un intervalle approché à 95 %.

**Intérêt** : il s'applique aux statistiques dont la loi est difficile à établir, comme la médiane, un coefficient de corrélation, un rapport de deux moyennes ou un quantile, et ne demande pas de supposer la population normale. Il remplace le calcul théorique par de la simulation sur ordinateur.

**Limites** : l'échantillon doit être représentatif de la population et pas trop petit, puisqu'il la remplace. Le bootstrap fonctionne mal pour les statistiques qui dépendent des valeurs extrêmes, comme le maximum : un échantillon bootstrap ne peut jamais dépasser le maximum observé. Il ne corrige pas un biais d'échantillonnage.

**En apprentissage automatique** : le [[Bagging|bagging]] (*bootstrap aggregating*) applique le même tirage avec remise pour entraîner un modèle par échantillon bootstrap, puis les combine ; chaque échantillon contient environ 63,2 % des exemples distincts.

## Dans le cours

Le cours ne le nomme pas : [[4 - Inferential statistics 1]] présente l'approximation d'une distribution d'échantillonnage par simulation de nombreux échantillons. Le bootstrap apparaît dans les compléments de cette fiche, comme la version de cette simulation qui n'utilise que les données observées.

Voir aussi : [[Distribution d'échantillonnage]], [[Estimateur]], [[Intervalle de confiance]], [[Tirage avec et sans remise]], [[Bagging]], [[Échantillonnage]].

Résumés : [[4 - Inferential statistics 1]]
