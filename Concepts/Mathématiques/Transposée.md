---
type: concept
tags:
  - year1
  - year2
  - year3
aliases:
  - transpose
  - transposes
  - transposée d'une matrice
  - transposed matrix
matieres:
  - Bilinear Algebra
  - Algèbre Linéaire
  - Data analysis (Thanos)
sources:
  - "[[Chp 0b - Matrix algebra (résumé)|Chp 0b - Matrix algebra]]"
  - "[[chp4 (résumé)|chp4 (Algèbre)]]"
  - "[[Summary functions in RStudio (résumé)|Summary functions in RStudio]]"
maj: 2026-11-06
---

La transposée $A^T$ d'une matrice $A$ de taille $m \times n$ est la matrice $n \times m$ dont les colonnes sont les lignes de $A$.

Propriétés : $(A^T)^T = A$, $(A + B)^T = A^T + B^T$, $(rA)^T = rA^T$, $(AB)^T = B^TA^T$ et $(ABC)^T = C^TB^TA^T$.

Le chapitre sur les déterminants ajoute $\det A^T = \det A$.

Le cours de 1re année (Algèbre Linéaire, chp4) dit seulement que la transposée d'une matrice $A$ de format $(n, p)$ est une matrice $A'$ de format $(p, n)$. En R (Data analysis), la fonction `t()` donne la transposée d'une matrice ([[Langage R]]).

Notion parente : [[Matrice]]. Liens : [[Matrice symétrique]], [[Déterminant]], [[Produit matriciel]], [[Sous-espaces fondamentaux]]

## À vérifier

- [[chp4 (résumé)|chp4 (Algèbre)]] ne donne que le format de la transposée, pas la règle $a'_{ij} = a_{ji}$.

Résumés : [[Chp 0b - Matrix algebra (résumé)]], [[Chp 0c - Determinants (résumé)]], [[chp4 (résumé)|chp4 (résumé)]], [[Summary functions in RStudio (résumé)]]
