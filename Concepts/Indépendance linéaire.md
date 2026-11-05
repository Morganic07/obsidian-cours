---
type: concept
aliases: [linearly independent, linear independence, linéairement indépendants, linéairement indépendantes, famille libre, familles libres, famille liée, familles liées]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0e - Eigenvalues and eigenvectors]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp1|chp1 (Algèbre)]]"]
maj: 2026-11-05
---

Une famille indépendante est dite **libre**, une famille dépendante **liée**. $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ est indépendant si $x_1\mathbf{v}_1 + \dots + x_n\mathbf{v}_n = \mathbf{0}$ n'a que la solution triviale. Les colonnes d'une matrice $A$ sont donc indépendantes si et seulement si $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale.

Un ensemble est **dépendant** si et seulement si l'un de ses vecteurs est une combinaison des autres. C'est notamment le cas :

- s'il contient le vecteur nul ;
- s'il a plus de vecteurs que de coordonnées ($p > n$ dans $\mathbb{R}^n$). Une matrice qui a plus de colonnes que de lignes a donc des colonnes dépendantes.

Dans une famille libre, la décomposition d'un vecteur est unique. Toute sous-famille d'une famille libre est libre. Ajouter à une famille libre un vecteur qui n'est pas combinaison de ses vecteurs la garde libre. Une application injective envoie une famille libre sur une famille libre.

Liens : [[Combinaison linéaire]], [[Base (algèbre linéaire)]], [[Matrice inversible]], [[Famille orthogonale]], [[Vecteur propre]], [[Déterminant]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp1 (résumé)|chp1 (résumé)]]
