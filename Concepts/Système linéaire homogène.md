---
type: concept
aliases: [système homogène, systèmes homogènes, système homogène associé, systèmes linéaires homogènes, homogeneous system, solution triviale, trivial solution, nonhomogeneous system, parametric vector form, forme vectorielle paramétrique]
sources: ["[[chp3]]", "[[Chp 0a - Linear combination]]"]
maj: 2026-11-06
---

Un système linéaire est **homogène** si son second membre est nul : il s'écrit $A\mathbf{x} = \mathbf{0}$. Il est toujours compatible, car $(0, \ldots, 0)$ est solution (la **solution triviale**) ; la question est donc l'existence d'une solution non triviale.

**Algèbre Linéaire** : l'ensemble des solutions d'un système homogène à $p$ équations et $n$ inconnues est un [[Sous-espace vectoriel]] de $\mathbb{R}^n$. Avec plus d'inconnues que d'équations, il a des solutions non nulles. Si $s_1$ et $s_2$ résolvent $(S)$, alors $s_1 - s_2$ résout le système homogène associé $(S_0)$.

**Bilinear Algebra** : pour un système non homogène compatible, la solution générale s'écrit en **forme vectorielle paramétrique** $\mathbf{w} = \mathbf{p} + \mathbf{v}_h$, où $\mathbf{p}$ est une solution particulière et $\mathbf{v}_h$ une solution quelconque du système homogène : l'ensemble des solutions est une translation de celui du système homogène.

Notion parente : [[Système linéaire]]. Voir aussi : [[Espace nul]], [[Indépendance linéaire]].

## À vérifier

- Dans [[Chp 0a - Linear combination]], la phrase « w = p + v_h is any solution » a perdu un mot (point 4 de [[Chp 0a - Linear combination (résumé)]]).

Résumés : [[chp3 (résumé)]], [[Chp 0a - Linear combination (résumé)]]
