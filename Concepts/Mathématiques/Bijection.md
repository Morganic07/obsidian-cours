---
type: concept
tags:
  - year1
aliases:
  - bijections
  - bijective
  - bijectives
  - bijectivité
  - bijection réciproque
matieres:
  - Outil Maths
  - Algèbre Linéaire
sources:
  - "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"
  - "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]"
  - "[[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]]"
maj: 2026-11-08
---

$f$ est bijective si elle est injective et surjective : $\forall y \in F, \exists! x \in E, y = f(x)$.

Sa bijection réciproque $f^{-1}$ vérifie $y = f(x) \iff x = f^{-1}(y)$, $f \circ f^{-1} = \mathrm{Id}_Y$ et $f^{-1} \circ f = \mathrm{Id}_X$. Réciproquement, si $f \circ g = \mathrm{Id}_Y$ et $g \circ f = \mathrm{Id}_X$, $f$ et $g$ sont bijectives et $g = f^{-1}$. Méthode du TD : résoudre $y = f(x)$ et vérifier l'unicité de la solution.

Attention : la réciproque d'une composée de bijections inverse l'ordre, $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$, soit $(f \circ g)^{-1}(x) = g^{-1}(f^{-1}(x))$. [[Erreurs du cours#^e-bijection|✎]]

**Algèbre Linéaire** : une bijection linéaire est un isomorphisme et envoie une base sur une base.

Notion parente : [[Injectivité et surjectivité]]. Voir aussi : [[Fonction identité]], [[Composition de fonctions]], [[Morphisme]], [[Matrice inversible]].

Résumés : [[4 - pdf]], [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire]], [[Cours/Mathématiques/Algèbre linéaire/1 - Algèbre linéaire]]
