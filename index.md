# Index du wiki

Catalogue de toutes les pages du wiki. À lire en premier pour répondre à une question.

État au 2026-11-05 : 53 concepts, 19 résumés, 3 matières, aucune synthèse. `Year 1/Algèbre Linéaire`, `Year 2/Bilinear Algebra` et `Year 2/Analyse dans Rn` sont intégrées.

## Concepts (53)

### Systèmes et vecteurs

- [[Système linéaire]] : équations à résoudre, compatibles ou non, homogènes ou non
- [[Combinaison linéaire]] : somme de vecteurs multipliés par des scalaires, ce que calcule $A\mathbf{x}$
- [[Espace engendré]] : Span, l'ensemble des combinaisons de vecteurs donnés
- [[Indépendance linéaire]] : $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale
- [[Forme échelonnée]] : forme réduite d'une matrice, qui montre pivots et variables libres
- [[Transformation linéaire]] : application qui respecte l'addition et la multiplication par un scalaire
- [[Injectivité et surjectivité]] : au plus un ou au moins un antécédent
- [[Morphisme]] : homomorphisme, endomorphisme, isomorphisme, automorphisme
- [[Changement de base]] : matrice de passage et $A' = P^{-1}AP$

### Matrices

- [[Produit matriciel]] : $AB$ a pour colonnes les $A\mathbf{b}_j$, et n'est pas commutatif
- [[Matrice inversible]] : matrice carrée qui a un inverse, et ses 20 énoncés équivalents
- [[Transposée]] : la matrice $A^T$, dont les colonnes sont les lignes de $A$
- [[Déterminant]] : nombre associé à une matrice carrée, lié à l'inversibilité et au volume
- [[Matrice symétrique]] : $A^T = A$, orthogonalement diagonalisable
- [[Rang d'une matrice]] : dimension de l'espace des colonnes

### Espaces vectoriels

- [[Espace vectoriel]] : ensemble de vecteurs régi par dix axiomes
- [[Sous-espace vectoriel]] : partie stable contenant le vecteur nul
- [[Espace des colonnes]] : Col $A$, les combinaisons linéaires des colonnes de $A$
- [[Espace nul]] : Nul $A$, les solutions de $A\mathbf{x} = \mathbf{0}$
- [[Sous-espaces fondamentaux]] : Col $A$, Row $A$, Nul $A$ et Nul $A^T$
- [[Somme directe]] : sous-espaces supplémentaires, décomposition unique
- [[Base (algèbre linéaire)]] : famille libre qui engendre un sous-espace
- [[Dimension (algèbre linéaire)]] : nombre de vecteurs d'une base

### Valeurs propres et décompositions

- [[Valeur propre]] : scalaire $\lambda$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ a une solution non triviale
- [[Vecteur propre]] : vecteur non nul associé à une valeur propre
- [[Espace propre]] : Nul$(A - \lambda I)$, le vecteur nul et les vecteurs propres de $\lambda$
- [[Diagonalisation]] : écriture $A = PDP^{-1}$ avec $D$ diagonale
- [[Décomposition en valeurs singulières]] : écriture $A = U\Sigma V^T$, valable pour toute matrice
- [[Factorisation QR]] : écriture $A = QR$, avec $Q$ à colonnes orthonormales

### Orthogonalité

- [[Produit scalaire]] : opération $\mathbf{u} \cdot \mathbf{v}$, d'où vient la norme
- [[Orthogonalité]] : $\mathbf{u} \cdot \mathbf{v} = 0$
- [[Procédé de Gram-Schmidt]] : construit une base orthogonale à partir d'une base
- [[Moindres carrés]] : meilleure solution approchée de $A\mathbf{x} = \mathbf{b}$
- [[Norme]] : taille d'un vecteur, normes $\|\cdot\|_1$, $\|\cdot\|_2$, $\|\cdot\|_\infty$, et distance associée
- [[Complément orthogonal]] : $W^\perp$, les vecteurs orthogonaux à tout $W$
- [[Famille orthogonale]] : vecteurs deux à deux orthogonaux, et familles orthonormales
- [[Projection orthogonale]] : décomposition $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, et point de $W$ le plus proche de $\mathbf{y}$
- [[Matrice orthogonale]] : matrice carrée à colonnes orthonormales, avec $U^{-1} = U^T$
- [[Régression linéaire]] : droite qui minimise la somme des carrés des résidus

### Topologie et limites

- [[Boule et voisinage]] : boules ouvertes et fermées, et parties qui contiennent une boule autour d'un point
- [[Ouvert et fermé]] : parties voisinage de leurs points, et leurs complémentaires
- [[Intérieur et adhérence]] : plus grand ouvert contenu, plus petit fermé contenant, frontière
- [[Limite et continuité]] : définition en $\epsilon$ et $\eta$, et méthode en deux variables
- [[Application lipschitzienne]] : variation majorée par $k\|x - y\|$, et continuité uniforme

### Calcul différentiel

- [[Dérivée partielle]] : dérivée selon une variable, dérivation en chaîne et théorème de Schwarz
- [[Différentielle]] : approximation linéaire de $f$ en un point
- [[Fonction de classe Ck]] : dérivées partielles continues jusqu'à l'ordre $k$
- [[Matrice jacobienne]] : matrice de la différentielle, et jacobien
- [[Gradient]] : vecteur des dérivées partielles, direction de plus grande pente
- [[Équation aux dérivées partielles]] : solutions connues et résolution des systèmes
- [[Difféomorphisme]] : bijection $\mathcal{C}^1$ de réciproque $\mathcal{C}^1$, changements de variables et polaires

### Formes

- [[Forme bilinéaire]] : fonction de deux vecteurs, linéaire en chacun
- [[Forme quadratique]] : $Q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$ avec $A$ symétrique

## Résumés de sources (19)

Le nombre entre parenthèses est celui des points à vérifier dans le cours.

### Year 1 - Algèbre Linéaire

- [[Sources/Year 1/Algèbre Linéaire/chp1 (résumé)|chp1 (résumé)]] : espaces vectoriels, familles, bases (2)
- [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2 (résumé)]] : applications linéaires, morphismes, rang (4)
- [[Sources/Year 1/Algèbre Linéaire/chp3 (résumé)|chp3 (résumé)]] : pivot de Gauss, systèmes (3)
- [[Sources/Year 1/Algèbre Linéaire/chp4 (résumé)|chp4 (résumé)]] : matrices, matrice d'une application (2)
- [[Sources/Year 1/Algèbre Linéaire/chp5 (résumé)|chp5 (résumé)]] : changement de base, déterminant (2)
- [[Sources/Year 1/Algèbre Linéaire/chp6 (résumé)|chp6 (résumé)]] : déterminant, caractérisation des bases (3)
- [[Sources/Year 1/Algèbre Linéaire/chp7 (résumé)|chp7 (résumé)]] : éléments propres, somme directe (2)

### Year 2 - Analyse dans Rn

- [[Chp 2 - éléments de topologie dans Rn (résumé)]] : normes, boules, ouverts, intérieur et adhérence (5)
- [[Chp 3 - Limite et continuité d’applications (résumé)]] : limites, continuité, applications lipschitziennes (5)
- [[Chp 4 - Calcul différentiel du premier ordre (résumé)]] : différentielle, gradient, EDP d'ordre 1, difféomorphismes (6)
- [[Chp 5 - Calcul différentiel d'ordre supérieur (résumé)]] : classe $\mathcal{C}^k$, Schwarz, systèmes et EDP d'ordre 2 (3)

### Year 2 - Bilinear Algebra

- [[Chp 0a - Linear combination (résumé)]] : systèmes, Span, indépendance, transformations (4)
- [[Chp 0b - Matrix algebra (résumé)]] : produit, transposée, inverse (1)
- [[Chp 0c - Determinants (résumé)]] : déterminant, Cramer, formule de l'inverse (1)
- [[Chp 0d - Vector Space (résumé)]] : sous-espaces, base, dimension, rang (1)
- [[Chp 0e - Eigenvalues and eigenvectors (résumé)]] : valeurs propres, diagonalisation (3)
- [[chp 1 - Orthogonality (résumé)]] : projection orthogonale, Gram-Schmidt, QR et moindres carrés (5)
- [[Chp2 - Symmetric matrices and quadratic forms (résumé)]] : théorème spectral, formes quadratiques, SVD (5)
- [[Invertible matrix theorem (résumé)]] : les 20 énoncés équivalents (0)

## Matières (3)

- [[Year 2 - Analyse dans Rn]] : 4 notes intégrées sur 4, et ce qu'il faut revoir en priorité
- [[Year 1 - Algèbre Linéaire]] : 7 notes intégrées sur 7, vocabulaire français et anglais, et ce qu'il faut revoir en priorité
- [[Year 2 - Bilinear Algebra]] : 8 notes intégrées sur 8, et ce qu'il faut revoir en priorité

## Synthèses (0)

Aucune pour l'instant.

## Sources disponibles

Notes présentes dans `Cours/` (175), par matière. Le nombre entre parenthèses est le nombre de notes.

### Year 1

Algo Maths (3), Algèbre Linéaire (7), Analyse Maths (2), Communication orale (2), Corps à l'oeuvre (1), Dessein au cube (10), HDA (1), Outil Maths (4), Peinture (9), Philosophie (2), Projet design (6)

### Year 2

Algo (5), Analyse (3), Analyse dans Rn (4), Anglais (3), Bilinear Algebra (8), Corps à l'oeuvre (1), Operating System (21), Philosophie (5), Probability (7), Projet Design (4), écriture narrative (1)

### Year 3

Computer Network (7), Culture du vivant (3), Data analysis (Thanos) (15), Data base (2), IA (1), Java (1), SHS (3), Statistics (7), Séries (7), ligue football (2), workshop (1), plus 1 note à la racine de `Year 3`

### Year 4

C++ (3), Culture du vivant (1), SHS (3), data mining (1), graph theory (5), management de l'innovationb (2), projet court (1)
