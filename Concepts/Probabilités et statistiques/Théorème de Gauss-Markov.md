---
type: concept
tags: [year3]
aliases: [Gauss-Markov theorem, BLUE, best linear unbiased estimator, meilleur estimateur linéaire sans biais]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 10 : linear regression.docx|Cours 10 - linear regression]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : dans le modèle linéaire $\mathbf{y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ (avec $X$ de rang plein), si les erreurs vérifient

1. $E(\varepsilon_i) = 0$ pour tout $i$ (espérance nulle),
2. $\mathrm{Var}(\varepsilon_i) = \sigma^2$ pour tout $i$ (même variance, [[Homoscédasticité|homoscédasticité]]),
3. $\mathrm{Cov}(\varepsilon_i, \varepsilon_j) = 0$ pour $i \neq j$ (erreurs non corrélées),

alors l'estimateur des [[Moindres carrés|moindres carrés]]
$$\hat{\boldsymbol{\beta}} = (X^\top X)^{-1} X^\top \mathbf{y}$$
est, parmi tous les [[Estimateur|estimateurs]] linéaires en $\mathbf{y}$ et sans biais de $\boldsymbol{\beta}$, celui de variance minimale. On dit qu'il est **BLUE** (*Best Linear Unbiased Estimator*, « meilleur estimateur linéaire sans biais »). Sa matrice de variance est $\mathrm{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2 (X^\top X)^{-1}$, et pour tout autre estimateur linéaire sans biais $\tilde{\boldsymbol{\beta}}$, $\mathrm{Var}(\tilde{\boldsymbol{\beta}}) - \mathrm{Var}(\hat{\boldsymbol{\beta}})$ est une matrice symétrique positive : chaque coefficient, et même chaque combinaison linéaire des coefficients, est estimé avec une variance au plus égale.

**Ce que le théorème ne demande pas, et ce qu'il ne dit pas.**
- Il ne suppose **pas la normalité** des erreurs. La normalité sert seulement à connaître la loi exacte des estimateurs, donc aux tests $t$ et $F$ et aux [[Intervalle de confiance|intervalles de confiance]] (pour les petits échantillons surtout).
- Il ne compare les moindres carrés qu'aux estimateurs **linéaires et sans biais**. Un estimateur biaisé (régression ridge par exemple) ou non linéaire peut avoir une erreur quadratique moyenne plus faible.
- Si la variance n'est pas constante (hétéroscédasticité) ou si les erreurs sont corrélées (série temporelle par exemple), les moindres carrés restent sans biais mais ne sont plus de variance minimale ; les erreurs standard calculées par la formule usuelle deviennent fausses. Les moindres carrés généralisés (ou pondérés), qui tiennent compte de la structure de la variance, redeviennent alors BLUE.

## Dans le cours

Le cours ne le nomme pas. [[10 - linear regression]] liste les quatre hypothèses sur l'erreur (moyenne nulle, variance constante, normalité, indépendance) sans dire à quoi chacune sert ; la fiche les relie au théorème dans ses compléments : les hypothèses de moyenne nulle, de variance constante et d'indépendance suffisent à Gauss-Markov, la normalité ne sert qu'à l'inférence.

Voir aussi : [[Régression linéaire]], [[Moindres carrés]], [[Estimateur]], [[Homoscédasticité]], [[Résidu (régression)]], [[Multicolinéarité]], [[Série temporelle]]

Résumés : [[10 - linear regression]]
