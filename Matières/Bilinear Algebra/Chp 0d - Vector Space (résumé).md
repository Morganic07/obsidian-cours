---
type: source
tags: [year2]
sources: ["[[Chp 0d - Vector Space]]"]
maj: 2026-11-05
---

Résumé de [[Chp 0d - Vector Space]], dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre généralise les vecteurs de $\mathbb{R}^n$, puis décrit une matrice par ses quatre sous-espaces, sa dimension et son rang.

## Contenu, dans l'ordre du cours

- **[[Espace vectoriel]]** : ensemble muni d'une addition et d'une multiplication par un scalaire, soumis à dix axiomes.
- **[[Sous-espace vectoriel]]** : contient $\mathbf{0}$, stable par addition et par multiplication par un scalaire. Une droite qui ne passe pas par l'origine n'en est pas un, et $\mathbb{R}^2$ n'est pas un sous-espace de $\mathbb{R}^3$. Span$\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$ en est toujours un.
- **[[Sous-espaces fondamentaux]]** : Col $A$ et Nul $A^T$ dans $\mathbb{R}^m$, Row $A$ et Nul $A$ dans $\mathbb{R}^n$.
- **[[Espace des colonnes]]** : Col $A$ est l'ensemble des $\mathbf{b}$ pour lesquels $A\mathbf{x} = \mathbf{b}$ a une solution.
- **[[Espace nul]]** : Nul $A$ est l'ensemble des solutions de $A\mathbf{x} = \mathbf{0}$. Le cours compare Nul $A$ et Col $A$ en 8 points : Nul $A$ est défini implicitement, Col $A$ explicitement.
- **[[Base (algèbre linéaire)]]** : ensemble indépendant qui engendre $H$. Les colonnes de $I_n$ forment la base standard de $\mathbb{R}^n$, et celles de toute matrice inversible forment une base.
- **[[Dimension (algèbre linéaire)]]** et **[[Rang d'une matrice]]** : $\text{rank } A + \dim \text{Nul } A = n$.
- **Théorème de la matrice inversible** : énoncés m à r, voir [[Invertible matrix theorem]].
- **Noyau et image** : $\ker(T) = \{\mathbf{v} \mid T\mathbf{v} = \mathbf{0}\}$ et $\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$, voir [[Transformation linéaire]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Dixième axiome** : image lue directement, elle s'arrête à l'axiome 9, alors que le texte annonce dix axiomes. Le manquant est $1\mathbf{u} = \mathbf{u}$ : il figure dans les propriétés de $\mathbb{R}^n$ de [[Chp 0a - Linear combination]] et dans la définition de [[Cours/Year 1/Algèbre Linéaire/Cours/chp1|chp1 (Algèbre)]].
