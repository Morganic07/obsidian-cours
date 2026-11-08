---
type: concept
tags:
  - year1
aliases:
  - nombre flottant
  - nombres flottants
  - flottant
  - flottants
  - float
  - floating-point number
  - virgule flottante
  - double précision
matieres:
  - Algo Maths
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : représentation approchée d'un nombre réel sous la forme $(-1)^s \times m \times 2^e$, avec un signe $s$, une mantisse $m$ et un exposant $e$ stockés sur un nombre fixe de bits ; la virgule « flotte » selon la valeur de l'exposant, ce qui permet de couvrir à la fois de très petits et de très grands nombres.

## Dans le cours

« En programmation, un float n'est pas un nombre réel » : les flottants ne représentent les réels que de façon approchée (Cours 1). Exemple : $0.1 + 0.2 \ne 0.3$ (en Python, `0.1 + 0.2 == 0.3` vaut `False`). [[Erreurs du cours#^e-nombre-a-virgule-flottante|✎]]

## Mécanisme (complément, hors du cours)

- **Codage** : le `float` de Python (et le `double` de C, C++ ou Java) suit la [[Norme IEEE 754]] en **double précision**, sur 64 bits : 1 bit de signe, 11 bits d'exposant, 52 bits de mantisse. Un nombre normalisé vaut $(-1)^s \times 1{,}f \times 2^{E - 1023}$, où $f$ est la mantisse et $E$ l'exposant stocké. Cela donne environ 15 à 17 chiffres décimaux significatifs ; l'écart entre 1 et le flottant suivant (epsilon machine) vaut $2^{-52} \approx 2{,}2 \times 10^{-16}$. La simple précision (`float` en C) utilise 32 bits : 1, 8 et 23.
- **Pourquoi 0,1 est inexact** : un nombre n'a une écriture binaire finie que si c'est une fraction dont le dénominateur est une puissance de 2. Or $0{,}1 = 1/10$ et $10 = 2 \times 5$ : en base 2, $0{,}1 = 0{,}0001100110011\ldots_2$, avec le motif $0011$ répété à l'infini, comme $1/3 = 0{,}333\ldots$ en base 10. Le nombre est donc arrondi au flottant le plus proche, et les arrondis s'accumulent au fil des calculs : en Python, `0.1 + 0.2` affiche `0.30000000000000004`.
- **Comparer deux flottants** : jamais avec `==`, mais à une tolérance près.

  ```python
  import math

  a = 0.1 + 0.2
  b = 0.3
  a == b                      # False
  abs(a - b) < 1e-9           # True : tolérance absolue
  math.isclose(a, b)          # True : tolérance relative (1e-09 par défaut)
  ```

- **Conséquences pratiques** : pour des montants d'argent, on calcule en centimes entiers ou avec le module `decimal` ; une somme de nombreux flottants peut dépendre de l'ordre des additions.

Notion parente : [[Type primitif]]. Voir aussi : [[Norme IEEE 754]], [[Langage Python]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[0 - diapo prof]]
