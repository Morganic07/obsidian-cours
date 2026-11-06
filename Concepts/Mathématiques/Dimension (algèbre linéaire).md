---
type: concept
tags:
  - year1
  - year2
aliases:
  - dimension
  - dimensions
  - dimension finie
  - dimension infinie
matieres:
  - Bilinear Algebra
  - Algèbre Linéaire
sources:
  - "[[Chp 0d - Vector Space]]"
  - "[[chp1|chp1 (Algèbre)]]"
  - "[[chp3|chp3 (Algèbre)]]"
  - "[[chp4|chp4 (Algèbre)]]"
  - ".raw/Year 1/Contrôles.pdf"
maj: 2026-11-06
---

La dimension d'un sous-espace non nul est le nombre de vecteurs de n'importe laquelle de ses bases. Le sous-espace $\{\mathbf{0}\}$ est de dimension zéro. $\mathbb{R}^n$ est de dimension $n$. Dans $\mathbb{R}^3$, un plan passant par $\mathbf{0}$ est de dimension 2, et une droite passant par $\mathbf{0}$ de dimension 1. Le chapitre 0d l'introduit avec le rang : $\dim \text{Nul}\,A = n - r$ et $\dim \text{Col}\,A = r$ ([[Théorème du rang]]).

**Dimension finie ou infinie** (chp1 d'Algèbre linéaire) : $E$ est de dimension finie s'il existe une famille génératrice finie, de dimension infinie sinon. $M_{n,p}(\mathbb{R})$ est de dimension $n \times p$. Le chp3 associe le nombre d'inconnues libres d'un système à la dimension de l'ensemble des solutions (point, droite, plan).

Dans un espace de dimension $n$ :

- une famille génératrice a au moins $n$ vecteurs, une famille libre au plus $n$ ;
- avec exactement $n$ vecteurs, une famille libre ou génératrice est une base ;
- un sous-espace $F$ est de dimension au plus $n$, et $F = E$ s'il est de dimension $n$.

Les évaluations 2 et 3 de première année demandent des dimensions de sous-espaces de $\mathbb{R}^3$ et $\mathbb{R}^4$, de $\mathrm{Span}(u_1, u_2, u_3)$, de $F$ et de $E \cap F$ ([[Espace engendré]]).

Notion parente : [[Base (algèbre linéaire)]]. Voir aussi : [[Rang d'une matrice]], [[Théorème du rang]], [[Espace engendré]], [[Sous-espaces fondamentaux]], [[Somme directe]]

## À vérifier

- chp3 : « 1 inconnue = dim 0, 2 inconnues = dim 1, 3 inconnues = dim 2 » ne vaut que pour une seule équation non triviale.
- chp4 emploie « dimension n x n » pour le format d'une matrice, un autre sens du mot.

Résumés : [[Chp 0d - Vector Space (résumé)]], [[chp1 (résumé)|chp1 (résumé)]], [[chp3 (résumé)]], [[chp4 (résumé)]], [[Contrôles (résumé)]]
