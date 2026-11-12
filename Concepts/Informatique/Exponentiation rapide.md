---
type: concept
tags: [year1, year4]
aliases: [puissance par dichotomie]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-12
---

Le TD3 fait calculer $n^k$ de façon naïve, puis en récursivité terminale, puis « par dichotomie » avec $n^k = (n \cdot n)^{k/2}$ si $k$ est pair, et enfin par dichotomie terminale.

Notion parente : [[Récursivité]]. Voir aussi : [[Recherche dichotomique]], [[Récursivité terminale]].

## Dans le cours

- [[tp4]] : le programme 4.5 calcule $x^n$ ([[Puissance (mathématiques)|puissance]]) par $n$ multiplications successives ; la fiche signale l'exponentiation rapide, environ $2\log_2 n$ multiplications, comme alternative.
- [[tp6]] : même remarque pour la fonction `puissance(valeur, exposant)` du programme 6.1 ([[Exponentiation]]), en version itérative ou récursive.

Résumés : [[0 - diapo prof]]
