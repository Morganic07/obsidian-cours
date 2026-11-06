---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre 4 - Fonctions (PDF)]]"]
maj: 2026-11-06
---

Résumé du support du professeur [[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre 4 - Fonctions (PDF)]] (25 pages, 2023), dans [[Outil Maths (matière)]]. Ce chapitre n'existe qu'en PDF. Il prolonge [[Chapitre 3 - Relation binaire (résumé)]] (une fonction est une relation binaire) et [[Chapitre2-Ensemble (4) (résumé)]]. Les propriétés d'injectivité et de surjectivité sont reprises, pour les applications linéaires, dans [[Injectivité et surjectivité]].

## Contenu, dans l'ordre

- **Application** : deux ensembles (départ $E$, arrivée $F$) et une règle associant à chaque $x$ un unique $f(x)$. On parle de fonction quand $F = \mathbb{R}$.
- **Antécédent** : $x$ tel que $f(x) = y$ ; un $y$ a 0, 1 ou plusieurs antécédents. Ensemble des antécédents $f^{-1}(\{y\})$.
- **Définition logique** : $\forall x \in X, \exists y \in Y, y = f(x)$, et $f(x_1) \neq f(x_2) \Rightarrow x_1 \neq x_2$ (l'image est unique).
- **Image** $\mathrm{Im}(f) = \{f(x) \mid x \in X\}$ ; **ensemble de définition** $D_f$.
- **Exemples** : $\sin$, $x \mapsto x^2$, identité $\mathrm{id}_E$, fonction indicatrice $1_A$, conjugaison complexe, suites ($\mathbb{N} \to \mathbb{R}$). Exercice : vérifier que $f = \{(a,2),(b,4),(c,2)\}$ est une fonction et donner son image.
- **Fonctions particulières** : identité, injection canonique $A \hookrightarrow X$, restriction $f|_A$, indicatrice.
- **Image d'une partie** $f(A) = \{f(x) \mid x \in A\}$ et **image réciproque** $f^{-1}(B) = \{x \in E \mid f(x) \in B\}$ (définie même si $f$ n'est pas bijective).
- **Graphe** $\{(x,y) \in X \times Y \mid f(x) = y\}$ : une fonction est une relation binaire où chaque $x$ figure dans un unique couple. Toute droite verticale coupe le graphe en un seul point.
- **Composition** $(g \circ f)(x) = g(f(x))$, si l'image de $f$ est dans le domaine de $g$ ; $f \circ \mathrm{id}_X = f = \mathrm{id}_Y \circ f$.
- **Égalité de deux fonctions** : même ensemble de définition, même ensemble d'arrivée, mêmes valeurs. Exemple : $\sin : \mathbb{R} \to \mathbb{R}$ et $\sin : \mathbb{R} \to [-1,1]$ sont deux fonctions différentes.
- **Injective** : $f(x) = f(x') \Rightarrow x = x'$, ou par contraposée $x \neq x' \Rightarrow f(x) \neq f(x')$ ; chaque $y$ a au plus un antécédent. Tests : $3x+1$ et $x^2$ sur $\mathbb{R}$.
- **Surjective** : $\forall y \in Y, \exists x \in X, f(x) = y$ ; $f(E) = F$. Mêmes tests.
- **Bijective** : injective et surjective, soit $\forall y, \exists! x, y = f(x)$. Bijection réciproque $f^{-1}$, avec $f \circ f^{-1} = \mathrm{Id}_Y$ et $f^{-1} \circ f = \mathrm{Id}_X$. Réciproquement, si $f \circ g = \mathrm{Id}_Y$ et $g \circ f = \mathrm{Id}_X$, alors $f$ et $g$ sont bijectives et $g = f^{-1}$.
- **Exemple** : $f(n) = n+1$ et $g(n) = \max(n-1, 0)$ sur $\mathbb{N}$ : étudier injectivité, surjectivité, $f \circ g$ et $g \circ f$.
- **Propriétés image / image réciproque** : $f(A \cup B) = f(A) \cup f(B)$ ; $f(A \cap B) \subset f(A) \cap f(B)$, avec égalité si et seulement si $f$ est injective ; $f^{-1}$ commute avec l'union, l'intersection et le complémentaire.
- **Exemples à calculer** : $f(x) = 3x+4$ ($f([0,+\infty[)$, $f^{-1}(]-\infty,1])$) ; $f(x) = x^2$ (images et images réciproques de $[-2,2]$, $[0,4]$, $[-2,-1]$, etc.).

## Points à vérifier

- **Égalité avec injectivité** (complément) : l'énoncé « égalité si, et seulement si, $f$ est injective » est écrit sur $f(A \cap B)$ pour tous $A$, $B$. C'est exact lu ainsi : l'équivalence porte sur « pour tous $A$, $B$ ».
- **Définition d'une fonction** : la seconde condition ($f(x_1) \neq f(x_2) \Rightarrow x_1 \neq x_2$) exprime l'unicité de l'image, et non l'injectivité. La confusion est possible à la lecture (complément).
