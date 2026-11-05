---
type: source
sources: ["[[Chapitre 3 - Relation binaire]]"]
maj: 2026-11-05
---

Résumé de [[Chapitre 3 - Relation binaire]], dans [[Year 1 - Outil Maths]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une relation binaire relie des éléments d'un ensemble. Deux familles comptent : les relations d'équivalence (classer) et les relations d'ordre (hiérarchiser). Voir [[Relation d'équivalence]] et [[Relation d'ordre]].

## Contenu, dans l'ordre du cours

- **Définition** : une relation $\mathcal{R}$ sur $E$ est une propriété reliant deux éléments, ou une partie de $E \times E$.
- **Propriétés** : réflexive ($xRx$), symétrique ($xRy \Leftrightarrow yRx$), antisymétrique, transitive.
- **Relation d'équivalence** (notée $\sim$) : transitive, symétrique, réflexive. **Classe** $[x] = \{y \in E \mid x \sim y\}$. **Ensemble quotient** $E/R = \{[a] \mid a \in E\}$. Une classe s'exprime par « avoir le même (propriété) ».
- **Relation d'ordre** : transitive, antisymétrique, réflexive. Elle est **totale** si deux éléments sont toujours comparables, **partielle** sinon. La réflexivité est imposée : $\le$ et $\ge$ sont des ordres, $<$ et $>$ n'en sont pas.
- **Majorants et minorants** dans $(E, \preceq)$ avec $A \subseteq E$ : élément maximal, majorant, plus grand élément $\max(A)$ (au plus un, par antisymétrie), borne supérieure $\sup(A)$ (plus petit des majorants). Définitions symétriques pour minimal, minorant, $\min(A)$, $\inf(A)$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes.

1. **Antisymétrie dans le tableau** : le cours écrit « $(xRy$ et $yRz) \Rightarrow x = y$ ». La définition usuelle est $(xRy$ et $yRx) \Rightarrow x = y$ (complément). **À corriger avant un examen.**
2. **« Au plus un seul majorant dans $A$ »** : le texte dit que $A$ admet au plus un majorant qui soit dans $A$, c'est le plus grand élément. La formulation est elliptique : ce sont les majorants appartenant à $A$ qui sont au plus un.
3. **Image minuscule de l'ordre** : la transcription la dit peut-être décorative, et lit les symboles $\leqslant$, $\preccurlyeq$, $\precsim$ d'après leur forme. Rien d'important n'en dépend.
