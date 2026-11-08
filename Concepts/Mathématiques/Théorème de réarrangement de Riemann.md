---
type: concept
tags: [year3]
aliases: [théorème de Riemann sur les séries, réarrangement d'une série, Riemann rearrangement theorem, Riemann series theorem]
sources: ["[[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un réarrangement de la série $\sum a_n$ est une série $\sum a_{\sigma(n)}$, où $\sigma : \mathbb{N} \to \mathbb{N}$ est une [[Bijection]] : on prend les mêmes termes, chacun une seule fois, dans un autre ordre.
- Si $\sum a_n$ est **absolument convergente**, tout réarrangement converge (absolument) et a la même somme : la sommation est commutative.
- Si $\sum a_n$ est **conditionnellement convergente** ([[Convergence conditionnelle]]), alors pour tout réel $S$, et aussi pour $S = +\infty$ ou $S = -\infty$, il existe une bijection $\sigma$ telle que $\sum a_{\sigma(n)}$ ait pour somme $S$. C'est le théorème de réarrangement de Riemann.

**Idée de la preuve.** Pour une série conditionnellement convergente, la série des termes positifs et celle des termes négatifs divergent toutes deux (si l'une convergeait, l'autre aussi, et la série serait absolument convergente), alors que $a_n \to 0$. Pour viser $S$ réel, on prend des termes positifs, dans leur ordre, jusqu'à dépasser $S$, puis des termes négatifs jusqu'à repasser sous $S$, et ainsi de suite. Chaque étape est possible car il reste toujours une réserve infinie de chaque signe, et l'écart à $S$ est majoré par le dernier terme utilisé, qui tend vers 0.

**Exemple.** La série harmonique alternée $1 - \frac12 + \frac13 - \frac14 + \dots$ a pour somme $\ln 2$. En prenant un terme positif puis deux termes négatifs :
$$1 - \frac12 - \frac14 + \frac13 - \frac16 - \frac18 + \frac15 - \dots = \left(\frac12 - \frac14\right) + \left(\frac16 - \frac18\right) + \dots = \frac12\left(1 - \frac12 + \frac13 - \dots\right) = \frac{\ln 2}{2}.$$
Mêmes termes, somme divisée par deux.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[2 - Alternating and absolutly convergent series]], après la définition de la convergence conditionnelle.

Notion parente : [[Série numérique]]. Voir aussi : [[Convergence conditionnelle]], [[Bijection]], [[Critère des séries alternées]].

Résumés : [[2 - Alternating and absolutly convergent series]]
