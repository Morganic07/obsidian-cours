---
type: source
tags:
  - year1
sources:
  - "[[Python|Python (Algo Maths)]]"
maj: 2026-11-05
---

Résumé de [[Python|Python (Algo Maths)]], dans [[Algo Maths (matière)]]. Note courte, sans image.

## Contenu, dans l'ordre du cours

- Afficher prend plus de temps que calculer.
- `for _ in range(n):` : `_` quand la variable de boucle ne sert pas. `range(3)` compte de 0 à 2.
- `print("bjr", end="")` n'ajoute pas de retour à la ligne : deux appels donnent `bjrbjr`. On peut mettre un autre texte, par exemple un espace.
- `range(x, y, z)` : $i$ parcourt $[x ; y[$ avec un pas $z$, positif ou négatif.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`range(2,10,+5)` renvoie « 2, 4, 8 »** : faux, `list(range(2, 10, 5))` donne `[2, 7]` (vérifié). La liste 2, 4, 8 est celle d'un pas de 2 qui s'arrêterait avant 10, mais 2, 4, 6, 8 donnerait `range(2, 10, 2)` (complément). **À corriger avant un examen.**
2. **`range(10, -1, -2)` renvoie « 10, 8, 6, ... »** : correct, la suite s'arrête à 0.
