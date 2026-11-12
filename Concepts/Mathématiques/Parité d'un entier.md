---
type: concept
tags: [year1, year4]
aliases: [même parité, nombre pair, nombre impair, entier pair, entier impair]
matieres: [Outil Maths]
sources: ["[[1 - logique|Chapitre 1 logique]]"]
maj: 2026-11-12
---

Un entier est pair s'il s'écrit $2k$, impair s'il s'écrit $2k+1$.

Théorèmes à connaître du cours de logique : la somme de deux impairs ($2k+1$ et $2l+1$) est paire ; si $x + y$ est pair, $x$ et $y$ ont la même parité (par [[Preuve par contraposition|contraposition]]) ; lemme : si $a^2$ est pair, $a$ est pair (contraposée : $a = 2u + 1$ donne $a^2$ impair).

Voir aussi : [[Irrationalité de √2]].

## Dans le cours

- [[tp3]] : parité testée en C par le reste `chiffre % 2` (3.7), puis par `nombre/2*2 == nombre` (3.9, [[Division euclidienne|division entière]]) ; la fiche ajoute le test `(nombre & 1) == 0` ([[Opérateur bit à bit]]) et rappelle que `n % 2 == 1` échoue sur un impair négatif.
- [[tp4]] : nombres pairs de 0 à 100, en filtrant par `%` (`algo1`) ou en avançant de 2 en 2 (`algo2`) (4.4).
- [[tp5]] : `nombre % 2 == 0` choisit la branche de la [[Conjecture de Syracuse|suite de Syracuse]] (5.8).
- [[tp7]] : `tab[i] % 2 != 0` repère les cases impaires d'un tableau.

Résumés : [[1 - logique]]
