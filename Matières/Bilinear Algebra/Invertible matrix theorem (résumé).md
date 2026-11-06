---
type: source
tags: [year2]
sources: ["[[Invertible matrix theorem]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Invertible matrix theorem]], dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

Cette note rassemble les 20 énoncés (a à t) du théorème, tous équivalents pour une matrice carrée : ils sont tous vrais, ou tous faux. Ils sont classés par thème dans [[Matrice inversible]] (voir aussi [[Théorème de la matrice inversible]]).

Les énoncés a à l viennent de [[Chp 0b - Matrix algebra]], m à r de [[Chp 0d - Vector Space]], s et t de [[Chp 0e - Eigenvalues and eigenvectors]].

## Le théorème de la matrice inversible (*The Invertible Matrix Theorem*)

Soit $A$ une matrice carrée $n \times n$. Les énoncés suivants sont équivalents : pour une matrice $A$ donnée, ils sont tous vrais ou tous faux.

### Énoncés a à l (réduction, systèmes, transformation)

- a. $A$ est inversible.
- b. $A$ est [[Opérations élémentaires sur les lignes|équivalente par lignes]] à la matrice identité $I_n$.
- c. $A$ a $n$ positions pivots.
- d. L'équation $A\mathbf x = \mathbf 0$ n'a que la [[Système linéaire homogène|solution triviale]].
- e. Les colonnes de $A$ forment une famille [[Indépendance linéaire|linéairement indépendante]].
- f. La [[Transformation linéaire|transformation linéaire]] $\mathbf x \mapsto A\mathbf x$ est [[Injectivité et surjectivité|injective]] (*one-to-one*).
- g. L'équation $A\mathbf x = \mathbf b$ a au moins une solution pour tout $\mathbf b \in \mathbb R^n$.
- h. Les colonnes de $A$ [[Espace engendré|engendrent]] $\mathbb R^n$.
- i. La transformation $\mathbf x \mapsto A\mathbf x$ envoie $\mathbb R^n$ **sur** $\mathbb R^n$ (surjective, *onto*).
- j. Il existe une matrice $C$ ($n \times n$) telle que $CA = I$.
- k. Il existe une matrice $D$ ($n \times n$) telle que $AD = I$.
- l. $A^T$ est inversible.

### Énoncés m à r (base, sous-espaces, rang)

Chacun équivaut à « $A$ est inversible » :
- m. Les colonnes de $A$ forment une [[Base (algèbre linéaire)|base]] de $\mathbb R^n$.
- n. $\text{Col}\,A = \mathbb R^n$ ([[Espace des colonnes]]).
- o. $\dim \text{Col}\,A = n$.
- p. $\text{rank}\,A = n$ ([[Rang d'une matrice]]).
- q. $\text{Nul}\,A = \{\mathbf 0\}$ ([[Espace nul]]).
- r. $\dim \text{Nul}\,A = 0$.

### Énoncés s et t (valeurs propres, déterminant)

$A$ est inversible si et seulement si :
- s. le nombre $0$ n'est **pas** une [[Valeur propre|valeur propre]] de $A$ ;
- t. le [[Déterminant|déterminant]] de $A$ n'est **pas** nul.

## Points à vérifier

Aucun point à vérifier.
