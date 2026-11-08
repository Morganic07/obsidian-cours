---
type: concept
tags: [year1]
aliases: [diagrammes de Hasse, Hasse diagram]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un diagramme de Hasse représente un ensemble fini muni d'une [[Relation d'ordre|relation d'ordre]] $\preceq$. Les éléments sont placés du bas vers le haut : si $x \prec y$, $x$ est dessiné plus bas que $y$. On trace un trait entre $x$ et $y$ seulement quand $y$ **couvre** $x$, c'est-à-dire $x \prec y$ sans élément $z$ tel que $x \prec z \prec y$.

Ce qu'on ne dessine pas, parce que c'est sous-entendu :
- les boucles $x \preceq x$ (réflexivité) ;
- les flèches « raccourcis » $x \preceq z$ quand il existe déjà un chemin montant $x \to y \to z$ (transitivité) ;
- l'orientation des traits : elle est donnée par la hauteur.

C'est une version allégée du diagramme sagittal ([[Représentation d'une relation binaire]]), réservée aux relations d'ordre : on retrouve la relation complète en lisant $x \preceq y$ dès qu'il existe un chemin montant de $x$ à $y$.

**Exemples.**
- $\mathcal{P}(\{a,b,c\})$ ordonné par l'[[Inclusion (ensembles)|inclusion]] donne un cube : $\emptyset$ en bas, les trois singletons au-dessus, puis les trois paires, et $\{a,b,c\}$ en haut. Chaque trait ajoute un élément.
- Les diviseurs de 12, $\{1, 2, 3, 4, 6, 12\}$, ordonnés par la [[Divisibilité]] : $1$ en bas, relié à $2$ et $3$ ; $2$ relié à $4$ et $6$ ; $3$ relié à $6$ ; $4$ et $6$ reliés à $12$ en haut. Il n'y a pas de trait de $1$ à $4$ : il passe par $2$.

**Lecture.** On y lit directement :
- les [[Élément maximal|éléments maximaux]] (aucun trait ne monte au-dessus) et minimaux (aucun trait ne descend) ;
- le [[Plus grand élément|plus grand élément]] ou le plus petit quand il existe (un seul sommet en haut, ou en bas, relié à tous) ;
- les majorants d'une partie (éléments atteignables en montant depuis chacun de ses éléments).

Un ordre **total** donne un diagramme en ligne droite (une chaîne) ; plus le diagramme est « large », plus l'ordre est partiel.

## Dans le cours

Le cours ne le nomme pas. Il est ajouté dans les compléments de [[3 - pdf]], à propos de l'inclusion (diapositive 24).

Voir aussi : [[Relation d'ordre]], [[Représentation d'une relation binaire]], [[Inclusion (ensembles)]], [[Divisibilité]], [[Élément maximal]], [[Plus grand élément]].

Résumés : [[3 - pdf]]
