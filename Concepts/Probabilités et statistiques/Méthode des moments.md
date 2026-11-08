---
type: concept
tags: [year3]
aliases: [method of moments, estimateur des moments, méthode des moments de Pearson]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la méthode des moments construit un [[Estimateur|estimateur]] en égalant les moments théoriques de la loi, qui dépendent du ou des paramètres inconnus, aux moments d'échantillon correspondants, puis en résolvant en $\theta$.

- Moment théorique d'ordre $k$ : $\mu_k(\theta) = E(X^k)$ ([[Espérance et variance]]).
- Moment d'échantillon d'ordre $k$ : $m_k = \dfrac{1}{n}\sum_{i=1}^n x_i^k$ ; en particulier $m_1 = \bar{x}$.
- On écrit $\mu_k(\theta) = m_k$ pour $k = 1, \dots, p$ : il faut **autant d'équations que de paramètres** ($p$). La solution $\hat\theta$ est l'estimateur des moments.

La méthode est due à Karl Pearson (fin du XIXᵉ siècle). Elle repose sur la [[Loi des grands nombres]] : $m_k$ converge vers $E(X^k)$, si bien que l'estimateur obtenu est en général convergent.

**Exemple 1, [[Loi exponentielle|loi exponentielle]] de paramètre $\lambda$** : $E(X) = 1/\lambda$. L'équation $1/\lambda = \bar{x}$ donne
$$\hat\lambda = \frac{1}{\bar{x}}.$$

**Exemple 2, [[Loi normale|loi normale]] $N(\mu, \sigma)$** (deux paramètres, deux équations) : $E(X) = \mu$ et $E(X^2) = \sigma^2 + \mu^2$. D'où
$$\hat\mu = \bar{x}, \qquad \hat\sigma^2 = \frac{1}{n}\sum_{i=1}^n x_i^2 - \bar{x}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2.$$
Cet estimateur de $\sigma^2$ est **biaisé** : son espérance vaut $\frac{n-1}{n}\sigma^2$, alors que $s^2$, de dénominateur $n - 1$, est sans biais ([[Variance et écart-type d'échantillon]]).

**Exemple 3, [[Loi uniforme|loi uniforme]] sur $[0, \theta]$** : $E(X) = \theta/2$, d'où $\hat\theta = 2\bar{x}$. Cet estimateur est sans biais, mais il peut être inférieur à la plus grande observation, ce qui est absurde puisque toutes les données sont $\le \theta$.

**Avantages et limites** : la méthode est simple et donne souvent une formule explicite. Mais l'estimateur obtenu peut être biaisé, ou moins précis (de variance plus grande) que celui du [[Maximum de vraisemblance|maximum de vraisemblance]] ; il sert aussi de valeur de départ pour calculer numériquement ce dernier. Les deux méthodes donnent parfois le même résultat, comme pour les exemples 1 et 2.

## Dans le cours

Le cours ne la nomme pas : il donne les estimateurs usuels ($\bar{x}$, $s^2$, $\hat{p}$) sans méthode générale pour en construire. Elle apparaît dans les compléments de [[4 - Inferential statistics 1]].

Voir aussi : [[Estimateur]], [[Maximum de vraisemblance]], [[Loi des grands nombres]], [[Paramètre et statistique]].

Résumés : [[4 - Inferential statistics 1]]
