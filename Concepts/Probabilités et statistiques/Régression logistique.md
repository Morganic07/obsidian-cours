---
type: concept
tags: [year3]
aliases: [logistic regression, régression logit, modèle logit]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 3 : Paradoxe de Simpson.docx|Cours 3 - Paradoxe de Simpson]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la régression logistique est un modèle de régression pour une variable à expliquer **binaire** $Y \in \{0, 1\}$ (succès/échec, guéri/non guéri). Au lieu de modéliser $Y$ directement, comme la [[Régression linéaire|régression linéaire]], elle modélise la probabilité $p = P(Y = 1 \mid x_1, \dots, x_k)$ par son **logit** :

$$\operatorname{logit}(p) = \ln\frac{p}{1-p} = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k,$$

d'où

$$p = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots + \beta_k x_k)}}.$$

La fonction $x \mapsto 1/(1+e^{-x})$ (sigmoïde) envoie toute valeur réelle dans $]0 ; 1[$ : la prédiction reste une probabilité, ce que ne garantit pas une régression linéaire sur une variable 0/1.

- **Cote et odds ratio** : $p/(1-p)$ est la cote (*odds*) du succès. Quand $x_i$ augmente d'une unité, toutes les autres variables égales par ailleurs, la cote est multipliée par $e^{\beta_i}$ : c'est l'**odds ratio** associé à $x_i$. $e^{\beta_i} > 1$ signale un effet favorable au succès, $e^{\beta_i} < 1$ un effet défavorable.
- **Estimation** : les coefficients s'estiment par maximum de [[Vraisemblance|vraisemblance]], et non par moindres carrés ; il n'y a pas de formule fermée, le calcul est itératif.
- **Ajustement** : mettre un facteur de confusion parmi les variables explicatives donne un effet du traitement **ajusté**, c'est-à-dire mesuré à valeur égale de ce facteur. Comparer l'effet brut (traitement seul) et l'effet ajusté sert à détecter ou à corriger un [[Paradoxe de Simpson]].
- **En R** : `glm(y ~ x1 + x2, family = binomial)` ; `summary()` donne les $\beta_i$ et leurs tests, `exp(coef(modele))` les odds ratios, `predict(modele, type = "response")` les probabilités prédites.

## Dans le cours

Le cours ne la nomme pas. [[3 - Paradoxe de Simpson]] parle de « modèles plus complexes (comme la régression multivariée) » qui ajustent les résultats sur les variables cachées ; la régression logistique, adaptée à un résultat binaire comme guéri / non guéri, apparaît dans les compléments de cette fiche.

Voir aussi : [[Régression linéaire]], [[Paradoxe de Simpson]], [[Vraisemblance]], [[Variable indicatrice]], [[Corrélation et causalité]].

Résumés : [[3 - Paradoxe de Simpson]]
