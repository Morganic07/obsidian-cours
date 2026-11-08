---
type: concept
tags: [year1]
aliases: [dérivable, dérivables, nombre dérivé, dérivée à gauche, dérivée à droite, dérivées usuelles]
matieres: [Analyse Maths, Analyse, Analyse dans Rn]
sources: ["[[4 - dérivabilité|Chp4 - dérivabilité]]"]
maj: 2026-11-08
---

$f$ est dérivable en $a$ si $f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$ existe et est finie, ce qui revient à des dérivées à gauche et à droite égales. Dérivable implique continue, sans réciproque. La tangente est $y = f(a) + f'(a)(x - a)$ ([[Tangente à une courbe]]). Si la limite vaut $\pm\infty$, la tangente est verticale.

**Opérations** : le cours donne un tableau des dérivées usuelles, puis combinaison linéaire, $(uv)' = u'v + uv'$, $(u/v)' = \frac{u'v - uv'}{v^2}$, $(u \circ v)' = v'(u' \circ v)$ et $(f^{-1})' = \frac{1}{f' \circ f^{-1}}$ si $f'$ ne s'annule pas. [[Erreurs du cours#^e-derivabilite|✎]]

**Extremums** ([[Extremum local]]) : un extremum local hors des extrémités de $I$ donne $f'(a) = 0$. La réciproque est fausse. Il faut aussi étudier les extrémités.

**Sur $[a, b]$, avec $f$ continue, et dérivable sur $]a, b[$** :

- **[[Théorème de Rolle|Rolle]]** : si $f(a) = f(b)$, il existe $c \in\, ]a, b[$ tel que $f'(c) = 0$. [[Erreurs du cours#^e-derivabilite|✎]]
- **Accroissements finis** : il existe $c \in\, ]a, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$. [[Erreurs du cours#^e-derivabilite|✎]]
- **Inégalité** ([[Inégalité des accroissements finis]]) : si $m \le f' \le M$, alors $m(b - a) \le f(b) - f(a) \le M(b - a)$. Si $|f'| \le M$, alors $|f(b) - f(a)| \le M(b - a)$.

**Variations sur un intervalle** ([[Monotonie et signe de la dérivée]]) : $f$ est constante si et seulement si $f' = 0$, et croissante si et seulement si $f' \ge 0$. Avec « strictement », seule l'implication $f' > 0 \Rightarrow f$ strictement croissante est vraie : $x^3$ est strictement croissante, alors que sa dérivée s'annule en 0. [[Erreurs du cours#^e-derivabilite|✎]]

**[[Règle de l'Hôpital]]** : si $f(x_0) = g(x_0) = 0$, si $g'$ ne s'annule pas hors de $x_0$, et si $f'/g' \to \ell$, alors $f/g \to \ell$.

Liens : [[Limite et continuité]], [[Fonction de classe Ck]], [[Application lipschitzienne]], [[Développement limité]], [[Primitive]], [[Dérivée partielle]], [[Formule de Leibniz]]

Résumés : [[4 - dérivabilité]], [[0 - rappels pdf]]
