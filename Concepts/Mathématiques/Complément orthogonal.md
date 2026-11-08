---
type: concept
tags: [year2]
aliases: [orthogonal complement, orthogonal complements, compléments orthogonaux, W perp]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]"]
maj: 2026-11-08
---

$W^\perp$ est l'ensemble des vecteurs orthogonaux à tous les vecteurs du sous-espace $W$. C'est lui-même un sous-espace de $\mathbb{R}^n$. Pour une matrice $A$ de taille $m \times n$ (Theorem 3) : $(\text{Row } A)^\perp = \text{Nul } A$ et $(\text{Col } A)^\perp = \text{Nul } A^T$, ce qui relie les [[Sous-espaces fondamentaux|sous-espaces fondamentaux]].

Exemple du cours : dans $\mathbb{R}^3$, un plan $W$ et la droite $L$ qui lui est perpendiculaire, tous deux passant par l'origine, vérifient $L = W^\perp$ et $W = L^\perp$. Autre exemple : pour $A = \begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$, Nul $A$ est la droite dirigée par $(1,-2,1)$, perpendiculaire au plan Row $A$, et Nul $A^T = \{\mathbf{0}\}$.

## Compléments (hors du cours)

**Critère pratique** : $\mathbf{x} \in W^\perp$ si et seulement si $\mathbf{x}$ est orthogonal à chaque vecteur d'une famille génératrice de $W$. Il suffit donc de tester les vecteurs d'une base, et non tous les vecteurs de $W$.

**Propriétés** (dans $\mathbb{R}^n$) :
- $W \cap W^\perp = \{\mathbf{0}\}$ (un vecteur orthogonal à lui-même est nul) ;
- $\dim W + \dim W^\perp = n$ ;
- $(W^\perp)^\perp = W$ ;
- $\mathbb{R}^n = W \oplus W^\perp$ ([[Somme directe]]), ce qui est le contenu du théorème de décomposition orthogonale ([[Projection orthogonale]]).

**Pourquoi $(\text{Row } A)^\perp = \text{Nul } A$** : la $i$-ème coordonnée de $A\mathbf{x}$ est le [[Produit scalaire|dot product]] de la $i$-ème ligne de $A$ avec $\mathbf{x}$. Donc $A\mathbf{x} = \mathbf{0}$ si et seulement si $\mathbf{x}$ est orthogonal à toutes les lignes, c'est-à-dire (critère ci-dessus) à Row $A$. La seconde égalité s'obtient en appliquant la première à $A^T$, dont les lignes sont les colonnes de $A$. Combiné au [[Théorème du rang]], on retrouve $\dim \text{Row } A + \dim \text{Nul } A = n$.

Vérification sur l'exemple du cours : $(1,-2,1)\cdot(1,2,3) = 1 - 4 + 3 = 0$ et $(1,-2,1)\cdot(4,5,6) = 4 - 10 + 6 = 0$ ; $A$ est de rang 2, donc $\dim \text{Row } A + \dim \text{Nul } A = 2 + 1 = 3$.

Notion parente : [[Orthogonalité]]. Voir aussi : [[Somme directe]], [[Théorème du rang]], [[Sous-espaces fondamentaux]], [[Sous-espace vectoriel]], [[Espace nul]], [[Espace des colonnes]], [[Projection orthogonale]]

Résumé : [[1 - Orthogonality]]
