---
type: concept
tags:
  - year1
  - year2
aliases:
  - one-to-one
  - injective
  - injectives
  - injectivité
  - surjective
  - surjectives
  - surjectivité
  - injection
  - surjection
  - one-to-one mapping
matieres:
  - Bilinear Algebra
  - Algèbre Linéaire
  - Outil Maths
  - Analyse Maths
sources:
  - "[[0 - Linear combination|Chp 0a - Linear combination]]"
  - "[[0 - Matrix algebra|Chp 0b - Matrix algebra]]"
  - "[[0 - Vector Space|Chp 0d - Vector Space]]"
  - "[[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2 (Algèbre)]]"
  - "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"
  - "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-07
---

Pour $T : \mathbb{R}^n \to \mathbb{R}^m$ :

- **Surjective** (onto) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au moins** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Col $A = \mathbb{R}^m$.
- **Injective** (one-to-one) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au plus** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Nul $A = \{\mathbf{0}\}$.

Pour une matrice carrée, ces deux propriétés figurent toutes les deux dans le théorème de la [[Matrice inversible]] ([[Théorème de la matrice inversible]]).

Pour $f$ linéaire : $f$ est injective si et seulement si Ker $f = \{0\}$, et surjective si et seulement si Im$(f) = F$. Une application injective conserve les familles libres, une surjective les familles génératrices, une bijective les bases.

> [!warning] Écart dans le cours
> [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]] écrit « dim E = dim F ⇒ f bijective ». C'est faux tel quel, car l'application nulle est un contre-exemple. Si $\dim E = \dim F$, injective, surjective et bijective sont en fait équivalentes (complément).

**Pour une application quelconque** (Outil Maths, chapitre 4) : $f$ est injective si $f(x) = f(x') \Rightarrow x = x'$, surjective si $f(E) = F$, et bijective si elle est les deux, avec alors une bijection réciproque. Avec les images, $f$ est injective si et seulement si $A = f^{-1}(f(A))$ pour toute partie $A$, et surjective si et seulement si $f(f^{-1}(C)) = C$ pour toute partie $C$. Pour une [[Composition de fonctions|composée]], $g \circ f$ injective implique $f$ injective, et $g \circ f$ surjective implique $g$ surjective. Méthode du TD 4 : pour nier l'injectivité, exhiber deux antécédents distincts d'un même élément ; pour nier la surjectivité, un élément sans antécédent. Voir [[Bijection]].

Le DS2 d'Outils math demande ces définitions, « $g \circ f$ surjective $\Rightarrow g$ surjective » et « $g \circ f$ injective et $f$ surjective $\Rightarrow g$ injective », l'étude de $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2 - 1$ (injective ? surjective ?), puis la bijectivité de $g : [1, +\infty[ \to [0, +\infty[$, $g(x) = x^2 - 1$, avec sa réciproque (page 22 de [[Raw/Year 1/Contrôles.pdf|Contrôles]]). **En analyse** : une fonction continue sur un intervalle est injective si et seulement si elle est strictement monotone ([[0 - rappels pdf]], [[Théorème de la bijection]]).

Notion parente : [[Application (mathématiques)]].

Liens : [[Transformation linéaire]], [[Espace nul]], [[Espace des colonnes]], [[Morphisme]], [[Image et image réciproque]]

Résumés : [[0 - Linear combination]], [[0 - Vector Space]], [[Cours/Mathématiques/Algèbre linéaire/2 - Algèbre linéaire|chp2]], [[4 - pdf]], [[0 - rappels pdf]]
