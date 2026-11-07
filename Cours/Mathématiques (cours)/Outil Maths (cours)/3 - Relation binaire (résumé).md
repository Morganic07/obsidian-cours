---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 3 - Relation binaire.docx|Chapitre 3 - Relation binaire]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 3 - Relation binaire.docx|Chapitre 3 - Relation binaire]] (cours d'Outils maths du 29/11/23), dans [[Outil Maths (index)]]. En cas d'écart, le cours et ses images font foi. Le cours ne contient aucune figure : ses images sont des encadrés de définitions (recopiés ici) et une petite icône décorative.

## Idée générale

Une [[Relation binaire]] relie des éléments d'un ensemble. Deux familles comptent : les relations d'équivalence (classer) et les relations d'ordre (hiérarchiser). Voir [[Relation d'équivalence]] et [[Relation d'ordre]].

## Relation binaire

**Définition 1.** Une relation binaire $\mathcal{R}$ définie sur un ensemble $E$ est, au choix :
- une propriété qui relie ou non deux éléments $x$ et $y$ de $E$ ; on note $x\,\mathcal{R}\,y$ pour dire que $x$ est en relation avec $y$ ;
- une partie de $E \times E$ (voir [[Produit cartésien]]) ; on note $x\,\mathcal{R}\,y$ si $(x, y) \in \mathcal{R}$.

### Propriétés possibles d'une relation

| Propriété | Définition (tableau du cours) |
|---|---|
| [[Relation réflexive\|Réflexive]] | $x\mathcal{R}x$ |
| [[Relation symétrique\|Symétrique]] | $x\mathcal{R}y \iff y\mathcal{R}x$ |
| [[Relation antisymétrique\|Antisymétrique]] | le cours écrit $(x\mathcal{R}y$ et $y\mathcal{R}z) \Rightarrow x = y$ ; définition usuelle : $(x\mathcal{R}y$ et $y\mathcal{R}x) \Rightarrow x = y$ (voir « Points à vérifier ») |
| [[Relation transitive\|Transitive]] | $x\mathcal{R}y$ et $y\mathcal{R}z \Rightarrow x\mathcal{R}z$ |

Toutes ces propriétés s'entendent « pour tous $x, y, z \in E$ ».

## Relation d'équivalence

Une relation d'équivalence, parfois notée $\sim$ ($x \sim y$), doit être à la fois (moyen mnémotechnique **TSR**) :
- **T**ransitive,
- **S**ymétrique,
- **R**éflexive.

**Classe d'équivalence** de $x \in E$, notée $[x]$, $\mathrm{Cl}(x)$ ou $\bar x$ : l'ensemble des éléments $y$ de $E$ en relation avec $x$ par $\mathcal{R}$ :
$$[x] = \{y \in E \mid x \sim y\}.$$

Toute classe d'équivalence peut s'exprimer par « avoir le même [propriété de la relation] » (par exemple : avoir le même reste dans la division par $n$, voir [[Congruence modulo n]]).

**Ensemble quotient** : l'ensemble des classes d'équivalence de tous les éléments de $E$ muni de $\mathcal{R}$, noté $E/\mathcal{R}$ :
$$E/\mathcal{R} = \{[a] \mid a \in E\}.$$

Les classes forment une [[Partition d'un ensemble|partition]] de $E$ (complément usuel, non écrit dans le cours).

## Relation d'ordre

Une relation d'ordre, parfois notée $\leqslant$ ou $\preccurlyeq$ ($x \preccurlyeq y$), doit être à la fois (moyen mnémotechnique **TAR**) :
- **T**ransitive,
- **A**ntisymétrique,
- **R**éflexive.

**Ordre total, ordre partiel** :
- $\mathcal{R}$ est **totale** si deux éléments quelconques de $E$ sont comparables :
$$\forall x, y \in E,\ x\mathcal{R}y \ \text{ou}\ y\mathcal{R}x ;$$
- $\mathcal{R}$ est **partielle** dans le cas contraire.

Remarque du cours : la réflexivité est imposée dans la définition des relations d'ordre ; on privilégie les relations du type « inférieur **ou égal** ». La transitivité et l'antisymétrie permettent de hiérarchiser les éléments d'un ensemble. Sur $\mathbb{R}$, $\le$ et $\ge$ sont des relations d'ordre, tandis que $<$ et $>$ ne le sont pas, faute de réflexivité.

### Majorant, maximum, borne supérieure

Soit $(E, \preceq)$ un ensemble ordonné et $A \subseteq E$ (voir [[Majorant et minorant]]).

- $x \in A$ est **maximal** dans $A$ s'il n'existe pas d'élément plus grand que lui dans $A$ (voir [[Élément maximal]]).
- $x \in E$ est un **majorant** de $A$ si $\forall y \in A,\ y \preceq x$.
- $A$ admet au plus un majorant qui appartienne à $A$ (par antisymétrie) : c'est le **[[Plus grand élément|plus grand élément]]** de $A$, noté $\max(A)$ s'il existe.
- Le plus petit des majorants est la **[[Borne supérieure|borne supérieure]]**, notée $\sup(A)$. Autrement dit :
$$\forall y \in A,\ y \preceq \sup(A) \quad \text{et} \quad \forall z \text{ majorant de } A,\ \sup(A) \preceq z.$$

### Minorant, minimum, borne inférieure (définitions symétriques)

- $x \in A$ est **minimal** dans $A$ s'il n'existe pas d'élément plus petit que lui dans $A$.
- $x \in E$ est un **minorant** de $A$ si $\forall y \in A,\ x \preceq y$.
- $A$ admet au plus un minorant qui appartienne à $A$ (par antisymétrie) : c'est le **plus petit élément** de $A$, noté $\min(A)$ s'il existe.
- Le plus grand des minorants est la **borne inférieure**, notée $\inf(A)$ :
$$\forall y \in A,\ \inf(A) \preceq y \quad \text{et} \quad \forall z \text{ minorant de } A,\ z \preceq \inf(A).$$

### Tableau récapitulatif

| Notion | Appartient à | Condition |
|---|---|---|
| Élément maximal | $A$ | aucun élément de $A$ strictement plus grand |
| Majorant | $E$ | $\forall y \in A,\ y \preceq x$ |
| $\max(A)$ | $A$ | majorant de $A$ qui est dans $A$ (unique s'il existe) |
| $\sup(A)$ | $E$ | plus petit des majorants |
| Élément minimal | $A$ | aucun élément de $A$ strictement plus petit |
| Minorant | $E$ | $\forall y \in A,\ x \preceq y$ |
| $\min(A)$ | $A$ | minorant de $A$ qui est dans $A$ (unique s'il existe) |
| $\inf(A)$ | $E$ | plus grand des minorants |

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Antisymétrie dans le tableau** : le cours écrit « $(xRy$ et $yRz) \Rightarrow x = y$ ». La définition usuelle est $(xRy$ et $yRx) \Rightarrow x = y$ (complément). **À corriger avant un examen.**
2. **« Au plus un seul majorant dans $A$ »** : le texte dit que $A$ admet au plus un majorant qui soit dans $A$, c'est le plus grand élément. La formulation est elliptique : ce sont les majorants appartenant à $A$ qui sont au plus un.
3. **Image minuscule de l'ordre** : la transcription la dit peut-être décorative, et lit les symboles $\leqslant$, $\preccurlyeq$, $\precsim$ d'après leur forme. Rien d'important n'en dépend. (L'image des courbes colorées, placée sous le titre « Relation d'ordre », a été ouverte : c'est une icône décorative, sans contenu de cours. L'image des symboles n'a pas été ouverte.)
4. **Symétrie** : le cours l'écrit $xRy \iff yRx$ ; la définition usuelle est $xRy \Rightarrow yRx$, équivalente une fois quantifiée sur tous $x, y$.
5. **Coquilles de forme** : le cours écrit « deux éléments quelconques de $E$ sont comparable » et « (par antisymétrique) » ; la fiche écrit « comparables » et « par antisymétrie ». Rien ne change sur le fond.
