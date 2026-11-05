---
type: concept
aliases: [court-circuit, short-circuit, évaluation paresseuse, opérateur paresseux, lazy operator]
matieres: [Java, C++]
sources: ["[[Chp1 - Intro Java]]", "[[Chp1 - basiques]]"]
maj: 2026-11-05
---

Les opérateurs `&&` et `||` n'évaluent pas toujours leurs deux opérandes : l'évaluation va de gauche à droite et s'arrête dès que le résultat est connu.

- `A || B` : si `A` est vrai, `B` n'est pas évalué.
- `A && B` : si `A` est faux, `B` n'est pas évalué.

**Java** : `&&` et `||` sont les versions court-circuit, `&` et `|` évaluent toujours les deux côtés.

**C (cours de C++)** : le cours l'illustre avec `if (x > 5 || (y = 20))`. Comme `x > 5` est vrai, l'affectation `y = 20` n'a jamais lieu. Si l'on écrit `if ((y = 20) || x > 5)`, l'affectation est évaluée, vaut 20, donc est vraie, et `x > 5` n'est pas lu : le programme affiche `vrai` puis `y = 20`.

À retenir : une affectation placée dans une condition peut ne jamais s'exécuter.

Résumés : [[Chp1 - Intro Java (résumé)]], [[Chp1 - basiques (résumé)]]
