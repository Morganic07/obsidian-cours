---
type: concept
tags: [year3]
aliases: [bias-variance tradeoff, bias-variance trade-off, dilemme biais-variance, décomposition biais-variance]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la décomposition de l'erreur quadratique moyenne d'un [[Estimateur|estimateur]],
$$\text{MSE}(\hat\theta) = E[(\hat\theta - \theta)^2] = V(\hat\theta) + [E(\hat\theta) - \theta]^2 = \text{variance} + \text{biais}^2,$$
montre que l'erreur totale a deux sources. Réduire l'une augmente souvent l'autre : un estimateur légèrement biaisé peut donc être préférable à un estimateur sans biais s'il a une variance nettement plus faible. Le bon critère est l'erreur totale, pas l'absence de biais.

**Exemple, variance d'un échantillon normal** : $S^2 = \frac{1}{n-1}\sum (X_i - \bar{X})^2$ est sans biais, de variance $\frac{2\sigma^4}{n-1}$, donc de MSE $\frac{2\sigma^4}{n-1}$. L'estimateur $\hat\sigma^2 = \frac{1}{n}\sum (X_i - \bar{X})^2 = \frac{n-1}{n}S^2$ a un biais $-\sigma^2/n$ et une variance $\frac{2(n-1)\sigma^4}{n^2}$, d'où
$$\text{MSE}(\hat\sigma^2) = \frac{2(n-1)\sigma^4}{n^2} + \frac{\sigma^4}{n^2} = \frac{(2n-1)\sigma^4}{n^2} < \frac{2\sigma^4}{n-1}.$$
Le biais est plus que compensé par la baisse de variance ([[Variance et écart-type d'échantillon]]).

**En apprentissage automatique** : pour un modèle $\hat f$ qui prédit $y = f(x) + \varepsilon$, avec un bruit $\varepsilon$ de moyenne nulle et de variance $\sigma^2$, l'erreur de prédiction attendue en un point $x$ se décompose en
$$E\big[(y - \hat f(x))^2\big] = \underbrace{\big(E[\hat f(x)] - f(x)\big)^2}_{\text{biais}^2} + \underbrace{V\big(\hat f(x)\big)}_{\text{variance}} + \underbrace{\sigma^2}_{\text{bruit irréductible}},$$
l'espérance portant sur les jeux d'apprentissage possibles.
- Un modèle **trop simple** (droite pour un phénomène courbe) a un biais fort : c'est le **sous-apprentissage**.
- Un modèle **trop complexe** (arbre très profond, polynôme de haut degré) suit le bruit des données d'apprentissage et change beaucoup d'un jeu de données à l'autre : variance forte, c'est le [[Surapprentissage|surapprentissage]].
- On choisit la complexité qui minimise l'erreur de généralisation, mesurée sur des données non vues (jeu de test). Le bruit $\sigma^2$, lui, ne peut être réduit par aucun modèle.

Plusieurs techniques jouent sur ce compromis : l'élagage d'un [[Arbre de décision|arbre de décision]] augmente le biais pour réduire la variance ; le [[Bagging|bagging]] et les [[Forêt aléatoire|forêts aléatoires]] réduisent la variance en moyennant des modèles instables ; le [[Boosting|boosting]] réduit surtout le biais en combinant des modèles faibles.

## Dans le cours

Le cours ne le nomme pas : [[4 - Inferential statistics 1]] énonce la décomposition MSE = variance + biais² et illustre biais et variance par des cibles. Le compromis apparaît dans les compléments de cette fiche.

Voir aussi : [[Estimateur]], [[Surapprentissage]], [[Méthodes d'ensemble]], [[Maximum de vraisemblance]].

Résumés : [[4 - Inferential statistics 1]]
