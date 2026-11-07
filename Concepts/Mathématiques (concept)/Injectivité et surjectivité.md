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
  - "[[chp 0a - Linear combination (résumé)|Chp 0a - Linear combination]]"
  - "[[chp 0b - Matrix algebra (résumé)|Chp 0b - Matrix algebra]]"
  - "[[chp 0d - Vector Space (résumé)|Chp 0d - Vector Space]]"
  - "[[Cours/Mathématiques (cours)/Algèbre linéaire (cours)/chp 2 - Algèbre linéaire (résumé)|chp2 (Algèbre)]]"
  - "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre4-Fonctions (1).pdf|Chapitre4-Fonctions (1).pdf]]"
  - "[[Raw/Year 1/Outil Maths/Exos/TD4Applications-Solutions.pdf|TD4Applications-Solutions.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-06
---

Pour $T : \mathbb{R}^n \to \mathbb{R}^m$ :

- **Surjective** (onto) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au moins** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Col $A = \mathbb{R}^m$.
- **Injective** (one-to-one) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au plus** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Nul $A = \{\mathbf{0}\}$.

Pour une matrice carrée, ces deux propriétés figurent toutes les deux dans le théorème de la [[Matrice inversible]] ([[Théorème de la matrice inversible]]).

Pour $f$ linéaire : $f$ est injective si et seulement si Ker $f = \{0\}$, et surjective si et seulement si Im$(f) = F$. Une application injective conserve les familles libres, une surjective les familles génératrices, une bijective les bases.

> [!warning] Écart dans le cours
> [[Cours/Mathématiques (cours)/Algèbre linéaire (cours)/chp 2 - Algèbre linéaire (résumé)|chp2]] écrit « dim E = dim F ⇒ f bijective ». C'est faux tel quel, car l'application nulle est un contre-exemple. Si $\dim E = \dim F$, injective, surjective et bijective sont en fait équivalentes (complément).

**Pour une application quelconque** (Outil Maths, chapitre 4) : $f$ est injective si $f(x) = f(x') \Rightarrow x = x'$, surjective si $f(E) = F$, et bijective si elle est les deux, avec alors une bijection réciproque. Avec les images, $f$ est injective si et seulement si $A = f^{-1}(f(A))$ pour toute partie $A$, et surjective si et seulement si $f(f^{-1}(C)) = C$ pour toute partie $C$. Pour une [[Composition de fonctions|composée]], $g \circ f$ injective implique $f$ injective, et $g \circ f$ surjective implique $g$ surjective. Méthode du TD 4 : pour nier l'injectivité, exhiber deux antécédents distincts d'un même élément ; pour nier la surjectivité, un élément sans antécédent. Voir [[Bijection]].

Le DS2 d'Outils math demande ces définitions, la propriété sur $g \circ f$ surjective, et une bijection pour $x^2 - 1$ sur $[1, +\infty[$ ([[Contrôles (résumé)]]). **En analyse** : une fonction continue sur un intervalle est injective si et seulement si elle est strictement monotone ([[AnalyseID1 (résumé)]], [[Théorème de la bijection]]).

Notion parente : [[Application (mathématiques)]].

Liens : [[Transformation linéaire]], [[Espace nul]], [[Espace des colonnes]], [[Morphisme]], [[Image et image réciproque]]

## À vérifier

- [[Contrôles (résumé)]] : « bijection de $x^2 - 1$ sur $[1, +\infty[$ » est la formulation du résumé ; les ensembles de départ et d'arrivée sont à vérifier dans le scan.
- [[chp 7 - Algèbre linéaire (résumé)|chp7 (Algèbre)]] : coquille « non-injonctive ».

Résumés : [[chp 0a - Linear combination (résumé)]], [[chp 0d - Vector Space (résumé)]], [[Cours/Mathématiques (cours)/Algèbre linéaire (cours)/chp 2 - Algèbre linéaire (résumé)|chp2 (résumé)]], [[Chapitre4-Fonctions (1) (résumé)]], [[TD4Applications (résumé)]], [[TD4Applications-Solutions (résumé)]], [[Exo_Chapitre1_Logique (résumé)]], [[AnalyseID1 (résumé)]], [[Contrôles (résumé)]]
