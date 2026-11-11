---
type: concept
tags: [year4]
aliases: [recherche du minimum, recherche du maximum, min et max, std::min_element]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : algorithme qui parcourt une série une seule fois en gardant la plus petite et la plus grande valeur vues jusque-là : chaque nouvelle valeur `x` remplace `min` si `x < min`, et `max` si `x > max`. On initialise `min` et `max` avec la première valeur, ou avec des bornes extrêmes (`min` au plus grand possible, `max` au plus petit). Le coût est linéaire, n − 1 comparaisons pour chacun (voir [[Complexité algorithmique]], [[Recherche séquentielle]]). En C++, `std::min_element`, `std::max_element` et `std::minmax_element` (en-tête `<algorithm>`) le font sur un conteneur.

## Dans le cours

[[4 - Cours complet]] demande d'ajouter le calcul du minimum et du maximum des notes au programme de moyenne (question 35).

Résumés : [[4 - Cours complet]]
