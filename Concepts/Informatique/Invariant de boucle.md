---
type: concept
tags: [year1]
aliases: [invariant, loop invariant, variant de boucle, loop variant]
matieres: [Algo Maths]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un invariant de boucle est une propriété portant sur les variables d'une boucle, vraie avant la première itération et conservée par chaque itération. Combiné à la condition de sortie, il établit le résultat de la boucle : c'est l'outil de preuve de la **correction partielle** (si la boucle s'arrête, le résultat est juste).

La preuve se fait en trois temps, sur le même schéma qu'une [[Récurrence|récurrence]] :

1. **Initialisation** : la propriété est vraie avant le premier tour.
2. **Conservation** : si elle est vraie au début d'un tour, elle l'est encore à la fin.
3. **Sortie** : à la sortie, invariant ET négation de la condition de boucle donnent le résultat voulu.

La [[Terminaison d'un algorithme|terminaison]] se prouve à part, par un **variant** : une quantité entière, positive, qui décroît strictement à chaque tour. Comme il n'existe pas de suite infinie strictement décroissante d'entiers positifs, la boucle s'arrête. Correction partielle et terminaison donnent ensemble la correction totale.

**Exemple 1** : pour `POUR i DE 1 A n : resultat ← resultat + i` (avec `resultat ← 0` au départ), l'invariant est « après le tour $i$, $\text{resultat} = 1 + 2 + \ldots + i$ ». À la sortie ($i = n$), $\text{resultat} = \frac{n(n+1)}{2}$.

**Exemple 2** : dans `divisionEntiere` par soustractions successives (avec $a \ge 0$, $b > 0$), l'invariant est $a_{\text{initial}} = \text{quotient} \times b + a$ avec $a \ge 0$. À la sortie, la condition de boucle $a \ge b$ est fausse, donc $0 \le a < b$ : $a$ est le reste de la [[Division euclidienne|division euclidienne]]. Le variant est $a$ lui-même, qui décroît de $b > 0$ à chaque tour.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[0 - diapo prof]], à propos de la correction des algorithmes et de la procédure `divisionEntiere`.

Voir aussi : [[Correction d'un algorithme]], [[Terminaison d'un algorithme]], [[Récurrence]], [[Boucle (programmation)]], [[Somme des premiers entiers]].

Résumés : [[0 - diapo prof]]
