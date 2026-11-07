---
type: concept
tags:
  - year2
aliases:
  - column space
  - column spaces
  - Col A
sources:
  - "[[0 - Vector Space (résumé)|Chp 0d - Vector Space]]"
maj: 2026-11-06
---

Col $A = \text{Span}\{\mathbf{a}_1, \dots, \mathbf{a}_n\}$ est l'ensemble des combinaisons linéaires des colonnes de $A$, c'est-à-dire l'ensemble des $\mathbf{b}$ tels que $A\mathbf{x} = \mathbf{b}$ a une solution. C'est un sous-espace de $\mathbb{R}^m$, et l'image de la transformation $\mathbf{x} \mapsto A\mathbf{x}$.

Col $A = \mathbb{R}^m$ si et seulement si $A\mathbf{x} = \mathbf{b}$ a une solution pour tout $\mathbf{b}$, c'est-à-dire si la transformation est surjective.

Il est défini explicitement : ses vecteurs se construisent directement à partir des colonnes. En revanche, savoir si un $\mathbf{v}$ donné y appartient demande de réduire $[A \ \mathbf{v}]$. C'est l'inverse pour l'[[Espace nul]].

Le même chapitre définit l'image d'une [[Transformation linéaire]] $T$ : $\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$.

Notion parente : [[Sous-espaces fondamentaux]]. Voir aussi : [[Espace nul]], [[Rang d'une matrice]], [[Combinaison linéaire]], [[Espace engendré]], [[Transformation linéaire]], [[Injectivité et surjectivité]]

Résumé : [[0 - Vector Space (résumé)]]
