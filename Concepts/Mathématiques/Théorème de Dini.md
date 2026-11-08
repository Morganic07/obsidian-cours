---
type: concept
tags: [year3]
aliases: [Dini's theorem, Dini theorem]
sources: ["[[Raw/Year 3/Séries/Chp3 : Sequence of function.docx|Chp3 - Sequence of function]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : soit $(f_n)$ une suite de fonctions définies sur un segment $[a, b]$. Si
1. chaque $f_n$ est continue sur $[a, b]$,
2. la suite est monotone : pour tout $x$, $(f_n(x))$ est croissante (ou, pour tout $x$, décroissante),
3. $(f_n)$ converge simplement vers une fonction $f$ continue sur $[a, b]$,

alors la convergence est [[Convergence uniforme|uniforme]] sur $[a, b]$.

**Les trois hypothèses sont indispensables.**
- Limite continue : $f_n(x) = x^n$ sur $[0, 1]$ est continue et décroissante en $n$, mais sa limite simple ($0$ sur $[0, 1[$, $1$ en $1$) est discontinue ; la convergence n'est pas uniforme.
- Monotonie : les « triangles » de hauteur $n$ du chapitre 3 sont continus et convergent simplement vers la fonction nulle, continue, mais la suite n'est pas monotone et la convergence n'est pas uniforme ($\|f_n\|_\infty = n$).
- Segment : sur $[0, 1[$, la suite $x^n$ converge simplement vers $0$, continue, en décroissant, et la convergence n'est pas uniforme ($\sup_{[0,1[} x^n = 1$).

**Intérêt.** Obtenir la convergence uniforme sans calculer $\|f_n - f\|_\infty$, par exemple pour une suite définie par récurrence dont on sait seulement qu'elle est monotone.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[3 - Sequence of function]], dans les « erreurs courantes » : la continuité de la limite ne suffit pas seule à donner la convergence uniforme, mais elle suffit avec la monotonie sur un segment.

Voir aussi : [[Convergence uniforme]], [[Interversion de limites]], [[Compact élémentaire]].

Résumés : [[3 - Sequence of function]]
