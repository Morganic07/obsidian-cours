---
type: concept
aliases: [règle de la chaîne, chain rule, dérivée d'une composée, composition et changement de variables]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-06
---

Le cours ne parle pas de « règle de la chaîne » : il s'agit de la section « Composition et changement de variables » ; le résumé dit « formule de dérivation en chaîne ».

**Propriété 6** : si $f$ est $\mathcal{C}^1$ et $u_1,\dots,u_n$ sont $\mathcal{C}^1$ sur $I$, alors $g(t)=f(u_1(t),\dots,u_n(t))$ est $\mathcal{C}^1$ et
$$g'(t)=\sum_i u_i'(t)\,\frac{\partial f}{\partial x_i},$$
analogue de $(g\circ f)'=(g'\circ f)\times f'$.

**Propriété 7** : pour $h(u,v)=f(g_1(u,v),g_2(u,v))$,
$$\frac{\partial h}{\partial u}=\frac{\partial f}{\partial x}\frac{\partial g_1}{\partial u}+\frac{\partial f}{\partial y}\frac{\partial g_2}{\partial u},$$
et de même en $v$.

Notion parente : [[Différentielle]]. Voir aussi : [[Fonction de classe Ck]], [[Matrice jacobienne]], [[Difféomorphisme]].

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]]
