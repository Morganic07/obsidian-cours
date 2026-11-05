---
type: source
sources: ["[[Chp 0a - Linear combination]]"]
maj: 2026-11-05
---

Résumé de [[Chp 0a - Linear combination]], dans [[Year 2 - Bilinear Algebra]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre montre qu'une même question s'écrit de trois façons équivalentes : un système, une équation vectorielle et une équation matricielle. Il en tire les notions de base : engendrer, être indépendant, transformer.

## Contenu, dans l'ordre du cours

- **[[Système linéaire]]** : il a 0, 1 ou une infinité de solutions. On le résout sur sa matrice augmentée par des opérations élémentaires sur les lignes, réversibles et qui conservent les solutions.
- **[[Forme échelonnée]]** : la forme réduite est unique pour chaque matrice. Une colonne sans pivot correspond à une variable libre. Le système est incompatible si et seulement si la dernière colonne de la matrice augmentée est une colonne pivot.
- **[[Combinaison linéaire]]** et **[[Espace engendré]]** : $\mathbf{b}$ est dans $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ si et seulement si le système de matrice augmentée $[\mathbf{v}_1 \cdots \mathbf{v}_n \mid \mathbf{b}]$ a une solution.
- **Équation $A\mathbf{x} = \mathbf{b}$** : $A\mathbf{x}$ est la combinaison des colonnes de $A$, de poids les coefficients de $\mathbf{x}$. Elle a la même solution que les deux autres formes. Elle a une solution pour tout $\mathbf{b}$ si et seulement si $A$ a un pivot par ligne.
- **Ensemble des solutions** : $A\mathbf{x} = \mathbf{0}$ a toujours la solution triviale. Les solutions de $A\mathbf{x} = \mathbf{b}$ sont $\mathbf{p} + \mathbf{v}_h$, où $\mathbf{p}$ est une solution particulière et $\mathbf{v}_h$ une solution homogène : géométriquement, une translation.
- **[[Indépendance linéaire]]** : $x_1\mathbf{v}_1 + \dots + x_n\mathbf{v}_n = \mathbf{0}$ n'a que la solution triviale. Un ensemble contenant $\mathbf{0}$, ou plus de vecteurs que de coordonnées, est dépendant.
- **[[Transformation linéaire]]** : $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ et $T(c\mathbf{u}) = cT(\mathbf{u})$. Le cours donne les matrices des transformations du plan : réflexions, contractions et dilatations, cisaillements, projections.
- **[[Injectivité et surjectivité]]** : surjective si tout $\mathbf{b}$ a au moins un antécédent, injective s'il en a au plus un.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Théorème « Let A be a nxm matrix »** : il mélange les dimensions, avec $\mathbf{b}$ dans $\mathbb{R}^n$ puis des colonnes qui engendrent $\mathbb{R}^m$. Avec $A$ de taille $n \times m$, les colonnes sont dans $\mathbb{R}^n$ : il faudrait lire $\mathbb{R}^n$ partout (complément, le cours ne le dit pas).
2. **Tableau des réflexions** : image lue directement, deux libellés rouges ne correspondent pas à leur ligne. « Reflection through the line $x_2 = x_1$ » apparaît deux fois, dont une avec le libellé « d'axe $x_2 = -x_1$ », et « Reflection through the line $x_2 = -x_1$ » porte le libellé « d'axe $Ox_2$ ». Les matrices et le texte anglais restent cohérents. Tu as déjà coché ce point dans ta liste, sans que je connaisse ta conclusion.
3. **Colonnes pivots** : « une colonne pivot est linéairement indépendante » est imprécis, car l'indépendance concerne un ensemble de vecteurs. Plus juste : une colonne non pivot est combinaison des colonnes précédentes (complément).
4. **Théorème sur les solutions** : la phrase « **w** = **p** + **v_h** is any solution » a perdu un mot. Il faut lire « où **v_h** est une solution quelconque de $A\mathbf{x} = \mathbf{0}$ ». De même, $\mathbf{x} = t\mathbf{v}$ ne décrit que le cas d'une seule variable libre.
