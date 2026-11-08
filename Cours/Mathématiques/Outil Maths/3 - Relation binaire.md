---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 3 - Relation binaire.docx|Chapitre 3 - Relation binaire]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 3 - Relation binaire.docx|Chapitre 3 - Relation binaire]] (cours d'Outils maths du 29/11/23), dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]. Le cours ne contient aucune figure : ses images sont des encadrés de définitions (recopiés ici) et une petite icône décorative.

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
| [[Relation antisymétrique\|Antisymétrique]] | $(x\mathcal{R}y$ et $y\mathcal{R}x) \Rightarrow x = y$ [[Erreurs du cours#^e-3-relation-binaire\|✎]] |
| [[Relation transitive\|Transitive]] | $x\mathcal{R}y$ et $y\mathcal{R}z \Rightarrow x\mathcal{R}z$ |

Toutes ces propriétés s'entendent « pour tous $x, y, z \in E$ ».

Symétrique et antisymétrique ne sont pas des contraires : l'égalité $=$ est à la fois symétrique et antisymétrique, et une relation peut n'être ni l'une ni l'autre (sur $\{1, 2, 3\}$, la relation $\{(1, 2), (2, 1), (2, 3)\}$ : $(1,2)$ et $(2,1)$ empêchent l'antisymétrie, $(2,3)$ sans $(3,2)$ empêche la symétrie). Pour montrer qu'une propriété est fausse, un seul contre-exemple suffit. [[Complément hors du cours|ⓘ]]

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

Exemple : sur $\mathbb{Z}$, $x \sim y \iff 3 \mid (x - y)$ (même reste dans la division par 3). Il y a trois classes, $[0] = \{\dots, -3, 0, 3, 6, \dots\}$, $[1] = \{\dots, -2, 1, 4, \dots\}$ et $[2] = \{\dots, -1, 2, 5, \dots\}$ ; l'ensemble quotient est $\mathbb{Z}/3\mathbb{Z} = \{[0], [1], [2]\}$. Une classe a plusieurs noms : $[1] = [4] = [-2]$. [[Complément hors du cours|ⓘ]]

Propriété clé : $x \sim y \iff [x] = [y]$, et deux classes sont soit égales, soit disjointes. Raison : si $z \in [x] \cap [y]$, alors $x \sim z$ et $y \sim z$, donc $x \sim y$ par symétrie et transitivité, et les deux classes coïncident. [[Complément hors du cours|ⓘ]]

Les classes forment une [[Partition d'un ensemble|partition]] de $E$ : chaque classe est non vide ($x \in [x]$ par réflexivité), deux classes distinctes sont disjointes, et leur réunion est $E$. [[Complément hors du cours|ⓘ]]

Méthode générale : si $g : E \to F$ est une application, la relation $x \sim y \iff g(x) = g(y)$ est toujours une relation d'équivalence (elle hérite des propriétés de l'égalité), et ses classes sont les ensembles d'éléments de même image. C'est le sens précis de « avoir le même … » : même reste ($g$ = reste), même âge, même direction. [[Complément hors du cours|ⓘ]]

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

Exemples d'ordres partiels : la [[Divisibilité]] sur $\mathbb{N}^*$ (2 et 3 ne sont pas comparables : ni $2 \mid 3$ ni $3 \mid 2$) et l'[[Inclusion (ensembles)|inclusion]] sur les parties d'un ensemble ($\{1\}$ et $\{2\}$ ne sont pas comparables). L'**ordre lexicographique** (celui du dictionnaire) est un exemple d'ordre total sur les mots ou sur $\mathbb{R}^2$ : $(a, b) \preccurlyeq (a', b')$ si $a < a'$, ou si $a = a'$ et $b \le b'$. [[Complément hors du cours|ⓘ]]

À toute relation d'ordre $\preccurlyeq$ on associe l'**ordre strict** $x \prec y \iff (x \preccurlyeq y$ et $x \neq y)$ : il est irréflexif (jamais $x \prec x$) et transitif. C'est le statut de $<$ par rapport à $\le$ : $<$ n'est pas une relation d'ordre au sens du cours, mais l'ordre strict associé à $\le$. [[Complément hors du cours|ⓘ]]

### Majorant, maximum, borne supérieure

Soit $(E, \preceq)$ un ensemble ordonné et $A \subseteq E$ (voir [[Majorant et minorant]]).

- $x \in A$ est **maximal** dans $A$ s'il n'existe pas d'élément plus grand que lui dans $A$ (voir [[Élément maximal]]).
- $x \in E$ est un **majorant** de $A$ si $\forall y \in A,\ y \preceq x$.
- $A$ admet au plus un majorant qui appartienne à $A$ (par antisymétrie) : c'est le **[[Plus grand élément|plus grand élément]]** de $A$, noté $\max(A)$ s'il existe.
- Le plus petit des majorants est la **[[Borne supérieure|borne supérieure]]**, notée $\sup(A)$. Autrement dit :
$$\forall y \in A,\ y \preceq \sup(A) \quad \text{et} \quad \forall z \text{ majorant de } A,\ \sup(A) \preceq z.$$

Liens entre ces notions : si $\max(A)$ existe, c'est aussi $\sup(A)$ et c'est le seul élément maximal de $A$. La réciproque est fausse dans un ordre partiel : avec l'inclusion, $A = \{\{1\}, \{2\}\}$ a deux éléments maximaux, $\{1\}$ et $\{2\}$, mais pas de plus grand élément ; sa borne supérieure (dans les parties de $\{1, 2\}$) est $\{1\} \cup \{2\} = \{1, 2\}$, qui n'est pas dans $A$. Dans un ordre total, élément maximal et plus grand élément se confondent. [[Complément hors du cours|ⓘ]]

Dans $(\mathbb{R}, \le)$, toute partie non vide et majorée admet une borne supérieure : c'est la propriété fondamentale qui distingue $\mathbb{R}$ de $\mathbb{Q}$ (dans $\mathbb{Q}$, $\{x \in \mathbb{Q} \mid x^2 < 2\}$ est majorée mais n'a pas de borne supérieure rationnelle, car $\sqrt 2 \notin \mathbb{Q}$ : voir [[Irrationalité de √2]]). Caractérisation pratique dans $\mathbb{R}$ : $M = \sup(A)$ si et seulement si $M$ majore $A$ et $\forall \varepsilon > 0,\ \exists a \in A,\ M - \varepsilon < a$. Voir [[Borne supérieure]]. [[Complément hors du cours|ⓘ]]

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
