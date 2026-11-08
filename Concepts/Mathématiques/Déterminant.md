---
type: concept
tags:
  - year1
  - year2
aliases:
  - determinant
  - determinants
  - déterminants
  - geometric view of det
  - multiplication properties of determinant
  - règle de Sarrus
  - Sarrus rule
  - développement selon une ligne
  - cofactor expansion
matieres:
  - Bilinear Algebra
  - Algèbre Linéaire
sources:
  - "[[0 - Determinants|Chp 0c - Determinants]]"
  - "[[0 - Matrix algebra|Chp 0b - Matrix algebra]]"
  - "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[5 - Algèbre linéaire|chp5 (Algèbre)]]"
  - "[[6 - Algèbre linéaire|chp6 (Algèbre)]]"
  - "[[7 - Algèbre linéaire|chp7 (Algèbre)]]"
  - "[[Raw/Year 2/Bilinear Algebra/Chp 0c - Determinants.docx|Chp 0c - Determinants]]"
maj: 2026-11-08
---

Nombre associé à une [[Matrice|matrice]] carrée, défini par récurrence sur la taille : $ad - bc$ en taille 2, et $\det A = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} \det A_{1j}$ en général, où $A_{ij}$ est $A$ privée de la ligne $i$ et de la colonne $j$. Pour une [[Matrice triangulaire|matrice triangulaire]], c'est le produit de la diagonale.

- **Inversibilité** : $A$ est inversible si et seulement si $\det A \neq 0$. $\det A = 0$ équivaut à des lignes ou des colonnes dépendantes.
- **Opérations sur les lignes ou les colonnes** ([[Opérations élémentaires sur les lignes]]) : ajouter un multiple d'une ligne à une autre ne change rien (en 1re année : ajouter une combinaison linéaire des autres), échanger deux lignes change le signe (chp6 : deux colonnes adjacentes), multiplier une ligne par $k$ multiplie le déterminant par $k$. Tout ce qui vaut pour les colonnes vaut pour les lignes. [[Erreurs du cours#^e-determinant|✎]]
- **Propriétés** : $\det A^T = \det A$ et $\det AB = (\det A)(\det B)$.
- **Géométrie** : $|\det A|$ est l'aire du parallélogramme ou le volume du parallélépipède défini par les colonnes.
- **[[Règle de Cramer]]** : $x_i = \frac{\det A_i(\mathbf{b})}{\det A}$, efficace en tailles 2 et 3.
- **Inverse** : $A^{-1} = \frac{1}{\det A} \text{adj } A$, où adj $A$ est la transposée de la matrice des cofacteurs ([[Comatrice]]) ; on en tire $(\det A)\,I = (\text{adj } A)A$. [[Erreurs du cours#^e-determinant|✎]]
- **Linéarité** : à colonnes fixées sauf une, le déterminant est linéaire par rapport à cette colonne ([[Forme multilinéaire alternée]]).
- **Bases** (théorème fondamental) : $n$ vecteurs forment une base si et seulement si le déterminant de leurs composantes est non nul ; il est nul si et seulement si la famille est liée. Il suffit donc de le calculer pour montrer qu'une famille est libre.
- **Valeurs propres** : ce sont les $\lambda$ tels que $\det(A - \lambda\,\mathrm{Id}) = 0$ ([[7 - Algèbre linéaire|chp7 (Algèbre)]]).
- **Cas nuls** : deux lignes ou deux colonnes égales donnent 0.

## Compléments (complément, hors du cours)

**Développement selon n'importe quelle ligne ou colonne.** Avec le cofacteur $C_{ij} = (-1)^{i+j}\det A_{ij}$, pour toute ligne $i$ et toute colonne $j$ :
$$\det A = \sum_{j=1}^{n} a_{ij} C_{ij} \quad\text{(ligne } i\text{)} \qquad \det A = \sum_{i=1}^{n} a_{ij} C_{ij} \quad\text{(colonne } j\text{)}.$$
On choisit la ligne ou la colonne qui contient le plus de zéros. Les signes $(-1)^{i+j}$ forment un damier commençant par $+$ en haut à gauche.

**Règle de Sarrus** (taille 3 uniquement) : pour $A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$,
$$\det A = aei + bfg + cdh - ceg - afh - bdi.$$

**Par réduction.** Si l'on ramène $A$ à une forme échelonnée $U$ en n'utilisant que des remplacements (ajout d'un multiple d'une ligne à une autre) et $r$ échanges, alors $\det A = (-1)^r \times$ (produit des pivots de $U$), puisque $U$ est triangulaire. **Coût** : le développement complet demande de l'ordre de $n!$ produits (plus de $10^{18}$ pour $n = 20$), la réduction de l'ordre de $n^3$ opérations ; c'est ainsi que les logiciels le calculent.

**Autres propriétés**, pour $A$, $B$ de taille $n$ :

- $\det(kA) = k^n \det A$ (chacune des $n$ lignes est multipliée par $k$) ;
- $\det(A^{-1}) = \dfrac{1}{\det A}$ pour $A$ inversible, car $\det A \det A^{-1} = \det I = 1$ ;
- $\det(PAP^{-1}) = \det A$ : deux [[Matrices semblables|matrices semblables]] ont le même déterminant, qui ne dépend donc que de l'application linéaire, pas de la base ;
- $\det(A + B) \neq \det A + \det B$ en général (le déterminant n'est pas linéaire en la matrice) ;
- $\det A$ est le produit des [[Valeur propre|valeurs propres]] de $A$, comptées avec leur multiplicité (dans $\mathbb{C}$).

**Orientation et volume.** Pour $T(\mathbf{x}) = A\mathbf{x}$, $|\det A|$ est le facteur par lequel $T$ multiplie les aires (dans le plan) ou les volumes (dans l'espace) : l'image d'une région $S$ a pour aire $|\det A| \times$ aire$(S)$. Le signe indique l'orientation : $\det A > 0$ la conserve (rotation, dilatation), $\det A < 0$ la renverse (réflexion), et $\det A = 0$ écrase l'espace sur un sous-espace de dimension inférieure.

Notion parente : [[Matrice]].

Liens : [[Matrice inversible]], [[Valeur propre]], [[Transposée]], [[Produit matriciel]], [[Base (algèbre linéaire)]], [[Indépendance linéaire]], [[Matrices semblables]], [[Forme échelonnée]], [[Transformations géométriques du plan]]

Résumés : [[0 - Determinants]], [[2 - Symmetric matrices and quadratic forms]], [[5 - Algèbre linéaire|chp5]], [[6 - Algèbre linéaire|chp6]], [[7 - Algèbre linéaire|chp7]]
