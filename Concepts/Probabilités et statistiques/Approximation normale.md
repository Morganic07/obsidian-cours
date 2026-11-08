---
type: concept
tags:
  - year3
aliases:
  - normal approximation
  - approximation normale de la binomiale
  - approximation de la binomiale par la loi normale
  - correction de continuité
  - continuity correction
sources:
  - "[[7 - Z-Test|Cours 7 - Z-Test]]"
  - "[[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]]"
  - "[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"
maj: 2026-11-08
---

Le [[Théorème central limite]] justifie d'approcher par une loi normale la [[Loi binomiale|binomiale]] ($n$ grand), la [[Loi de Poisson|Poisson]] ($\mu$ grand), la [[Loi binomiale négative|binomiale négative]] ($r$ grand) et la gamma ($\alpha$ grand).

**Statistics** : pour une proportion, $\hat P$ est approximativement normale si $np \ge 10$ et $n(1-p) \ge 10$.

**Data analysis** : le cours demande $nP \ge 5$ et $n(1-P) \ge 5$, avec $\mu = np$ et $\sigma = \sqrt{np(1-p)}$.

Les deux seuils (10 en Statistics, 5 en Data analysis) ont été relus dans les images des deux cours : ce sont deux règles pratiques différentes pour la même approximation. Retenir celle de la matière évaluée.

**Correction de continuité** : une loi discrète à valeurs entières donne une probabilité à chaque entier, alors que la loi normale, continue, donne une probabilité nulle à chaque point. Pour l'approcher, on représente la valeur entière $x$ par l'intervalle $[x - 0{,}5 ;\ x + 0{,}5]$. Pour $X \sim \mathrm{Bin}(n, p)$, avec $\Phi$ la fonction de répartition de la normale centrée réduite : [[Complément hors du cours|ⓘ]]
$$P(X \le x) \approx \Phi\left(\frac{x + 0{,}5 - np}{\sqrt{np(1-p)}}\right), \qquad P(X \ge x) \approx 1 - \Phi\left(\frac{x - 0{,}5 - np}{\sqrt{np(1-p)}}\right), \qquad P(X = x) \approx \Phi\left(\frac{x + 0{,}5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{x - 0{,}5 - np}{\sqrt{np(1-p)}}\right).$$

Exemple : $n = 100$, $p = 0{,}5$, donc $np = 50$ et $\sqrt{np(1-p)} = 5$. $P(X \le 55) \approx \Phi(5{,}5/5) = \Phi(1{,}1) \approx 0{,}864$, pour une valeur exacte de $0{,}864$, alors que sans correction $\Phi(5/5) = \Phi(1) \approx 0{,}841$. La correction compte surtout quand $n$ est modéré ; son effet s'efface quand $n$ grandit. [[Complément hors du cours|ⓘ]]

Notion parente : [[Théorème central limite]]. Voir aussi : [[Loi binomiale]], [[Loi de Poisson]], [[Loi exponentielle]], [[Test Z]], [[Loi binomiale négative]].

Résumés : [[7 - Z-Test]], [[4 - Inferential statistics 1]], [[4 - Inferential statistics 3]]
