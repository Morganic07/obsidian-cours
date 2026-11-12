---
type: concept
tags: [year1, year2, year4]
aliases: [Fibonacci, Fibonacci sequence, suite de Fibonacci]
matieres: [Analyse Maths, Algo Maths, Algo]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]]"]
maj: 2026-11-12
---

**Analyse Maths** : exemple de suite au chapitre 2 du polycopié.

**Algo Maths** : la version récursive naïve `fibo(n) = fibo(n-1) + fibo(n-2)` refait des sous-calculs (pour `Fibo(5)`, `Fibo(3)` est calculé deux fois et `Fibo(2)` trois fois) ; la version terminale `fiboRT(n, fn-2, fn-1)` les évite.

**Algo (Year 2)** : exemple de récursivité multiple dans [[1 - récursivité et complexité]], avec $F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$.

## Compléments (complément, hors du cours)

**Deux numérotations.** Le polycopié d'analyse pose $F_0 = F_1 = 1$ ($1, 1, 2, 3, 5, 8, \ldots$) ; la fiche d'algorithmique de 2e année pose $F_0 = 0$, $F_1 = 1$ ($0, 1, 1, 2, 3, 5, \ldots$). C'est la même suite, décalée d'un rang. Sauf mention contraire, les formules ci-dessous utilisent $F_0 = 0$, $F_1 = 1$.

**Nombre d'or.** Le rapport $\frac{F_{n+1}}{F_n}$ tend vers $\varphi = \frac{1 + \sqrt5}{2} \approx 1{,}618$, racine positive de $x^2 = x + 1$. Avec l'autre racine $\psi = \frac{1 - \sqrt5}{2}$ :

- formule de Binet pour $F_0 = 0$, $F_1 = 1$ : $F_n = \frac{\varphi^{n} - \psi^{n}}{\sqrt5}$ ;
- pour la numérotation $F_0 = F_1 = 1$ du cours d'analyse : $F_n = \frac{\varphi^{n+1} - \psi^{n+1}}{\sqrt5}$ (vérification : $n = 0$ donne $\frac{\varphi - \psi}{\sqrt5} = 1$, $n = 1$ donne $\frac{\varphi^2 - \psi^2}{\sqrt5} = \varphi + \psi = 1$).

Comme $|\psi| < 1$, $F_n$ croît comme $\varphi^n$. $\varphi$ est aussi la limite de la suite $u_{n+1} = \sqrt{1 + u_n}$, exercice du chapitre 2 d'analyse : la limite $\ell \ge 0$ vérifie $\ell^2 = 1 + \ell$.

**Coût de la version récursive naïve.** Le nombre d'appels $A(n)$ vérifie $A(0) = A(1) = 1$ et $A(n) = A(n-1) + A(n-2) + 1$. La suite $A(n) + 1$ vérifie donc la relation de Fibonacci, avec $A(0) + 1 = 2 = 2F_1$ et $A(1) + 1 = 2 = 2F_2$, d'où

$$A(n) = 2F_{n+1} - 1,$$

un coût exponentiel, de l'ordre de $\varphi^n$ : `fibo(40)` fait $2F_{41} - 1 = 331\,160\,281$ appels, plus de 300 millions.

**Remèdes, en $O(n)$.**

- **Mémoïsation** : on range chaque $F_k$ calculé dans un tableau et on le relit au lieu de le recalculer ; chaque valeur n'est calculée qu'une fois, soit de l'ordre de $n$ appels. C'est l'idée de la [[Programmation dynamique|programmation dynamique]]. En Python, le décorateur `@functools.lru_cache` le fait automatiquement :

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)
```

- **Boucle sur deux variables** :

```python
def fibo(n):
    a, b = 0, 1          # F_0, F_1
    for _ in range(n):
        a, b = b, a + b
    return a
```

Notion parente : [[Suite numérique]]. Voir aussi : [[Récursivité]], [[Récursivité terminale]], [[Programmation dynamique]], [[Complexité algorithmique]], [[Nombre d'or]].

## Dans le cours

- [[tp4]] : le programme 4.6 calcule les [[Nombres de Lucas|nombres de Lucas]], qui suivent la même récurrence avec d'autres termes initiaux ($L_0 = 2$, $L_1 = 1$), par une boucle sur deux variables comme ci-dessus, en langage C.

Résumés : [[0 - rappels pdf]], [[0 - diapo prof]], [[1 - récursivité et complexité]]
