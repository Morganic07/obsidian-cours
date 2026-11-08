---
type: concept
tags: [year1]
aliases: [Sarrus' rule, Sarrus rule, règle de Sarrus]
sources: ["[[Raw/Year 1/Algèbre Linéaire/Cours /chp6.docx|chp6 (Algèbre)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la règle de Sarrus est une méthode de calcul du [[Déterminant|déterminant]] d'une matrice $3 \times 3$, et d'elle seule. Pour $A = (a_{ij})$ :

$$\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}.$$

**Moyen mnémotechnique** : on recopie les deux premières colonnes à droite de la matrice,

$$\begin{matrix} a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\ a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\ a_{31} & a_{32} & a_{33} & a_{31} & a_{32} \end{matrix}$$

puis on additionne les produits des trois diagonales descendantes (de gauche à droite, vers le bas) et on retranche ceux des trois diagonales montantes.

Elle donne le même résultat que le développement selon la première ligne ([[Développement colonnes-lignes]]) : les six termes sont ceux de $a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})$.

**Attention** : elle ne se généralise pas à $n \geq 4$. Un déterminant $n \times n$ compte $n!$ termes, soit $24$ pour $n = 4$, alors qu'un « Sarrus » à quatre colonnes n'en produirait que $8$ : il faut développer selon une ligne ou une colonne, ou se ramener à une [[Matrice triangulaire|matrice triangulaire]] par opérations sur les lignes.

**Exemple** : pour $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$,
$$\det A = \underbrace{1\cdot1\cdot0}_{0} + \underbrace{2\cdot4\cdot5}_{40} + \underbrace{3\cdot0\cdot6}_{0} - \underbrace{3\cdot1\cdot5}_{15} - \underbrace{1\cdot4\cdot6}_{24} - \underbrace{2\cdot0\cdot0}_{0} = 1.$$

## Dans le cours

Le cours ne la nomme pas : le chapitre 6 calcule les déterminants par développement selon une ligne ou une colonne. Elle apparaît dans les compléments de [[6 - Algèbre linéaire]].

Voir aussi : [[Déterminant]], [[Développement colonnes-lignes]], [[Matrice triangulaire]], [[Matrice inversible]].

Résumés : [[6 - Algèbre linéaire]]
