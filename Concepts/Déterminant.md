---
type: concept
aliases: [determinant, determinants, déterminants]
matieres: [Bilinear Algebra, Algèbre Linéaire]
sources: ["[[Chp 0c - Determinants]]", "[[Chp 0b - Matrix algebra]]", "[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

Nombre associé à une matrice carrée : $ad - bc$ en taille 2, et $\det A = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} \det A_{1j}$ en général. Pour une matrice triangulaire, c'est le produit de la diagonale.

- **Inversibilité** : $A$ est inversible si et seulement si $\det A \neq 0$. $\det A = 0$ équivaut à des lignes ou des colonnes dépendantes.
- **Opérations sur les lignes ou les colonnes** : ajouter un multiple d'une ligne à une autre ne change rien, échanger deux lignes change le signe, multiplier une ligne par $k$ multiplie le déterminant par $k$.
- **Propriétés** : $\det A^T = \det A$ et $\det AB = (\det A)(\det B)$.
- **Géométrie** : $|\det A|$ est l'aire du parallélogramme ou le volume du parallélépipède défini par les colonnes.
- **Règle de Cramer** : $x_i = \frac{\det A_i(\mathbf{b})}{\det A}$, efficace en tailles 2 et 3.
- **Inverse** : $A^{-1} = \frac{1}{\det A} \text{adj } A$, où adj $A$ est la transposée de la matrice des cofacteurs.
- **Linéarité** : à colonnes fixées sauf une, le déterminant est linéaire par rapport à cette colonne.

> [!warning] À vérifier
> [[Chp 0c - Determinants]] écrit $\det A = (\text{adj } A)A$, qui égale un nombre à une matrice. On attendrait $(\det A)\,I = (\text{adj } A)A$.

Liens : [[Matrice inversible]], [[Valeur propre]], [[Transposée]], [[Produit matriciel]]

Résumé : [[Chp 0c - Determinants (résumé)]]
