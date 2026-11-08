---
type: concept
tags: [year3]
aliases: [correlation circle, PCA graph of variables, cercle de corrélation, variable supplémentaire, supplementary variable]
sources: ["[[13 - PCA in R|Cours 13 - PCA in R]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]]"]
maj: 2026-11-08
---

Graphe des variables d'une ACP. Une annotation de l'étudiant sur la note donne la lecture par les angles entre variables :

- angle très fermé : corrélation positive ;
- angle droit : corrélation nulle ;
- angle proche de 180° : corrélation négative.

Exemple du décathlon : Dim 1 à 32,72 % et Dim 2 à 17,37 %, avec deux variables supplémentaires (Rank, Points).

**Pourquoi un cercle (complément, hors du cours)** : dans une ACP réduite ([[Centrage et réduction]]), la flèche d'une variable a pour coordonnées ses corrélations avec les axes (Dim 1, Dim 2). Une corrélation étant comprise entre $-1$ et $1$, et la somme des carrés des corrélations d'une variable avec tous les axes valant 1, la flèche reste dans le cercle de rayon 1.

**Justification de la règle des angles (complément, hors du cours)** : le cosinus de l'angle entre deux flèches approche la corrélation entre les deux variables ; il lui est égal quand les deux variables sont parfaitement représentées dans le plan. D'où la lecture : angle fermé, $\cos \approx 1$ ; angle droit, $\cos = 0$ ; angle plat, $\cos \approx -1$.

**Qualité de représentation (complément, hors du cours)** : la règle ne vaut que pour les variables bien représentées, dont la flèche arrive près du cercle. La qualité de représentation d'une variable dans le plan est son **cos²**, carré de la longueur de sa flèche (somme des carrés de ses coordonnées sur les deux axes). Une flèche courte signale une variable mal résumée par le plan : son angle avec les autres ne dit rien de fiable.

**Variable supplémentaire (complément, hors du cours)** : elle ne sert pas à construire les axes ; elle est projetée ensuite pour aider à les interpréter. Dans le décathlon, Points est fortement corrélée à Dim 1, qui se lit donc comme un axe de performance globale. Ces variables s'affichent en pointillés bleus dans le graphe produit par `PCA()` du paquet R FactoMineR (argument `quanti.sup`).

Notion parente : [[Analyse en composantes principales]]. Voir aussi : [[Covariance et corrélation]], [[Loadings et scores (ACP)]].

Résumés : [[13 - PCA in R]]
