---
type: concept
aliases: [dérivable, dérivables, nombre dérivé, dérivée à gauche, dérivée à droite, dérivées usuelles]
matieres: [Analyse Maths, Analyse, Analyse dans Rn]
sources: ["[[Chp4 - dérivabilité]]"]
maj: 2026-11-06
---

$f$ est dérivable en $a$ si $f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$ existe et est finie, ce qui revient à des dérivées à gauche et à droite égales. Dérivable implique continue, sans réciproque. La tangente est $y = f(a) + f'(a)(x - a)$ ([[Tangente à une courbe]]). Si la limite vaut $\pm\infty$, la tangente est verticale.

**Opérations** : le cours donne un tableau des dérivées usuelles, puis combinaison linéaire, $(uv)' = u'v + uv'$, $(u/v)' = \frac{u'v - uv'}{v^2}$, $(u \circ v)' = v'(u' \circ v)$ et $(f^{-1})' = \frac{1}{f' \circ f^{-1}}$ si $f'$ ne s'annule pas.

**Extremums** ([[Extremum local]]) : un extremum local hors des extrémités de $I$ donne $f'(a) = 0$. La réciproque est fausse. Il faut aussi étudier les extrémités.

**Sur $[a, b]$, avec $f$ continue, et dérivable sur $]a, b[$** :

- **[[Théorème de Rolle|Rolle]]** : si $f(a) = f(b)$, il existe $c$ tel que $f'(c) = 0$.
- **Accroissements finis** : il existe $c$ tel que $f(b) - f(a) = f'(c)(b - a)$.
- **Inégalité** ([[Inégalité des accroissements finis]]) : si $m \le f' \le M$, alors $m(b - a) \le f(b) - f(a) \le M(b - a)$. Si $|f'| \le M$, alors $|f(b) - f(a)| \le M(b - a)$.

**Variations sur un intervalle** ([[Monotonie et signe de la dérivée]]) : $f$ est constante si et seulement si $f' = 0$, et croissante si et seulement si $f' \ge 0$.

**[[Règle de l'Hôpital]]** : si $f(x_0) = g(x_0) = 0$, si $g'$ ne s'annule pas hors de $x_0$, et si $f'/g' \to \ell$, alors $f/g \to \ell$.

> [!warning] Écart dans le cours
> [[Chp4 - dérivabilité]] ajoute « pareil avec strictement » pour le sens de variation. Seul $f' > 0 \Rightarrow$ strictement croissante est vrai : $x^3$ est strictement croissante, alors que $f'(0) = 0$ (complément).

Liens : [[Limite et continuité]], [[Fonction de classe Ck]], [[Application lipschitzienne]], [[Développement limité]], [[Primitive]], [[Dérivée partielle]], [[Formule de Leibniz]]

## À vérifier

- [[Chp4 - dérivabilité]] écrit $c \in [a, b]$ pour Rolle et les accroissements finis, alors que le théorème usuel donne $c \in ]a, b[$.
- Pour la dérivée de la réciproque, le cours écrit « si $f$ ne s'annule pas » au lieu de $f'$.

Résumés : [[Chp4 - dérivabilité (résumé)]], [[AnalyseID1 (résumé)]], [[Contrôles (résumé)]]
