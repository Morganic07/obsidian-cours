---
type: concept
tags: [year1]
aliases: ["nombres d'Armstrong"]
sources: ["[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

Définition de l'examen d'informatique du 14 novembre 2022 (partie 2, pages 31-32 de `Contrôles.pdf`) : « Un nombre est considéré comme un nombre d'Armstrong s'il est égal à la somme des cubes des chiffres qui le composent. »

Exemple de l'énoncé : $153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27$.

L'exercice demande d'écrire la fonction `armstrong(n : entier) : booléen`, qui teste cette propriété.

Voir aussi : [[Fonction et procédure]], [[Nombre parfait]].

## À vérifier

- La définition usuelle élève chaque chiffre à une puissance égale au **nombre de chiffres** du nombre, pas toujours au cube ; les deux coïncident pour les nombres à trois chiffres, comme 153 (complément, hors du cours).

Résumés : [[Contrôles (résumé)]]
