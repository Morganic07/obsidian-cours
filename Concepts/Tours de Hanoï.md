---
type: concept
aliases: [Hanoï, tours de Hanoi, Tower of Hanoi]
matieres: [Algo Maths, graph theory]
sources: ["[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]", "[[chp3 - complexité]]"]
maj: 2026-11-05
---

Problème : déplacer $n$ disques d'un pilier à un autre, avec un nombre minimal de coups. Algorithme **récursif** : déplacer les $n - 1$ disques du dessus sur le pilier intermédiaire, déplacer le grand disque, replacer les $n - 1$ disques dessus.

Nombre de coups : $f(0) = 0$, $f(n+1) = 2f(n) + 1$, donc $f(n) = 2^n - 1$, démontré par [[Récurrence]] dans [[Sources/Year 1/Algo Maths/Cours 1 (résumé)|Cours 1 (résumé, Algo Maths)]]. Le cours de graphes retrouve $T(n) = 2T(n-1) + 1$ et conclut $\Theta(2^n)$ : voir [[Complexité algorithmique]].

Résumés : [[Sources/Year 1/Algo Maths/Cours 1 (résumé)|Cours 1 (résumé, Algo Maths)]], [[chp3 - complexité (résumé)]]
