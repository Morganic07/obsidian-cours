---
type: concept
tags:
  - year1
aliases:
  - sommes directes
  - direct sum
  - sous-espaces supplémentaires
  - en somme directe
  - formule de Grassmann
  - somme de sous-espaces
sources:
  - "[[7 - Algèbre linéaire|chp7 (Algèbre)]]"
  - "[[1 - Algèbre linéaire|chp1 (Algèbre)]]"
  - "[[Raw/Year 1/Algèbre Linéaire/Cours /chp1 .docx|chp1 (Algèbre)]]"
maj: 2026-11-08
---

$E_1$ et $E_2$, sev de $E$, sont supplémentaires, ce qu'on note $E = E_1 \oplus E_2$, si tout $x$ de $E$ s'écrit de façon unique $x_1 + x_2$ avec $x_1 \in E_1$ et $x_2 \in E_2$. Cela équivaut à $\dim E = \dim E_1 + \dim E_2$ et $E_1 \cap E_2 = \{0\}$.

Plusieurs sev sont en somme directe si $x_1 + \dots + x_p = 0$ entraîne $x_1 = \dots = x_p = 0$. C'est le cas des [[Espace propre|espaces propres]] de valeurs propres distinctes.

## Compléments (hors du cours)

- **Somme de deux sev** : $F + G = \{x + y \mid x \in F,\ y \in G\}$. C'est le plus petit sev de $E$ contenant $F$ et $G$, autrement dit $F + G = \operatorname{vect}(F \cup G)$ (voir [[Espace engendré]]).
- **Critère** : la somme $F + G$ est directe (toute décomposition y est unique) si et seulement si $F \cap G = \{0\}$. Ce critère d'intersection ne vaut que pour deux sous-espaces ; à partir de trois, il faut la définition ci-dessus.
- **Formule de Grassmann** (dimension finie) :
$$\dim(F + G) = \dim F + \dim G - \dim(F \cap G).$$
La somme est donc directe si et seulement si $\dim(F + G) = \dim F + \dim G$.
- **Existence d'un supplémentaire** en dimension finie : par le [[Théorème de la base incomplète]], on complète une base de $F$ en une base de $E$ ; les vecteurs ajoutés engendrent un supplémentaire $G$ de $F$. Ce supplémentaire n'est pas unique.
- **Exemple** : dans $\mathbb{R}^2$, deux droites distinctes passant par l'origine sont supplémentaires : leur intersection est $\{0\}$ et $1 + 1 = 2 = \dim \mathbb{R}^2$. L'axe des abscisses a donc une infinité de supplémentaires.
- Une décomposition $E = F \oplus G$ définit la projection sur $F$ parallèlement à $G$ (voir [[Projecteur]]).

Notion parente : [[Sous-espace vectoriel]]. Liens : [[Dimension (algèbre linéaire)]], [[Espace propre]], [[Complément orthogonal]], [[Projecteur]], [[Base (algèbre linéaire)]]

Résumé : [[7 - Algèbre linéaire|chp7]], [[1 - Algèbre linéaire|chp1]]
