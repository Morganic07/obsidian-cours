---
type: source
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-05
---

Résumé de [[Chp 4 - Calcul différentiel du premier ordre]], dans [[Year 2 - Analyse dans Rn]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une fonction de plusieurs variables se dérive d'abord direction par direction. La différentielle en donne une approximation linéaire complète, et sert ensuite à résoudre des équations aux dérivées partielles par changement de variables.

## Contenu, dans l'ordre du cours

- **[[Dérivée partielle]]** : $\left.\frac{\partial f}{\partial x_j}\right|_a = \lim_{t \to 0} \frac{f(a + te_j) - f(a)}{t}$. Avoir toutes ses dérivées partielles en un point n'implique pas d'y être continue.
- **[[Différentielle]]** : $f(a + h) = f(a) + D_af(h) + \|h\|\epsilon(h)$, avec $D_af$ linéaire et unique. Différentiable implique continue et dérivable partiellement.
- **[[Fonction de classe Ck|Classe $\mathcal{C}^1$]]** : dérivées partielles continues. Chaîne d'implications : $\mathcal{C}^1$ ⇒ différentiable ⇒ continue et dérivées partielles définies.
- **Composition** : formule de dérivation en chaîne, avec $\mathcal{C}^1$ conservée par composition.
- **[[Matrice jacobienne]]** : matrice $(\partial f_i / \partial x_j)$ de la différentielle. Son déterminant, si $n = p$, est le jacobien.
- **[[Gradient]]** : $D_af(h) = \vec{\nabla}_af \cdot h$. Il est perpendiculaire aux directions où $f$ est constante, et pointe vers la plus grande pente.
- **Accroissements finis** : si $\|\vec{\nabla}_xf\|_1 \le M$, alors $|f(b) - f(a)| \le M\|b - a\|_1$. Sur un ouvert convexe, $f$ est alors $M$-lipschitzienne, et constante si et seulement si son gradient est nul. Ta note précise : « pas vu en cours, voir si le prof va revenir dessus ».
- **[[Équation aux dérivées partielles]]** : les solutions de $\partial f/\partial x = g$ sont $K(y) + \int g\,dx$.
- **[[Difféomorphisme]]** : $\mathcal{C}^1$, bijectif, de réciproque $\mathcal{C}^1$. Un jacobien non nul rend $D_a\phi$ bijective. Le cours donne la méthode de changement de variables, directe et indirecte, puis les coordonnées polaires sur 3 demi-plans.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Si f n'est que différentiable, les dérivées premières sont définies mais pas continues »** : image lue directement. Il faut lire « pas forcément continues » (complément). **À corriger avant un examen.**
2. **Théorème 5** : $f \times g$ n'a pas de sens dans un EVN $F$ quelconque, faute de produit. L'énoncé vaut par exemple pour $F = \mathbb{R}$ (complément).
3. **Propriété 3** : la somme porte sur $i$, mais la dérivée sur $x_j$. Il faut le même indice.
4. **Propriété 11** : l'énoncé se termine par « alors $f$ est $M$-lipschitzienne », reste de la propriété 10.
5. **Quantificateurs** : la propriété 8 écrit $(a, h) \in U^2$, alors que $h$ est dans $\mathbb{R}^p$. La définition 1 écrit $a \in \mathbb{R}^p$, alors qu'il faut $a \in U$. La propriété 10 dit « pour tout point $a$ », mais sa formule porte sur $x$.
6. **Tableau du changement de variables** : le cas direct a $\varphi : V \to U$, alors que la ligne suivante parle d'un difféomorphisme « de $U$ sur $V$ » pour les deux colonnes.
