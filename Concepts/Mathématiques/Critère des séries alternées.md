---
type: concept
tags: [year3]
aliases: [alternating series test, critère spécial des séries alternées]
sources: ["[[2 - Alternating and absolutly convergent series|Chp2 - Alternating and absolutly convergent series]]", "[[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-08
---

Si $(b_n)$ est décroissante et tend vers 0, la série $\sum (-1)^n b_n$ converge. Sa somme est comprise entre deux sommes partielles consécutives, et le reste vérifie $|R_n| \le b_{n+1}$.

La p-série alternée $\sum \frac{(-1)^n}{n^p}$ converge si et seulement si $p > 0$.

## Compléments (hors du cours)

**Idée de la preuve.** Notons $S_n = \sum_{k=0}^{n} (-1)^k b_k$. Comme $(b_n)$ décroît, $S_{2n+2} - S_{2n} = b_{2n+2} - b_{2n+1} \le 0$ et $S_{2n+3} - S_{2n+1} = b_{2n+2} - b_{2n+3} \ge 0$ : $(S_{2n})$ est décroissante et $(S_{2n+1})$ croissante. De plus $S_{2n} - S_{2n+1} = b_{2n+1} \to 0$. Ce sont donc des [[Suites adjacentes]] : elles convergent vers une même limite $S$, et $(S_n)$ converge vers $S$. L'encadrement $S_{2n+1} \le S \le S_{2n}$ donne la majoration du reste.

**Signe du reste.** Le reste $R_n = \sum_{k > n} (-1)^k b_k$ a le signe de son premier terme $(-1)^{n+1}b_{n+1}$, et $|R_n| \le b_{n+1}$.

**La décroissance est indispensable.** Pour $n \ge 2$, $b_n = \frac{1}{\sqrt n} + \frac{(-1)^n}{n}$ est positif et tend vers 0, mais n'est pas décroissant. Or $(-1)^n b_n = \frac{(-1)^n}{\sqrt n} + \frac{1}{n}$ : c'est la somme du terme d'une série convergente (critère des séries alternées) et de celui de la série harmonique, divergente. La série $\sum (-1)^n b_n$ diverge donc.

Notion parente : [[Série numérique]]. Voir aussi : [[Reste d'une série]], [[Convergence conditionnelle]], [[Suites adjacentes]].

Résumés : [[2 - Alternating and absolutly convergent series]]
