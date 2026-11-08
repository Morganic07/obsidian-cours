---
type: concept
tags:
  - year1
  - year2
aliases:
  - matrice de f
  - matrice d'une application
  - standard matrix
  - matrice standard
sources:
  - "[[4 - Algèbre linéaire|chp4]]"
  - "[[5 - Algèbre linéaire|chp5 (Algèbre Linéaire)]]"
  - "[[0 - Linear combination|Chp 0a - Linear combination]]"
  - "[[Raw/Year 2/Bilinear Algebra/Chp 0a - Linear combination .docx|Chp 0a - Linear combination]]"
maj: 2026-11-08
---

La matrice de $f$ dans les bases $B$ et $B'$ a pour colonne $j$ les coordonnées dans $B'$ de l'image par $f$ du $j$-ième vecteur de $B$. [[Erreurs du cours#^e-matrice-d-une-application-lineaire|✎]]

La matrice de la composée est le produit : $M_{g \circ f} = M_g \times M_f$. Changer de base change la matrice : $A' = P^{-1}AP$.

**Matrice standard, cas de $\mathbb{R}^n$** (Bilinear Algebra, complément, hors du cours) : toute [[Transformation linéaire|transformation linéaire]] $T : \mathbb{R}^n \to \mathbb{R}^m$ s'écrit $T(\mathbf{x}) = A\mathbf{x}$ pour une unique matrice $A$ de taille $m \times n$, sa **matrice standard** :
$$A = [\,T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\ \cdots\ T(\mathbf{e}_n)\,],$$
où $\mathbf{e}_1, \dots, \mathbf{e}_n$ sont les colonnes de la matrice identité. Raison : $\mathbf{x} = x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n$, donc par linéarité $T(\mathbf{x}) = x_1T(\mathbf{e}_1) + \cdots + x_nT(\mathbf{e}_n) = A\mathbf{x}$. C'est le cas particulier de la définition ci-dessus avec les bases canoniques au départ et à l'arrivée. Cette méthode construit les matrices du tableau des [[Transformations géométriques du plan]] de [[0 - Linear combination]] : on lit l'image du carré unité.

Notion parente : [[Matrice]]. Voir aussi : [[Transformation linéaire]], [[Changement de base]], [[Produit matriciel]], [[Coordonnées dans une base]], [[Composition de fonctions]], [[Transformations géométriques du plan]].

Dans le document chp4, les sections « Matrice d'une application », « Calcul de l'image d'un vecteur » et « Application » sont vides (les formules annoncées par « Dans cette base, on note » et « Si je note » n'y figurent pas).

Résumés : [[4 - Algèbre linéaire]], [[5 - Algèbre linéaire|chp5 (Algèbre Linéaire)]], [[0 - Linear combination]]
