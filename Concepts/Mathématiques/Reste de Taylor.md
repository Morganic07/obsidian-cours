---
type: concept
tags: [year3]
aliases: [Taylor's inequality, inégalité de Taylor, Lagrange's form of the remainder, forme de Lagrange du reste, reste de Lagrange, integral form of the remainder, reste intégral, Taylor-Lagrange]
matieres: [Séries]
sources: ["[[Chp5 - power series]]"]
maj: 2026-11-06
---

$R_n = f - T_n$, où $T_n$ est le polynôme de Taylor d'ordre $n$ en $\alpha$. Si $R_n(x) \to 0$, $f$ est la somme de sa série de Taylor ([[Chp5 - power series]]).

- **Inégalité de Taylor** : si $|f^{(n+1)}| \le M$, alors $|R_n(x)| \le \dfrac{M}{(n+1)!}|x - \alpha|^{n+1}$.
- **Forme intégrale** : $R_n(x) = \dfrac{1}{n!}\displaystyle\int_\alpha^x (x - t)^n f^{(n+1)}(t)\,dt$.
- **Forme de Lagrange** : $R_n(x) = \dfrac{f^{(n+1)}(c)}{(n+1)!}(x - \alpha)^{n+1}$.

Notion parente : [[Série entière]]. Voir aussi : [[Développement limité]], [[Reste d'une série]].

## À vérifier

- Le cours écrit l'intervalle « [d − α, d + α] », à lire $[\alpha - d, \alpha + d]$.

Résumés : [[Chp5 - power series (résumé)]]
