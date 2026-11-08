---
type: concept
tags: [year1]
aliases: [points fixes, point fixe attractif, point fixe répulsif, fixed point, application contractante]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]", "[[Raw/Year 1/Analyse Maths/Cours/Chp4 - dérivabilité.docx|Chp4 - dérivabilité]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : $\ell$ est un point fixe de $f$ si $f(\ell) = \ell$, c'est-à-dire si la courbe de $f$ coupe la droite $y = x$ en $\ell$.

Pour une suite récurrente $u_{n+1} = f(u_n)$ avec $f$ continue, si $u_n \to \ell$ alors $f(\ell) = \ell$ : la limite éventuelle est un point fixe de $f$.

Le TD4 distingue point fixe attractif et point fixe répulsif. Le TDSuites étudie le signe de $f(x) - x$ et les points fixes de $f \circ f$.

**Cas contractant (complément, hors du cours)** : si $f$ est $k$-lipschitzienne avec $k < 1$ sur un intervalle $I$ stable par $f$, si $u_0 \in I$ et si $\ell \in I$ est un point fixe de $f$, alors

$$|u_{n+1} - \ell| = |f(u_n) - f(\ell)| \le k\,|u_n - \ell|, \qquad \text{donc} \qquad |u_n - \ell| \le k^n\,|u_0 - \ell| \xrightarrow[n \to +\infty]{} 0.$$

La convergence est géométrique, et la majoration donne une estimation de l'erreur commise à chaque rang. En pratique, on obtient $k$ en majorant $|f'|$ sur $I$ : si $|f'| \le k$ sur $I$, l'[[Inégalité des accroissements finis]] montre que $f$ est $k$-lipschitzienne (voir [[Application lipschitzienne]]).

Notion parente : [[Suite numérique]]. Voir aussi : [[Intervalle stable]], [[Limite et continuité]], [[Application lipschitzienne]], [[Inégalité des accroissements finis]].

Résumés : [[0 - rappels pdf]], [[4 - dérivabilité]]
