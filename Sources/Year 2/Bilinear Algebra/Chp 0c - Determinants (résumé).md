---
type: source
sources: ["[[Chp 0c - Determinants]]"]
maj: 2026-11-05
---

Résumé de [[Chp 0c - Determinants]], dans [[Year 2 - Bilinear Algebra]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le [[Déterminant]] résume une matrice carrée en un nombre, qui dit si elle est inversible et mesure un volume.

## Contenu, dans l'ordre du cours

- **Définition** : $ad - bc$ en taille 2, puis $\det A = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} \det A_{1j}$. Pour une matrice triangulaire, c'est le produit de la diagonale.
- **Opérations sur les lignes** (aussi valables sur les colonnes) : ajouter un multiple d'une ligne ne change rien, échanger deux lignes change le signe, multiplier une ligne par $k$ multiplie le déterminant par $k$.
- **Nullité** : $\det A = 0$ si et seulement si les lignes ou les colonnes sont dépendantes. En pratique, cela se voit quand deux lignes sont identiques ou qu'une ligne est nulle.
- **Géométrie** : $|\det A|$ est l'aire du parallélogramme (taille 2) ou le volume du parallélépipède (taille 3) défini par les colonnes.
- **Propriétés** : $\det A^T = \det A$ et $\det AB = (\det A)(\det B)$.
- **Règle de Cramer** : $x_i = \frac{\det A_i(\mathbf{b})}{\det A}$, où $A_i(\mathbf{b})$ est $A$ dont la colonne $i$ est remplacée par $\mathbf{b}$. Le cours la dit efficace en tailles 2 et 3.
- **Formule de l'inverse** : $A^{-1} = \frac{1}{\det A} \text{adj } A$, où adj $A$ est la transposée de la matrice des cofacteurs.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **$\det A = (\text{adj } A)A$** : image lue directement, c'est bien ce que le cours écrit, et c'est souligné. Or le membre de gauche est un nombre et celui de droite une matrice. On attendrait $(\det A)\,I = (\text{adj } A)A$ (complément). Tu as déjà coché ce point dans ta liste, sans que je connaisse ta conclusion.
