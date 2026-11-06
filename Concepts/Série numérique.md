---
type: concept
aliases: [séries numériques, numerical series, série convergente, série divergente, série géométrique, série harmonique, série de Riemann, séries de Riemann, p-series, série alternée, convergence absolue, absolutely convergent, série télescopique, somme partielle, telescoping series, harmonic series]
matieres: [Séries, Analyse Maths, Analyse]
sources: ["[[Chp1 - Convergent, divergent and positive terms SERIES]]", "[[Chp2 - Alternating and absolutly convergent series]]", "[[raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1]]", "[[raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites]]", "[[raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1)]]"]
maj: 2026-11-06
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

**Avant le cours de Séries** : en Analyse Maths (1re année), les séries apparaissent comme suites de sommes partielles : $\sum 1/k^2$ converge (limite monotone), $\sum 1/k!$ (via des [[Suites adjacentes|suites adjacentes]]), la série alternée $\sum (-1)^{k-1}/k$ (suites des termes pairs et impairs adjacentes), et $\sum (-1)^k/k!$ en DS. En Analyse (2e année), le TD7 (ex. 11) étudie $I_n = \int_0^1 \frac{x^n}{1+x}\,dx$, qui tend vers 0, calcule $I_n + I_{n+1}$, puis la limite de la série alternée $\sum (-1)^{k+1}/k$.

Liens : [[Critère de d'Alembert et de Cauchy]], [[Reste d'une série]], [[Condition nécessaire de convergence]], [[Critère de comparaison]], [[Comparaison série-intégrale]], [[Critère des séries alternées]], [[Convergence conditionnelle]], [[Série entière]], [[Convergence uniforme]], [[Suite numérique]], [[Intégrale]], [[Constante d'Euler]]

Résumés : [[Chp1 - Convergent, divergent and positive terms SERIES (résumé)]], [[Chp2 - Alternating and absolutly convergent series (résumé)]], [[AnalyseID1 (résumé)]], [[TDSuites (résumé)]], [[Sources/Year 1/Contrôles (résumé)|Contrôles (résumé)]], [[TD7-integration (1) (résumé)]]
