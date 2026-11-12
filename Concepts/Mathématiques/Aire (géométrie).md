---
type: concept
tags: [year4]
aliases: [aire d'un rectangle, aire du disque, area]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.6.c|2.6.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'aire mesure l'étendue d'une surface plane. Elle s'exprime en unités de longueur au carré (m², cm²) : un carré de 1 cm de côté a une aire de 1 cm². L'aire est **additive** (celle d'une figure découpée en morceaux sans recouvrement est la somme des aires des morceaux) et invariante par déplacement (translation, rotation, symétrie : voir [[Transformations géométriques du plan]]).

Formules usuelles :

| Figure | Aire |
|---|---|
| Rectangle de longueur $L$ et de largeur $l$ | $L \times l$ |
| Carré de côté $a$ | $a^2$ |
| Triangle de base $b$ et de hauteur $h$ | $\dfrac{b \times h}{2}$ |
| Parallélogramme | base × hauteur |
| Trapèze de bases $B$, $b$ et de hauteur $h$ | $\dfrac{(B + b)\,h}{2}$ |
| Disque de rayon $r$ | $\pi r^2$ (voir [[Nombre pi]]) |

L'aire d'une figure délimitée par des courbes se calcule par une [[Intégrale|intégrale]] (aire sous le [[Graphe d'une fonction|graphe d'une fonction]]) ou par une [[Intégrale multiple|intégrale double]]. Multiplier toutes les longueurs par $k$ ([[Homothétie|homothétie]] de rapport $k$) multiplie l'aire par $k^2$ ; le [[Volume (géométrie)|volume]] est la notion analogue en dimension 3, où le facteur devient $k^3$.

En programmation, une aire calculée sur des entiers peut dépasser la capacité du type : avec des `int` de 32 bits, un rectangle de 50 000 × 50 000 donne $2{,}5 \times 10^9$, au-delà de $2^{31} - 1$ ([[Dépassement d'entier]]).

## Dans le cours

- [[tp2]] : le programme 2.6 lit la largeur et la longueur d'un rectangle et affiche leur produit, son aire.

Voir aussi : [[Volume (géométrie)]], [[Nombre pi]], [[Théorème de Pythagore]].
