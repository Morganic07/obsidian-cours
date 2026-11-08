---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp 0c - Determinants.docx|Chp 0c - Determinants]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Bilinear Algebra/Chp 0c - Determinants.docx|Chp 0c - Determinants]] (« Chapter 0c - Determinants »), dans [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Idée générale

Le [[Déterminant]] résume une matrice carrée en un nombre, qui dit si elle est inversible et mesure un volume.

## 1. Définitions

> **Matrice $2 \times 2$** : soit $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $\det A = ad - bc$. Si $ad - bc \neq 0$, $A$ est inversible et
> $$A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} ;$$
> si $ad - bc = 0$, $A$ n'est pas inversible.

Pour inverser une $2 \times 2$ de tête : échanger les deux coefficients de la diagonale, changer le signe des deux autres, diviser par le déterminant. Exemple : $\begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$ a pour déterminant $6 - 5 = 1$, donc pour inverse $\begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

> **Définition générale ($n \times n$)** : pour $n \ge 2$, le déterminant de $A = [a_{ij}]$ est la somme de $n$ termes $\pm a_{1j}\det A_{1j}$, de signes alternés, les $a_{1j}$ étant les coefficients de la première ligne ($A_{1j}$ : matrice obtenue en supprimant la ligne 1 et la colonne $j$) :
> $$\det A = a_{11}\det A_{11} - a_{12}\det A_{12} + \cdots + (-1)^{1+n}a_{1n}\det A_{1n} = \sum_{j=1}^{n} (-1)^{1+j}a_{1j}\det A_{1j}.$$

**Développement selon n'importe quelle ligne ou colonne** (*cofactor expansion*, ou développement de Laplace). En notant $C_{ij} = (-1)^{i+j}\det A_{ij}$ le **cofacteur** de $a_{ij}$ (voir [[Comatrice]]), le déterminant se développe selon la ligne $i$ ou la colonne $j$ de son choix, avec le même résultat :
$$\det A = \sum_{j=1}^{n} a_{ij}C_{ij} \ \text{(ligne } i\text{)} \qquad \det A = \sum_{i=1}^{n} a_{ij}C_{ij} \ \text{(colonne } j\text{)}.$$
On choisit donc la ligne ou la colonne qui contient le plus de zéros. Les signes $(-1)^{i+j}$ forment un damier qui commence par $+$ en haut à gauche : $\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$. [[Complément hors du cours|ⓘ]]

**Règle de Sarrus** (taille $3$ seulement) : recopier les deux premières colonnes à droite de la matrice, additionner les produits des trois diagonales descendantes et retrancher ceux des trois diagonales montantes :
$$\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = aei + bfg + cdh - ceg - afh - bdi.$$
Elle ne se généralise pas aux tailles $n \ge 4$. [[Complément hors du cours|ⓘ]]

**Coût du calcul.** Le développement complet d'un déterminant $n \times n$ fait apparaître $n!$ produits ($3\,628\,800$ pour $n = 10$) : il est inutilisable au-delà des petites tailles. La réduction par lignes de la section 2 demande de l'ordre de $n^3$ opérations, c'est elle qu'emploient les logiciels. [[Complément hors du cours|ⓘ]]

> **Théorème** : si $A$ est une [[Matrice triangulaire|matrice triangulaire]], $\det A$ est le produit des coefficients de sa diagonale principale.

Pourquoi : pour une triangulaire supérieure, on développe selon la première colonne, qui n'a qu'un coefficient non nul, $a_{11}$ ; il reste $a_{11}$ fois le déterminant d'une triangulaire plus petite, et on recommence. En particulier, $\det I_n = 1$. [[Complément hors du cours|ⓘ]]

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

En formule : si l'on n'utilise que des remplacements et $r$ échanges pour obtenir la forme échelonnée $U$, alors $\det A = (-1)^r \times (\text{produit des pivots de } U)$, et $\det A = 0$ dès qu'il manque un pivot. Exemple :
$$\begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 3 & 5 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 1 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$
($L_2 \leftarrow L_2 - 2L_1$, $L_3 \leftarrow L_3 - L_1$, puis $L_3 \leftarrow L_3 - L_2$) : aucun échange, donc $\det A = 1 \times 1 \times 1 = 1$. Le développement selon la première ligne donne bien $1(25 - 21) - 2(10 - 7) + 3(6 - 5) = 1$. [[Complément hors du cours|ⓘ]]

Conséquence de la règle c appliquée aux $n$ lignes : $\det(kA) = k^n \det A$ pour une matrice $n \times n$, et non $k \det A$. [[Complément hors du cours|ⓘ]]

- $\det A = 0 \iff$ les lignes ou les colonnes de $A$ sont [[Indépendance linéaire|linéairement dépendantes]].
- En pratique, la dépendance est évidente quand deux lignes (ou colonnes) sont identiques, ou qu'une ligne (ou colonne) est entièrement nulle.

> **Théorème (vision géométrique)** : si $A$ est $2 \times 2$, l'aire du parallélogramme défini par les colonnes de $A$ est $|\det A|$. Si $A$ est $3 \times 3$, le volume du parallélépipède défini par les colonnes de $A$ est $|\det A|$.

**Preuve (cas diagonal)** :
$$\left|\det\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}\right| = |ad| = \text{aire du rectangle}, \qquad \left|\det\begin{bmatrix} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{bmatrix}\right| = |abc| = \text{volume du pavé}.$$

![[Chp 0c - Determinants - image6.png]]
*Figure : rectangle de côtés $(a,0)$ et $(0,d)$, d'aire $|ad|$ ; pavé de côtés $(a,0,0)$, $(0,b,0)$, $(0,0,c)$, de volume $|abc|$ (la phrase de la preuve est coupée sur l'image).*

Pour une matrice quelconque, on se ramène au cas diagonal : un remplacement de colonne fait glisser un côté du parallélogramme parallèlement à l'autre (un cisaillement), ce qui ne change ni la base ni la hauteur, donc ni l'aire ; et il ne change pas non plus le déterminant. [[Complément hors du cours|ⓘ]]

Plus généralement, si $T(\mathbf x) = A\mathbf x$ avec $A$ de taille $2 \times 2$ (ou $3 \times 3$), $T$ multiplie toutes les aires (ou tous les volumes) par $|\det A|$ : $\text{aire}(T(S)) = |\det A| \cdot \text{aire}(S)$ pour toute région $S$. Le **signe** de $\det A$ dit si $T$ conserve l'orientation ($\det A > 0$) ou la renverse comme un miroir ($\det A < 0$) ; $\det A = 0$ signifie que $T$ écrase le plan sur une droite ou un point (voir [[Transformation linéaire]]). [[Complément hors du cours|ⓘ]]

> **Théorème** : si $A$ est $n \times n$, $\det A^T = \det A$ (voir [[Transposée]]).

> **Théorème (multiplicativité)** : si $A$ et $B$ sont $n \times n$, $\det AB = (\det A)(\det B)$.

Conséquences utiles : [[Complément hors du cours|ⓘ]]
- si $A$ est inversible, $\det(A^{-1}) = \dfrac{1}{\det A}$, puisque $\det A \cdot \det A^{-1} = \det I = 1$ ; [[Complément hors du cours|ⓘ]]
- $\det(PAP^{-1}) = \det A$ : deux [[Matrices semblables|matrices semblables]] ont le même déterminant ; [[Complément hors du cours|ⓘ]]
- en revanche, le déterminant n'est **pas** additif : en général $\det(A + B) \neq \det A + \det B$ (avec $A = B = I_2$ : $\det(2I_2) = 4$, alors que $\det I_2 + \det I_2 = 2$). [[Complément hors du cours|ⓘ]]

## 3. Règle de Cramer (*Cramer's rule*)

Efficace sur les matrices $2 \times 2$ et $3 \times 3$ (voir [[Règle de Cramer]]).

> **Théorème** : $A$ inversible $n \times n$. Pour tout $\mathbf b \in \mathbb R^n$, l'unique solution $\mathbf x$ de $A\mathbf x = \mathbf b$ a pour coordonnées
> $$x_i = \frac{\det A_i(\mathbf b)}{\det A}, \quad i = 1, 2, \ldots, n,$$
> où $A_i(\mathbf b)$ est la matrice obtenue à partir de $A$ en remplaçant la colonne $i$ par $\mathbf b$.

Exemple : $3x_1 - 2x_2 = 6$, $-5x_1 + 4x_2 = 8$. $\det A = 3 \cdot 4 - (-2)(-5) = 2$ ; $\det A_1(\mathbf b) = \det\begin{bmatrix} 6 & -2 \\ 8 & 4 \end{bmatrix} = 40$ et $\det A_2(\mathbf b) = \det\begin{bmatrix} 3 & 6 \\ -5 & 8 \end{bmatrix} = 54$, d'où $x_1 = 20$ et $x_2 = 27$ (vérification : $60 - 54 = 6$ et $-100 + 108 = 8$). [[Complément hors du cours|ⓘ]]

Au-delà de $3 \times 3$, la règle demande $n + 1$ déterminants et devient bien plus coûteuse que la réduction de la matrice augmentée : elle sert surtout en théorie (par exemple pour voir comment la solution dépend de $\mathbf b$). [[Complément hors du cours|ⓘ]]

## 4. Formule de l'inverse (*an inverse formula*)

> **Théorème** : $A$ inversible $n \times n$. Alors
> $$A^{-1} = \frac{1}{\det A}\,\text{adj}\,A = \frac{1}{\det A}\begin{bmatrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & \vdots & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \end{bmatrix}$$
> avec les cofacteurs $C_{ji} = (-1)^{i+j}\det A_{ji} = \det A_i(\mathbf e_j)$.

La **matrice adjointe** (*adjugate matrix*, [[Comatrice]]) est la **transposée** de la matrice des cofacteurs : par exemple, $C_{12}$ va en position $(2,1)$.

Vérification en taille $2$ : pour $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, les cofacteurs sont $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$, $C_{22} = a$ ; en les transposant, $\text{adj}\,A = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$, et l'on retrouve la formule de la section 1. [[Complément hors du cours|ⓘ]]

Le cours en tire la relation $(\det A)\,I = (\text{adj}\,A)A$ (à gauche, la matrice $\det A$ fois l'identité, puisque le membre de droite est une matrice) : [[Erreurs du cours#^e-0-determinants|✎]]
$$A^{-1} = \frac{1}{\det A}(\text{adj}\,A) \iff A^{-1}A = \frac{1}{\det A}(\text{adj}\,A)A \iff I = \frac{1}{\det A}(\text{adj}\,A)A \iff (\det A)\,I = (\text{adj}\,A)A$$
