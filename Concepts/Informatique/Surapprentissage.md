---
type: concept
tags: [year3, year4]
aliases: [overfitting, sur-apprentissage, surajustement]
matieres: [Data analysis (Thanos), data mining]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Avec trop de variables par rapport au nombre d'observations, un modèle risque de « mémoriser » le bruit et les particularités du jeu de données au lieu d'apprendre la règle générale. Réduire les « degrés de liberté » le rend plus robuste ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]).

## En data mining (complément, hors du cours)

- L'erreur d'entraînement est optimiste : un modèle souple (arbre poussé jusqu'à des feuilles pures, par exemple) peut apprendre les exemples par cœur, avec une erreur d'entraînement nulle, et mal généraliser.
- Signe du surapprentissage : un grand écart entre l'erreur d'entraînement et l'erreur de test.
- Remèdes vus dans le cours [[1 - pdf du prof]] : ensemble de test et validation croisée ([[Ensemble d'entraînement et de test]], [[Validation d'un classifieur]]), [[Élagage]] des arbres (CART, C4.5) et conditions d'arrêt, vote de modèles ([[Bagging]], [[Forêt aléatoire]]).

Voir aussi : [[Réduction de dimension]], [[Analyse en composantes principales]].

Résumés : [[13 - Principal Components Analysis]], [[1 - pdf du prof]]
