---
type: concept
aliases: [determinant, determinants, déterminants, geometric view of det, multiplication properties of determinant]
matieres: [Bilinear Algebra, Algèbre Linéaire]
sources: ["[[Chp 0c - Determinants]]", "[[Chp 0b - Matrix algebra]]", "[[Chp2 - Symmetric matrices and quadratic forms]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp5|chp5 (Algèbre)]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp6|chp6 (Algèbre)]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp7|chp7 (Algèbre)]]"]
maj: 2026-11-06
---

Nombre associé à une [[Matrice|matrice]] carrée, défini par récurrence sur la taille : $ad - bc$ en taille 2, et $\det A = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} \det A_{1j}$ en général, où $A_{ij}$ est $A$ privée de la ligne $i$ et de la colonne $j$. Pour une [[Matrice triangulaire|matrice triangulaire]], c'est le produit de la diagonale.

- **Inversibilité** : $A$ est inversible si et seulement si $\det A \neq 0$. $\det A = 0$ équivaut à des lignes ou des colonnes dépendantes.
- **Opérations sur les lignes ou les colonnes** ([[Opérations élémentaires sur les lignes]]) : ajouter un multiple d'une ligne à une autre ne change rien (en 1re année : ajouter une combinaison linéaire des autres), échanger deux lignes change le signe (chp6 : deux colonnes adjacentes), multiplier une ligne par $k$ multiplie le déterminant par $k$. Tout ce qui vaut pour les colonnes vaut pour les lignes.
- **Propriétés** : $\det A^T = \det A$ et $\det AB = (\det A)(\det B)$.
- **Géométrie** : $|\det A|$ est l'aire du parallélogramme ou le volume du parallélépipède défini par les colonnes.
- **[[Règle de Cramer]]** : $x_i = \frac{\det A_i(\mathbf{b})}{\det A}$, efficace en tailles 2 et 3.
- **Inverse** : $A^{-1} = \frac{1}{\det A} \text{adj } A$, où adj $A$ est la transposée de la matrice des cofacteurs ([[Comatrice]]).
- **Linéarité** : à colonnes fixées sauf une, le déterminant est linéaire par rapport à cette colonne ([[Forme multilinéaire alternée]]).
- **Bases** (théorème fondamental) : $n$ vecteurs forment une base si et seulement si le déterminant de leurs composantes est non nul ; il est nul si et seulement si la famille est liée. Il suffit donc de le calculer pour montrer qu'une famille est libre.
- **Valeurs propres** : ce sont les $\lambda$ tels que $\det(A - \lambda\,\mathrm{Id}) = 0$ ([[Cours/Year 1/Algèbre Linéaire/Cours/chp7|chp7 (Algèbre)]]).
- **Cas nuls** : deux lignes ou deux colonnes égales donnent 0.

> [!warning] À vérifier
> [[Chp 0c - Determinants]] écrit $\det A = (\text{adj } A)A$, qui égale un nombre à une matrice. On attendrait $(\det A)\,I = (\text{adj } A)A$.

> [!warning] À vérifier
> Dans [[Cours/Year 1/Algèbre Linéaire/Cours/chp6|chp6 (Algèbre)]], la formule de définition (« On définit par récurrence l'application », « Par : », « On a : ») est vide dans l'export. Le cours écrit aussi « combinaison linéaire des deux autres », à lire « des autres ».

Notion parente : [[Matrice]].

Liens : [[Matrice inversible]], [[Valeur propre]], [[Transposée]], [[Produit matriciel]], [[Base (algèbre linéaire)]], [[Indépendance linéaire]]

Résumés : [[Chp 0c - Determinants (résumé)]], [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp5 (résumé)|chp5 (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp6 (résumé)|chp6 (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp7 (résumé)|chp7 (résumé)]]
