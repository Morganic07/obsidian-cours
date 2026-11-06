---
type: concept
aliases: [span, spanned, espaces engendrés, espace vectoriel engendré, famille génératrice, familles génératrices]
matieres: [Bilinear Algebra, Algèbre Linéaire]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0d - Vector Space]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp1|chp1 (Algèbre)]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp2|chp2 (Algèbre)]]"]
maj: 2026-11-06
---

$\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$, aussi noté $L(\mathbf{v}_1, \dots, \mathbf{v}_n)$ ou $\text{vect}(\mathbf{v}_1, \dots, \mathbf{v}_n)$, est l'ensemble des vecteurs de la forme $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n$. Géométriquement, un vecteur engendre une droite passant par l'origine, et deux vecteurs non colinéaires un plan passant par l'origine. Il contient toujours $\mathbf{0}$, et c'est un sous-espace.

$\mathbf{b}$ est dans le Span si et seulement si $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n = \mathbf{b}$ a une solution, c'est-à-dire si le système de [[Matrice augmentée|matrice augmentée]] $[\mathbf{v}_1 \cdots \mathbf{v}_n \mid \mathbf{b}]$ est compatible.

Une **famille génératrice** de $E$ est une famille dont le Span est $E$ : tout vecteur de $E$ est combinaison linéaire de ses vecteurs. S'il en existe une finie, $E$ est de dimension finie. Toute sur-famille d'une famille génératrice reste génératrice, et on peut en extraire une base. En dimension $n$, une famille génératrice a au moins $n$ vecteurs ([[Dimension (algèbre linéaire)]]). Pour $f$ linéaire, $f(\text{vect}(e_1, \dots, e_n)) = \text{vect}(f(e_1), \dots, f(e_n))$, et $\mathrm{Im}(f) = \mathrm{vect}(f(v_1), \dots, f(v_n))$ pour une base $(v_i)$.

L'évaluation 3 de 1re année demande la dimension et une base de $\mathrm{Span}(u_1, u_2, u_3)$ ([[Contrôles (résumé)]]).

Notions parentes : [[Sous-espace vectoriel]], [[Espace vectoriel]], [[Combinaison linéaire]].

Liens : [[Espace des colonnes]], [[Base (algèbre linéaire)]]

## À vérifier

- [[Chp 0a - Linear combination]] : le théorème « Let A be a nxm matrix » mélange $\mathbb{R}^n$ et $\mathbb{R}^m$.

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Chp 0d - Vector Space (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp1 (résumé)|chp1 (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp2 (résumé)|chp2 (résumé)]], [[Contrôles (résumé)]]
