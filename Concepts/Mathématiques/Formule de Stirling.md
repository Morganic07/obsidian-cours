---
type: concept
tags: [year1]
aliases: [Stirling, Stirling's formula, Stirling's approximation, formule de Stirling, équivalent de la factorielle]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/chp5.docx|chp5 (Analyse)]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la formule de Stirling donne un équivalent de la [[Factorielle|factorielle]] quand $n \to +\infty$ :

$$n! \underset{+\infty}{\sim} \sqrt{2\pi n}\left(\frac{n}{e}\right)^n.$$

**Conséquence sur le logarithme** : en prenant le logarithme (permis ici, car la limite de $\sqrt{2\pi n}(n/e)^n$ n'est pas 1),

$$\ln(n!) = n\ln n - n + O(\ln n), \qquad \text{en particulier } \ln(n!) \underset{+\infty}{\sim} n\ln n.$$

**Place dans l'échelle des [[Croissances comparées]]** : pour $q > 1$, $q^n = o(n!)$ et $n! = o(n^n)$. La formule précise le second point : $\dfrac{n!}{n^n} \sim \sqrt{2\pi n}\,e^{-n} \to 0$.

**Usages** :

- estimer des [[Coefficient binomial|coefficients binomiaux]] : par exemple $\dbinom{2n}{n} = \dfrac{(2n)!}{(n!)^2} \sim \dfrac{4^n}{\sqrt{\pi n}}$ ;
- évaluer des probabilités en [[Dénombrement|dénombrement]] quand $n$ est grand ;
- en algorithmique, $\log(n!) = \Theta(n\log n)$ : c'est l'origine de la borne inférieure $\Omega(n \log n)$ du nombre de comparaisons d'un tri par comparaison, qui doit distinguer les $n!$ ordres possibles (voir [[Complexité algorithmique]]).

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[5 - Analyse Maths]], à côté des croissances comparées et des équivalents.

Voir aussi : [[Comparaison asymptotique]], [[Équivalent (comparaison asymptotique)]], [[Croissances comparées]], [[Factorielle]], [[Coefficient binomial]], [[Complexité algorithmique]]

Résumés : [[5 - Analyse Maths]]
