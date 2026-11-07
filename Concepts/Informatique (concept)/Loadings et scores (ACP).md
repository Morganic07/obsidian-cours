---
type: concept
tags: [year3]
aliases: [loadings, loading, PCA scores, scores de l'ACP, graphique des loadings, loading plot]
matieres: [Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-06
---

Les **loadings** sont les poids de chaque variable dans une composante principale, par exemple $PC1 = 0{,}9a_1 + 0{,}1a_2$ ; le cours dit aussi que c'est la corrélation entre la variable et la composante. Les **scores** sont les coordonnées d'un échantillon dans le système tourné, obtenues en multipliant les données par les loadings ([[13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]).

Avec la [[Décomposition en valeurs singulières]] $A = U\Sigma V^T$, $V$ est la matrice des loadings. Le biplot superpose les loadings (vecteurs) et les scores (points).

Notion parente : [[Analyse en composantes principales]]. Voir aussi : [[Décomposition en valeurs singulières]], [[Cercle des corrélations]].

## À vérifier

- Le cours confond les poids normés et la corrélation variable-composante.
- Il écrit « U = matrice des scores », alors que les scores sont $U\Sigma$.

Résumés : [[13 - Principal Components Analysis (résumé)]], [[13 - PCA in R (résumé)]]
