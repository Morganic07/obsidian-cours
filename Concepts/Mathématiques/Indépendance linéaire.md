---
type: concept
tags:
  - year1
  - year2
aliases:
  - linearly independent
  - linear independence
  - linéairement indépendants
  - linéairement indépendantes
  - famille libre
  - familles libres
  - famille liée
  - familles liées
  - linearly dependent
  - linear dependence relation
  - relation de dépendance linéaire
sources:
  - "[[Chp 0a - Linear combination (résumé)|Chp 0a - Linear combination]]"
  - "[[Chp 0e - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[chp1 (résumé)|chp1 (Algèbre)]]"
  - "[[chp5 - Algèbre linéaire (résumé)|chp5 (Algèbre)]]"
  - "[[chp6 (résumé)|chp6 (Algèbre)]]"
  - "[[chp7 (résumé)|chp7 (Algèbre)]]"
maj: 2026-11-06
---

Une famille indépendante est dite **libre**, une famille dépendante **liée**. $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ est indépendant si $x_1\mathbf{v}_1 + \dots + x_n\mathbf{v}_n = \mathbf{0}$ n'a que la solution triviale. Les colonnes d'une matrice $A$ sont donc indépendantes si et seulement si $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale.

Un ensemble est **dépendant** si et seulement si l'un de ses vecteurs est une combinaison des autres. C'est notamment le cas :

- s'il contient le vecteur nul ;
- s'il a plus de vecteurs que de coordonnées ($p > n$ dans $\mathbb{R}^n$). Une matrice qui a plus de colonnes que de lignes a donc des colonnes dépendantes.

Dans une famille libre, la décomposition d'un vecteur est unique. Toute sous-famille d'une famille libre est libre. Ajouter à une famille libre un vecteur qui n'est pas combinaison de ses vecteurs la garde libre. Une application injective envoie une famille libre sur une famille libre.

En dimension $n$, une famille libre a au plus $n$ vecteurs. On teste la liberté par le [[Déterminant]]. Des vecteurs propres associés à des valeurs propres distinctes forment une famille libre, de même que des vecteurs non nuls deux à deux orthogonaux. Chaque *linear dependence relation* (relation de dépendance linéaire) entre les colonnes de $A$ correspond à une solution non triviale de $A\mathbf{x} = \mathbf{0}$ ([[Chp 0a - Linear combination (résumé)|Chp 0a - Linear combination]]).

Notion parente : [[Espace vectoriel]]. Voir aussi : [[Combinaison linéaire]], [[Base (algèbre linéaire)]], [[Espace engendré]], [[Matrice inversible]], [[Famille orthogonale]], [[Vecteur propre]], [[Déterminant]], [[Système linéaire homogène]].

Résumés : [[Chp 0a - Linear combination (résumé)]], [[chp1 (résumé)|chp1 (résumé)]], [[chp5 - Algèbre linéaire (résumé)|chp5 (résumé)]], [[chp6 (résumé)|chp6 (résumé)]], [[chp7 (résumé)|chp7 (résumé)]]
