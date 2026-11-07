---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp4.docx|chp4 (Algèbre)]]"
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Algèbre Linéaire/Cours /chp4.docx|chp4 (Algèbre)]], dans [[Cours/Mathématiques/Algèbre linéaire/_index|Algèbre linéaire]] : chapitre 4, matrices. En cas d'écart, le cours et ses images font foi.

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

- L'ensemble des matrices $n \times p$ se note $\mathcal{M}_{n,p}(\mathbb{R})$ (parfois sans préciser $\mathbb{R}$) ; celui des matrices carrées, $\mathcal{M}_n(\mathbb{R})$.
- **Théorème** : $\mathcal{M}_{n,p}(\mathbb{R})$ est un [[Espace vectoriel|espace vectoriel]] de [[Dimension (algèbre linéaire)|dimension]] $n \times p$.
- La [[Transposée]] d'une matrice $A$ de format $(n,p)$ est une matrice $A'$ de format $(p,n)$.
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

[[Produit matriciel]] : $A_{(n,m)} \times B_{(m,p)} = C_{(n,p)}$, et pour tout coefficient de $C$ :
$$\forall i \in [\![1; n]\!],\ \forall j \in [\![1; p]\!],\quad c_{ij} = \sum_{k=1}^{m} a_{ik} b_{kj}$$
L'image du cours porte $n$ comme borne de la somme, mais un dessin ajoute un « m » à cet endroit, ce qui correspond aux tailles (voir Erreurs du cours).

Propriétés :

- $AB \neq BA$ en général ;
- $AC = BC \not\Rightarrow A = B$ ;
- $A(BC) = (AB)C$ ;
- $\lambda(AB) = (\lambda A)B = A(\lambda B)$ ;
- si $B$ et $C$ ont même dimension : $A(B + C) = AB + AC$.

## Matrice d'une application linéaire

On appelle [[Matrice d'une application linéaire|matrice de $f$]] dans les [[Base (algèbre linéaire)|bases]] $B$ et $B'$ la matrice de $\mathcal{M}_{n,p}(\mathbb{R})$ dont les colonnes sont les coordonnées dans $B'$ des (images des) vecteurs de $B$ (voir Erreurs du cours).

### Matrice d'un vecteur

Soit une base $B = (e_1, \dots, e_n)$ : tout vecteur $x$ de $E$ s'écrit comme [[Combinaison linéaire|combinaison linéaire]] des vecteurs de la base, $x = \lambda_1 e_1 + \lambda_2 e_2 + \dots + \lambda_n e_n$ ([[Coordonnées dans une base]]). « Dans cette base, on note » n'est suivi de rien dans le cours.

### Matrice d'une application

« Si je note » n'est suivi de rien. Le cours conclut : la matrice a pour colonne $j$ l'image du $j$-ième vecteur de la base.

### Calcul de l'image d'un vecteur

Section vide dans le cours.

### Matrice de la composée

**Théorème** ([[Composition de fonctions|composée]]) : soit $M_f$ la matrice de $f$ et $M_g$ celle de $g$ dans la base $B$. Alors
$$M_{g \circ f} = M_g \times M_f.$$
Donc si $f$ admet une réciproque $f^{-1}$, $M_{f^{-1}}$ vérifie $M_f \times M_{f^{-1}} = \ $ (la fin manque dans le cours ; on attend la matrice identité, voir [[Matrice inversible]]).

### Application

Section vide dans le cours.

## Erreurs du cours

- [[Raw/Year 1/Algèbre Linéaire/Cours /chp4.docx|chp4 (Algèbre)]] écrit $c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$ pour $A_{(n,m)} \times B_{(m,p)}$ ; il faut $\sum_{k=1}^{m}$, comme l'indique le « m » ajouté par un dessin à cet endroit.
- Le cours définit la matrice de $f$ comme celle dont « les colonnes sont les coordonnées dans B' des vecteurs de B » ; il faut « des images par $f$ des vecteurs de B », comme le dit la section suivante.
