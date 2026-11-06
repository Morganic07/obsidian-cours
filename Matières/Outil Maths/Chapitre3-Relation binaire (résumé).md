---
type: source
tags: [year1]
sources: [".raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf"]
maj: 2026-11-06
---

Résumé du support du professeur Chapitre 3 - Relation binaire (PDF) (`.raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf`) (28 diapositives, novembre 2023), dans [[Outil Maths (matière)]]. Version du professeur du cours déjà résumé dans [[Chapitre 3 - Relation binaire (résumé)]]. Notions : [[Relation d'équivalence]], [[Relation d'ordre]].

## Contenu, dans l'ordre

- **Motivation** : équivalences dans la vie courante (heures « 18:45 ~ 6:45 PM », fractions $3/2 \sim 6/4$, écritures d'un même ensemble, sacs d'aspirateur compatibles avec plusieurs marques).
- **Relation binaire** entre $A$ et $B$ : partie de $A \times B$ ; $aRb$ si $(a,b) \in R$ ; relation **sur** $A$ si $B = A$. **Domaine** (premières coordonnées) et **rang** (secondes). Exemple : perpendicularité des droites du plan.
- **Exemples et représentations** : élèves et cours, cadeaux entre élèves ; diagramme cartésien, matrice de la relation, diagramme sagittal.
- **Relation fonctionnelle** : au plus un $y$ pour chaque $x$. Elle correspond au graphe d'une fonction ([[Chapitre4-Fonctions (1) (résumé)]]).
- **Réflexive** : $\forall a, aRa$ (diagonale pleine, boucles). $=$ et $\leq$ le sont, $<$ non.
- **Symétrique** : $aRb \Rightarrow bRa$. **Antisymétrique** : $(a \neq b \wedge aRb) \Rightarrow \neg bRa$, ou de façon équivalente $(aRb \wedge bRa) \Rightarrow a = b$.
- **Transitive** : $(aRb \wedge bRc) \Rightarrow aRc$ (tout chemin a un raccourci).
- Exemple filé sur $\mathbb{R}^2$ : $(x,y)R(x',y') \iff x = x'$, avec les trois preuves.
- **Relation d'équivalence** : réflexive, symétrique, transitive. **Classe** $[a] = \{x \mid aRx\}$ ; représentant.
- **Théorème** : les classes forment une partition de $E$ ; réciproquement toute partition définit une équivalence.
- **Ensemble quotient** $E/R$ et surjection $x \mapsto \mathrm{Cl}(x)$ de $E$ dans $E/R$.
- **Exemple** : $xRy \iff x^2 - y^2 = x - y$ sur $\mathbb{R}$. Réécrit $x^2 - x = y^2 - y$, d'où l'équivalence ; classe $\mathrm{Cl}(x) = \{x, 1 - x\}$ (en factorisant $(x-y)(x+y) = x - y$).
- **Ordre** : réflexive, antisymétrique, transitive. **Total** si deux éléments quelconques sont comparables, **partiel** sinon. Exercice : propriétés de $\leq$, $<$, $\subseteq$, $\perp$, $\parallel$.
- **Exemples d'ordres** : $\leq$ et $\geq$ (total sur $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{R}$) ; $<$ et $>$ ne sont pas des ordres ; divisibilité sur $\mathbb{N}^*$ (ordre non total, avec les trois preuves) ; inclusion sur $\mathcal{P}(E)$ (non total).
- **Fonctions croissantes, décroissantes** entre ensembles ordonnés, strictement ou non. Une application strictement monotone sur un ensemble de départ totalement ordonné est injective ([[Injectivité et surjectivité]]).
- **Minimal, minorant, plus petit élément** $\min(A)$, **borne inférieure** $\inf(A)$ (plus grand des minorants) ; symétriquement maximal, majorant, $\max(A)$, **borne supérieure** $\sup(A)$.
- **Exemples** : $[0,1]$, $]0,1]$, $]0,1[$ dans $(\mathbb{R}, \leq)$ ; $\emptyset$ minimum et $E$ maximum de $(\mathcal{P}(E), \subset)$ ; $]1,+\infty[$ a pour borne inférieure 1 et pas de borne supérieure.

## Points à vérifier

- **Partition** (diapositive 19) : la définition donnée omet la condition « parties non vides », présente au [[Chapitre2-Ensemble (4) (résumé)|chapitre 2]]. Sans elle, le théorème « les classes forment une partition » reste vrai, mais la définition est incomplète (complément).
- **Divisibilité** (diapositive 28) : « 0 est le maximum (...) » pour la divisibilité sur $\mathbb{N}$. Cela vaut sur $\mathbb{N}$ entier (tout entier divise 0), alors que l'ordre a été défini sur $\mathbb{N}^*$ ; et la fin de la phrase est tronquée (« ni maximum ni minimum 3 », renvoi de note perdu). Le support est ambigu à cet endroit.
- **Minorant** : « A admet au plus un seul minorant dans A » veut dire : au plus un minorant appartenant à $A$.
