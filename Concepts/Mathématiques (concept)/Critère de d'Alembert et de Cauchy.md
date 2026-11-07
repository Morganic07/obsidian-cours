---
type: concept
tags: [year1, year3]
aliases: [critère de d'Alembert, règle de d'Alembert, ratio test, critère de la racine, critère de Cauchy, root test, test du rapport]
matieres: [Séries, Analyse Maths]
sources: ["[[chp 2 - Alternating and absolutly convergent series (résumé)|Chp2 - Alternating and absolutly convergent series]]", "[[chp 5 - power series (résumé)|Chp5 - power series]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]"]
maj: 2026-11-06
---

Deux critères pour une série $\sum a_n$ :
- **rapport** : $\left|\frac{a_{n+1}}{a_n}\right| \to L$ ;
- **racine** : $\sqrt[n]{|a_n|} \to L$.

Dans les deux cas : $L < 1$, série absolument convergente ; $L > 1$ ou $+\infty$, divergente ; $L = 1$, aucune conclusion (par exemple $\frac{1}{n}$, $(-1)^n\frac{n}{n^2+1}$, $(-1)^n\frac{1}{n^2+1}$ ont tous $L = 1$ pour le rapport avec trois comportements différents). Le rapport convient aux factorielles et produits, la racine aux puissances $n$-ièmes.

Pour une [[Série entière]], les mêmes limites donnent le rayon de convergence $R = 1/\ell$.

**Version pour les suites** (Analyse Maths, TDSuites ex. 13) : pour $u_n > 0$ avec $u_{n+1}/u_n \to l$, $l < 1$ donne $u_n \to 0$, $l > 1$ donne $u_n \to +\infty$, $l = 1$ ne permet pas de conclure. Applications : $a^n/n!$, $n^n/n!$, etc.

Liens : [[Série numérique]], [[Suite numérique]], [[Suite géométrique]]

## À vérifier

Réciproque « L = 1 pour la racine implique L = 1 pour le rapport » non garantie.

Résumés : [[chp 2 - Alternating and absolutly convergent series (résumé)]], [[chp 5 - power series (résumé)]], [[TDSuites (résumé)]]
