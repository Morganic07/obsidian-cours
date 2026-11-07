---
type: concept
tags: [year1, year2]
aliases: [lipschitzienne, lipschitziennes, lipschitzien, k-lipschitzien, k-lipschitzienne, M-lipschitzienne]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[chp 3 - Limite et continuité d’applications (résumé)|Chp 3 - Limite et continuité d’applications]]", "[[chp 4 - Calcul différentiel du premier ordre (résumé)|Chp 4 - Calcul différentiel du premier ordre]]", "[[chp 4 - dérivabilité (résumé)|Chp4 - dérivabilité]]", "[[démonstrations - integration (résumé)|démonstrations - integration]]"]
maj: 2026-11-06
---

$f$ est $k$-lipschitzienne sur $A$ si $\forall x, y \in A, \|f(x) - f(y)\|_F \le k\|x - y\|_E$.

En première année ([[chp 4 - dérivabilité (résumé)|Chp4 - dérivabilité]]), la définition est donnée pour $f : I \to \mathbb{R}$ : $f$ est $k$-lipschitzienne ($k \ge 0$) si $\forall (x, y) \in I^2,\ |f(x) - f(y)| \le k|x - y|$. Elle vient après l'[[Inégalité des accroissements finis]].

Le cours de deuxième année la relie à la [[Continuité uniforme]], où le $\delta$ est le même partout : une application lipschitzienne est uniformément continue.

**Avec le gradient** : sur un ouvert convexe, si $f$ est $\mathcal{C}^1$ et si $\|\vec{\nabla}_xf\|_1 \le M$, alors $f$ est $M$-lipschitzienne. $f$ est constante si et seulement si elle est 0-lipschitzienne. En une variable, si $f$ est de classe $\mathcal{C}^1$ sur $[a, b]$, elle est lipschitzienne, ce qui sert à prouver la convergence des [[Somme de Riemann|sommes de Riemann]] ([[démonstrations - integration (résumé)]]).

> [!warning] Écart dans le cours
> Une note de [[chp 3 - Limite et continuité d’applications (résumé)|Chp 3 - Limite et continuité d’applications]] écrit « $k$-lipschitzien ⇔ uniformément continue ». Seule l'implication ⇒ est vraie : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue, sans être lipschitzienne (complément).

Notions parentes : [[Limite et continuité]], [[Dérivabilité]].

## À vérifier

- Note manuscrite « k-lipschitzien ⇔ uniformément continue » : seule ⇒ est vraie (contre-exemple $\sqrt{x}$), voir l'encadré ci-dessus.

Liens : [[Continuité uniforme]], [[Inégalité des accroissements finis]], [[Somme de Riemann]], [[Limite et continuité]], [[Gradient]], [[Norme]], [[Dérivabilité]], [[Intégrale]], [[Convergence uniforme]] (pour les suites de fonctions, une notion différente)

Résumés : [[chp 3 - Limite et continuité d’applications (résumé)]], [[chp 4 - Calcul différentiel du premier ordre (résumé)]], [[chp 4 - dérivabilité (résumé)]], [[démonstrations - integration (résumé)]]
