---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp6.docx|chp6 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp6.docx|chp6 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 6, [[Déterminant]].
## En dimension 2 et 3

**Définition** : pour $A \in \mathcal{M}_n(\mathbb{R})$, on définit le déterminant par récurrence sur $n$. On note $A_{ij} \in \mathcal{M}_{n-1}(\mathbb{R})$ la [[Matrice|matrice]] obtenue à partir de $A$ en enlevant la ligne $i$ et la colonne $j$.

Les formules (« On définit par récurrence l'application … Par : … On a : ») sont vides dans l'export. La définition est donnée dans [[0 - Determinants|Chp 0c - Determinants]] ; voir aussi [[Développement colonnes-lignes]] et [[Comatrice]].

La définition par récurrence attendue est la suivante : pour $n = 1$, $\det(a) = a$ ; pour $n \geq 2$, on développe selon la première ligne, [[Complément hors du cours|ⓘ]]
$$\det A = \sum_{j=1}^{n} (-1)^{1+j}\, a_{1j} \det A_{1j}.$$
On peut développer de même selon n'importe quelle ligne $i$ ou colonne $j$, avec le signe $(-1)^{i+j}$ (damier de signes $+ - +$ en partant du coin supérieur gauche) : on choisit la ligne ou la colonne qui contient le plus de zéros. [[Complément hors du cours|ⓘ]]

**En dimension 2** : $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$. Exemple : $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = 4 - 6 = -2$. [[Complément hors du cours|ⓘ]]

**En dimension 3**, le développement selon la première ligne donne [[Complément hors du cours|ⓘ]]
$$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}.$$

La [[Règle de Sarrus|règle de Sarrus]] donne le même résultat en dimension 3 seulement : on additionne les produits des trois « diagonales descendantes » et on retranche ceux des trois « diagonales montantes », $\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}$. Elle ne se généralise pas à $n \geq 4$. [[Complément hors du cours|ⓘ]]

Pour une [[Matrice triangulaire|matrice triangulaire]] (en particulier diagonale), le déterminant est le produit des coefficients diagonaux ; donc $\det I_n = 1$. [[Complément hors du cours|ⓘ]]

**Interprétation géométrique** : $|\det A|$ est l'aire du parallélogramme construit sur les deux colonnes (dimension 2), ou le volume du parallélépipède construit sur les trois colonnes (dimension 3). Le signe indique l'orientation : positif si la famille est orientée comme la base canonique. Un déterminant nul signifie que les vecteurs sont « aplatis » dans une droite ou un plan, ce qui éclaire le lien avec les familles liées vu plus bas. [[Complément hors du cours|ⓘ]]

## Le déterminant, une forme multilinéaire alternée

([[Forme multilinéaire alternée]])

Les deux mots du titre : **multilinéaire**, le déterminant est linéaire par rapport à chaque colonne quand on fixe les autres, $\det(\dots, \lambda c + \mu c', \dots) = \lambda \det(\dots, c, \dots) + \mu \det(\dots, c', \dots)$ ; **alternée**, il s'annule dès que deux colonnes sont égales. Le déterminant est l'unique forme multilinéaire alternée des colonnes qui vaut 1 sur la matrice identité. [[Complément hors du cours|ⓘ]]

- **Théorème** : deux lignes égales donnent $\det = 0$ ; deux colonnes égales donnent $\det = 0$.
- Le déterminant est linéaire par rapport à chaque colonne.
- **Théorème** : si l'on échange deux colonnes adjacentes, le déterminant change de signe.
- Le changement de signe vaut pour l'échange de deux colonnes quelconques. Il découle des deux propriétés précédentes : en développant $\det(\dots, c + c', \dots, c + c', \dots) = 0$ par linéarité, on obtient $\det(\dots, c, \dots, c', \dots) + \det(\dots, c', \dots, c, \dots) = 0$. [[Complément hors du cours|ⓘ]]
- Attention : la linéarité vaut colonne par colonne, pas pour la matrice entière. Multiplier une colonne par $\lambda$ multiplie le déterminant par $\lambda$, mais pour $A \in \mathcal{M}_n(\mathbb{R})$, $\det(\lambda A) = \lambda^n \det A$, et en général $\det(A + B) \neq \det A + \det B$. [[Complément hors du cours|ⓘ]]
- **Théorème** : si $A = (c_1 \dots c_n)$, alors $\det A \neq 0 \iff (c_1, \dots, c_n)$ est une [[Base (algèbre linéaire)|base]]. Le déterminant d'une matrice est non nul si et seulement si ses vecteurs colonnes forment une [[Indépendance linéaire|famille libre]].
- **Méthode** : pour démontrer qu'une famille de vecteurs est libre, on calcule le déterminant de la matrice formée de ses vecteurs en colonne. Vecteurs liés : $\det = 0$ ; vecteurs libres : $\det \neq 0$.
- Exemple : $u = (1, 2)$ et $v = (2, 4)$ donnent $\begin{vmatrix} 1 & 2 \\ 2 & 4 \end{vmatrix} = 4 - 4 = 0$ : la famille est liée ($v = 2u$). Avec $v = (3, 1)$, $\begin{vmatrix} 1 & 3 \\ 2 & 1 \end{vmatrix} = 1 - 6 = -5 \neq 0$ : la famille est libre, donc une base de $\mathbb{R}^2$. [[Complément hors du cours|ⓘ]]
- Tous les théorèmes vus sur les colonnes valent aussi pour les lignes.
- La raison : un déterminant est égal à celui de sa [[Transposée|transposée]], $\det A^T = \det A$, et transposer échange lignes et colonnes. [[Complément hors du cours|ⓘ]]
- Un déterminant reste inchangé si l'on ajoute à une ligne (ou une colonne) une [[Combinaison linéaire|combinaison linéaire]] des autres, quelle que soit la taille de la matrice. [[Erreurs du cours#^e-6-algebre-lineaire|✎]]
- Justification : par linéarité, le terme ajouté donne une somme de déterminants ayant deux colonnes proportionnelles, donc nuls. C'est la méthode de calcul pratique : on fait apparaître des zéros par ces opérations (comme dans le [[Forme échelonnée|pivot de Gauss]]), puis on développe ou on lit le produit de la diagonale d'une matrice devenue triangulaire. [[Complément hors du cours|ⓘ]]
- **Déterminant d'un produit** : $\det(AB) = \det A \cdot \det B$. On en déduit que $A$ est [[Matrice inversible|inversible]] si et seulement si $\det A \neq 0$, et qu'alors $\det(A^{-1}) = \dfrac{1}{\det A}$. [[Complément hors du cours|ⓘ]]

## Application des déterminants à la théorie du rang

### Caractérisation des bases

**Théorème fondamental** : soit $A = \| C_1 \dots C_n \|$ une matrice $(n,n)$. Les vecteurs $\{c_1, \dots, c_n\}$ forment une base $\iff \det A \neq 0$.

$\| C_1 \dots C_n \|$ est la matrice dont les colonnes sont les composantes des vecteurs dans la base.

Équivalences :
$$\det A = 0 \iff \text{une des colonnes est combinaison linéaire des autres} \iff \text{la famille des vecteurs colonnes est liée.}$$

Le choix d'une base $(e_1, \dots, e_n)$ de $E$ permet d'identifier $E$ à $\mathbb{K}^n$.

Concrètement, l'application qui associe à $x$ la colonne de ses [[Coordonnées dans une base|coordonnées]] est linéaire et bijective (un isomorphisme) : une famille de $E$ est libre si et seulement si la famille des colonnes de coordonnées l'est dans $\mathbb{K}^n$. C'est ce qui permet d'appliquer le critère du déterminant à des vecteurs d'un espace quelconque (polynômes, matrices), une fois une base choisie. $\mathbb{K}$ désigne $\mathbb{R}$ ou $\mathbb{C}$. [[Complément hors du cours|ⓘ]]

**Théorème** : soit $E$ un espace vectoriel de [[Dimension (algèbre linéaire)|dimension]] $n$. Les vecteurs $(v_1, \dots, v_n)$ forment une base de $E$ $\iff \det \| v_1 \dots v_n \| \neq 0$.

Le critère exige autant de vecteurs que la dimension (matrice carrée) : en dimension $n$, une famille libre de $n$ vecteurs est automatiquement génératrice, donc une base. Pour une famille de $p \neq n$ vecteurs, le déterminant n'est pas défini ; on étudie alors le [[Rang d'une matrice|rang]]. [[Complément hors du cours|ⓘ]]

Le lien avec la « théorie du rang » du titre : un **mineur** d'ordre $r$ d'une matrice est le déterminant d'une sous-matrice carrée $r \times r$ obtenue en gardant $r$ lignes et $r$ colonnes. Le rang d'une matrice (nombre maximal de colonnes linéairement indépendantes) est le plus grand $r$ tel qu'il existe un mineur d'ordre $r$ non nul. Pour une matrice carrée $n \times n$, $\det A \neq 0$ équivaut donc à $\operatorname{rg} A = n$. [[Complément hors du cours|ⓘ]]
