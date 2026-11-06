---
type: concept
aliases: [invertible matrix, invertible matrices, matrices inversibles, inverse matrix, matrice inverse, invertible transformation, transformation inversible, algorithm for finding A^-1]
sources: ["[[Chp 0b - Matrix algebra]]", "[[Invertible matrix theorem]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp4|chp4 (Algèbre)]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp5|chp5 (Algèbre)]]"]
maj: 2026-11-06
---

[[Matrice]] carrée $A$ pour laquelle il existe une unique $A^{-1}$ telle que $A^{-1}A = AA^{-1} = I_n$ (nonsingular). Sinon, elle est dite singular.

- **Calcul** : en taille 2, $A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ si $ad - bc \neq 0$. En général, on réduit $[A \ I]$ jusqu'à $[I \ A^{-1}]$.
- **Propriétés** : $(A^{-1})^{-1} = A$, $(AB)^{-1} = B^{-1}A^{-1}$ et $(A^T)^{-1} = (A^{-1})^T$.
- **Système** : $A\mathbf{x} = \mathbf{b}$ a l'unique solution $\mathbf{x} = A^{-1}\mathbf{b}$.
- **Inverse par la comatrice** : $A^{-1} = \frac{1}{\det A}\,\text{adj } A$ ([[Comatrice]]).
- **Transformation inversible** : $T$ est inversible s'il existe $S$ avec $S(T(\mathbf{x})) = \mathbf{x}$ et $T(S(\mathbf{x})) = \mathbf{x}$ pour tout $\mathbf{x}$.

**En 1re année** : le chp4 annonce que si $f$ admet une réciproque $f^{-1}$ ([[Bijection]]), sa matrice vérifie « $M_f \times M_{f^{-1}} =$ », sans suite dans l'export. Le chp5 utilise l'inverse de la matrice de passage : $P^{-1} = P_{B' \to B}$ ([[Changement de base]]).

## Théorème de la matrice inversible

Voir aussi la page [[Théorème de la matrice inversible]].

Pour $A$ de taille $n \times n$, ces énoncés sont équivalents : tous vrais, ou tous faux.

- **Lignes** : (a) $A$ est inversible ; (b) $A$ est équivalente par lignes à $I_n$ ; (c) $A$ a $n$ pivots.
- **Injectivité** : (d) $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale ; (e) les colonnes sont indépendantes ; (f) $\mathbf{x} \mapsto A\mathbf{x}$ est injective ; (q) Nul $A = \{\mathbf{0}\}$ ; (r) $\dim \text{Nul } A = 0$.
- **Surjectivité** : (g) $A\mathbf{x} = \mathbf{b}$ a une solution pour tout $\mathbf{b}$ ; (h) les colonnes engendrent $\mathbb{R}^n$ ; (i) $\mathbf{x} \mapsto A\mathbf{x}$ est surjective ; (n) Col $A = \mathbb{R}^n$ ; (o) $\dim \text{Col } A = n$ ; (p) $\text{rank } A = n$.
- **Inverses** : (j) il existe $C$ telle que $CA = I$ ; (k) il existe $D$ telle que $AD = I$ ; (l) $A^T$ est inversible.
- **Base** : (m) les colonnes forment une base de $\mathbb{R}^n$.
- **Nombres** : (s) 0 n'est pas valeur propre ; (t) $\det A \neq 0$.

Notion parente : [[Matrice]].

Liens : [[Déterminant]], [[Rang d'une matrice]], [[Valeur propre]], [[Forme échelonnée]], [[Injectivité et surjectivité]]

## À vérifier

- [[Cours/Year 1/Algèbre Linéaire/Cours/chp4|chp4 (Algèbre)]] : la formule « $M_f \times M_{f^{-1}} =$ » est tronquée dans l'export Google.
- [[Chp 0b - Matrix algebra]] : l'exemple $e^x$ / $\ln$ est une analogie hors des transformations linéaires.

Résumés : [[Chp 0b - Matrix algebra (résumé)]], [[Invertible matrix theorem (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp4 (résumé)|chp4 (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp5 (résumé)|chp5 (résumé)]]
