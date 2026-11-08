---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Algo Maths/Python.docx|Python (Algo Maths)]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algo Maths/Python.docx|Python (Algo Maths)]] (séance du 05/10/23), dans [[Cours/Informatique/Algo/_index|Algo]]. Courte note du cours de Python, sans image. Voir [[Langage Python]].

## Affichage et boucles

- Afficher prend plus de temps que calculer.
- La raison : un calcul reste dans le processeur, alors qu'un `print` est une [[Opération d'entrée-sortie|opération d'entrée-sortie]] : il convertit les valeurs en texte, passe par le système d'exploitation et attend que le terminal affiche. Dans une boucle de millions de tours, on évite donc d'afficher à chaque tour : on affiche le résultat final, ou on construit le texte puis on l'affiche en une fois (`print("\n".join(lignes))`). [[Complément hors du cours|ⓘ]]
- `for _ in range(n):` : on nomme la variable `_` quand la boucle n'en a pas besoin ([[Boucle (programmation)]]).
- `_` est un nom de variable ordinaire : c'est une simple convention de lecture, qui dit « cette valeur ne sert pas ». Exemple : `for _ in range(3): print("bjr")` affiche trois fois `bjr`. [[Complément hors du cours|ⓘ]]
- `range(3)` compte de 0 à 2 ([[Fonction range (Python)]]).
- `range(n)` donne les $n$ entiers $0, 1, \dots, n-1$ : la borne de fin est **exclue**, ce qui fait exactement $n$ tours et correspond aux indices d'une liste de longueur $n$ (le premier élément a l'indice 0). `range` ne fabrique pas de liste en mémoire : il produit les nombres au fur et à mesure ; pour les voir tous, `list(range(3))` donne `[0, 1, 2]`. [[Complément hors du cours|ⓘ]]
- Une boucle `for` parcourt en fait n'importe quelle séquence, pas seulement un `range` : `for lettre in "bjr":` parcourt les caractères, `for x in [4, 7, 1]:` les éléments d'une liste. Quand on veut à la fois l'indice et l'élément, `for i, x in enumerate(liste):` évite d'écrire `range(len(liste))`. [[Complément hors du cours|ⓘ]]

## `print` sans retour à la ligne

```python
print("bjr", end="")
print("bjr")
```

affiche `bjrbjr` : `end=""` empêche de passer à la ligne. On peut y mettre autre chose, par exemple un simple espace.

Par défaut, `print` termine par `end="\n"`, le caractère de retour à la ligne : c'est pour cela que deux `print` successifs s'affichent sur deux lignes. Un second paramètre, `sep`, règle ce qui sépare plusieurs valeurs affichées ensemble (un espace par défaut) : [[Complément hors du cours|ⓘ]]

```python
print(1, 2, 3)               # 1 2 3
print(1, 2, 3, sep="-")      # 1-2-3
print("a", "b", sep="", end="!\n")   # ab!
for i in range(5):
    print(i, end=" ")        # 0 1 2 3 4 sur une seule ligne
```

Pour mêler texte et valeurs, la **f-string** est la forme la plus lisible : `print(f"{n} disques : {2**n - 1} coups")`. [[Complément hors du cours|ⓘ]]

## `range` avec un pas

`for i in range(x, y, ±z)` : `i` parcourt $[\![x ; y[\![$ avec un saut de $+z$ ou $-z$.

Exemples du cours :
- `range(2, 10, +5)` donne 2, 7 : on part de 2, on avance de 5 et on s'arrête avant 10 ; [[Erreurs du cours#^e-0-python|✎]]
- `range(10, -1, -2)` donne 10, 8, 6, …, 0.

Pour aller jusqu'à 0 en descendant, il faut une fin à `-1` : la fin étant toujours exclue, `range(10, 0, -2)` s'arrêterait à 2. Formes abrégées : `range(y)` vaut `range(0, y, 1)` et `range(x, y)` vaut `range(x, y, 1)`. [[Complément hors du cours|ⓘ]]

Règles utiles : [[Complément hors du cours|ⓘ]]
- les trois arguments doivent être des **entiers** (`range(0, 1, 0.5)` provoque une erreur ; pour des pas décimaux, on calcule `i / 2` dans la boucle) ;
- un pas nul est interdit (`ValueError`) ;
- si le départ est déjà « au-delà » de la fin dans le sens du pas, le `range` est vide et la boucle ne fait aucun tour : `range(5, 2)` ou `range(2, 10, -1)` ne donnent rien ;
- avec un pas positif $z$, le nombre d'éléments est $\left\lceil \frac{y - x}{z} \right\rceil$ (ou 0 si $y \le x$) : pour `range(2, 10, 5)`, $\lceil 8/5 \rceil = 2$ éléments, 2 et 7.
