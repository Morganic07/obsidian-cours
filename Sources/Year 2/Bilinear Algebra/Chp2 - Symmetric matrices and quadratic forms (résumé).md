---
type: source
sources: ["[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

Résumé de [[Chp2 - Symmetric matrices and quadratic forms]], dans [[Year 2 - Bilinear Algebra]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les matrices symétriques se diagonalisent dans une base orthonormale. Ce résultat permet de simplifier et de classer les formes quadratiques, d'optimiser sous contrainte, puis, via $A^TA$, de factoriser n'importe quelle matrice.

## Contenu, dans l'ordre du cours

- **[[Transformation linéaire]]** : le déterminant est linéaire par rapport à une colonne quand les autres sont fixées.
- **[[Forme bilinéaire]]** : $f : V \times V \to \mathbb{R}$, linéaire en chaque variable, de la forme $\mathbf{x}^TA\mathbf{y}$ sur $\mathbb{R}^n$. Le [[Produit scalaire]] en est l'exemple type.
- **[[Matrice symétrique]]** : orthogonalement diagonalisable si et seulement si $A^T = A$. Le théorème spectral lui donne $n$ valeurs propres réelles et des espaces propres orthogonaux entre eux.
- **Décomposition spectrale** : $A = \lambda_1\mathbf{u}_1\mathbf{u}_1^T + \dots + \lambda_n\mathbf{u}_n\mathbf{u}_n^T$, obtenue par le développement colonnes-lignes du produit $PDP^T$. Chaque $\mathbf{u}_j\mathbf{u}_j^T$ est une matrice de [[Projection orthogonale|projection]].
- **[[Forme quadratique]]** : $Q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$. Le changement de variable $\mathbf{x} = P\mathbf{y}$ supprime les termes croisés (axes principaux) et remet la courbe en position standard.
- **Classement** : définie positive, définie négative ou indéfinie, selon le signe des valeurs propres.
- **Optimisation sous contrainte** : sur $\|\mathbf{x}\| = 1$, le maximum de $\mathbf{x}^TA\mathbf{x}$ est la plus grande valeur propre et le minimum la plus petite. Avec les contraintes $\mathbf{x}^T\mathbf{u}_1 = \dots = \mathbf{x}^T\mathbf{u}_{k-1} = 0$, le maximum est $\lambda_k$.
- **[[Décomposition en valeurs singulières]]** : $A = U\Sigma V^T$ pour toute matrice. Les $\sigma_i = \sqrt{\lambda_i}$ viennent de $A^TA$ et sont les longueurs des $A\mathbf{v}_i$. Le cours relie aussi la SVD au conditionnement et aux [[Sous-espaces fondamentaux]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Negative definite** : le cours écrit $Q(\mathbf{x}) > 0$, la même condition que pour positive definite. Il faut lire $Q(\mathbf{x}) < 0$ pour $\mathbf{x} \neq \mathbf{0}$, comme le confirment la figure en dôme et le théorème sur les valeurs propres. **À corriger avant un examen.** La liste ne définit pas non plus « indefinite », pourtant utilisé ensuite.
2. **Corps $F$** : « $F = \mathbb{N}$ » est faux, car $\mathbb{N}$ n'est pas un corps. « field (ensemble) » est aussi trop vague : un corps n'est pas n'importe quel ensemble (complément).
3. **Coupes horizontales** : le cours annonce une parabole pour $z = 3x_1^2$. Or $3x_1^2 = c$ donne deux droites parallèles. La parabole apparaît en coupe verticale (complément). La figure ne tranche pas ce point.
4. **« $f(\mathbf{x}, \mathbf{y}) = \mathbf{x} + \mathbf{y}$ (linear form) »** : image lue directement, c'est bien écrit. Or $\mathbf{x} + \mathbf{y}$ est un vecteur, pas un nombre, alors qu'une forme donne un scalaire (complément).
5. **SVD** : « $A = U\Sigma V^r$ » est une coquille pour $V^T$, et « $n \times m$ » diffère du $m \times n$ utilisé dans tout le reste.