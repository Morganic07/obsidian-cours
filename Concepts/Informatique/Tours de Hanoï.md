---
type: concept
tags: [year1, year4]
aliases: [Hanoï, tours de Hanoi, Tower of Hanoi]
matieres: [Algo Maths, graph theory]
sources: ["[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]", "[[chp3 - complexité]]", "[[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1]]"]
maj: 2026-11-06
---

Problème : déplacer $n$ disques d'un pilier à un autre, avec un nombre minimal de coups. Algorithme **récursif** : déplacer les $n - 1$ disques du dessus sur le pilier intermédiaire, déplacer le grand disque, replacer les $n - 1$ disques dessus.

Nombre de coups : $f(0) = 0$, $f(n+1) = 2f(n) + 1$, donc $f(n) = 2^n - 1$, démontré par [[Récurrence]] dans [[Cours 1 - Algo Maths (résumé)|Cours 1 (résumé, Algo Maths)]]. Le pseudo-code de 1re année s'écrit `Déplacer(n, de, à, par)`. Le cours de graphes retrouve $T(n) = 2T(n-1) + 1$, $T(1) = 1$, d'où $T(n) = \sum_{k=0}^{n-1} 2^k = 2^n - 1$ et $\Theta(2^n)$ : voir [[Complexité algorithmique]] et [[Calcul de complexité et théorème de résolution]].

Notion parente : [[Récursivité]].

## À vérifier

- Dans [[chp3 - complexité]], l'équation est introduite pour « $n > 0$ » alors que la base est $T(1)$, et la fin de la résolution est coupée sur l'image.

Résumés : [[Cours 1 - Algo Maths (résumé)|Cours 1 (résumé, Algo Maths)]], [[chp3 - complexité (résumé)]], [[AlgoID1 (résumé)]]
