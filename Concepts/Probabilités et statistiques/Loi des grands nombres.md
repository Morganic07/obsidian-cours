---
type: concept
tags:
  - year3
aliases:
  - law of large numbers
  - LLN
  - loi faible des grands nombres
  - loi forte des grands nombres
  - weak law of large numbers
  - strong law of large numbers
matieres:
  - Statistics
sources:
  - "[[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]]"
  - "[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"
maj: 2026-11-08
---

Si $X_1, \dots, X_n$ est un échantillon d'une loi de moyenne $\mu$ et de variance finie, $\bar{X}$ converge vers $\mu$ :
1. en moyenne quadratique : $E[(\bar{X} - \mu)^2] \to 0$ ;
2. en probabilité : $P(|\bar{X} - \mu| \ge \varepsilon) \to 0$ pour tout $\varepsilon > 0$.

Pour des variables de Bernoulli de paramètre $p$, la proportion $\hat{P}$ converge de même vers $p$. En langage statistique : $\bar{X}$ est un estimateur consistant de $\mu$, et $\hat{P}$ de $p$ ([[Estimateur]]).

**Preuve de la loi faible** : $\bar{X}$ a pour espérance $\mu$ et pour variance $\sigma^2/n$, ce qui donne le point 1. L'inégalité de [[Espérance et variance|Bienaymé-Tchebychev]] donne alors le point 2 : [[Complément hors du cours|ⓘ]]
$$P(|\bar{X} - \mu| \ge \varepsilon) \le \frac{V(\bar{X})}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \xrightarrow[n \to \infty]{} 0.$$

**Loi forte** : la loi faible dit que, pour chaque $n$ grand, un écart d'au moins $\varepsilon$ est improbable ; la loi forte affirme que $\bar{X}_n$ converge vers $\mu$ **avec probabilité 1** (convergence presque sûre), c'est-à-dire que la suite des moyennes d'une réalisation finit par rester près de $\mu$. Elle ne demande que des variables iid de moyenne finie, sans hypothèse sur la variance. [[Complément hors du cours|ⓘ]]

**Portée** : [[Complément hors du cours|ⓘ]]
- elle fonde l'interprétation fréquentiste de la probabilité : sur de nombreuses répétitions indépendantes, la [[Fréquence relative|fréquence relative]] d'un événement tend vers sa probabilité (cas Bernoulli ci-dessus) ;
- elle justifie les méthodes de Monte-Carlo, qui estiment une espérance (ou une intégrale, ou une probabilité) par la moyenne de nombreuses simulations ;
- elle ne prévoit aucune « compensation » des écarts passés : après une série de pile avec une pièce équilibrée, face n'est pas plus probable au lancer suivant (erreur du joueur). L'écart se dilue dans la moyenne au fil des lancers ; il n'est pas rattrapé.

Le [[Théorème central limite]] précise la vitesse de cette convergence : l'écart $\bar{X} - \mu$ est de l'ordre de $\sigma/\sqrt{n}$. [[Complément hors du cours|ⓘ]]

Voir aussi : [[Théorème central limite]], [[Distribution d'échantillonnage]], [[Convergence en probabilité]].

Résumé : [[4 - Inferential statistics 1]]
