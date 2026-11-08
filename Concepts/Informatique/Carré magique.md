---
type: concept
tags:
  - year1
aliases:
  - carrés magiques
  - magic square
  - Lo Shu
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]"
maj: 2026-11-08
---

Grille $3 \times 3$ des 9 nombres de 1 à 9 dont chaque ligne, chaque colonne et chaque diagonale a la même somme. [[Erreurs du cours#^e-carre-magique|✎]] La somme totale vaut 45, donc la somme par direction vaut 15, et la case centrale vaut 5 ; il y a huit façons d'obtenir 15 avec trois nombres distincts. Le cours répond « 8 » au nombre de solutions.

## Compléments (complément, hors du cours)

- **Pourquoi le centre vaut 5** : les 4 alignements passant par le centre $c$ (ligne du milieu, colonne du milieu, deux diagonales) totalisent $4 \times 15 = 60$. Ils couvrent chaque case une fois, sauf le centre, compté 4 fois : $45 + 3c = 60$, donc $c = 5$.
- **Les 8 triplets et les 8 alignements** : les 8 façons d'écrire 15 avec trois nombres distincts de 1 à 9 correspondent exactement aux 8 alignements (3 lignes, 3 colonnes, 2 diagonales). Le 5 apparaît dans 4 triplets (centre), chaque pair dans 3 (coin : une ligne, une colonne, une diagonale), chaque impair autre que 5 dans 2 (milieu d'un bord) : les pairs vont dans les coins, les impairs au milieu des bords.
- **Une seule solution à symétrie près** : le carré de Lo Shu, connu en Chine depuis l'Antiquité,

$$\begin{array}{ccc} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{array}$$

  Les 8 solutions sont ses images par les 4 rotations et les 4 symétries du carré.
- **Constante magique** d'un carré $n \times n$ rempli avec $1, \ldots, n^2$ : la somme totale $\frac{n^2(n^2+1)}{2}$ se répartit sur $n$ lignes, d'où $\frac{n(n^2+1)}{2}$, soit 15 pour $n = 3$ et 34 pour $n = 4$.

Voir aussi : [[Somme des premiers entiers]].

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]]
