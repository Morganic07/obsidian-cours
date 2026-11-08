---
type: concept
tags: [year3]
aliases: [séries de Bertrand, Bertrand series]
sources: ["[[Raw/Year 3/Séries/Chp1 : Convergent, divergent and positive terms SERIES.docx|Chp1 - Convergent, divergent and positive terms SERIES]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : pour $\alpha, \beta$ réels, la série de Bertrand est
$$\sum_{n \ge 2} \frac{1}{n^\alpha (\ln n)^\beta}.$$
Elle converge si et seulement si $\alpha > 1$, ou bien $\alpha = 1$ et $\beta > 1$. Pour $\beta = 0$, on retrouve les séries de Riemann $\sum \frac{1}{n^\alpha}$ : les séries de Bertrand affinent cette échelle de comparaison au cas limite $\alpha = 1$.

**Preuve.** Les termes sont positifs, on raisonne par comparaison.
- $\alpha > 1$ : on choisit $\gamma$ avec $1 < \gamma < \alpha$. Par [[Croissances comparées]], $n^\gamma \cdot \frac{1}{n^\alpha (\ln n)^\beta} = \frac{1}{n^{\alpha - \gamma}(\ln n)^\beta} \to 0$, donc le terme est majoré par $\frac{1}{n^\gamma}$ à partir d'un certain rang : la série converge.
- $\alpha < 1$ : de même $n \cdot \frac{1}{n^\alpha (\ln n)^\beta} = \frac{n^{1-\alpha}}{(\ln n)^\beta} \to +\infty$, donc le terme dépasse $\frac{1}{n}$ à partir d'un certain rang : la série diverge.
- $\alpha = 1$ : si $\beta \le 0$, le terme est supérieur à $\frac{1}{n}$ et la série diverge. Si $\beta > 0$, $f(x) = \frac{1}{x(\ln x)^\beta}$ est positive, continue et décroissante sur $[2, +\infty[$ : on applique la [[Comparaison série-intégrale]]. Une primitive de $f$ est $\ln(\ln x)$ si $\beta = 1$, qui tend vers $+\infty$, et $\frac{(\ln x)^{1-\beta}}{1-\beta}$ sinon, qui a une limite finie en $+\infty$ si et seulement si $\beta > 1$.

**Exemples.** $\sum \frac{1}{n \ln n}$ diverge (ses sommes partielles croissent comme $\ln(\ln n)$, très lentement) ; $\sum \frac{1}{n (\ln n)^2}$ converge ; $\sum \frac{\ln n}{n^2}$ converge ($\alpha = 2$, $\beta = -1$).

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[1 - Convergent, divergent and positive terms SERIES]], après les séries de Riemann.

Notion parente : [[Série numérique]]. Voir aussi : [[Comparaison série-intégrale]], [[Croissances comparées]], [[Critère de comparaison]], [[Intégrale généralisée]].

Résumés : [[1 - Convergent, divergent and positive terms SERIES]]
