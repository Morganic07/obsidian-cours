---
type: source
tags:
  - year1
sources:
  - "[[Python|Python (Algo Maths)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[Python|Python (Algo Maths)]], dans [[Algo Maths (matière)]] : notes de la séance du 05/10/23, premier cours de [[Langage Python|Python]]. Note courte, sans image.

## Remarque générale

- Afficher des choses prend plus de temps que les calculer : un `print` dans une boucle ralentit le programme.

## Boucle `for` et `range`

### La variable muette `_`

```python
for _ in range(n):
    ...
```

On écrit `_` à la place du nom de la variable de boucle lorsqu'on n'a pas besoin de cette variable dans le corps de la boucle (on veut seulement répéter $n$ fois).

### `range(n)`

[[Fonction range (Python)|`range(n)`]] compte de $0$ à $n-1$ : `range(3)` donne 0, 1, 2.

### `range(x, y, z)`

```python
for i in range(x, y, z):   # z positif ou négatif
    ...
```

$i$ part de $x$ et avance par sauts de $+z$ (ou $-z$), dans l'intervalle $[x ; y[$ : la borne $y$ est exclue.

Exemples du cours :

| Appel | Valeurs données par le cours | Remarque |
|---|---|---|
| `range(2, 10, +5)` | 2, 4, 8 | faux, voir « Points à vérifier » : on obtient 2, 7 |
| `range(10, -1, -2)` | 10, 8, 6, ... | correct : 10, 8, 6, 4, 2, 0 |

## Afficher sans retour à la ligne : `end`

```python
print("bjr", end="")
print("bjr")
# affiche : bjrbjr
```

Par défaut, `print` passe à la ligne après le texte. Le paramètre `end=""` l'en empêche ; on peut mettre autre chose dans `end`, par exemple un simple espace (`end=" "`).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **`range(2,10,+5)` renvoie « 2, 4, 8 »** : faux, `list(range(2, 10, 5))` donne `[2, 7]` (vérifié). La liste 2, 4, 8 est celle d'un pas de 2 qui s'arrêterait avant 10, mais 2, 4, 6, 8 donnerait `range(2, 10, 2)` (complément). **À corriger avant un examen.**
2. **`range(10, -1, -2)` renvoie « 10, 8, 6, ... »** : correct, la suite s'arrête à 0.
3. **Notation de l'intervalle** : la note écrit « \[\[x;y\[\[ » ; il faut lire $[x ; y[$ (borne $y$ exclue).
