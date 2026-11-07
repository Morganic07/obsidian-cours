---
type: concept
tags: [year3]
aliases: [ggplot2, ggplot, geom_smooth]
matieres: [Data analysis (Thanos)]
sources: ["[[Séance 3 - Paradoxe de Simpson (résumé)|Cours 3 - Paradoxe de Simpson]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : ggplot2 est un paquet du [[Langage R]] qui construit des graphiques par couches, selon la « grammaire des graphiques ». On part d'un jeu de données et d'une correspondance entre variables et propriétés visuelles (`aes()` : abscisse, ordonnée, couleur…), puis on ajoute avec `+` des couches géométriques (`geom_point()` pour un nuage de points, `geom_smooth()` pour une courbe ou droite d'ajustement, etc.), des échelles et des thèmes.

## Dans le cours

Nommé dans [[Séance 3 - Paradoxe de Simpson (résumé)|Cours 3 - Paradoxe de Simpson]] sans définition : paquet R de graphiques, que le cours utilise pour détecter un [[Paradoxe de Simpson]] en colorant les points par groupe (`geom_smooth(method = "lm")`, `color = stade_cancer`). Le cours cite aussi `glimpse()`, le paquet finalfit et un jeu de données meldata, sans les définir.

Notion parente : [[Langage R]]. Voir aussi : [[Paradoxe de Simpson]].

Résumés : [[Séance 3 - Paradoxe de Simpson (résumé)]]
