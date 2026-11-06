---
type: concept
aliases: [one-to-one, injective, injectives, injectivité, surjective, surjectives, surjectivité]
matieres: [Bilinear Algebra, Algèbre Linéaire, Outil Maths]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0b - Matrix algebra]]", "[[Chp 0d - Vector Space]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp2|chp2 (Algèbre)]]"]
maj: 2026-11-05
---

Pour $T : \mathbb{R}^n \to \mathbb{R}^m$ :

- **Surjective** (onto) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au moins** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Col $A = \mathbb{R}^m$.
- **Injective** (one-to-one) : chaque $\mathbf{b}$ de $\mathbb{R}^m$ est l'image d'**au plus** un $\mathbf{x}$. Pour $\mathbf{x} \mapsto A\mathbf{x}$, cela équivaut à Nul $A = \{\mathbf{0}\}$.

Pour une matrice carrée, ces deux propriétés figurent toutes les deux dans le théorème de la [[Matrice inversible]].

Pour $f$ linéaire : $f$ est injective si et seulement si Ker $f = \{0\}$, et surjective si et seulement si Im$(f) = F$. Une application injective conserve les familles libres, une surjective les familles génératrices, une bijective les bases.

> [!warning] Écart dans le cours
> [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2]] écrit « dim E = dim F ⇒ f bijective ». C'est faux tel quel, car l'application nulle est un contre-exemple. Si $\dim E = \dim F$, injective, surjective et bijective sont en fait équivalentes (complément).

**Pour une application quelconque** (Outil Maths, chapitre 4) : $f$ est injective si $f(x) = f(x') \Rightarrow x = x'$, surjective si $f(E) = F$, et bijective si elle est les deux, avec alors une bijection réciproque. Avec les images, $f$ est injective si et seulement si $A = f^{-1}(f(A))$ pour toute partie $A$, et surjective si et seulement si $f(f^{-1}(C)) = C$ pour toute partie $C$. Pour une composée, $g \circ f$ injective implique $f$ injective, et $g \circ f$ surjective implique $g$ surjective.

Liens : [[Transformation linéaire]], [[Espace nul]], [[Espace des colonnes]], [[Morphisme]], [[Image et image réciproque]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Chp 0d - Vector Space (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2 (résumé)]], [[Chapitre4-Fonctions (1) (résumé)]]
