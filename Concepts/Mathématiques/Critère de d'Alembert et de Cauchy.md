---
type: concept
tags: [year1, year3]
aliases: [critère de d'Alembert, règle de d'Alembert, ratio test, critère de la racine, critère de Cauchy, root test, test du rapport]
matieres: [Séries, Analyse Maths]
sources: ["[[2 - Alternating and absolutly convergent series|Chp2 - Alternating and absolutly convergent series]]", "[[5 - power series|Chp5 - power series]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]"]
maj: 2026-11-07
---

Deux critères pour une série $\sum a_n$ :
- **rapport** : $\left|\frac{a_{n+1}}{a_n}\right| \to L$ ;
- **racine** : $\sqrt[n]{|a_n|} \to L$.

Dans les deux cas : $L < 1$, série absolument convergente ; $L > 1$ ou $+\infty$, divergente ; $L = 1$, aucune conclusion (par exemple $\frac{1}{n}$, $(-1)^n\frac{n}{n^2+1}$, $(-1)^n\frac{1}{n^2+1}$ ont tous $L = 1$ pour le rapport avec trois comportements différents). Le rapport convient aux factorielles et produits, la racine aux puissances $n$-ièmes.

Pour une [[Série entière]], les mêmes limites donnent le rayon de convergence $R = 1/\ell$.

**Version pour les suites** (Analyse Maths, TDSuites ex. 13) : pour $u_n > 0$ avec $u_{n+1}/u_n \to l$, $l < 1$ donne $u_n \to 0$, $l > 1$ donne $u_n \to +\infty$, $l = 1$ ne permet pas de conclure. Applications : $a^n/n!$, $n^n/n!$, etc.

Liens : [[Série numérique]], [[Suite numérique]], [[Suite géométrique]]

## Erreurs du cours

- [[2 - Alternating and absolutly convergent series|Chp2 - Alternating and absolutly convergent series]] écrit : « if $L = 1$ in the ratio test, then $L = 1$ in the root test and conversely » ; il faut retirer « and conversely ». Si le rapport a une limite, la racine a la même ; mais la racine peut tendre vers 1 sans que le rapport ait de limite, par exemple pour $a_n$ valant alternativement 1 et 2 (complément, hors du cours).

Résumés : [[2 - Alternating and absolutly convergent series]], [[5 - power series]]
