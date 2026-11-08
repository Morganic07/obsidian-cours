---
type: concept
tags:
  - year3
aliases:
  - centrage
  - centering
  - standardisation
  - standardization
  - score Z
  - z-score
  - z-scores
  - mise à l'échelle
  - données centrées réduites
matieres:
  - Data analysis (Thanos)
  - Statistics
sources:
  - "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"
  - "[[13 - PCA in R|Cours 13 - PCA in R]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
maj: 2026-11-08
---

**Data analysis** : **centrer**, c'est soustraire à chaque variable sa moyenne (le centre du nuage passe à l'origine, les positions relatives ne changent pas). **Mettre à l'échelle**, c'est diviser par l'écart-type, pour que des variables d'unités différentes pèsent autant dans l'[[Analyse en composantes principales|ACP]]. Sans cette mise à l'échelle, des notes de maths sur 100 et d'histoire sur 10 donnent aux maths un écart-type environ 10 fois plus grand, donc une variance (importance) environ 100 fois plus grande. [[Erreurs du cours#^e-centrage-et-reduction|✎]] Soustraire seulement la moyenne est un centrage, pas une standardisation. [[Erreurs du cours#^e-centrage-et-reduction|✎]]

**Statistics** : l'aide-mémoire donne les scores Z $\frac{X - \bar X}{s}$, $\frac{X - \mu}{\sigma}$ et $\frac{\bar X - \mu}{\sigma/\sqrt n}$.

Voir aussi : [[Analyse en composantes principales]], [[Loi normale]], [[Variance et écart-type d'échantillon]].

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]], [[0 - proba&stats utilitaire]]
