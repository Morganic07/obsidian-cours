---
type: concept
tags: [year1]
aliases: [racines de l'unité, racine de l'unité, racines n-ièmes de l'unité, roots of unity, root of unity]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 5 - Complexes.docx|Chapitre 5 - Complexes]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : pour un entier $n \ge 1$, une racine $n$-ième de l'unité est un [[Nombre complexe|nombre complexe]] $z$ tel que $z^n = 1$. Il y en a exactement $n$ :
$$\omega_k = e^{2ik\pi/n}, \qquad k = 0, 1, \dots, n-1.$$

**Démonstration.** On écrit $z = re^{i\theta}$ avec $r > 0$ ([[Forme trigonométrique et exponentielle]]). Alors $z^n = r^n e^{in\theta}$, et $z^n = 1 = 1 \cdot e^{i0}$ impose $r^n = 1$, donc $r = 1$ ($r$ réel positif), et $n\theta \equiv 0 \pmod{2\pi}$, soit $\theta = \frac{2k\pi}{n}$ avec $k \in \mathbb{Z}$. Deux valeurs de $k$ donnent le même complexe si et seulement si elles diffèrent d'un multiple de $n$ : les valeurs $k = 0, \dots, n-1$ donnent donc les $n$ racines distinctes.

**Propriétés.**
- $\omega_k = \omega_1^k$ : toutes les racines sont les puissances de $\omega_1 = e^{2i\pi/n}$.
- Toutes ont pour module 1 : les points d'affixe $\omega_k$ sont les sommets d'un polygone régulier à $n$ côtés inscrit dans le cercle trigonométrique, dont un sommet est le point d'affixe 1.
- Pour $n \ge 2$, leur somme est nulle : c'est une somme géométrique de raison $\omega_1 \ne 1$ ([[Suite géométrique]]),
$$\sum_{k=0}^{n-1} \omega_1^k = \frac{1 - \omega_1^n}{1 - \omega_1} = \frac{1 - 1}{1 - \omega_1} = 0.$$
- Le conjugué d'une racine $n$-ième est encore une racine $n$-ième : $\overline{\omega_k} = \omega_{n-k}$.

**Cas particuliers.**
- $n = 2$ : $1$ et $-1$.
- $n = 3$ : $1$, $j = e^{2i\pi/3} = \dfrac{-1 + i\sqrt3}{2}$ et $j^2 = \bar j = \dfrac{-1 - i\sqrt3}{2}$. On a $1 + j + j^2 = 0$ : $j$ et $j^2$ sont les racines de $z^2 + z + 1$, puisque $z^3 - 1 = (z - 1)(z^2 + z + 1)$. Les trois points forment un triangle équilatéral.
- $n = 4$ : $1$, $i$, $-1$, $-i$ (un carré).

**Méthode** : pour résoudre $z^n = a$ avec $a = \rho e^{i\alpha} \ne 0$, une solution est $z_0 = \rho^{1/n} e^{i\alpha/n}$, et les $n$ solutions sont $z_0\,\omega_k$.

## Dans le cours

Le cours ne les traite pas. Elles apparaissent dans les compléments de [[5 - Complexes]]. L'équation $z^2 + z + 1 = 0$, dont les racines sont $j$ et $j^2$, figure au contrôle d'Outils math ([[Nombre complexe]]).

Voir aussi : [[Nombre complexe]], [[Forme trigonométrique et exponentielle]], [[Suite géométrique]], [[Théorème fondamental de l'algèbre]], [[Polynôme]].

Résumés : [[5 - Complexes]]
