---
type: matiere
tags:
  - year1
sources:
  - "[[Cours/Mathématiques/Algèbre linéaire/1 - Algèbre linéaire|chp1 (Algèbre)]]"
  - "[[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2 (Algèbre)]]"
  - "[[3 - Algèbre linéaire|chp3 (Algèbre)]]"
  - "[[4 - Algèbre linéaire|chp4 (Algèbre)]]"
  - "[[5 - Algèbre linéaire|chp5 (Algèbre)]]"
  - "[[6 - Algèbre linéaire|chp6 (Algèbre)]]"
  - "[[7 - Algèbre linéaire|chp7 (Algèbre)]]"
maj: 2026-11-08
---

Algèbre linéaire de 1re année, en français et centrée sur les applications linéaires. [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]] reprend les mêmes notions en anglais, à partir des matrices. Les 7 notes sont intégrées.

## Chapitres

| Note | Sujet | Résumé |
|---|---|---|
| [[Cours/Mathématiques/Algèbre linéaire/1 - Algèbre linéaire\|chp1]] | Espaces vectoriels, familles, bases | [[Cours/Mathématiques/Algèbre linéaire/1 - Algèbre linéaire\|Résumé]] |
| [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire\|chp2]] | Applications linéaires, morphismes, rang | [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire\|Résumé]] |
| [[3 - Algèbre linéaire\|chp3]] | Pivot de Gauss, systèmes | [[3 - Algèbre linéaire\|Résumé]] |
| [[4 - Algèbre linéaire\|chp4]] | Matrices, matrice d'une application | [[4 - Algèbre linéaire\|Résumé]] |
| [[5 - Algèbre linéaire\|chp5]] | Changement de base, déterminant | [[5 - Algèbre linéaire\|Résumé]] |
| [[6 - Algèbre linéaire\|chp6]] | Déterminant, caractérisation des bases | [[6 - Algèbre linéaire\|Résumé]] |
| [[7 - Algèbre linéaire\|chp7]] | Éléments propres, somme directe | [[7 - Algèbre linéaire\|Résumé]] |

## Concepts

- **Espaces vectoriels (chp1)** : [[Espace vectoriel]], [[Sous-espace vectoriel]], [[Combinaison linéaire]], [[Espace engendré]], [[Indépendance linéaire]], [[Base (algèbre linéaire)]], [[Théorème de la base incomplète]], [[Dimension (algèbre linéaire)]], [[Coordonnées dans une base]]
- **Applications linéaires (chp2)** : [[Morphisme]], [[Transformation linéaire]], [[Fonction identité]], [[Homothétie]], [[Composition de fonctions]], [[Injectivité et surjectivité]], [[Bijection]], [[Groupe linéaire]], [[Espace nul]], [[Image d'une application linéaire]], [[Rang d'une matrice]], [[Théorème du rang]]
- **Systèmes et pivot de Gauss (chp3)** : [[Système linéaire]], [[Système linéaire homogène]], [[Opérations élémentaires sur les lignes]], [[Forme échelonnée]]
- **Matrices (chp4 et chp5)** : [[Matrice]], [[Matrice d'une application linéaire]], [[Produit matriciel]], [[Transposée]], [[Matrice inversible]], [[Changement de base]]
- **Déterminant (chp5 et chp6)** : [[Forme multilinéaire alternée]], [[Déterminant]]
- **Éléments propres (chp7)** : [[Valeur propre]], [[Vecteur propre]], [[Spectre (algèbre linéaire)]], [[Espace propre]], [[Somme directe]]
- **Ajoutés par l'enrichissement** : [[Projecteur]], [[Matrices semblables]], [[Règle de Sarrus]], [[Théorème de Cayley-Hamilton]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

[[Morphisme]], [[Changement de base]] et [[Somme directe]] sont propres à cette matière. La plupart des autres sont communs avec [[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]].

## Liens avec les autres matières

- **[[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]]** : les mêmes notions en anglais, à partir des matrices (voir ci-dessous les correspondances de vocabulaire).
- **[[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]** : la [[Bijection]], la [[Composition de fonctions]] et la [[Fonction identité]] y sont vues pour les fonctions en général, avant d'être appliquées ici aux applications linéaires.

## Correspondances de vocabulaire

- Famille libre : linearly independent set
- Famille génératrice : spanning set
- Système compatible : consistent system
- vect$(\dots)$ : Span$\{\dots\}$
- Ker $f$ : Nul $A$
- Im $f$ : Col $A$
- rg : rank

Attention aux tailles : ce cours note une matrice $n \times p$, avec $n$ lignes, alors que Bilinear Algebra note $m \times n$.

## À revoir en priorité avant un examen

- [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]] : si $\dim E = \dim F$ (finie), $f$ injective $\iff$ $f$ surjective $\iff$ $f$ bijective, mais l'égalité des dimensions seule ne rend pas $f$ bijective ; $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.
- [[7 - Algèbre linéaire|chp7]] : un vecteur propre est non nul par définition, alors qu'une valeur propre peut être nulle.

## Contenu manquant

Des formules semblent absentes de [[4 - Algèbre linéaire|chp4]], [[5 - Algèbre linéaire|chp5]] et [[6 - Algèbre linéaire|chp6]] : l'export de Google est vide à ces endroits. Il faut vérifier dans les Google Docs.
