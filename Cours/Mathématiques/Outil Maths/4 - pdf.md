---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du support du professeur Chapitre 4 - Fonctions (PDF) ([[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]) (25 diapositives, « Outils Mathématiques - Semestre 1 - 2023 », sous-titre « Fonctions injectives, surjectives, bijectives — Ensembles et fonctions »), dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]. Ce chapitre n'existe qu'en PDF. Il prolonge [[3 - Relation binaire]] (une fonction est une relation binaire) et [[2 - pdf]]. Les propriétés d'injectivité et de surjectivité sont reprises, pour les applications linéaires, dans [[Injectivité et surjectivité]]. Les exercices du support sont posés sans correction.

## Introduction

**Définition (application).** Une [[Application (mathématiques)|application]], c'est deux ensembles $E$ (l'ensemble de **départ** ou de définition) et $F$ (l'ensemble d'**arrivée**) et un procédé $f$ qui associe à chaque élément $x$ de $E$ un élément de $F$ noté $f(x)$. Lorsque $F = \mathbb{R}$, on parle souvent de **fonction**.

**Définition (antécédent).** Soient $E$, $F$ deux ensembles, $f : E \to F$ et $y \in F$. Un **antécédent** de $y$ par $f$ est un $x \in E$ tel que $f(x) = y$. Un élément $y$ peut avoir 0, 1 ou plusieurs antécédents. L'ensemble des antécédents de $y$, éventuellement vide, est noté $f^{-1}(\{y\})$.

**Définition (fonction, forme logique).** Soient $X$ et $Y$ deux ensembles. Une fonction $f$ de $X$ dans $Y$ est une règle qui attribue à chaque $x \in X$ un **unique** $y \in Y$ ; on note $f : X \to Y$ et $f(x) = y$. Formellement :

$$(\forall x \in X,\ \exists y \in Y,\ y = f(x)) \;\wedge\; (\forall x_1 \in X,\ \forall x_2 \in X,\ f(x_1) \ne f(x_2) \Rightarrow x_1 \ne x_2).$$

(La seconde condition exprime l'unicité de l'image, et non l'injectivité.) [[Complément hors du cours|ⓘ]]

Application et fonction : dans l'usage français courant, une **application** associe une image à **tout** élément de l'ensemble de départ, alors qu'une **fonction** peut n'être définie que sur une partie de celui-ci, son [[Ensemble de définition|ensemble de définition]] (ainsi $x \mapsto 1/x$ est une fonction de $\mathbb{R}$ dans $\mathbb{R}$, mais une application seulement de $\mathbb{R}^*$ dans $\mathbb{R}$). D'où la notion de $D_f$ ci-dessous. [[Complément hors du cours|ⓘ]]

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
   Correction : $a$, $b$ et $c$ apparaissent chacun dans exactement un couple, donc $f$ est bien une fonction ($f(a) = 2$, $f(b) = 4$, $f(c) = 2$), et $\mathrm{Im}(f) = \{2, 4\}$. Elle n'est ni injective ($f(a) = f(c)$) ni surjective (1 et 3 n'ont pas d'antécédent). [[Complément hors du cours|ⓘ]]

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

La composition est **associative**, $h \circ (g \circ f) = (h \circ g) \circ f$, mais **pas commutative** : avec $f(x) = x + 1$ et $g(x) = x^2$ sur $\mathbb{R}$, $(g \circ f)(x) = (x + 1)^2$ alors que $(f \circ g)(x) = x^2 + 1$. On lit $g \circ f$ « $g$ rond $f$ » et on applique d'abord $f$, puis $g$. [[Complément hors du cours|ⓘ]]

## Égalité de deux fonctions

**Définition** ([[Égalité de deux fonctions]]). Deux fonctions $f$ et $g$ sont égales si :
1. elles ont le même ensemble de définition $D$ ;
2. elles ont le même ensemble d'arrivée ;
3. $\forall x \in D,\ f(x) = g(x)$.

**Exercice** : comparer $f : \mathbb{R} \to \mathbb{R},\ x \mapsto \sin x$ et $f : \mathbb{R} \to [-1, 1],\ x \mapsto \sin x$. (D'après la définition, ce sont deux fonctions différentes, car leurs ensembles d'arrivée diffèrent.)

Cette distinction n'est pas un détail : la première n'est pas surjective (2 n'a pas d'antécédent), la seconde l'est. La surjectivité dépend de l'ensemble d'arrivée choisi, l'injectivité de l'ensemble de départ (sur $[-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$, $\sin$ devient injective, et même bijective vers $[-1, 1]$ : c'est ainsi qu'on définit $\arcsin$, voir [[Fonctions trigonométriques réciproques]]). [[Complément hors du cours|ⓘ]]

## Fonctions injectives

Voir [[Injectivité et surjectivité]].

**Définition.** $f : X \to Y$ est **injective** (une **injection**) si

$$\forall x \in X,\ \forall x' \in X,\quad f(x) = f(x') \Rightarrow x = x'.$$

Par [[Preuve par contraposition|contraposition]] : $\forall x, x' \in X,\ x \ne x' \Rightarrow f(x) \ne f(x')$.

**Définition équivalente.** $f : E \to F$ est injective si tout $y \in F$ a **au plus un** antécédent (éventuellement aucun).

![[Chapitre4-Fonctions - p14.jpg]]
*Figure : fonctions injectives : diagramme sagittal où deux éléments de $E$ n'ont jamais la même image (un élément de $F$ reste sans antécédent) ; graphe d'une fonction strictement croissante avec un saut, chaque ordonnée étant atteinte au plus une fois.*

**Exercice** : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto 3x + 1$ et $g : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$ sont-elles injectives ? (Sans correction.)

Correction : $f$ est injective, car $3x + 1 = 3x' + 1 \Rightarrow 3x = 3x' \Rightarrow x = x'$. $g$ ne l'est pas : un contre-exemple suffit, $g(-1) = g(1) = 1$ avec $-1 \neq 1$. [[Complément hors du cours|ⓘ]]

Lecture graphique, pour une fonction de $\mathbb{R}$ dans $\mathbb{R}$ : $f$ est injective si toute droite horizontale coupe le graphe **au plus une fois**, surjective si toute droite horizontale le coupe **au moins une fois**, bijective si elle le coupe **exactement une fois**. [[Complément hors du cours|ⓘ]]

## Fonctions surjectives

**Définition.** $f : X \to Y$ est **surjective** (une **surjection**) si tout $y \in Y$ admet un antécédent :

$$\forall y \in Y,\ \exists x \in X,\ f(x) = y.$$

L'ensemble image de $f$ est alors l'ensemble d'arrivée.

**Définition équivalente.** $f : E \to F$ est surjective si tout $y \in F$ a **au moins un** antécédent ; autrement dit, $f$ est surjective si et seulement si $f(E) = F$.

![[Chapitre4-Fonctions - p16.jpg]]
*Figure : fonctions surjectives : diagramme sagittal où chaque élément de $F$ reçoit au moins une flèche (deux éléments de $E$ ont la même image) ; graphe d'une fonction oscillante dont les valeurs couvrent tout l'intervalle $F$.*

**Exercice** : les mêmes $f(x) = 3x + 1$ et $g(x) = x^2$ de $\mathbb{R}$ dans $\mathbb{R}$ sont-elles surjectives ? (Sans correction.)

Correction : $f$ est surjective, car pour tout $y \in \mathbb{R}$, $x = \dfrac{y - 1}{3}$ vérifie $f(x) = y$ (méthode : résoudre $f(x) = y$ en $x$). $g$ ne l'est pas : $-1$ n'a pas d'antécédent, puisqu'un carré est toujours positif ; $\mathrm{Im}(g) = [0, +\infty[$. Bilan : $f$ est bijective, de réciproque $f^{-1}(y) = \dfrac{y - 1}{3}$. [[Complément hors du cours|ⓘ]]

## Fonctions bijectives

**Définition.** $f : X \to Y$ est **bijective** (une **[[Bijection]]**) si elle est injective et surjective : tout $y \in Y$ a un **unique** antécédent $x \in X$. On définit alors la **bijection réciproque** $f^{-1} : Y \to X$ :

$$\forall x \in X,\ \forall y \in Y,\quad y = f(x) \iff x = f^{-1}(y).$$

**Définition équivalente.** $f$ est bijective si et seulement si $\forall y \in F,\ \exists!\, x \in E,\ y = f(x)$.

![[Chapitre4-Fonctions - p18.jpg]]
*Figure : bijection : diagramme sagittal où chaque élément de $F$ reçoit exactement une flèche ; graphe d'une fonction strictement croissante et continue qui atteint chaque valeur de $F$ une seule fois.*

### Propriétés

**Proposition.** Si $f$ est une bijection de $X$ dans $Y$ : $f \circ f^{-1} = \mathrm{Id}_Y$ et $f^{-1} \circ f = \mathrm{Id}_X$.

**Proposition.** Soient $f : X \to Y$ et $g : Y \to X$ telles que $f \circ g = \mathrm{Id}_Y$ et $g \circ f = \mathrm{Id}_X$. Alors $f$ et $g$ sont des bijections et $f^{-1} = g$.

Composition et injectivité : la composée de deux injections est injective, celle de deux surjections est surjective, celle de deux bijections est bijective, avec $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ (l'ordre s'inverse, comme pour enfiler puis retirer chaussettes et chaussures). Dans l'autre sens, si $g \circ f$ est injective alors $f$ l'est, et si $g \circ f$ est surjective alors $g$ l'est (voir [[Composition de fonctions]]). [[Complément hors du cours|ⓘ]]

Ensembles finis : si $E$ et $F$ sont finis et $f : E \to F$, une injection impose $|E| \le |F|$ et une surjection $|E| \ge |F|$ ; une bijection existe si et seulement si $|E| = |F|$ (voir [[Cardinal d'un ensemble]]). Si $|E| = |F|$, être injective, surjective ou bijective revient au même. La première inégalité est le **principe des tiroirs** : si l'on range $n + 1$ objets dans $n$ tiroirs, un tiroir en contient au moins deux. [[Complément hors du cours|ⓘ]]

Pour des ensembles infinis, la bijection sert de définition de « même taille » : $\mathbb{N}$ et $\mathbb{Z}$ sont en bijection (on dit qu'ils sont dénombrables, voir [[Ensemble dénombrable]]), alors que Cantor a montré (dès 1874, puis par l'argument diagonal en 1891) qu'il n'existe aucune bijection entre $\mathbb{N}$ et $\mathbb{R}$. [[Complément hors du cours|ⓘ]]

### Exemple

Soient $f, g : \mathbb{N} \to \mathbb{N}$ :

$$f(n) = n + 1, \qquad g(n) = \begin{cases} 0 & \text{si } n = 0 \\ n - 1 & \text{si } n \ge 1. \end{cases}$$

Ces fonctions sont-elles injectives, surjectives, bijectives ? Étudier $f \circ g$ et $g \circ f$. (Sans correction.)

Correction : $f$ est injective ($n + 1 = m + 1 \Rightarrow n = m$) mais pas surjective (0 n'a pas d'antécédent dans $\mathbb{N}$). $g$ est surjective ($g(n + 1) = n$ pour tout $n$) mais pas injective ($g(0) = g(1) = 0$). Ni l'une ni l'autre n'est bijective. $g \circ f = \mathrm{Id}_{\mathbb{N}}$, car $g(n + 1) = n$ ; mais $f \circ g \neq \mathrm{Id}_{\mathbb{N}}$, car $(f \circ g)(0) = f(0) = 1$. L'exemple montre que, dans la deuxième proposition ci-dessus, **les deux** égalités sont nécessaires : une seule ne suffit pas à conclure à une bijection. [[Complément hors du cours|ⓘ]]

## Image et image réciproque d'un ensemble

**Définition.** Pour $f : X \to Y$ et $A \subset X$ : $f(A) = \{f(x) \mid x \in A\}$.
*Exercice* : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto 3x + 4$ ; calculer $f([0, +\infty[)$.

**Définition.** Pour $B \subset Y$ : $f^{-1}(B) = \{x \in X \mid f(x) \in B\}$.
*Exercice* : même $f$ ; calculer $f^{-1}(]-\infty, 1])$.

Correction : $f$ est strictement croissante et $f(0) = 4$, donc $f([0, +\infty[) = [4, +\infty[$. Ensuite $3x + 4 \le 1 \iff x \le -1$, donc $f^{-1}(]-\infty, 1]) = ]-\infty, -1]$. [[Complément hors du cours|ⓘ]]

**Remarque importante.** Malgré la même notation, pour $B \subseteq Y$, $f^{-1}(B)$ est défini **même si $f$ n'est pas bijective**, donc même si la fonction $f^{-1}$ n'existe pas de $Y$ dans $X$. Quand $f$ est bijective, $f^{-1}(B)$ est aussi l'image de $B$ par la fonction $f^{-1}$.

**Proposition.** Soient $f : X \to Y$, $A$ et $B$ deux parties de $X$, $C$ et $D$ deux parties de $Y$ :
1. $f(A \cup B) = f(A) \cup f(B)$ ;
2. $f(A \cap B) \subseteq f(A) \cap f(B)$, avec égalité si, et seulement si, $f$ est injective ;
3. $f^{-1}(C \cup D) = f^{-1}(C) \cup f^{-1}(D)$ ;
4. $f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D)$ ;
5. $f^{-1}(C^{\complement}) = f^{-1}(C)^{\complement}$.

Voir [[Intersection et union d'ensembles]] et [[Complémentaire d'un ensemble]].

Pourquoi l'inclusion du point 2 peut être stricte : avec $f(x) = x^2$, $A = [-1, 0]$ et $B = [0, 1]$, on a $f(A \cap B) = f(\{0\}) = \{0\}$, alors que $f(A) \cap f(B) = [0, 1] \cap [0, 1] = [0, 1]$. Un élément de $f(A) \cap f(B)$ peut avoir un antécédent dans $A$ et un autre dans $B$ sans en avoir dans $A \cap B$. L'image réciproque, elle, respecte toutes les opérations (points 3 à 5). [[Complément hors du cours|ⓘ]]

Deux inclusions utiles : $A \subseteq f^{-1}(f(A))$, avec égalité pour tout $A$ si $f$ est injective, et $f(f^{-1}(C)) \subseteq C$, avec égalité pour tout $C$ si $f$ est surjective. Exemple avec $x \mapsto x^2$ : $f^{-1}(f(\{1\})) = \{-1, 1\}$ et $f(f^{-1}([-1, 1])) = [0, 1]$. [[Complément hors du cours|ⓘ]]

**Exemple** : $f : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2$.
1. Déterminer $f([-2, 2])$, $f([-1, 2])$ et $f([2, +\infty[)$.
2. Déterminer $f^{-1}([0, 4])$, $f^{-1}([-2, 4])$, $f^{-1}([-2, -1])$ et $f^{-1}(]1, +\infty[)$.

(Sans correction dans le support.)

Correction (en lisant le graphe de la parabole) : [[Complément hors du cours|ⓘ]]
1. $f([-2, 2]) = [0, 4]$ ; $f([-1, 2]) = [0, 4]$ (le minimum 0 est atteint en 0, le maximum 4 en 2) ; $f([2, +\infty[) = [4, +\infty[$.
2. $f^{-1}([0, 4]) = [-2, 2]$ ; $f^{-1}([-2, 4]) = [-2, 2]$ (les valeurs négatives n'ont pas d'antécédent) ; $f^{-1}([-2, -1]) = \emptyset$ ; $f^{-1}(]1, +\infty[) = ]-\infty, -1[ \cup ]1, +\infty[$.
