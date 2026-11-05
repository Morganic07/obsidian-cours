---
type: concept
aliases: [span, spanned, espaces engendrés, espace vectoriel engendré, famille génératrice, familles génératrices]
matieres: [Bilinear Algebra, Algèbre Linéaire]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0d - Vector Space]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp1|chp1 (Algèbre)]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp2|chp2 (Algèbre)]]"]
maj: 2026-11-05
---

$\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$, aussi noté $L(\mathbf{v}_1, \dots, \mathbf{v}_n)$ ou $\text{vect}(\mathbf{v}_1, \dots, \mathbf{v}_n)$, est l'ensemble des vecteurs de la forme $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n$. Géométriquement, un vecteur engendre une droite passant par l'origine, et deux vecteurs non colinéaires un plan passant par l'origine. Il contient toujours $\mathbf{0}$, et c'est un sous-espace.

$\mathbf{b}$ est dans le Span si et seulement si $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n = \mathbf{b}$ a une solution.

Une **famille génératrice** de $E$ est une famille dont le Span est $E$. S'il en existe une finie, $E$ est de dimension finie. Toute sur-famille d'une famille génératrice reste génératrice, et on peut en extraire une base. Pour $f$ linéaire, $f(\text{vect}(e_1, \dots, e_n)) = \text{vect}(f(e_1), \dots, f(e_n))$.

Liens : [[Combinaison linéaire]], [[Sous-espace vectoriel]], [[Espace des colonnes]], [[Base (algèbre linéaire)]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Chp 0d - Vector Space (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp1 (résumé)|chp1 (résumé)]]
