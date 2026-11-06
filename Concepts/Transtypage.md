---
type: concept
aliases: [transtypage, transtypage implicite, transtypage explicite, type casting, conversion de type]
matieres: [Java, C++]
sources: ["[[Chp1 - Intro Java]]"]
maj: 2026-11-06
---

Le transtypage (type casting) convertit une valeur d'un [[Type primitif|type]] vers un autre.

- **Implicite** : automatique, quand le type d'arrivée est suffisant. Exemple : `float` vers `double`, ou `int` vers `float` (`r = i;` est correct).
- **Explicite** : écrit par le programmeur, avec un cast comme `(int)`. Nécessaire quand le type d'arrivée peut perdre de l'information : `i = r;` (de `float` à `int`) est incorrect sans cast. Pour `double` vers `float`, le résultat peut être correct ou non selon la valeur.

Le cours de Java donne la hiérarchie `double`, `float`, `long`, `int`, puis `short` et `char`, `byte` tout en bas.

Voir aussi : [[Type primitif]], [[Portée d'une variable]]

## À vérifier

- [[Chp1 - Intro Java]] marque `quotient = (int)(x/y);` comme « incorrect », alors que ce cast explicite est valide.

Résumé : [[Chp1 - Intro Java (résumé)]]
