---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

## Idée générale

Séries de signe quelconque : séries alternées, convergence absolue, puis critères de d'Alembert et de Cauchy, et une méthode pour choisir le bon critère. Voir [[Série numérique]] et [[Critère de d'Alembert et de Cauchy]].

## Séries alternées (*alternating series*)

**Définition.** Une série alternée est une série $\sum a_n$ avec
$$a_n = (-1)^n b_n \quad\text{ou}\quad a_n = (-1)^{n+1} b_n, \qquad b_n = |a_n| \ge 0.$$
Ses termes sont alternativement positifs et négatifs.

**Théorème (critère des séries alternées, *alternating test*).** Soit $\sum (-1)^{n+1} b_n$ (ou $\sum (-1)^n b_n$). Si
1. la suite $(b_n)$ est décroissante,
2. $\lim b_n = 0$,

alors la série alternée converge. Voir [[Critère des séries alternées]].

**Exercice.** Étudier :
1. $\sum_{n\ge1}(-1)^{n-1}\frac{1}{n}$, la série harmonique alternée ;
2. $\sum_{n\in\mathbb{N}}(-1)^n\frac{n^2}{n^3+1}$.

La note indique « Fait sur feuille » : la correction n'est pas rédigée.

**Proposition (reste).** Si $\sum (-1)^{n+1} b_n$ vérifie les hypothèses du critère, de somme $S$, alors $S$ est compris entre deux sommes partielles consécutives $S_n$ et $S_{n+1}$, et pour tout $n$ :
$$|R_n| = |S - S_n| \le b_{n+1}.$$

**Théorème ($p$-série alternée).** Pour $p$ réel, $\sum_{n} (-1)^n \frac{1}{n^p}$ converge si et seulement si $p > 0$.

**Remarque (note de l'étudiante).** On ne peut pas utiliser les équivalents avec des séries alternées : ils sont réservés aux séries à termes positifs.

## Séries absolument convergentes

**Définition.** $\sum a_n$ est absolument convergente si $\sum |a_n|$ converge.

**Exemples.**
1. $\sum \frac{(-1)^n}{n^2}$ est absolument convergente, car la $p$-série $\sum \frac{1}{n^2}$ converge.
2. La série harmonique alternée $\sum\frac{(-1)^n}{n}$ converge (critère des séries alternées) mais n'est pas absolument convergente, car $\sum\frac{1}{n}$ diverge.

Pour une série à termes positifs, convergence absolue et convergence coïncident (voir [[Critère de comparaison]]).

**Théorème.** Une série absolument convergente est convergente, et
$$\left|\sum_{n=0}^{+\infty} a_n\right| \le \sum_{n=0}^{+\infty} |a_n|.$$

**Définition.** $\sum a_n$ est [[Convergence conditionnelle|conditionnellement convergente]] si elle converge sans être absolument convergente.

## Critère du rapport (*ratio test*, d'Alembert)

**Théorème.** Soit $\sum a_n$ avec $a_n \ne 0$ à partir d'un rang $n_0$.
1. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = L < 1$, la série est absolument convergente.
2. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = L > 1$ ou $= +\infty$, la série diverge.
3. Si $\lim \left|\frac{a_{n+1}}{a_n}\right| = 1$, on ne peut rien conclure.

**Exemples avec $L = 1$** :

| $a_n$ | Nature de $\sum a_n$ |
|---|---|
| $(-1)^n \frac{n}{n^2+1}$ | conditionnellement convergente |
| $\frac{1}{n}$ | divergente |
| $(-1)^n \frac{1}{n^2+1}$ | absolument convergente |

## Critère de la racine (*root test*, Cauchy)

Pratique quand apparaissent des puissances $n$-ièmes ; la preuve est analogue à celle du critère du rapport.

**Théorème.** Soit $\sum a_n$ avec $a_n \ne 0$ à partir d'un rang $n_0$.
1. Si $\lim \sqrt[n]{|a_n|} = L < 1$, la série est absolument convergente.
2. Si $\lim \sqrt[n]{|a_n|} = L > 1$ ou $= +\infty$, la série diverge.
3. Si $\lim \sqrt[n]{|a_n|} = 1$, on ne peut rien conclure.

**Exercice.** Étudier $\sum_{n\ge1}\left(\frac{2n+3}{3n+2}\right)^n$ et $\sum_{n\ge2}\frac{n^{\ln n}}{n^n}$. Le cours ne donne pas la correction.

**Remarque.** On peut montrer que si $L = 1$ dans le critère du rapport, alors $L = 1$ dans celui de la racine, et réciproquement : les deux critères échouent alors (la réciproque est fausse en général, voir « Erreurs du cours »).

## Méthode pour choisir le bon critère

- Forme $\sum_{n\ge1}\frac{1}{n^p}$ : $p$-série ([[1 - Convergent, divergent and positive terms SERIES|séries de Riemann]]).
- Forme $\sum ar^n$ : série géométrique.
- Forme voisine d'une $p$-série ou d'une série géométrique : comparaison, comparaison par la limite, ou équivalents. En particulier, si $a_n$ est une fraction rationnelle ou une fonction algébrique, comparer à une $p$-série. Ces critères ne valent que pour des termes positifs ; si la série a des termes négatifs, les appliquer à $\sum |a_n|$ pour tester la convergence absolue.
- Si $\lim a_n \ne 0$ : [[Condition nécessaire de convergence|divergence grossière]] (*test for divergence*).
- Forme $\sum(-1)^n b_n$ ou $\sum(-1)^{n+1} b_n$ : critère des séries alternées.
- Factorielles ou produits : critère du rapport, sauf pour les $p$-séries, où la limite du rapport vaut 1.
- $a_n = (b_n)^n$ : critère de la racine.
- $a_n = f(n)$ avec $\int_1^{+\infty} f$ facile à calculer et $f$ vérifiant les bonnes hypothèses : [[Comparaison série-intégrale|critère intégral]] (*integral test*).

## Erreurs du cours

- [[Raw/Year 3/Séries/Chp2 : Alternating and absolutly convergent series.docx|Chp2 - Alternating and absolutly convergent series]] écrit « if $L = 1$ in the ratio test, then $L = 1$ in the root test and conversely » (vérifié sur l'image) ; la réciproque est fausse en général : la limite de la racine peut exister sans que celle du rapport existe. Le sens rapport vers racine vaut quand la limite du rapport existe.
