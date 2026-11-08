---
type: concept
tags: [year3]
aliases: [loadings, loading, PCA scores, scores de l'ACP, graphique des loadings, loading plot]
matieres: [Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Les **loadings** sont les poids de chaque variable dans une composante principale, par exemple $PC1 = 0{,}9a_1 + 0{,}1a_2$. Dans une seconde convention, le mot désigne la corrélation entre la variable et la composante, qui est une autre quantité : pour des variables centrées réduites, elle vaut le poids multiplié par $\sqrt{\lambda_k}$, écart-type de la composante $k$. [[Erreurs du cours#^e-loadings-et-scores-acp|✎]] Les **scores** sont les coordonnées d'un échantillon dans le système tourné, obtenues en multipliant les données par les loadings ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]).

Avec la [[Décomposition en valeurs singulières]] $A = U\Sigma V^T$, $V$ est la matrice des loadings et $U\Sigma$ (soit $AV$) la matrice des scores ; $U$ seule en est la version normée, chaque colonne divisée par $\sigma_k$. [[Erreurs du cours#^e-loadings-et-scores-acp|✎]] Le biplot superpose les loadings (vecteurs) et les scores (points).

Notion parente : [[Analyse en composantes principales]]. Voir aussi : [[Décomposition en valeurs singulières]], [[Cercle des corrélations]].

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]]
