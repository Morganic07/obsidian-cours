---
type: concept
aliases: [column space, column spaces, Col A]
sources: ["[[Chp 0d - Vector Space]]"]
maj: 2026-11-05
---

Col $A = \text{Span}\{\mathbf{a}_1, \dots, \mathbf{a}_n\}$ est l'ensemble des combinaisons linéaires des colonnes de $A$, c'est-à-dire l'ensemble des $\mathbf{b}$ tels que $A\mathbf{x} = \mathbf{b}$ a une solution. C'est un sous-espace de $\mathbb{R}^m$, et l'image de la transformation $\mathbf{x} \mapsto A\mathbf{x}$.

Col $A = \mathbb{R}^m$ si et seulement si $A\mathbf{x} = \mathbf{b}$ a une solution pour tout $\mathbf{b}$, c'est-à-dire si la transformation est surjective.

Il est défini explicitement : ses vecteurs se construisent directement à partir des colonnes. En revanche, savoir si un $\mathbf{v}$ donné y appartient demande de réduire $[A \ \mathbf{v}]$. C'est l'inverse pour l'[[Espace nul]].

Liens : [[Combinaison linéaire]], [[Espace engendré]], [[Espace nul]], [[Rang d'une matrice]], [[Sous-espaces fondamentaux]], [[Injectivité et surjectivité]]

Résumé : [[Chp 0d - Vector Space (résumé)]]
