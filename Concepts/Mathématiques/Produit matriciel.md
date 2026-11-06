---
type: concept
tags:
  - year1
  - year2
  - year4
aliases:
  - matrix product
  - matrix multiplication
  - produits matriciels
  - multiplication matricielle
sources:
  - "[[Chp 0a - Linear combination]]"
  - "[[Chp 0b - Matrix algebra]]"
  - "[[chp4|chp4 (Algèbre)]]"
  - ".raw/Year 1/Contrôles.pdf"
  - "[[chp3 - complexité]]"
maj: 2026-11-06
---

Si $A$ est de taille $m \times n$ et $B$ de taille $n \times p$, alors $AB$ est la matrice $m \times p$ de colonnes $A\mathbf{b}_1, \dots, A\mathbf{b}_p$. Coefficient par coefficient, c'est la somme sur $k$ des $a_{ik}b_{kj}$. $A\mathbf{x}$ est la combinaison des colonnes de $A$, de poids les coefficients de $\mathbf{x}$.

Propriétés : $A(BC) = (AB)C$, $A(B + C) = AB + AC$, $(B + C)A = BA + CA$, $r(AB) = (rA)B = A(rB)$, et $I_mA = A = AI_n$.

En général :

- $AB \neq BA$ ;
- $AB = AC$ n'implique pas $B = C$ ;
- $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.

Il représente la [[Composition de fonctions|composée]] d'applications : $M_{g \circ f} = M_g \times M_f$ (voir [[Matrice d'une application linéaire]]). Le [[Développement colonnes-lignes]] donne aussi $AB = \text{col}_1(A)\,\text{row}_1(B) + \dots + \text{col}_n(A)\,\text{row}_n(B)$.

**En Algèbre Linéaire (1re année)**, [[chp4|chp4 (Algèbre)]] écrit $A_{(n,m)} \times B_{(m,p)} = C_{(n,p)}$ avec $c_{ij} = \sum_{k=1}^{m} a_{ik}b_{kj}$, et note que $AC = BC$ n'implique pas $A = B$. L'évaluation 1 ([[Contrôles (résumé)|Contrôles]], en anglais) demande la taille et l'existence de produits, et de résoudre $A^2 = -I_2$ et $A^2 = 0$ pour une [[Matrice]] $2 \times 2$ à paramètres, ce qui ramène à un [[Système linéaire]].

**En graph theory**, [[chp3 - complexité]] prend le produit comme exemple de calcul de [[Complexité algorithmique|complexité]] : $A$ de taille $(m, n)$, $B$ de taille $(n, p)$, $C_{i,j} = \sum_k A_{i,k}B_{k,j}$.

Notion parente : [[Matrice]]. Voir aussi : [[Combinaison linéaire]], [[Transposée]], [[Matrice inversible]], [[Déterminant]], [[Transformation linéaire]], [[Matrice d'une application linéaire]], [[Composition de fonctions]], [[Développement colonnes-lignes]], [[Système linéaire]], [[Complexité algorithmique]]

## À vérifier

- [[chp4|chp4 (Algèbre)]] : l'image de la formule porte $n$ comme borne de la somme ; un dessin ajoute « m » à cet endroit, ce qui correspond aux tailles.
- [[chp3 - complexité]] écrit que $C$ est de dimension $(m, n)$ au lieu de $(m, p)$ (relevé du résumé).

Résumés : [[Chp 0b - Matrix algebra (résumé)]], [[chp4 (résumé)|chp4 (résumé)]], [[Contrôles (résumé)|Contrôles (résumé)]], [[chp3 - complexité (résumé)]]
