---
type: concept
tags: [year3]
aliases: [Kruskal-Wallis, Kruskal-Wallis test, test H de Kruskal-Wallis, ANOVA de Kruskal-Wallis]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : test [[Test paramétrique et non paramétrique|non paramétrique]] qui compare $k \geq 3$ groupes indépendants sans supposer la normalité. C'est l'équivalent de l'[[ANOVA]] à un facteur, fondé sur les rangs au lieu des valeurs ; il généralise le [[Test de Mann-Whitney|test de Mann-Whitney]] à plus de deux groupes.

**Hypothèses** : $H_0$ : les $k$ groupes proviennent de la même distribution. $H_1$ : au moins un groupe tend à prendre des valeurs plus grandes ou plus petites que les autres.

**Statistique** : on classe ensemble les $N$ observations (rang 1 pour la plus petite, rang moyen en cas d'égalité), puis on calcule la somme des rangs $R_i$ de chaque groupe $i$ de taille $n_i$ :

$$H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)$$

Sous $H_0$, chaque groupe devrait avoir un rang moyen proche de $\frac{N+1}{2}$ ; $H$ grandit quand les rangs moyens s'en écartent.

**Décision** : sous $H_0$, $H$ suit approximativement une [[Loi du khi-deux|loi du χ²]] à $k-1$ degrés de liberté, pourvu que les groupes ne soient pas trop petits (souvent au moins 5 observations chacun) ; sinon on recourt à des tables exactes. On rejette $H_0$ pour $H$ grand. Un $H$ significatif dit seulement qu'au moins un groupe diffère ; pour savoir lesquels, on fait des [[Comparaisons multiples|comparaisons multiples]] (par exemple des tests de Mann-Whitney deux à deux avec correction de Bonferroni).

**Quand l'utiliser** : normalité douteuse (petits échantillons, distributions asymétriques, valeurs aberrantes) ou réponse ordinale ([[Type de variable statistique]]). Si les conditions de l'ANOVA sont remplies, celle-ci est plus puissante.

**En R** : `kruskal.test(y ~ groupe, data = df)`.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[12 - ANOVA and F-statistic]], comme solution de repli quand la normalité requise par l'ANOVA ne tient pas.

Voir aussi : [[ANOVA]], [[Test paramétrique et non paramétrique]], [[Test de Mann-Whitney]], [[Loi du khi-deux]], [[Statistique F]].

Résumés : [[12 - ANOVA and F-statistic]]
