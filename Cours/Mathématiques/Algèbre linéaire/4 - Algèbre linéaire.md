---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp4.docx|chp4 (Algèbre)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp4.docx|chp4 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 4, matrices.
## Généralités

- Une [[Matrice]] $A$ de format $n \times p$ a $n$ lignes et $p$ colonnes.
- $a_{ij}$ est le coefficient de la $i$-ième ligne et de la $j$-ième colonne.

### Matrices particulières

| Matrice | Définition |
|---|---|
| Carrée d'ordre $n$ | Dimension $n \times n$ |
| [[Matrice diagonale\|Diagonale]] | Coefficients hors de la diagonale nuls |
| Identité | Matrice diagonale dont les coefficients diagonaux valent 1 |
| Nulle | Tous les coefficients valent 0 |

Deux autres familles reviennent souvent : la [[Matrice triangulaire|matrice triangulaire]] supérieure (coefficients nuls sous la diagonale, $a_{ij} = 0$ pour $i > j$) ou inférieure, et la [[Matrice symétrique|matrice symétrique]], égale à sa transposée ($a_{ij} = a_{ji}$). La matrice identité d'ordre $n$ se note $I_n$, la matrice nulle $O_{n,p}$. [[Complément hors du cours|ⓘ]]

- L'ensemble des matrices $n \times p$ se note $\mathcal{M}_{n,p}(\mathbb{R})$ (parfois sans préciser $\mathbb{R}$) ; celui des matrices carrées, $\mathcal{M}_n(\mathbb{R})$.
- **Théorème** : $\mathcal{M}_{n,p}(\mathbb{R})$ est un [[Espace vectoriel|espace vectoriel]] de [[Dimension (algèbre linéaire)|dimension]] $n \times p$.
- La dimension $n \times p$ vient de sa **base canonique** : les matrices élémentaires $E_{ij}$, dont tous les coefficients sont nuls sauf celui de la ligne $i$ et de la colonne $j$, qui vaut 1. Toute matrice s'écrit $A = \sum_{i,j} a_{ij} E_{ij}$, de façon unique. [[Complément hors du cours|ⓘ]]
- La [[Transposée]] d'une matrice $A$ de format $(n,p)$ est une matrice $A'$ de format $(p,n)$.
- Précisément, la transposée (notée aussi $A^T$ ou ${}^tA$) échange lignes et colonnes : son coefficient $(i,j)$ est $a_{ji}$. Elle vérifie $(A^T)^T = A$, $(A + B)^T = A^T + B^T$, $(\lambda A)^T = \lambda A^T$ et, attention à l'ordre, $(AB)^T = B^T A^T$. [[Complément hors du cours|ⓘ]]
- $-A$ est l'opposée de $A$ : $-A + A = O_{n,p}$.

## Opérations

| Somme | Produit par un scalaire |
|---|---|
| $A$ et $B$ de mêmes dimensions | $\lambda A = (\lambda a_{ij})$ |
| $c_{ij} = a_{ij} + b_{ij}$ | $\lambda(A + B) = \lambda A + \lambda B$ |
| $A + B = B + A$ ; $A + (B + C) = (A + B) + C$ | $(\alpha + \beta) A = \alpha A + \beta A$ |

- $A = B \iff A + C = B + C$ ;
- $A + C = B \iff A = B - C$.

### Produit matriciel

[[Produit matriciel]] : $A_{(n,m)} \times B_{(m,p)} = C_{(n,p)}$, et pour tout coefficient de $C$ (la somme porte sur les $m$ colonnes de $A$, qui sont les $m$ lignes de $B$) : [[Erreurs du cours#^e-4-algebre-lineaire|✎]]
$$\forall i \in [\![1; n]\!],\ \forall j \in [\![1; p]\!],\quad c_{ij} = \sum_{k=1}^{m} a_{ik} b_{kj}$$

Autrement dit, $c_{ij}$ est le produit de la ligne $i$ de $A$ par la colonne $j$ de $B$, terme à terme puis sommé : le produit n'existe que si le nombre de colonnes de $A$ égale le nombre de lignes de $B$. Exemple : [[Complément hors du cours|ⓘ]]
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1\cdot5 + 2\cdot7 & 1\cdot6 + 2\cdot8 \\ 3\cdot5 + 4\cdot7 & 3\cdot6 + 4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

Propriétés :

- $AB \neq BA$ en général ;
- $AC = BC \not\Rightarrow A = B$ ;
- $A(BC) = (AB)C$ ;
- $\lambda(AB) = (\lambda A)B = A(\lambda B)$ ;
- si $B$ et $C$ ont même dimension : $A(B + C) = AB + AC$.

Contre-exemples aux deux premières propriétés : avec $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ et $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $AB = B$ mais $BA = O_2$ ; ainsi $BA = O_2 \cdot A$ avec $B \neq O_2$, ce qui montre qu'on ne peut pas « simplifier » par une matrice. On ne le peut que si la matrice simplifiée est [[Matrice inversible|inversible]]. Un produit de matrices non nulles peut aussi être nul ($BA = O_2$) : il n'y a pas de règle du produit nul. [[Complément hors du cours|ⓘ]]

La matrice identité est l'élément neutre du produit : $I_n A = A I_n = A$ pour $A \in \mathcal{M}_n(\mathbb{R})$. On définit les puissances d'une matrice carrée par $A^0 = I_n$ et $A^{k+1} = A^k A$. Comme $AB \neq BA$ en général, $(A + B)^2 = A^2 + AB + BA + B^2$, et la [[Formule du binôme de Newton|formule du binôme]] ne vaut que si $AB = BA$. [[Complément hors du cours|ⓘ]]

## Matrice d'une application linéaire

On appelle [[Matrice d'une application linéaire|matrice de $f$]] dans les [[Base (algèbre linéaire)|bases]] $B$ et $B'$ la matrice de $\mathcal{M}_{n,p}(\mathbb{R})$ dont les colonnes sont les coordonnées dans $B'$ des images par $f$ des vecteurs de $B$. [[Erreurs du cours#^e-4-algebre-lineaire|✎]]

Ici $f : E \to F$ est linéaire, $B = (e_1, \dots, e_p)$ est une base de $E$ (dimension $p$) et $B' = (e'_1, \dots, e'_n)$ une base de $F$ (dimension $n$) : la matrice a autant de colonnes que la dimension de départ et autant de lignes que la dimension d'arrivée. Une application linéaire est entièrement déterminée par les images des vecteurs d'une base, d'où le fait que ces $p$ colonnes suffisent. [[Complément hors du cours|ⓘ]]

### Matrice d'un vecteur

Soit une base $B = (e_1, \dots, e_n)$ : tout vecteur $x$ de $E$ s'écrit comme [[Combinaison linéaire|combinaison linéaire]] des vecteurs de la base, $x = \lambda_1 e_1 + \lambda_2 e_2 + \dots + \lambda_n e_n$ ([[Coordonnées dans une base]]). « Dans cette base, on note » n'est suivi de rien dans le cours.

La notation attendue est la **matrice colonne des coordonnées** de $x$ dans $B$ : $X = \begin{pmatrix} \lambda_1 \\ \vdots \\ \lambda_n \end{pmatrix} \in \mathcal{M}_{n,1}(\mathbb{R})$. Les $\lambda_i$ sont uniques, parce que $B$ est une base (famille libre et génératrice). [[Complément hors du cours|ⓘ]]

### Matrice d'une application

« Si je note » n'est suivi de rien. Le cours conclut : la matrice a pour colonne $j$ l'image du $j$-ième vecteur de la base.

Exemple : $f : \mathbb{R}^2 \to \mathbb{R}^2$, $f(x, y) = (x + 2y,\ 3x)$, dans la base canonique $e_1 = (1,0)$, $e_2 = (0,1)$. On a $f(e_1) = (1, 3)$ et $f(e_2) = (2, 0)$, donc $M_f = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$. [[Complément hors du cours|ⓘ]]

### Calcul de l'image d'un vecteur

Section vide dans le cours.

Le résultat classique de cette section : si $X$ est la colonne des coordonnées de $x$ dans $B$ et $M$ la matrice de $f$ dans $B$ et $B'$, alors la colonne $Y$ des coordonnées de $f(x)$ dans $B'$ est $Y = MX$. Il découle de la linéarité : $f(x) = \lambda_1 f(e_1) + \dots + \lambda_p f(e_p)$, soit la combinaison des colonnes de $M$ par les coordonnées de $x$. Avec l'exemple précédent, $x = (1, 1)$ donne $\begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$, et bien $f(1,1) = (3, 3)$. [[Complément hors du cours|ⓘ]]

### Matrice de la composée

**Théorème** ([[Composition de fonctions|composée]]) : soit $M_f$ la matrice de $f$ et $M_g$ celle de $g$ dans la base $B$. Alors
$$M_{g \circ f} = M_g \times M_f.$$
Donc si $f$ admet une réciproque $f^{-1}$, $M_{f^{-1}}$ vérifie $M_f \times M_{f^{-1}} = \ $ (la fin manque dans le cours ; on attend la matrice identité, voir [[Matrice inversible]]).

Ce théorème explique la définition du produit matriciel : il est construit pour que composer les applications revienne à multiplier les matrices, ce qui explique aussi pourquoi $AB \neq BA$ ($g \circ f \neq f \circ g$ en général). Comme $f \circ f^{-1} = f^{-1} \circ f = \mathrm{Id}$, on obtient $M_f M_{f^{-1}} = M_{f^{-1}} M_f = I_n$ : $M_{f^{-1}} = (M_f)^{-1}$. Une matrice carrée est inversible exactement quand l'application qu'elle représente est bijective, et alors $(AB)^{-1} = B^{-1} A^{-1}$. [[Complément hors du cours|ⓘ]]

### Application

Section vide dans le cours.
