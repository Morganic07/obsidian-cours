---
type: concept
tags: [year4]
aliases: [volume d'un solide, volume du cylindre, volume de la sphère, volume de la boule, volume du cube]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.3.c|6.3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : le volume mesure l'espace occupé par un solide. Il s'exprime en unités de longueur au cube (m³, cm³ ; 1 L = 1 dm³). Comme l'[[Aire (géométrie)|aire]] en dimension 2, il est additif et invariant par déplacement ; multiplier toutes les longueurs par $k$ multiplie le volume par $k^3$.

Formules usuelles :

| Solide | Volume |
|---|---|
| Cube d'arête $a$ | $a^3$ |
| Pavé droit de dimensions $L$, $l$, $h$ ([[Pavé]]) | $L \times l \times h$ |
| Prisme ou cylindre de base d'aire $B$ et de hauteur $h$ | $B \times h$ |
| Cylindre de révolution de rayon $r$ et de hauteur $h$ | $\pi r^2 h$ |
| Pyramide ou cône de base d'aire $B$ et de hauteur $h$ | $\dfrac{B \times h}{3}$ |
| Cône de révolution | $\dfrac{\pi r^2 h}{3}$ |
| Boule (intérieur de la sphère) de rayon $r$ | $\dfrac{4}{3}\pi r^3$ |

Le cylindre est une base qui « s'empile » sur la hauteur, d'où aire de la base fois hauteur ; le cône et la pyramide en valent le tiers. Le volume d'un solide quelconque se calcule par une [[Intégrale multiple|intégrale triple]], souvent en [[Coordonnées cylindriques|coordonnées cylindriques]] ou [[Coordonnées sphériques|sphériques]] ; c'est ainsi que l'on retrouve $\frac43 \pi r^3$. Les formules font intervenir le [[Nombre pi|nombre π]].

En programmation, deux pièges classiques : $\frac43$ écrit `4/3` entre entiers vaut 1 ([[Division euclidienne]]), il faut `4.0/3` ; et une fonction qui renvoie un `int` tronque le volume. Le cube $a^3$ s'écrit `a*a*a` ou `pow(a, 3)` ([[Exponentiation]]).

## Dans le cours

- [[tp6]] : les fonctions `volumeCube`, `volumeCylindre` et `volumeSphere` du programme 6.3 ; les formules d'origine du cylindre ($\pi h r$ au lieu de $\pi r^2 h$) et de la sphère ($\frac34 \pi r^3$ au lieu de $\frac43 \pi r^3$) sont corrigées dans la fiche.

Voir aussi : [[Aire (géométrie)]], [[Nombre pi]], [[Intégrale multiple]].
