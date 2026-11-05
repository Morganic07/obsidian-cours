---
type: source
sources: ["[[Chp4 - dérivabilité]]"]
maj: 2026-11-05
---

Résumé de [[Chp4 - dérivabilité]], dans [[Year 1 - Analyse Maths]]. En cas d'écart, le cours et ses images font foi.

## Contenu, dans l'ordre du cours

- **[[Dérivabilité]]** : $f$ est dérivable en $a$ si $\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$ existe et est finie, ce qui équivaut à des dérivées à gauche et à droite égales. Dérivable implique continue. La tangente est $y = f(a) + f'(a)(x - a)$.
- **Opérations** : tableau des dérivées usuelles, puis combinaison linéaire, produit, quotient, composition et réciproque.
- **[[Fonction de classe Ck|Classe $\mathcal{C}^n$]]** : $n$ fois dérivable, de dérivée $n$-ième continue. $\mathcal{C}^1$ n'est pas « dérivable et continue », mais « dérivable à dérivée continue ». Formule de Leibniz : $(fg)^{(n)} = \sum_k \binom{n}{k} f^{(k)}g^{(n-k)}$.
- **Extremums** : un extremum local hors des extrémités donne $f'(a) = 0$, sans réciproque.
- **Rolle et accroissements finis** : si $f(a) = f(b)$, il existe $c$ avec $f'(c) = 0$. En général, $f'(c)(b - a) = f(b) - f(a)$. Une majoration de $f'$ donne ainsi une majoration de $f$ : $|f(b) - f(a)| \le M(b - a)$.
- **Variations** : $f$ est constante si et seulement si $f'$ est nulle, et croissante si et seulement si $f' \ge 0$.
- **[[Application lipschitzienne|Lipschitz]]** et **règle de l'Hôpital**.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« f croissante ⇔ f' positive (pareil avec strictement) »** : faux pour le cas strict. $x^3$ est strictement croissante, alors que sa dérivée s'annule en 0. Seul $f' > 0 \Rightarrow$ strictement croissante est vrai. De plus, ces équivalences demandent que $I$ soit un intervalle (complément). **À corriger avant un examen.**
2. **Réciproque** : le tableau écrit « si $f$ ne s'annule pas ». Il faut $f'$, comme dans le théorème en image de la même note.
3. **Rolle et accroissements finis** : le cours écrit $c \in [a, b]$. Le théorème usuel donne $c \in \,]a, b[$, ce qui est plus fort (complément).
4. **Composition** : le tableau écrit $u \circ v = u(v(x)) = v'(u' \circ v)$. Il faut lire $(u \circ v)' = v'(u' \circ v)$.
