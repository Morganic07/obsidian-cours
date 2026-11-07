---
type: concept
tags:
  - year1
  - year2
aliases:
  - lipschitzienne
  - lipschitziennes
  - lipschitzien
  - k-lipschitzien
  - k-lipschitzienne
  - M-lipschitzienne
matieres:
  - Analyse dans Rn
  - Analyse Maths
  - Analyse
sources:
  - "[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]"
  - "[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]"
  - "[[4 - dérivabilité|Chp4 - dérivabilité]]"
  - "[[1 - démonstrations|démonstrations - integration]]"
maj: 2026-11-07
---

$f$ est $k$-lipschitzienne sur $A$ si $\forall x, y \in A, \|f(x) - f(y)\|_F \le k\|x - y\|_E$.

En première année ([[4 - dérivabilité|Chp4 - dérivabilité]]), la définition est donnée pour $f : I \to \mathbb{R}$ : $f$ est $k$-lipschitzienne ($k \ge 0$) si $\forall (x, y) \in I^2,\ |f(x) - f(y)| \le k|x - y|$. Elle vient après l'[[Inégalité des accroissements finis]].

Le cours de deuxième année la relie à la [[Continuité uniforme]], où le $\delta$ est le même partout : une application lipschitzienne est uniformément continue.

**Avec le gradient** : sur un ouvert convexe, si $f$ est $\mathcal{C}^1$ et si $\|\vec{\nabla}_xf\|_1 \le M$, alors $f$ est $M$-lipschitzienne. $f$ est constante si et seulement si elle est 0-lipschitzienne. En une variable, si $f$ est de classe $\mathcal{C}^1$ sur $[a, b]$, elle est lipschitzienne, ce qui sert à prouver la convergence des [[Somme de Riemann|sommes de Riemann]] ([[1 - démonstrations]]).

Notions parentes : [[Limite et continuité]], [[Dérivabilité]].

Liens : [[Continuité uniforme]], [[Inégalité des accroissements finis]], [[Somme de Riemann]], [[Limite et continuité]], [[Gradient]], [[Norme]], [[Dérivabilité]], [[Intégrale]], [[Convergence uniforme]] (pour les suites de fonctions, une notion différente)

## Erreurs du cours

- Une note manuscrite de [[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]] écrit « $f$ est $k$-lipschitzien ⇔ $f$ uniformément continue » ; il faut « ⇒ » seulement : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue sans être lipschitzienne (complément, hors du cours).

Résumés : [[3 - Limite et continuité d’applications]], [[4 - Calcul différentiel du premier ordre]], [[4 - dérivabilité]], [[1 - démonstrations]]
