---
type: concept
tags: [year4]
aliases: [nombre π, constante π, constante d'Archimède, M_PI]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp6/6.3.c|6.3.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : $\pi$ est la constante mathématique égale au rapport de la circonférence d'un cercle à son diamètre, le même pour tous les cercles :

$$\pi \approx 3{,}14159\,26535\,89793$$

Il intervient dans le périmètre du cercle ($2\pi r$), l'[[Aire (géométrie)|aire]] du disque ($\pi r^2$), les [[Volume (géométrie)|volumes]] du cylindre ($\pi r^2 h$) et de la boule ($\frac43 \pi r^3$), et bien au-delà de la géométrie : mesure des angles en radians (un tour vaut $2\pi$, voir [[Fonctions trigonométriques]] et [[Fonction périodique]]), [[Intégrale de Gauss|intégrale de Gauss]] ($\int_{\mathbb R} e^{-x^2}\,dx = \sqrt\pi$), formule d'Euler $e^{i\pi} + 1 = 0$ ([[Forme trigonométrique et exponentielle]]), [[Formule de Stirling|formule de Stirling]].

Propriétés et histoire :

- Archimède (IIIe siècle av. J.-C.) l'encadre entre $3 + \frac{10}{71}$ et $3 + \frac17$ à l'aide de polygones inscrits et circonscrits à 96 côtés, d'où le nom de « constante d'Archimède » ;
- $\pi$ est **irrationnel** (Lambert, 1761) : son écriture décimale ne se termine pas et n'est pas périodique ([[Nombre rationnel]]) ;
- il est **transcendant** (Lindemann, 1882) : il n'est racine d'aucun [[Polynôme|polynôme]] non nul à coefficients entiers, ce qui démontre l'impossibilité de la quadrature du cercle à la règle et au compas ;
- $\frac{22}{7}$ et $\frac{355}{113}$ en sont des approximations classiques, la seconde juste à $3 \times 10^{-7}$ près.

**En programmation.** La [[Norme du C|norme du C]] ne définit pas de constante $\pi$. La macro `M_PI` de `<math.h>` vient de [[POSIX]] et n'existe pas sur toutes les plateformes (avec MSVC, il faut définir `_USE_MATH_DEFINES`). Le plus [[Portabilité (informatique)|portable]] est de définir sa propre [[Constante (programmation)|constante]], ou de la calculer par `acos(-1.0)` ; le [[Langage C++|C++]]20 fournit `std::numbers::pi` (en-tête `<numbers>`). Un `double` ne retient qu'environ 16 chiffres significatifs ([[Norme IEEE 754]]) : écrire plus de décimales dans le littéral ne change rien au résultat.

```c
#define PI 3.14159265358979323846     // ou : const double PI = acos(-1.0);
double aire = PI * r * r;
```

## Dans le cours

- [[tp6]] : $\pi$ est écrit en [[Valeur littérale|littéral]] `3.14159265358979323846` dans les volumes du cylindre et de la sphère (programme 6.3) ; la fiche conseille une constante nommée et signale que `M_PI` vient de POSIX.

Voir aussi : [[Aire (géométrie)]], [[Volume (géométrie)]], [[Nombre d'or]], [[Constante d'Euler]].
