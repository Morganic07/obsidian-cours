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
maj: 2026-11-07
---

**Data analysis** : **centrer**, c'est soustraire à chaque variable sa moyenne (le centre du nuage passe à l'origine, les positions relatives ne changent pas). **Mettre à l'échelle**, c'est diviser par l'écart-type, pour que des variables d'unités différentes pèsent autant dans l'[[Analyse en composantes principales|ACP]].

**Statistics** : l'aide-mémoire donne les scores Z $\frac{X - \bar X}{s}$, $\frac{X - \mu}{\sigma}$ et $\frac{\bar X - \mu}{\sigma/\sqrt n}$.

Voir aussi : [[Analyse en composantes principales]], [[Loi normale]], [[Variance et écart-type d'échantillon]].

## Erreurs du cours

- [[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]] (exemple Math / History, image vérifiée) écrit « variable "Math" has 10 times larger variance (importance) than variable "History" » ; il faut « 10 times larger standard deviation » : des notes sur 100 au lieu de 10 ont un écart-type environ 10 fois plus grand, donc une variance environ 100 fois plus grande.

Résumés : [[13 - Principal Components Analysis]], [[13 - PCA in R]], [[0 - proba&stats utilitaire]]
