---
type: concept
tags:
  - year1
  - year2
aliases:
  - linear transformation
  - linear transformations
  - linear map
  - linear maps
  - application linéaire
  - applications linéaires
  - matrix transformation
  - transformation matricielle
  - linear function
sources:
  - "[[0 - Linear combination|Chp 0a - Linear combination]]"
  - "[[0 - Matrix algebra|Chp 0b - Matrix algebra]]"
  - "[[0 - Vector Space|Chp 0d - Vector Space]]"
  - "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2 (Algèbre)]]"
  - "[[4 - Algèbre linéaire|chp4 (Algèbre)]]"
  - "[[5 - Algèbre linéaire|chp5 (Algèbre)]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-07
---

Application $T$ telle que $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ et $T(c\mathbf{u}) = cT(\mathbf{u})$. On en déduit $T(\mathbf{0}) = \mathbf{0}$ et $T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$. En 1re année : $f : E \to F$ est linéaire si $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$, elle respecte les combinaisons linéaires, donc $f(0_E) = 0_F$. L'ensemble des applications linéaires de $V$ dans $W$ se note $L(V, W)$ ; $L(E, F)$ et $L(E)$ sont des espaces vectoriels. Voir aussi [[Morphisme]].

- **Vocabulaire** : pour $T : \mathbb{R}^n \to \mathbb{R}^m$, $\mathbb{R}^n$ est le domain, $\mathbb{R}^m$ le codomain, et l'ensemble des images le range.
- **Matrices** : toute transformation matricielle $\mathbf{x} \mapsto A\mathbf{x}$ est linéaire, avec $A$ de taille $m \times n$. Son range est Col $A$.
- **Noyau et image** : $\ker(T) = \{\mathbf{v} \mid T\mathbf{v} = \mathbf{0}\}$ ([[Espace nul]]) et $\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$ ([[Image d'une application linéaire]]).
- **Inversible** : $T$ de $\mathbb{R}^n$ dans $\mathbb{R}^n$ est inversible s'il existe $S$ telle que $S(T(\mathbf{x})) = \mathbf{x}$ et $T(S(\mathbf{x})) = \mathbf{x}$.
- **Exemples dans le plan** : réflexions, contractions et dilatations, cisaillements, projections ([[Transformations géométriques du plan]]). Leurs matrices sont dans [[0 - Linear combination|Chp 0a - Linear combination]] ; deux annotations du tableau des réflexions y sont fausses (voir « Erreurs du cours » de [[Transformations géométriques du plan]]). L'[[Homothétie]] $f(x) = \lambda x$ est un autre exemple.
- **Matrice dans des bases** ([[Matrice d'une application linéaire]]) : ses colonnes sont les coordonnées des images des vecteurs de la base de départ. Celle d'une composée est le produit : $M_{g \circ f} = M_g \times M_f$. Elle dépend des bases, voir [[Changement de base]] : $A' = P^{-1}AP$ ([[5 - Algèbre linéaire|chp5]]).
- **[[Composition de fonctions|Composition]]** : $(f + g) \circ h = f \circ h + g \circ h$ et $h \circ (f + g) = h \circ f + h \circ g$. La composée de deux applications linéaires est linéaire, $f^n = f \circ \ldots \circ f$ et $f^0 = \mathrm{Id}_E$, et $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ (le cours de Year 1 écrit l'ordre inverse).
- **Rang** : $\text{rg}(f) = \dim \text{Im}(f)$, et Im$(f)$ est engendrée par les images d'une base. Voir [[Théorème du rang]].
- **En Bilinear Algebra, chapitre 2** : $L(V, W)$ y est introduit, et le cours remarque que le déterminant est linéaire en une colonne quand les autres sont fixées (voir aussi [[Forme linéaire]]).

L'évaluation 3 d'algèbre linéaire ([[Raw/Year 1/Contrôles.pdf|Contrôles]]) demande de reconnaître des applications linéaires ou non, et d'écrire la matrice d'une application dans une base de $\mathbb{R}^3$.

Voir aussi : [[Espace nul]], [[Espace des colonnes]], [[Injectivité et surjectivité]], [[Matrice inversible]], [[Morphisme]], [[Rang d'une matrice]], [[Changement de base]], [[Image d'une application linéaire]], [[Théorème du rang]], [[Matrice d'une application linéaire]], [[Homothétie]], [[Composition de fonctions]], [[Transformations géométriques du plan]], [[Forme linéaire]]

## Erreurs du cours

- [[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]] écrit, pour le corps des scalaires, « F is a field (ensemble), F = lR, F = lN ... » ; il faut un corps, par exemple $\mathbb{R}$ ou $\mathbb{C}$ : $\mathbb{N}$ n'est pas un corps.

Résumés : [[0 - Linear combination]], [[0 - Matrix algebra]], [[0 - Vector Space]], [[2 - Symmetric matrices and quadratic forms]], [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]], [[4 - Algèbre linéaire|chp4]], [[5 - Algèbre linéaire|chp5]]
