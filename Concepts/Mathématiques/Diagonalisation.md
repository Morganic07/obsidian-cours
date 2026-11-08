---
type: concept
tags:
  - year1
  - year2
aliases:
  - diagonalizable
  - diagonalization
  - orthogonally diagonalizable
  - diagonalisable
  - étapes pour diagonaliser
sources:
  - "[[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]]"
maj: 2026-11-08
---

$A$ est diagonalisable si $A = PDP^{-1}$ avec $D$ [[Matrice diagonale|diagonale]]. Cette écriture sert notamment à calculer $A^n = PD^nP^{-1}$.

- **Théorème** : $A$ est diagonalisable si et seulement si elle a $n$ vecteurs propres indépendants, qui forment alors les colonnes de $P$ et une base de vecteurs propres de $\mathbb{R}^n$. La diagonale de $D$ porte les valeurs propres correspondantes, dans le même ordre.
- **Condition suffisante** : $n$ valeurs propres distinctes suffisent, mais ne sont pas nécessaires.
- **Condition générale** : la somme des dimensions des [[Espace propre|espaces propres]] vaut $n$. Autrement dit, le polynôme caractéristique se factorise entièrement, et chaque espace propre a pour dimension la [[Multiplicité d'une valeur propre|multiplicité]] de sa valeur propre.
- **Orthogonalement diagonalisable** : $A = PDP^T$ avec $P$ orthogonale, ce qui équivaut à $A$ symétrique ([[Théorème spectral]]).

Méthode en six étapes : trouver les valeurs propres, puis les vecteurs propres, vérifier qu'il y en a $n$ indépendants, construire $P$ puis $D$ dans le même ordre, calculer $P^{-1}$ par $[P \mid I] \sim [I \mid P^{-1}]$, et vérifier.

## Pour un endomorphisme (complément, hors du cours)

Un endomorphisme $f \in L(E)$, $E$ de dimension finie, est **diagonalisable** s'il existe une base de $E$ formée de [[Vecteur propre|vecteurs propres]] de $f$ ; sa [[Matrice d'une application linéaire|matrice]] dans cette base est alors diagonale, avec les valeurs propres sur la diagonale. Si $\lambda_1, \dots, \lambda_p$ sont ses valeurs propres distinctes, les conditions suivantes sont équivalentes :
$$f \text{ diagonalisable} \iff E = E_{\lambda_1} \oplus \dots \oplus E_{\lambda_p} \iff \sum_{i=1}^{p} \dim E_{\lambda_i} = \dim E.$$
Cela s'appuie sur le théorème du chapitre 7 de 1re année : les [[Espace propre|espaces propres]] sont toujours en [[Somme directe|somme directe]], donc $\sum \dim E_{\lambda_i} \le \dim E$, et il suffit de réunir des bases de chaque $E_{\lambda_i}$ quand il y a égalité ([[7 - Algèbre linéaire]]). Une matrice $A$ est diagonalisable exactement quand l'endomorphisme $X \mapsto AX$ de $\mathbb{R}^n$ l'est.

**Exemple** : la projection $p(x, y) = (x, 0)$ de $\mathbb{R}^2$ a pour espaces propres $E_1 = \text{Vect}\big((1,0)\big)$ et $E_0 = \text{Vect}\big((0,1)\big)$ ; $\mathbb{R}^2 = E_0 \oplus E_1$, et dans la base $\big((1,0),(0,1)\big)$ la matrice de $p$ est $\text{diag}(1, 0)$.

Notion parente : [[Valeur propre]]. Voir aussi : [[Vecteur propre]], [[Espace propre]], [[Matrice diagonale]], [[Multiplicité d'une valeur propre]], [[Théorème spectral]], [[Matrice symétrique]], [[Décomposition en valeurs singulières]], [[Somme directe]], [[Matrices semblables]]

Résumés : [[0 - Eigenvalues and eigenvectors]], [[2 - Symmetric matrices and quadratic forms]], [[7 - Algèbre linéaire]]
