---
type: concept
tags:
  - year1
aliases:
  - range(n)
  - fonction range
matieres:
  - Algo Maths
sources:
  - "[[0 - Python|Python (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/Python.docx|Python (Algo Maths)]]"
maj: 2026-11-08
---

`range(3)` compte de 0 à 2. `range(x, y, z)` parcourt $[x ; y[$ avec un pas $z$, positif ou négatif : `range(2, 10, 5)` donne 2, 7 [[Erreurs du cours#^e-fonction-range-python|✎]] ; `range(10, -1, -2)` donne 10, 8, 6, ..., 0.

## Compléments (complément, hors du cours)

- **Borne de fin exclue** : `range(n)` fait exactement $n$ tours, de 0 à $n - 1$, soit les indices d'une liste de longueur $n$ : `for i in range(len(L))`.
- **Formes abrégées** : `range(y)` = `range(0, y)` = `range(0, y, 1)`.
- **Objet paresseux** : `range` ne fabrique pas de liste, il produit les valeurs à la demande ; `list(range(3))` donne `[0, 1, 2]`.
- **Contraintes** : les arguments doivent être des entiers (`range(1.5)` lève `TypeError`) et le pas ne peut pas être nul (`range(0, 5, 0)` lève `ValueError`).
- **Range vide** : si le départ a déjà dépassé la fin dans le sens du pas, aucune valeur n'est produite : `range(5, 2)` et `range(2, 5, -1)` sont vides.
- **Nombre d'éléments** : pour un pas $z > 0$, $\max\left(0, \left\lceil \frac{y - x}{z} \right\rceil\right)$ ; par exemple `range(2, 10, 5)` en compte $\lceil 8/5 \rceil = 2$.
- **Compter à rebours jusqu'à 0** : la fin doit valoir $-1$, puisqu'elle est exclue : `range(n - 1, -1, -1)` donne $n - 1, \ldots, 1, 0$.

Notion parente : [[Langage Python]]. Voir aussi : [[Boucle (programmation)]].

Résumés : [[0 - diapo prof]], [[0 - Python]]
