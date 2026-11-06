---
type: source
tags: [year2]
sources: ["[[Chap7-Integration]]"]
maj: 2026-11-05
---

Résumé de [[Chap7-Integration]], dans [[Analyse (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

L'[[Intégrale]] se construit d'abord pour les fonctions en escalier, puis pour les fonctions continues, en les encadrant. Le théorème fondamental la relie ensuite aux [[Primitive|primitives]], qui permettent de la calculer.

## Contenu, dans l'ordre du cours

- **Fonctions en escalier** : constantes sur chaque intervalle d'une subdivision. L'intégrale $\sum y_i(x_{i+1} - x_i)$ ne dépend pas de la subdivision.
- **Fonctions continues** : toute fonction continue s'encadre par deux fonctions en escalier, aussi proches que voulu. Son intégrale est le sup des intégrales par en dessous, égal à l'inf de celles par au-dessus.
- **Propriétés** : linéarité, Chasles, positivité, croissance, inégalité triangulaire et valeur moyenne. Une fonction continue positive d'intégrale nulle est nulle, ce qui est faux sans continuité.
- **[[Primitive]]** : deux primitives diffèrent d'une constante. Théorème fondamental : $x \mapsto \int_a^x f$ est l'unique primitive de $f$ nulle en $a$, et $\int_a^x f = F(x) - F(a)$.
- **Techniques** : dérivation de $\int_{u(x)}^{v(x)} f$, intégration par parties, changement de variable, parité et périodicité.
- **Recherche de primitives** : tableaux usuels, éléments simples, fonctions trigonométriques avec les règles de Bioche ou $t = \tan(x/2)$.
- **Approximation** : sommes de Riemann (méthode des rectangles, en $1/n$), méthode des trapèzes (en $1/n^2$ si $f$ est $\mathcal{C}^2$).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Somme de Riemann** : image lue directement, la formule porte sur $k = 1, \dots, n$, ce qui correspond aux rectangles à droite. La remarque suivante décrit pourtant $f(a_k)$ pour $0 \le k \le n - 1$, soit les rectangles à gauche. Les deux convergent vers l'intégrale, mais ce ne sont pas les mêmes sommes.
2. **Primitive** : « La primitive de $f$ est toute fonction » devrait dire « Une primitive », puisqu'il y en a une infinité.
