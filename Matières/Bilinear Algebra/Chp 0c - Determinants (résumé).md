---
type: source
tags: [year2]
sources: ["[[Chp 0c - Determinants]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp 0c - Determinants]] (« Chapter 0c - Determinants »), dans [[Bilinear Algebra (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le [[Déterminant]] résume une matrice carrée en un nombre, qui dit si elle est inversible et mesure un volume.

## 1. Définitions

> **Matrice $2 \times 2$** : soit $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $\det A = ad - bc$. Si $ad - bc \neq 0$, $A$ est inversible et
> $$A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} ;$$
> si $ad - bc = 0$, $A$ n'est pas inversible.

> **Définition générale ($n \times n$)** : pour $n \ge 2$, le déterminant de $A = [a_{ij}]$ est la somme de $n$ termes $\pm a_{1j}\det A_{1j}$, de signes alternés, les $a_{1j}$ étant les coefficients de la première ligne ($A_{1j}$ : matrice obtenue en supprimant la ligne 1 et la colonne $j$) :
> $$\det A = a_{11}\det A_{11} - a_{12}\det A_{12} + \cdots + (-1)^{1+n}a_{1n}\det A_{1n} = \sum_{j=1}^{n} (-1)^{1+j}a_{1j}\det A_{1j}.$$

> **Théorème** : si $A$ est une [[Matrice triangulaire|matrice triangulaire]], $\det A$ est le produit des coefficients de sa diagonale principale.

## 2. Propriétés du déterminant

> **Théorème (opérations sur les lignes)** : $A$ carrée.
> a. Si l'on ajoute à une ligne un multiple d'une autre pour obtenir $B$, $\det B = \det A$.
> b. Si l'on échange deux lignes pour obtenir $B$, $\det B = -\det A$.
> c. Si l'on multiplie une ligne par $k$ pour obtenir $B$, $\det B = k \cdot \det A$.
>
> Ces propriétés valent aussi pour les colonnes.

Forme échelonnée typique (triangulaire, voir [[Forme échelonnée]]) ; $\blacksquare$ = pivot non nul, $*$ = valeur quelconque :
$$U = \begin{bmatrix} \blacksquare & * & * & * \\ 0 & \blacksquare & * & * \\ 0 & 0 & \blacksquare & * \\ 0 & 0 & 0 & \blacksquare \end{bmatrix},\ \det U \neq 0 \qquad U = \begin{bmatrix} \blacksquare & * & * & * \\ 0 & \blacksquare & * & * \\ 0 & 0 & 0 & \blacksquare \\ 0 & 0 & 0 & 0 \end{bmatrix},\ \det U = 0$$

Méthode qui en découle : réduire $A$ à une forme échelonnée en notant les échanges et les mises à l'échelle, puis faire le produit de la diagonale.

- $\det A = 0 \iff$ les lignes ou les colonnes de $A$ sont [[Indépendance linéaire|linéairement dépendantes]].
- En pratique, la dépendance est évidente quand deux lignes (ou colonnes) sont identiques, ou qu'une ligne (ou colonne) est entièrement nulle.

> **Théorème (vision géométrique)** : si $A$ est $2 \times 2$, l'aire du parallélogramme défini par les colonnes de $A$ est $|\det A|$. Si $A$ est $3 \times 3$, le volume du parallélépipède défini par les colonnes de $A$ est $|\det A|$.

**Preuve (cas diagonal)** :
$$\left|\det\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}\right| = |ad| = \text{aire du rectangle}, \qquad \left|\det\begin{bmatrix} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{bmatrix}\right| = |abc| = \text{volume du pavé}.$$

![[Chp 0c - Determinants - image6.png]]
*Figure : rectangle de côtés $(a,0)$ et $(0,d)$, d'aire $|ad|$ ; pavé de côtés $(a,0,0)$, $(0,b,0)$, $(0,0,c)$, de volume $|abc|$ (la phrase de la preuve est coupée sur l'image).*

> **Théorème** : si $A$ est $n \times n$, $\det A^T = \det A$ (voir [[Transposée]]).

> **Théorème (multiplicativité)** : si $A$ et $B$ sont $n \times n$, $\det AB = (\det A)(\det B)$.

## 3. Règle de Cramer (*Cramer's rule*)

Efficace sur les matrices $2 \times 2$ et $3 \times 3$ (voir [[Règle de Cramer]]).

> **Théorème** : $A$ inversible $n \times n$. Pour tout $\mathbf b \in \mathbb R^n$, l'unique solution $\mathbf x$ de $A\mathbf x = \mathbf b$ a pour coordonnées
> $$x_i = \frac{\det A_i(\mathbf b)}{\det A}, \quad i = 1, 2, \ldots, n,$$
> où $A_i(\mathbf b)$ est la matrice obtenue à partir de $A$ en remplaçant la colonne $i$ par $\mathbf b$.

## 4. Formule de l'inverse (*an inverse formula*)

> **Théorème** : $A$ inversible $n \times n$. Alors
> $$A^{-1} = \frac{1}{\det A}\,\text{adj}\,A = \frac{1}{\det A}\begin{bmatrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & \vdots & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \end{bmatrix}$$
> avec les cofacteurs $C_{ji} = (-1)^{i+j}\det A_{ji} = \det A_i(\mathbf e_j)$.

La **matrice adjointe** (*adjugate matrix*, [[Comatrice]]) est la **transposée** de la matrice des cofacteurs : par exemple, $C_{12}$ va en position $(2,1)$.

Le cours en tire :
$$A^{-1} = \frac{1}{\det A}(\text{adj}\,A) \iff A^{-1}A = \frac{1}{\det A}(\text{adj}\,A)A \iff I = \frac{1}{\det A}(\text{adj}\,A)A \iff \det A = (\text{adj}\,A)A$$
(dernière égalité recopiée telle quelle, voir « Points à vérifier »).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **$\det A = (\text{adj } A)A$** : image lue directement, c'est bien ce que le cours écrit, et c'est souligné. Or le membre de gauche est un nombre et celui de droite une matrice. On attendrait $(\det A)\,I = (\text{adj } A)A$ (complément). Tu as déjà coché ce point dans ta liste, sans que je connaisse ta conclusion.
2. **Méthode « réduire puis faire le produit de la diagonale »** : le cours la suggère par le schéma des formes échelonnées sans l'écrire comme méthode ; la formulation de cette fiche est une reformulation.
