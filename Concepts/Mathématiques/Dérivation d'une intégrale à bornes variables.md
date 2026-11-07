---
type: concept
tags:
  - year2
aliases:
  - intégrale fonction de ses bornes
  - dérivée de x ↦ ∫ f
sources:
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]"
maj: 2026-11-07
---

Le chapitre 7 donne la dérivée de $x\mapsto\int_{u(x)}^{v(x)} f$. Soient $I, J$ deux intervalles de $\mathbb{R}$, $u, v : I \to \mathbb{R}$ de classe $\mathcal{C}^1$ telles que $u(I), v(I) \subset J$, et $f : J \to \mathbb{K}$ continue. Alors $g : x \mapsto \int_{u(x)}^{v(x)} f(t)\,dt$ est définie et de classe $\mathcal{C}^1$ sur $I$, et

$$\forall x \in I,\ g'(x) = f(v(x))\,v'(x) - f(u(x))\,u'(x).$$

Le TD7 consacre un tiers de ses exercices à $F(x)=\int_0^x f$ :

- $F$ est continue même si $f$ ne l'est pas, mais dérivable seulement là où $f$ est continue ;
- $f$ croissante ou périodique ne rend pas $F$ croissante ou périodique ;
- $f$ positive rend $F$ croissante.

Notion parente : [[Primitive]]. Voir aussi : [[Intégrale]].

Résumés : [[1 - Integration]]
