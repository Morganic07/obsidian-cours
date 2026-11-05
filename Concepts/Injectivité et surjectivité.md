---
type: concept
aliases: [one-to-one, injective, injectives, injectivité, surjective, surjectives, surjectivité]
matieres: [Bilinear Algebra, Algèbre Linéaire]
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

Liens : [[Transformation linéaire]], [[Espace nul]], [[Espace des colonnes]], [[Morphisme]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Chp 0d - Vector Space (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2 (résumé)]]
