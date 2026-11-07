---
type: concept
tags: [year3]
aliases: [prediction interval, prediction interval estimate, intervalle de prédiction d'une valeur individuelle]
matieres: [Data analysis (Thanos)]
sources: ["[[Séance 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-06
---

En [[Régression linéaire]], intervalle qui encadre la valeur $y$ d'un **individu** pour un $x_p$ donné : $\hat{y} \pm t_{\alpha/2}\,s\sqrt{1 + \dfrac{1}{n} + \dfrac{(x_p - \bar{x})^2}{SS_{xx}}}$, avec $n-2$ degrés de liberté.

Il se distingue de l'intervalle de confiance de la **moyenne** $E(y)$, qui n'a pas le « 1 » sous la racine. Ce « 1 » ajoute l'erreur aléatoire $\varepsilon$ : l'intervalle de prédiction est plus large, et ne descend jamais sous la variabilité naturelle, même avec un très grand $n$. Les deux s'élargissent quand $x_p$ s'éloigne de $\bar{x}$, et quand le niveau de confiance ou $s$ augmentent.

Exemple du cours (publicité 4 \$, $\hat{y} = 2{,}7$) : confiance $[1{,}645 ; 3{,}755]$, prédiction $[0{,}503 ; 4{,}897]$ (la diapositive inverse les bornes).

Notion parente : [[Régression linéaire]]. Voir aussi : [[Intervalle de confiance]], [[Erreur standard de la régression]].

## À vérifier

- La diapositive écrit « 4,897 ≤ y4 ≤ 0,503 » : bornes inversées (à corriger avant un examen).

Résumé : [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]]
