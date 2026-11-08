---
type: concept
tags: [year2]
aliases: [dot product, inner product, produits scalaires, produit hermitien, similarité cosinus, cosine similarity]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
---

Opération qui associe un nombre à deux vecteurs. Dans $\mathbb{R}^n$, le dot product vaut $\mathbf{x} \cdot \mathbf{y} = x_1y_1 + \dots + x_ny_n = \mathbf{x}^T\mathbf{y}$. L'inner product $\langle \mathbf{u}, \mathbf{v} \rangle$ est plus général : un dot product est un inner product, mais la réciproque est fausse.

Propriétés dans $\mathbb{R}^n$ : symétrie, linéarité par rapport à chaque vecteur, et $\mathbf{u} \cdot \mathbf{u} \ge 0$, avec égalité seulement pour $\mathbf{u} = \mathbf{0}$. La [[Norme]] s'en déduit : $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$. Géométriquement, $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$, et le résultat est un scalaire.

## Compléments (hors du cours)

**Définition générale d'un inner product** sur un espace vectoriel réel $V$ : une application $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$
- symétrique : $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$ ;
- bilinéaire : linéaire par rapport à chaque argument ;
- définie positive : $\langle \mathbf{u}, \mathbf{u} \rangle > 0$ pour tout $\mathbf{u} \neq \mathbf{0}$.

Exemples : le produit pondéré $\langle \mathbf{u}, \mathbf{v} \rangle = \sum_i w_i u_i v_i$ avec tous les $w_i > 0$ ; sur l'espace des fonctions continues sur $[a,b]$, $\langle f, g \rangle = \int_a^b f(t)g(t)\,dt$.

**Angle entre deux vecteurs non nuls** : $\cos\theta = \dfrac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$. Ce quotient est toujours dans $[-1, 1]$ grâce à l'[[Inégalité de Cauchy-Schwarz]], ce qui rend l'angle bien défini. Le signe de $\mathbf{u} \cdot \mathbf{v}$ donne la nature de l'angle : positif, angle aigu ; nul, angle droit ([[Orthogonalité|vecteurs orthogonaux]]) ; négatif, angle obtus. Ce même quotient est la **similarité cosinus** (cosine similarity), utilisée en fouille de textes pour comparer deux documents représentés par des vecteurs de fréquences de mots.

**Cas complexe** : sur $\mathbb{C}^n$, on utilise le produit hermitien $\langle \mathbf{u}, \mathbf{v} \rangle = \sum_i u_i \overline{v_i}$, qui donne $\langle \mathbf{v}, \mathbf{v} \rangle = \sum_i |v_i|^2 \ge 0$ (sans conjugué, $(i)\cdot(i) = -1$ serait négatif). Il est linéaire en la première variable et semi-linéaire en la seconde : c'est l'origine du conjugué dans la propriété $\langle \mathbf{u}, \lambda\mathbf{v} \rangle = \overline{\lambda}\langle \mathbf{u}, \mathbf{v} \rangle$ (voir [[Nombre complexe]]).

C'est l'exemple type de forme bilinéaire. Notion parente : [[Forme bilinéaire]]. Liens : [[Orthogonalité]], [[Norme]], [[Inégalité de Cauchy-Schwarz]], [[Nombre complexe]]

Résumés : [[1 - Orthogonality]], [[2 - Symmetric matrices and quadratic forms]]
