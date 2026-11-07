---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/DM/TD_Algo.docx|TD_Algo]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Algo/DM/TD_Algo.docx|TD_Algo]], dans [[Algo (matière)]]. Note de TD très courte : du code [[Langage Python|Python]] sans énoncé, qui dessine des motifs avec le caractère `#`. L'indentation a été perdue à la conversion : elle est reconstituée ci-dessous d'après la logique du code.

Le fichier commence par `from math import *` (pour `ceil` et `floor`, voir [[Partie entière]]).

## Q1 : carré de `n` × `n`

Afficher `n` lignes de `n` caractères `#`. Code mis en commentaire dans la note.

```python
n = int(input())
for _ in range(n):
    print(n * "#")
```

## Q2 : rectangle de `m` lignes et `n` colonnes

Code mis en commentaire dans la note.

```python
n = int(input())
m = int(input())
for _ in range(m):
    print(n * "#")
```

## Q3 : damier

Seule question non commentée. `a` et `b` sont la moitié de `n` arrondie au-dessus et au-dessous ; les lignes alternent `"# "` et `" #"` selon la parité de l'indice `i` ([[Boucle (programmation)|boucle]] `for` et [[Structure conditionnelle|structure conditionnelle]]).

```python
n = int(input())
a = ceil(n/2)
b = floor(n/2)
if n//2 == 0:
    print(b * "# ")
if n//2 != 0:
    print(a * "# ")
for i in range(n-1):
    if i % 2 == 0:
        print(b * " #")
    if i % 2 != 0:
        print(a * "# ")
# n = n-1
```

## Q4 : triangle

Ligne `k` (de 1 à `n`) : `k` caractères `#`, obtenus par `(n+1) - i` avec `i` décroissant de `n` à 1. Code mis en commentaire dans la note.

```python
n = int(input())
for i in range(n, 0, -1):
    print(((n+1) - i) * "#")
```

## Q5 : motif à double boucle (inachevé)

Parcours imbriqué sur `i` et `j` de 1 à `n`, avec un tableau `tab = [0]*n` non utilisé. Le motif visé semble être un triangle creux (bord gauche, diagonale, dernière ligne pleine), mais l'énoncé n'est pas donné. Code commenté et non terminé.

```python
n = int(input())
tab = [0] * n
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1:
            print("#")
        elif j == i:
            print((j-i+1)"#")      # erreur de syntaxe, voir plus bas
        elif i == n:
            print(n * "#")
        else:
            print(" ")
```

Aucune correction n'est fournie : la note ne contient que ce code.

## Points à vérifier dans le cours

L'énoncé n'étant pas donné, rien n'est vérifiable sur le résultat attendu.

1. **Q3** (complément) : le test `n//2 == 0` n'est vrai que pour `n` égal à 0 ou 1. Il voulait sans doute dire « `n` pair », soit `n % 2 == 0`.
2. **Q5** : `print((j-i+1)"#")` oublie l'opérateur `*` et ne s'exécute pas. Le code est de toute façon commenté.
3. **Mise en forme** : l'indentation est perdue à la conversion, le code ne se lit qu'avec effort. L'indentation donnée ici est une reconstitution.
4. **Q5** (complément) : chaque `print` va à la ligne, donc le motif à double boucle n'afficherait pas une figure en deux dimensions sans `end=""`. L'intention reste supposée.
5. **Q3** (complément) : la ligne `print(b * " #")` contient dans la note `" \#"`, dû à l'échappement de la conversion ; lu ici comme `" #"`.
