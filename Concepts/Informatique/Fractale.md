---
type: concept
tags:
  - year1
aliases:
  - fractales
  - flocon de Koch
  - autosimilaire
  - fractal
  - Koch snowflake
  - dimension fractale
  - fractal dimension
matieres:
  - Algo Maths
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
maj: 2026-11-08
---

Motif autosimilaire défini par récurrence ($u_0, u_1, u_2, \dots, u_n$). Selon Cours 1, les fractales ont un périmètre infini ; exemple : le flocon de Koch.

## Compléments (hors du cours)

**Origine** : le mot « fractale » est forgé par Benoît Mandelbrot en 1975 (*Les Objets fractals*), du latin *fractus*, « brisé ». Une fractale est une figure dont chaque partie, agrandie, ressemble au tout (autosimilarité), et dont l'irrégularité se retrouve à toutes les échelles.

**Construction du flocon de Koch** (Helge von Koch, 1904) : on part d'un triangle équilatéral de côté $a$ (ordre 0). À chaque étape, chaque segment est divisé en trois ; le tiers central est remplacé par deux côtés d'un triangle équilatéral pointant vers l'extérieur. Chaque segment devient ainsi **4 segments trois fois plus courts**.

- Nombre de côtés : $3 \times 4^n$ ; longueur d'un côté : $a / 3^n$.
- Périmètre : $P_n = 3 \times 4^n \times \dfrac{a}{3^n} = 3a\left(\dfrac{4}{3}\right)^n \xrightarrow[n \to \infty]{} +\infty$, puisque $4/3 > 1$ (suite géométrique).
- Aire : avec $A_0 = \dfrac{\sqrt{3}}{4} a^2$ l'aire du triangle initial, l'étape $n$ ajoute $3 \times 4^{n-1}$ petits triangles d'aire $A_0 / 9^n$, et l'aire tend vers $A_0\left(1 + \dfrac{1}{3}\sum_{k \ge 0}\left(\dfrac{4}{9}\right)^k\right) = A_0\left(1 + \dfrac{1}{3} \times \dfrac{9}{5}\right) = \dfrac{8}{5} A_0$.

Le flocon a donc un **périmètre infini** qui enclôt une **aire finie**.

**Dimension fractale** (dimension d'autosimilarité) : si une figure se compose de $N$ copies d'elle-même réduites d'un facteur $k$, sa dimension vaut
$$D = \frac{\ln N}{\ln k}.$$
Un segment ($N = k$) a la dimension 1, un carré ($N = k^2$) la dimension 2. Pour la courbe de Koch, $N = 4$ et $k = 3$, d'où $D = \ln 4 / \ln 3 \approx 1{,}26$ : plus qu'une ligne, moins qu'une surface.

**Exemples naturels** : côtes rocheuses (leur longueur mesurée augmente quand on raccourcit l'unité de mesure, question posée par Mandelbrot en 1967 dans l'article « How Long Is the Coast of Britain? », à propos de la côte de la Grande-Bretagne), fougères, chou romanesco, ramifications des bronches, des rivières et des éclairs. Autres fractales célèbres : triangle de Sierpiński, ensemble de Mandelbrot.

**Tracé récursif** : une fractale se dessine naturellement par [[Récursivité|récursivité]], avec un cas de base d'ordre 0.

```python
import turtle

def koch(longueur, ordre):
    if ordre == 0:                 # cas de base : un simple segment
        turtle.forward(longueur)
    else:
        for angle in (60, -120, 60, 0):
            koch(longueur / 3, ordre - 1)
            turtle.left(angle)

def flocon(longueur, ordre):
    for _ in range(3):
        koch(longueur, ordre)
        turtle.right(120)
```

Notion parente : [[Récurrence]]. Voir aussi : [[Récursivité]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]]
