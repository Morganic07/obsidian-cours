---
type: concept
tags: [year2]
aliases: [hessienne, hessiennes, matrices hessiennes, Hessian matrix, Hessian]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : pour $f : U \subset \mathbb{R}^p \to \mathbb{R}$ de classe $\mathcal{C}^2$ et $a \in U$, la matrice hessienne de $f$ en $a$ est la matrice $p \times p$ des dérivées secondes
$$H_f(a) = \left(\frac{\partial^2 f}{\partial x_i \partial x_j}(a)\right)_{1 \le i, j \le p}.$$
Pour $p = 2$, avec les notations de Monge : $H_f = \begin{pmatrix} r & s \\ s & t \end{pmatrix}$, où $r = \dfrac{\partial^2 f}{\partial x^2}$, $s = \dfrac{\partial^2 f}{\partial x \partial y}$, $t = \dfrac{\partial^2 f}{\partial y^2}$.

- Elle est **symétrique** par le [[Théorème de Schwarz]], donc diagonalisable en base orthonormée, à valeurs propres réelles ([[Théorème spectral]]).
- C'est la [[Matrice jacobienne|jacobienne]] du [[Gradient|gradient]] $x \mapsto \vec\nabla_x f$.
- **Formule de Taylor-Young à l'ordre 2** :
$$f(a + h) = f(a) + \vec\nabla_a f \cdot h + \tfrac{1}{2}\,{}^t h\, H_f(a)\, h + o(\|h\|^2),$$
la partie d'ordre 2 étant une [[Forme quadratique]] en $h$.
- **Nature d'un point critique** ($\vec\nabla_a f = 0$) : $H_f(a)$ [[Forme quadratique définie positive|définie positive]] ⇒ minimum local strict ; définie négative ⇒ maximum local strict ; valeurs propres non nulles de signes opposés ⇒ point col ; une valeur propre nulle ⇒ on ne peut pas conclure à l'ordre 2. Pour $p = 2$, $\det H_f = rt - s^2$ : $rt - s^2 > 0$ et $r > 0$ (minimum), $rt - s^2 > 0$ et $r < 0$ (maximum), $rt - s^2 < 0$ (col).

**Exemple** : $f(x, y) = x^2 + xy + y^2 - 3x$, $H_f = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, de valeurs propres $1$ et $3$ : définie positive, et le point critique $(2, -1)$ est un minimum local.

## Dans le cours

Le cours ne la nomme pas : il traite les extrema de deux variables avec les notations $r$, $s$, $t$. Elle apparaît dans les compléments de [[5 - Calcul différentiel d'ordre supérieur]].

Voir aussi : [[Extremum local d'une fonction de deux variables]], [[Forme quadratique définie positive]], [[Forme quadratique]], [[Théorème de Schwarz]], [[Valeur propre]], [[Reste de Taylor]].

Résumés : [[5 - Calcul différentiel d'ordre supérieur]]
