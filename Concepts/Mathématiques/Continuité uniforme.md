---
type: concept
tags: [year2]
aliases: [uniformément continue, uniformly continuous, uniform continuity, théorème de Heine]
sources: ["[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]", "[[Raw/Year 2/Analyse/chp7/démonstrations - integration .docx|démonstrations - integration]]", "[[Raw/Year 2/Analyse/chp7/Chap7-Integration.docx|Chap7-Integration]]"]
maj: 2026-11-08
---

Une application entre espaces métriques est uniformément continue si, pour toute précision fixée, un même $\delta$ convient en tout point :

$$\forall\epsilon>0,\ \exists\delta>0,\ \forall x,y,\quad d(x,y)<\delta\Rightarrow d(f(x),f(y))<\epsilon.$$

Une [[Application lipschitzienne|application lipschitzienne]] est uniformément continue.

## Compléments (complément, hors du cours)

**Différence avec la continuité** : dans la continuité simple, $\delta$ peut dépendre du point $x$ ($\forall x, \forall \epsilon, \exists \delta$) ; dans la continuité uniforme, il est choisi avant $x$ ($\forall \epsilon, \exists \delta, \forall x, y$).

**Lipschitzienne ⇒ uniformément continue** : si $d(f(x), f(y)) \le k\, d(x, y)$ avec $k > 0$, alors $\delta = \frac{\epsilon}{k}$ convient en tout point : $d(x, y) < \delta \Rightarrow d(f(x), f(y)) < k\delta = \epsilon$.

**Chaîne d'implications**, sans réciproques :
$$\text{lipschitzienne} \Rightarrow \text{uniformément continue} \Rightarrow \text{continue}.$$
- $x \mapsto \sqrt{x}$ est uniformément continue sur $[0, 1]$ (théorème de Heine ci-dessous) sans être lipschitzienne : $\frac{\sqrt{x} - \sqrt{0}}{x - 0} = \frac{1}{\sqrt{x}}$ n'est pas borné quand $x \to 0^+$.
- $x \mapsto x^2$ est continue sur $\mathbb{R}$ sans y être uniformément continue : avec $x_n = n + \frac{1}{n}$ et $y_n = n$, $|x_n - y_n| = \frac{1}{n} \to 0$ alors que $|x_n^2 - y_n^2| = 2 + \frac{1}{n^2} \ge 2$. Aucun $\delta$ ne convient donc pour $\epsilon = 2$.

**Théorème de Heine** : une fonction continue sur un segment $[a, b]$, et plus généralement sur une [[Partie compacte|partie compacte]] (dans $\mathbb{R}^n$ : fermée et bornée), y est uniformément continue. L'hypothèse est indispensable : $x \mapsto \frac{1}{x}$ est continue sur $]0, 1]$ (borné mais non fermé) sans y être uniformément continue, et $x \mapsto x^2$ est continue sur $\mathbb{R}$ (fermé mais non borné) sans l'être non plus.

## Dans le cours

- Le chapitre 3 d'Analyse dans $\mathbb{R}^n$ définit la continuité uniforme et énonce que les applications lipschitziennes le sont ([[3 - Limite et continuité d’applications]]).
- En intégration (Analyse, year 2), le cours ne nomme pas le théorème de Heine ; les compléments s'en servent pour prouver l'approximation d'une fonction continue par des fonctions en escalier et la convergence des sommes de Riemann ([[Somme de Riemann]]) pour $f$ seulement continue ([[1 - Integration]], [[1 - démonstrations]]).

Notion parente : [[Limite et continuité]]. Voir aussi : [[Application lipschitzienne]], [[Partie compacte]], [[Somme de Riemann]], [[Intégrale]].

Résumés : [[3 - Limite et continuité d’applications]], [[1 - Integration]], [[1 - démonstrations]]
