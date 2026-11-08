---
type: concept
tags:
  - year2
aliases:
  - column space
  - column spaces
  - Col A
sources:
  - "[[0 - Vector Space|Chp 0d - Vector Space]]"
maj: 2026-11-08
---

Col $A = \text{Span}\{\mathbf{a}_1, \dots, \mathbf{a}_n\}$ est l'ensemble des combinaisons linéaires des colonnes de $A$, c'est-à-dire l'ensemble des $\mathbf{b}$ tels que $A\mathbf{x} = \mathbf{b}$ a une solution. C'est un sous-espace de $\mathbb{R}^m$, et l'image de la transformation $\mathbf{x} \mapsto A\mathbf{x}$.

Col $A = \mathbb{R}^m$ si et seulement si $A\mathbf{x} = \mathbf{b}$ a une solution pour tout $\mathbf{b}$, c'est-à-dire si la transformation est surjective.

Il est défini explicitement : ses vecteurs se construisent directement à partir des colonnes. En revanche, savoir si un $\mathbf{v}$ donné y appartient demande de réduire $[A \ \mathbf{v}]$. C'est l'inverse pour l'[[Espace nul]].

Le même chapitre définit l'image d'une [[Transformation linéaire]] $T$ : $\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$.

**Base de Col $A$ (complément, hors du cours)** : les colonnes pivots de $A$ forment une [[Base (algèbre linéaire)|base]] de Col $A$. On repère les pivots sur une [[Forme échelonnée|forme échelonnée]] de $A$, mais on garde les colonnes correspondantes de **$A$ elle-même** : les [[Opérations élémentaires sur les lignes|opérations sur les lignes]] changent l'espace des colonnes (elles conservent seulement les relations de dépendance entre colonnes). Par conséquent $\dim \text{Col } A = \text{rank } A$, le nombre de pivots.

Exemple : pour $A = \begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$, la forme échelonnée a ses pivots dans les colonnes 1 et 2, donc $\{(1,4), (2,5)\}$ est une base de Col $A$, qui est tout $\mathbb{R}^2$.

**Lien avec l'orthogonalité (complément, hors du cours)** : Col $A$ et l'[[Espace nul]] de $A^T$ sont [[Complément orthogonal|compléments orthogonaux]] l'un de l'autre dans $\mathbb{R}^m$ : $(\text{Col } A)^\perp = \text{Nul } A^T$.

Notion parente : [[Sous-espaces fondamentaux]]. Voir aussi : [[Espace nul]], [[Rang d'une matrice]], [[Complément orthogonal]], [[Forme échelonnée]], [[Combinaison linéaire]], [[Espace engendré]], [[Transformation linéaire]], [[Injectivité et surjectivité]]

Résumé : [[0 - Vector Space]]
