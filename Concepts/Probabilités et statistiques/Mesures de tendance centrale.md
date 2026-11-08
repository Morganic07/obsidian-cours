---
type: concept
tags: [year3]
aliases: [tendance centrale, central tendency, moyenne de population, médiane de population, moyenne tronquée, trimmed mean, mode statistique]
sources: ["[[4 - Estimation|Cours 4 - Estimation]]", "[[2 - Descriptive statistics|Chp2 - Descriptive statistics]]"]
maj: 2026-11-08
---

- **Mode** : la valeur la plus fréquente.
- **Médiane** : la valeur du milieu, de rang $(n+1)/2$ si $n$ est impair, moyenne des valeurs de rangs $n/2$ et $n/2 + 1$ sinon.
- **Moyenne** : $\bar x = \dfrac{\sum x_i}{n}$.

Pour une population, on note $\mu$ la moyenne et $\tilde\mu$ la médiane : asymétrie négative si $\mu < \tilde\mu$, distribution symétrique si $\mu = \tilde\mu$, asymétrie positive si $\tilde\mu < \mu$ ([[4 - Estimation|Cours 4 - Estimation]], [[2 - Descriptive statistics|Chp2 - Descriptive statistics]]).

**Compléments (hors du cours)** :
- **Moyenne** : elle minimise $\sum (x_i - c)^2$ et elle est sensible aux valeurs extrêmes. **Médiane** : elle minimise $\sum |x_i - c|$ et elle est résistante. Sur les 12 durées du Chp2, remplacer 79,0 par 790 laisse la médiane à 66,90, alors que la moyenne passe d'environ 68,0 à environ 127,3.
- **Moyenne tronquée** (*trimmed mean*) : moyenne calculée après avoir retiré un pourcentage fixé des plus petites et des plus grandes valeurs (par exemple 10 % de chaque côté) ; compromis entre la moyenne et la médiane.
- **Mode** : seul indicateur de tendance centrale valable pour une variable nominale.

Notion parente : [[Statistique descriptive]]. Voir aussi : [[Variance et écart-type d'échantillon]], [[Forme d'une distribution]], [[Type de variable statistique]].

Résumés : [[4 - Estimation]], [[2 - Introduction statistics]], [[2 - Descriptive statistics]]
