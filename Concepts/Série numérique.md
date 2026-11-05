---
type: concept
aliases: [séries numériques, numerical series, série convergente, série divergente, série géométrique, série harmonique, série de Riemann, séries de Riemann, p-series, série alternée, série alternée, convergence absolue, absolutely convergent, série télescopique, somme partielle]
matieres: [Séries]
sources: ["[[Chp1 - Convergent, divergent and positive terms SERIES]]", "[[Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-05
---

Une **série** $\sum a_n$ est la suite de ses sommes partielles $S_n = \sum_{k=0}^n a_k$ ; elle converge si $(S_n)$ converge, et la limite est sa somme.

**Séries de référence** :
- géométrique $\sum ar^n$ : converge si et seulement si $|r| < 1$, somme $\frac{a}{1-r}$ ;
- télescopique $\sum (a_n - a_{n-1})$ : converge si et seulement si $(a_n)$ converge, somme $\ell - a_0$ ;
- harmonique $\sum \frac{1}{n}$ : diverge ;
- de Riemann $\sum \frac{1}{n^p}$ : converge si et seulement si $p > 1$.

**Condition nécessaire** : série convergente implique $a_n \to 0$ (pas de réciproque : harmonique).

**Termes positifs** : convergence équivaut à sommes partielles majorées. Critères : comparaison $a_n \le b_n$, $a_n = O(b_n)$, $a_n = o(b_n)$, limite du quotient non nulle, équivalents ([[Comparaison asymptotique]]), comparaison avec une intégrale ([[Intégrale]]) qui encadre aussi le reste $R_n$.

**Séries de signe quelconque** : alternée $\sum (-1)^n b_n$ convergente si $(b_n)$ décroît vers 0, avec $|R_n| \le b_{n+1}$. Absolument convergente si $\sum |a_n|$ converge, ce qui implique la convergence ; conditionnellement convergente sinon. Les équivalents sont réservés aux termes positifs.

Liens : [[Critère de d'Alembert et de Cauchy]], [[Série entière]], [[Convergence uniforme]]

Résumés : [[Chp1 - Convergent, divergent and positive terms SERIES (résumé)]], [[Chp2 - Alternating and absolutly convergent series (résumé)]]
