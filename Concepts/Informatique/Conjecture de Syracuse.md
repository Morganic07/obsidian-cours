---
type: concept
tags: [year1, year4]
aliases: [suite de Syracuse]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-12
---

Exemple (`exemple4`) d'AlgoID1 : un algorithme récursif dont on ne sait pas démontrer la terminaison. Le cours demande : « Cet algorithme se termine-t-il (conjecture de Syracuse) ? ».

```
Fonction exemple4(n : Entier):Entier
Début
    Si (n = 1) Alors
        retourner 1
    Sinon
        Si ((n mod 2) = 0) Alors
            retourner exemple4(n/2)
        Sinon
            retourner exemple4(3*n+1)
        FinSi
    FinSi
Fin
```

Règle de la suite : si $n$ est pair, on passe à $n/2$ ; s'il est impair, à $3n+1$ ; on s'arrête à 1. La diapositive suivante conclut : « La terminaison est un problème indécidable ! »

## Dans le cours

- [[tp5]] : en C, le programme 5.8 affiche la suite partant de 15 avec une boucle `while` ; elle atteint 1 en 17 étapes et culmine à 160.

Notion parente : [[Terminaison d'un algorithme]]. Voir aussi : [[Récursivité]].

Résumés : [[0 - diapo prof]]
