---
type: concept
tags: [year4]
aliases: [variable accumulatrice, accumulator]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - Cours complet]]) : variable dans laquelle on combine, tour de [[Boucle (programmation)|boucle]] après tour, les valeurs successives d'une série ; elle est initialisée à l'**élément neutre** de l'opération : 0 pour une somme, 1 pour un produit. Dans `somme1aN(n) = 0 + 0 + 1 + … + n` et `factorielle(n) = 1 * 1 * 2 * … * n`, le premier terme est la valeur initiale de l'accumulateur, chaque terme suivant un tour de boucle.

Complément, hors du cours : le schéma général est `acc = neutre; pour chaque x : acc = acc ⊕ x;`. Il vaut aussi pour un maximum (initialisé au plus petit possible), une concaténation (chaîne vide) ou un ET logique (`true`). La bibliothèque standard l'offre sous le nom `std::accumulate` (en-tête `<numeric>`).

## Dans le cours

[[4 - Cours complet]] l'emploie pour la somme des notes (exercice 3), la [[Somme des premiers entiers|somme des entiers de 1 à 100]] et la [[Factorielle|factorielle]] (exercice 4). Voir aussi [[Compteur (programmation)]].

- [[tp2]] : `somme`, initialisée à 0 et augmentée d'un terme à chaque tour, totalise les termes de la suite arithmétique du programme 2.10.
- [[tp4]] : accumulateur multiplicatif `result *= x`, initialisé à 1, pour calculer $x^n$ (4.5).
- [[tp5]] : la variable `compteur` accumule la somme des diviseurs pour tester un nombre parfait (5.5, 5.7) ; dans des boucles imbriquées, l'accumulateur doit être réinitialisé à chaque tour de la boucle externe.
- [[tp6]] : `resultat`, parti de 1 et multiplié `exposant` fois par `valeur`, dans la fonction `puissance` (6.1).
- [[tp7]] : `compteur` reçoit la somme des cases avant la division par l'effectif dans la procédure `moyenne` (7.3).

Résumés : [[4 - Cours complet]]
