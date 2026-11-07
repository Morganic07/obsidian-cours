---
type: concept
tags:
  - year1
  - year2
aliases:
  - linear system
  - linear systems
  - system of linear equation
  - system of linear equations
  - systems of linear equation
  - systems of linear equations
  - systèmes linéaires
  - système compatible
  - système incompatible
  - row picture
  - column picture
  - existence and uniqueness theorem
sources:
  - "[[0 - Linear combination (résumé)|Chp 0a - Linear combination]]"
  - "[[3 - Algèbre linéaire (résumé)|chp3 (Algèbre)]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-06
---

Ensemble d'équations $a_1x_1 + \dots + a_nx_n = b$. Deux systèmes sont équivalents s'ils ont les mêmes solutions. Un système est **compatible** (consistent) s'il a une ou une infinité de solutions, et **incompatible** (inconsistent) s'il n'en a aucune.

Trois écritures ont les mêmes solutions : $A\mathbf{x} = \mathbf{b}$, $x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{b}$ et la matrice augmentée $[\mathbf{a}_1 \cdots \mathbf{a}_n \mid \mathbf{b}]$.

Un système linéaire a 0, 1 ou une infinité de solutions.

- **Existence** (théorème d'existence et d'unicité, existence and uniqueness theorem) : le système est compatible si et seulement si la dernière colonne de la matrice augmentée n'est pas une colonne pivot. Une équation $0 = \lambda$ avec $\lambda \neq 0$ le rend donc incompatible.
- **Unicité** : un système compatible a une seule solution s'il n'a pas de variable libre, et une infinité sinon.
- **Homogène** : $A\mathbf{x} = \mathbf{0}$ a toujours la solution triviale $\mathbf{x} = \mathbf{0}$. Ses solutions forment un sous-espace, avec des solutions non nulles s'il y a plus d'inconnues que d'équations.
- **Non homogène** : les solutions sont $\mathbf{p} + \mathbf{v}_h$, où $\mathbf{p}$ est une solution particulière et $\mathbf{v}_h$ une solution de l'équation homogène.

**Algèbre Linéaire (1re année)** : avec plus d'inconnues que d'équations, la solution s'écrit en fonction d'une inconnue (exemple : $\{(2 - 8x_3; 1 + 5x_3; x_3)\}$). Le TD 4 d'Outil Maths résout un système pour étudier la surjectivité. L'évaluation 1 demande une résolution par pivot de Gauss, avec les opérations élémentaires à effectuer, sur un système de 4 équations qui modélise des températures sur une plaque.

Liens : [[Forme échelonnée]], [[Matrice augmentée]], [[Opérations élémentaires sur les lignes]], [[Système linéaire homogène]], [[Combinaison linéaire]], [[Espace nul]], [[Matrice inversible]], [[Moindres carrés]]

## À vérifier

- [[3 - Algèbre linéaire (résumé)|chp3 (Algèbre)]] écrit la solution « en fonction d'une inconnue » : il peut y en avoir plusieurs, selon le nombre de variables libres.

Résumés : [[0 - Linear combination (résumé)]], [[3 - Algèbre linéaire (résumé)|chp3 (résumé)]]
