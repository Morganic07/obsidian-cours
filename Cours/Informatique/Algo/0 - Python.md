---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Algo Maths/Python.docx|Python (Algo Maths)]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Algo Maths/Python.docx|Python (Algo Maths)]] (séance du 05/10/23), dans [[Cours/Informatique/Algo/_index|Algo]]. Courte note du cours de Python, sans image. Voir [[Langage Python]].

## Affichage et boucles

- Afficher prend plus de temps que calculer.
- `for _ in range(n):` : on nomme la variable `_` quand la boucle n'en a pas besoin ([[Boucle (programmation)]]).
- `range(3)` compte de 0 à 2 ([[Fonction range (Python)]]).

## `print` sans retour à la ligne

```python
print("bjr", end="")
print("bjr")
```

affiche `bjrbjr` : `end=""` empêche de passer à la ligne. On peut y mettre autre chose, par exemple un simple espace.

## `range` avec un pas

`for i in range(x, y, ±z)` : `i` parcourt $[\![x ; y[\![$ avec un saut de $+z$ ou $-z$.

Exemples du cours :
- `range(2, 10, +5)` donne 2, 7 (la note écrit autre chose, voir « Erreurs du cours ») ;
- `range(10, -1, -2)` donne 10, 8, 6, …, 0.

## Erreurs du cours

- La note écrit « range(2,10,+5) renvoit 2, 4, 8 » ; il faut « 2, 7 » : on part de 2, on avance de 5 et on s'arrête avant 10. Même remarque dans [[Fonction range (Python)]].
