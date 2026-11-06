---
type: source
tags:
  - year1
sources:
  - "[[chp4|chp4 (Algèbre)]]"
maj: 2026-11-06
complet: true
---

Résumé de [[chp4|chp4 (Algèbre)]], dans [[Algèbre linéaire (matière)]] : chapitre 4, matrices. En cas d'écart, le cours et ses images font foi.

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
L'image du cours porte $n$ comme borne de la somme, mais un dessin ajoute un « m » à cet endroit, ce qui correspond aux tailles (voir les points à vérifier).

Propriétés :

- $AB \neq BA$ en général ;
- $AC = BC \not\Rightarrow A = B$ ;
- $A(BC) = (AB)C$ ;
- $\lambda(AB) = (\lambda A)B = A(\lambda B)$ ;
- si $B$ et $C$ ont même dimension : $A(B + C) = AB + AC$.

## Matrice d'une application linéaire

On appelle [[Matrice d'une application linéaire|matrice de $f$]] dans les [[Base (algèbre linéaire)|bases]] $B$ et $B'$ la matrice de $\mathcal{M}_{n,p}(\mathbb{R})$ dont les colonnes sont les coordonnées dans $B'$ des (images des) vecteurs de $B$.

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Contenu absent** : « Dans cette base, on note », « Si je note », « Calcul de l'image d'un vecteur » et « Application » ne sont suivis de rien, et « M_f × M_f-1 = » s'arrête après le signe égal. L'export de Google, en docx comme en PDF, est vide à ces endroits. Regarde si ton Google Doc contient ces formules. **Je ne les ai pas complétées.**
2. **Matrice de $f$** : « les coordonnées dans B' des vecteurs de B » doit se lire « des **images par $f$** des vecteurs de B », comme le dit la section suivante.
3. **Borne du produit matriciel** : l'image écrit $\sum_{k=1}^{n}$ ; avec $A$ de format $(n,m)$, la borne est $m$, comme l'indique le « m » du dessin.
