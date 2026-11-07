---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du support du professeur Chapitre 4 - Fonctions (PDF) ([[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]) (25 diapositives, « Outils Mathématiques - Semestre 1 - 2023 », sous-titre « Fonctions injectives, surjectives, bijectives — Ensembles et fonctions »), dans [[Outil Maths (index)]]. Ce chapitre n'existe qu'en PDF. Il prolonge [[3 - Relation binaire (résumé)]] (une fonction est une relation binaire) et [[2 - pdf (résumé)]]. Les propriétés d'injectivité et de surjectivité sont reprises, pour les applications linéaires, dans [[Injectivité et surjectivité]]. Les exercices du support sont posés sans correction.

## Introduction

**Définition (application).** Une [[Application (mathématiques)|application]], c'est deux ensembles $E$ (l'ensemble de **départ** ou de définition) et $F$ (l'ensemble d'**arrivée**) et un procédé $f$ qui associe à chaque élément $x$ de $E$ un élément de $F$ noté $f(x)$. Lorsque $F = \mathbb{R}$, on parle souvent de **fonction**.

**Définition (antécédent).** Soient $E$, $F$ deux ensembles, $f : E \to F$ et $y \in F$. Un **antécédent** de $y$ par $f$ est un $x \in E$ tel que $f(x) = y$. Un élément $y$ peut avoir 0, 1 ou plusieurs antécédents. L'ensemble des antécédents de $y$, éventuellement vide, est noté $f^{-1}(\{y\})$.

**Définition (fonction, forme logique).** Soient $X$ et $Y$ deux ensembles. Une fonction $f$ de $X$ dans $Y$ est une règle qui attribue à chaque $x \in X$ un **unique** $y \in Y$ ; on note $f : X \to Y$ et $f(x) = y$. Formellement :

$$(\forall x \in X,\ \exists y \in Y,\ y = f(x)) \;\wedge\; (\forall x_1 \in X,\ \forall x_2 \in X,\ f(x_1) \ne f(x_2) \Rightarrow x_1 \ne x_2).$$

(Voir point à vérifier 2 sur la seconde condition.)

## Ensembles de départ, d'arrivée, ensemble image, ensemble de définition

- $X$ est l'ensemble de **départ**, $Y$ l'ensemble d'**arrivée**. $y$ est l'**image** de $x$ par $f$, et $x$ un **antécédent** de $y$.
- L'**ensemble image** de $f$ est le sous-ensemble de $Y$ des éléments qui ont un antécédent dans $X$ :

$$\mathrm{Im}(f) = \{f(x) \mid x \in X\}.$$

- L'**[[Ensemble de définition]]** $D_f$ d'une fonction de départ $X$ est l'ensemble des éléments de $X$ qui ont une image par $f$, c'est-à-dire pour lesquels $f(x)$ existe :

$$D_f = \{x \in X \mid \exists\, y \in Y,\ y = f(x)\}.$$

## Exemples

![[Chapitre4-Fonctions - p5.jpg]]
*Figure : à gauche, diagramme sagittal de $f : E \to F$ où trois éléments $x_1, x_2, x_3$ de $E$ ont la même image $y$ ; à droite, graphe d'une fonction réelle où la droite horizontale d'ordonnée $y$ coupe la courbe en $x_1, x_2, x_3$.*

L'élément $y$ admet **trois antécédents** par $f$ : $x_1$, $x_2$, $x_3$.

**Notations par formule.** La fonction qui associe à tout réel son carré se note $f(x) = x^2$, $x \mapsto x^2$ ou $y = x^2$. Dans la première notation, $x$ est la **variable** et $f$ la fonction ; dans la deuxième, la flèche signifie que $x$ est envoyé sur $x^2$ ; dans la troisième, $x$ est la **variable indépendante** et $y$ la **variable dépendante**, car sa valeur dépend de celle de $x$.

1. $f : \mathbb{R} \to \mathbb{R},\ x \mapsto \sin x$.
2. **Exercice** : soient $X = \{a, b, c\}$ et $Y = \{1, 2, 3, 4\}$, et $f = \{(a, 2), (b, 4), (c, 2)\}$. Vérifier que $f$ est une fonction et donner son image. (Pas de correction dans le support.)

**Autres exemples** :
- $f$ définie sur $\mathbb{R}$ par $f(x) = \sin x$ (sous-entendu $F = \mathbb{R}$) ;
- $f$ définie sur $]0, 1[$ par $f(x) = \dfrac{1}{x^2 - x}$ (sous-entendu $F = \mathbb{R}$) ;
- l'**application identique** $\mathrm{id}_E : E \to E$, $\mathrm{id}_E(x) = x$ ;
- la **fonction caractéristique** ou **indicatrice** $c_A : E \to \{0, 1\}$ d'une partie $A$ de $E$ : $c_A(x) = 1$ si $x \in A$, $0$ sinon ;
- la **conjugaison** $\mathbb{C} \to \mathbb{C}$, qui à $z = x + iy$ associe $\bar z = x - iy$ ([[Nombre complexe]]) ;
- une application de $\mathbb{N}$ dans $\mathbb{R}$ (resp. $\mathbb{C}$) est une **suite** de réels (resp. de complexes), notée $u_n$ au lieu de $f(n)$ ; par exemple $u_n = \dfrac{1}{n+1}$ ([[Suite numérique]]).

## Fonctions particulières

1. **Identité** ([[Fonction identité]]) : sur un ensemble $X$, $x \mapsto x$, notée $\mathrm{Id}_X$ : $\forall x \in X,\ \mathrm{Id}_X(x) = x$.
2. **Injection canonique et restriction** ([[Injection canonique]], [[Restriction d'une fonction]]) : soit $A \subset X$. L'injection canonique de $A$ dans $X$, notée $i : A \hookrightarrow X$, est définie par $\forall x \in A,\ i(x) = x$. Pour $f : X \to Y$, la **restriction** de $f$ à $A$, notée $f|_A$, est définie par $\forall x \in A,\ f|_A(x) = f(x)$.
3. **Indicatrice** ([[Fonction indicatrice]]) d'une partie $A$ de $X$ :

$$1_A : X \to \{0, 1\},\qquad x \mapsto \begin{cases} 1 & \text{si } x \in A \\ 0 & \text{si } x \notin A. \end{cases}$$

## Ensemble image et image réciproque d'une partie

Voir [[Image et image réciproque]].

**Définition.** Soient $f : E \to F$ et $A \subset E$. L'**image de $A$** par $f$ est

$$f(A) := \{f(x) \mid x \in A\},$$

l'ensemble des éléments de $F$ qui ont au moins un antécédent dans $A$.

Soit $B \subset F$. L'**image réciproque** de $B$ par $f$ est

$$f^{-1}(B) := \{x \in E \mid f(x) \in B\},$$

l'ensemble des antécédents des éléments de $B$.

## Fonctions et relations binaires

Le **graphe** de $f : X \to Y$ est ([[Graphe d'une fonction]]) :

$$\text{Graph}(f) = \{(x, y) \in X \times Y \mid f(x) = y\}.$$

**Définition.** Une fonction $f : X \to Y$ est une [[Relation binaire]] sur $X \times Y$ telle que tout $x \in X$ appartienne à une **unique** paire ordonnée $(x, y)$ vérifiant $y = f(x)$ (voir [[Relation fonctionnelle]], [[Produit cartésien]]).

Pour une fonction de $\mathbb{R}$ dans $\mathbb{R}$ : toute droite verticale coupe le graphe en exactement un point.

## Composition des fonctions

**Définition.** Soient $f : X \to Y$ et $g : Y \to Z$, l'image de $f$ étant contenue dans le domaine de définition de $g$. La **composée** de $f$ par $g$, notée $g \circ f$, est la fonction de $X$ dans $Z$ ([[Composition de fonctions]]) :

$$(g \circ f)(x) \overset{\text{def}}{=} g(f(x)).$$

Pour $f : X \to Y$ : $f \circ \mathrm{Id}_X = f$ et $\mathrm{Id}_Y \circ f = f$.

## Égalité de deux fonctions

**Définition** ([[Égalité de deux fonctions]]). Deux fonctions $f$ et $g$ sont égales si :
1. elles ont le même ensemble de définition $D$ ;
2. elles ont le même ensemble d'arrivée ;
3. $\forall x \in D,\ f(x) = g(x)$.

**Exercice** : comparer $f : \mathbb{R} \to \mathbb{R},\ x \mapsto \sin x$ et $f : \mathbb{R} \to [-1, 1],\ x \mapsto \sin x$. (D'après la définition, ce sont deux fonctions différentes, car leurs ensembles d'arrivée diffèrent.)

## Fonctions injectives

Voir [[Injectivité et surjectivité]].

**Définition.** $f : X \to Y$ est **injective** (une **injection**) si

$$\forall x \in X,\ \forall x' \in X,\quad f(x) = f(x') \Rightarrow x = x'.$$

Par [[Preuve par contraposition|contraposition]] : $\forall x, x' \in X,\ x \ne x' \Rightarrow f(x) \ne f(x')$.

**Définition équivalente.** $f : E \to F$ est injective si tout $y \in F$ a **au plus un** antécédent (éventuellement aucun).

![[Chapitre4-Fonctions - p14.jpg]]
*Figure : fonctions injectives : diagramme sagittal où deux éléments de $E$ n'ont jamais la même image (un élément de $F$ reste sans antécédent) ; graphe d'une fonction strictement croissante avec un saut, chaque ordonnée étant atteinte au plus une fois.*

**Exercice** : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto 3x + 1$ et $g : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$ sont-elles injectives ? (Sans correction.)

## Fonctions surjectives

**Définition.** $f : X \to Y$ est **surjective** (une **surjection**) si tout $y \in Y$ admet un antécédent :

$$\forall y \in Y,\ \exists x \in X,\ f(x) = y.$$

L'ensemble image de $f$ est alors l'ensemble d'arrivée.

**Définition équivalente.** $f : E \to F$ est surjective si tout $y \in F$ a **au moins un** antécédent ; autrement dit, $f$ est surjective si et seulement si $f(E) = F$.

![[Chapitre4-Fonctions - p16.jpg]]
*Figure : fonctions surjectives : diagramme sagittal où chaque élément de $F$ reçoit au moins une flèche (deux éléments de $E$ ont la même image) ; graphe d'une fonction oscillante dont les valeurs couvrent tout l'intervalle $F$.*

**Exercice** : les mêmes $f(x) = 3x + 1$ et $g(x) = x^2$ de $\mathbb{R}$ dans $\mathbb{R}$ sont-elles surjectives ? (Sans correction.)

## Fonctions bijectives

**Définition.** $f : X \to Y$ est **bijective** (une **[[Bijection]]**) si elle est injective et surjective : tout $y \in Y$ a un **unique** antécédent $x \in X$. On définit alors la **bijection réciproque** $f^{-1} : Y \to X$ :

$$\forall x \in X,\ \forall y \in Y,\quad y = f(x) \iff x = f^{-1}(y).$$

**Définition équivalente.** $f$ est bijective si et seulement si $\forall y \in F,\ \exists!\, x \in E,\ y = f(x)$.

![[Chapitre4-Fonctions - p18.jpg]]
*Figure : bijection : diagramme sagittal où chaque élément de $F$ reçoit exactement une flèche ; graphe d'une fonction strictement croissante et continue qui atteint chaque valeur de $F$ une seule fois.*

### Propriétés

**Proposition.** Si $f$ est une bijection de $X$ dans $Y$ : $f \circ f^{-1} = \mathrm{Id}_Y$ et $f^{-1} \circ f = \mathrm{Id}_X$.

**Proposition.** Soient $f : X \to Y$ et $g : Y \to X$ telles que $f \circ g = \mathrm{Id}_Y$ et $g \circ f = \mathrm{Id}_X$. Alors $f$ et $g$ sont des bijections et $f^{-1} = g$.

### Exemple

Soient $f, g : \mathbb{N} \to \mathbb{N}$ :

$$f(n) = n + 1, \qquad g(n) = \begin{cases} 0 & \text{si } n = 0 \\ n - 1 & \text{si } n \ge 1. \end{cases}$$

Ces fonctions sont-elles injectives, surjectives, bijectives ? Étudier $f \circ g$ et $g \circ f$. (Sans correction.)

## Image et image réciproque d'un ensemble

**Définition.** Pour $f : X \to Y$ et $A \subset X$ : $f(A) = \{f(x) \mid x \in A\}$.
*Exercice* : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto 3x + 4$ ; calculer $f([0, +\infty[)$.

**Définition.** Pour $B \subset Y$ : $f^{-1}(B) = \{x \in X \mid f(x) \in B\}$.
*Exercice* : même $f$ ; calculer $f^{-1}(]-\infty, 1])$.

**Remarque importante.** Malgré la même notation, pour $B \subseteq Y$, $f^{-1}(B)$ est défini **même si $f$ n'est pas bijective**, donc même si la fonction $f^{-1}$ n'existe pas de $Y$ dans $X$. Quand $f$ est bijective, $f^{-1}(B)$ est aussi l'image de $B$ par la fonction $f^{-1}$.

**Proposition.** Soient $f : X \to Y$, $A$ et $B$ deux parties de $X$, $C$ et $D$ deux parties de $Y$ :
1. $f(A \cup B) = f(A) \cup f(B)$ ;
2. $f(A \cap B) \subseteq f(A) \cap f(B)$, avec égalité si, et seulement si, $f$ est injective ;
3. $f^{-1}(C \cup D) = f^{-1}(C) \cup f^{-1}(D)$ ;
4. $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$ ;
5. $f^{-1}(C^{\complement}) = f^{-1}(C)^{\complement}$.

Voir [[Intersection et union d'ensembles]] et [[Complémentaire d'un ensemble]].

**Exemple** : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$.
1. Déterminer $f([-2, 2])$, $f([-1, 2])$ et $f([2, +\infty[)$.
2. Déterminer $f^{-1}([0, 4])$, $f^{-1}([-2, 4])$, $f^{-1}([-2, -1])$ et $f^{-1}(]1, +\infty[)$.

(Sans correction dans le support.)

## Points à vérifier

- **Égalité avec injectivité** (complément) : l'énoncé « égalité si, et seulement si, $f$ est injective » est écrit sur $f(A \cap B)$ pour tous $A$, $B$. C'est exact lu ainsi : l'équivalence porte sur « pour tous $A$, $B$ ».
- **Définition d'une fonction** : la seconde condition ($f(x_1) \neq f(x_2) \Rightarrow x_1 \neq x_2$) exprime l'unicité de l'image, et non l'injectivité. La confusion est possible à la lecture (complément).
- **Coquilles du support** : « $f : E \Longrightarrow F$ » (double flèche) dans la définition de la surjection ; « Equalité » ; « Graph of f » et « and » laissés en anglais ; « le composée ».
- **Ensemble de définition** : $D_f$ est défini comme une partie de $X$, alors que la définition d'une fonction exige que tout $x \in X$ ait une image (dans ce cas $D_f = X$). Les deux points de vue (fonction partielle ou application) coexistent dans le support (complément).
