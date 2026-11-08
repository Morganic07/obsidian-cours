---
type: concept
tags: [year2]
aliases: [elementary matrix, elementary matrices, matrices élémentaires]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0b - Matrix algebra.docx|Chp 0b - Matrix algebra]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : une matrice élémentaire est la matrice obtenue en appliquant **une seule** [[Opérations élémentaires sur les lignes|opération élémentaire sur les lignes]] à la matrice identité $I_n$. Il y en a trois sortes :

- **échange** de deux lignes ($L_i \leftrightarrow L_j$) ;
- **multiplication** d'une ligne par un scalaire non nul ($L_i \leftarrow cL_i$, $c \neq 0$) ;
- **ajout** à une ligne d'un multiple d'une autre ($L_i \leftarrow L_i + cL_j$, $i \neq j$).

**Propriété** : effectuer cette opération sur une matrice $A$ à $m$ lignes revient à calculer le [[Produit matriciel|produit]] $EA$, où $E$ est la matrice élémentaire $m \times m$ correspondante.

**Inversibilité** : toute matrice élémentaire est [[Matrice inversible|inversible]], et son inverse est la matrice élémentaire de l'opération inverse (échanger à nouveau les deux lignes, multiplier par $1/c$, ajouter $-c$ fois la ligne). Par exemple, l'inverse de $L_2 \leftarrow L_2 - 2L_1$ est $L_2 \leftarrow L_2 + 2L_1$.

**Exemple** : pour $n = 2$, la matrice élémentaire de $L_2 \leftarrow L_2 - 2L_1$ est

$$E = \begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}, \qquad E^{-1} = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}.$$

**Application au calcul de l'inverse** : si une suite d'opérations réduit $A$ à $I$, soit $E_k \cdots E_1 A = I$, alors $A^{-1} = E_k \cdots E_1$, c'est-à-dire le résultat des mêmes opérations appliquées à $I$. C'est ce qui justifie l'algorithme qui réduit $[A \ \ I]$ en $[I \ \ A^{-1}]$. On en tire aussi qu'une matrice est inversible si et seulement si elle est un produit de matrices élémentaires.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[0 - Matrix algebra]], pour expliquer pourquoi la réduction de $[A \ \ I]$ donne $A^{-1}$.

Voir aussi : [[Opérations élémentaires sur les lignes]], [[Matrice inversible]], [[Produit matriciel]], [[Forme échelonnée]], [[Théorème de la matrice inversible]]

Résumés : [[0 - Matrix algebra]]
