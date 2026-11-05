---
type: source
sources: ["[[Cours/Year 1/Algèbre Linéaire/Cours/chp4|chp4 (Algèbre)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 1/Algèbre Linéaire/Cours/chp4|chp4 (Algèbre)]], dans [[Year 1 - Algèbre Linéaire]]. En cas d'écart, le cours et ses images font foi.

## Contenu

- **Généralités** : une matrice $n \times p$ a $n$ lignes et $p$ colonnes. Le cours définit les matrices carrée, diagonale, identité et nulle. $M_{n,p}(\mathbb{R})$ est un espace vectoriel de dimension $n \times p$.
- **Opérations** : somme de matrices de même taille, produit par un scalaire, [[Transposée]].
- **[[Produit matriciel]]** : $A_{(n,m)} \times B_{(m,p)} = C_{(n,p)}$, avec $c_{ij} = \sum_{k=1}^{m} a_{ik}b_{kj}$. L'image porte $n$ comme borne, mais un dessin ajoute un « m » à cet endroit, ce qui correspond aux tailles. Il est associatif et non commutatif, et $AC = BC$ n'implique pas $A = B$.
- **Matrice d'une [[Transformation linéaire|application linéaire]]** : ses colonnes viennent des images des vecteurs de la base.
- **Composée** : $M_{g \circ f} = M_g \times M_f$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Contenu absent** : « Dans cette base, on note », « Si je note », « Calcul de l'image d'un vecteur » et « Application » ne sont suivis de rien, et « M_f × M_f-1 = » s'arrête après le signe égal. L'export de Google, en docx comme en PDF, est vide à ces endroits. Regarde si ton Google Doc contient ces formules. **Je ne les ai pas complétées.**
2. **Matrice de $f$** : « les coordonnées dans B' des vecteurs de B » doit se lire « des **images par $f$** des vecteurs de B », comme le dit la section suivante.