---
type: concept
aliases: [preuve par récurrence, raisonnement par récurrence, démonstration par récurrence, hérédité]
matieres: [Outil Maths, Algo Maths]
sources: ["[[Chapitre 1 logique]]", "[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]"]
maj: 2026-11-05
---

Preuve qu'une propriété $P(n)$ est vraie pour tout entier $n$ à partir d'un rang : **initialisation** ($P$ vraie au premier rang), **hérédité** (si $P(n)$ est vraie, $P(n+1)$ l'est), **conclusion**.

Exemples du cours : $1 + 2 + \ldots + n = \frac{n(n+1)}{2}$ (chapitre de logique) et $f(n) = 2^n - 1$ pour $f(0) = 0$, $f(n+1) = 2f(n) + 1$ (nombre de coups des [[Tours de Hanoï]]).

**Piège** : le problème des crayons « tous de la même couleur » est une fausse récurrence, dont l'hérédité échoue au passage de 1 à 2 crayons.

Une suite définie par récurrence sert aussi à compter la complexité d'un algorithme récursif : voir [[Complexité algorithmique]].

Exemples dans les documents PDF : $\binom{n}{p}$ est entier, et la formule du binôme ([[Chap0-Rappels-etc (résumé)]]) ; $2^n > n^2$ pour $n \ge 5$ ([[Contrôles (résumé)]]). Une fonction récursive se prouve souvent par récurrence : voir [[Récursivité]].

Liens : [[Logique propositionnelle]], [[Récursivité]]

Résumés : [[Chapitre 1 logique (résumé)]], [[Sources/Year 1/Algo Maths/Cours 1 (résumé)|Cours 1 (résumé, Algo Maths)]]
