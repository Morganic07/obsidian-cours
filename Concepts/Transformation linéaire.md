---
type: concept
aliases: [linear transformation, linear transformations, linear map, linear maps, application linéaire, applications linéaires]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0d - Vector Space]]", "[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

Application $T$ telle que $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ et $T(c\mathbf{u}) = cT(\mathbf{u})$. On en déduit $T(\mathbf{0}) = \mathbf{0}$ et $T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$. L'ensemble des applications linéaires de $V$ dans $W$ se note $L(V, W)$.

- **Vocabulaire** : pour $T : \mathbb{R}^n \to \mathbb{R}^m$, $\mathbb{R}^n$ est le domain, $\mathbb{R}^m$ le codomain, et l'ensemble des images le range.
- **Matrices** : toute transformation matricielle $\mathbf{x} \mapsto A\mathbf{x}$ est linéaire, avec $A$ de taille $m \times n$. Son range est Col $A$.
- **Noyau et image** : $\ker(T) = \{\mathbf{v} \mid T\mathbf{v} = \mathbf{0}\}$ et $\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$.
- **Inversible** : $T$ de $\mathbb{R}^n$ dans $\mathbb{R}^n$ est inversible s'il existe $S$ telle que $S(T(\mathbf{x})) = \mathbf{x}$ et $T(S(\mathbf{x})) = \mathbf{x}$.
- **Exemples dans le plan** : réflexions, contractions et dilatations, cisaillements, projections. Leurs matrices sont dans [[Chp 0a - Linear combination]], où deux libellés du tableau des réflexions sont à vérifier.

Liens : [[Espace nul]], [[Espace des colonnes]], [[Injectivité et surjectivité]], [[Matrice inversible]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Chp 0d - Vector Space (résumé)]]
