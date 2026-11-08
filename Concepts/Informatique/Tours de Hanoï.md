---
type: concept
tags:
  - year1
  - year4
aliases:
  - Hanoï
  - tours de Hanoi
  - Tower of Hanoi
matieres:
  - Algo Maths
  - graph theory
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[3 - complexité|chp3 - complexité]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]"
maj: 2026-11-08
---

Problème : déplacer $n$ disques d'un pilier à un autre, avec un nombre minimal de coups. Algorithme **récursif** : déplacer les $n - 1$ disques du dessus sur le pilier intermédiaire, déplacer le grand disque, replacer les $n - 1$ disques dessus.

Nombre de coups : $f(0) = 0$, $f(n+1) = 2f(n) + 1$, donc $f(n) = 2^n - 1$, démontré par [[Récurrence]] dans [[0 - Algo Maths|Cours 1 (Algo Maths)]]. Le pseudo-code de 1re année s'écrit `Déplacer(n, de, à, par)`. Le cours de graphes retrouve $T(n) = 2T(n-1) + 1$ pour $n > 1$, avec $T(1) = 1$, d'où [[Erreurs du cours#^e-tours-de-hanoi|✎]] $T(n) = \sum_{k=0}^{n-1} 2^k = 2^n - 1$ et $\Theta(2^n)$ : voir [[Complexité algorithmique]] et [[Calcul de complexité et théorème de résolution]].

## Compléments (complément, hors du cours)

- **Origine** : casse-tête publié en 1883 par le mathématicien Édouard Lucas.
- **Règles** : trois piliers ; on ne déplace qu'un disque à la fois, celui du dessus d'une pile, et on ne pose jamais un disque sur un plus petit.
- **Minimalité** : le grand disque doit bouger au moins une fois ; avant son premier déplacement, les $n - 1$ autres doivent tous être dégagés sur le troisième pilier (au moins $f(n-1)$ coups), et après son dernier, reposés sur lui (encore au moins $f(n-1)$ coups). Donc $f(n) \ge 2f(n-1) + 1$, et l'algorithme récursif atteint cette borne : il est optimal.
- **Trouver $2^n - 1$ sans le deviner** : avec $v_n = f(n) + 1$, la relation $f(n) = 2f(n-1) + 1$ devient $v_n = 2v_{n-1}$ ; $(v_n)$ est une [[Suite géométrique|suite géométrique]] de raison 2 et $v_0 = 1$, donc $v_n = 2^n$ et $f(n) = 2^n - 1$.
- **Ordre de grandeur** : pour 64 disques, $2^{64} - 1 \approx 1{,}8 \times 10^{19}$ coups ; à un coup par seconde, environ 585 milliards d'années.
- **Version Python** :

```python
def hanoi(n, de, a, par):
    if n == 0:          # cas de base : rien à déplacer
        return
    hanoi(n - 1, de, par, a)
    print(de, "->", a)
    hanoi(n - 1, par, a, de)

hanoi(3, "A", "C", "B")   # 7 déplacements
```

Notion parente : [[Récursivité]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[3 - complexité]], [[0 - diapo prof]]
