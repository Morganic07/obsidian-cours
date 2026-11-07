---
type: concept
tags: [year3]
aliases: [loadings, loading, PCA scores, scores de l'ACP, graphique des loadings, loading plot]
matieres: [Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-07
---

Les **loadings** sont les poids de chaque variable dans une composante principale, par exemple $PC1 = 0{,}9a_1 + 0{,}1a_2$ ; le cours dit aussi que c'est la corrélation entre la variable et la composante. Les **scores** sont les coordonnées d'un échantillon dans le système tourné, obtenues en multipliant les données par les loadings ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]).

Avec la [[Décomposition en valeurs singulières]] $A = U\Sigma V^T$, $V$ est la matrice des loadings. Le biplot superpose les loadings (vecteurs) et les scores (points).

Notion parente : [[Analyse en composantes principales]]. Voir aussi : [[Décomposition en valeurs singulières]], [[Cercle des corrélations]].

## Erreurs du cours

- [[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]] présente le loading comme le poids de la variable dans la composante ($PC1 = 0{,}9a_1 + 0{,}1a_2$), puis écrit que « le loading est en réalité le coefficient de corrélation entre la variable d'origine et la composante principale » ; il faut distinguer les deux : le poids est une coordonnée du vecteur propre (norme 1), et la corrélation avec la composante $k$ vaut ce poids multiplié par $\sqrt{\lambda_k}$, pour des variables centrées réduites (complément, hors du cours). Vérifié sur l'image de la diapositive.
- La diapositive 128 écrit « U → is also called the scores matrix » ; il faut « $U\Sigma$ (soit $AV$) est la matrice des scores » : $U$ n'en donne que la version normée, chaque colonne divisée par $\sigma_k$. Vérifié sur l'image.

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]]
