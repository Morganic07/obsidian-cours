---
type: concept
tags: [year3]
aliases: [maximum likelihood, maximum likelihood estimation, estimateur du maximum de vraisemblance, EMV, MLE]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part 1 : Inferential statistics.docx|Chp4 Part 1 - Inferential statistics]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'estimateur du maximum de vraisemblance (EMV, *MLE*) d'un paramètre $\theta$ est la valeur $\hat\theta$ qui maximise la [[Vraisemblance|vraisemblance]] des données observées,
$$L(\theta) = \prod_{i=1}^n f(x_i; \theta),$$
produit des densités (loi continue) ou des probabilités $P(X = x_i)$ (loi discrète) pour un échantillon indépendant. C'est la valeur du paramètre qui rend les données observées les plus probables. La méthode a été développée par R. A. Fisher dans les années 1910-1920.

**Méthode** :
1. Écrire la log-vraisemblance $\ell(\theta) = \ln L(\theta) = \sum_{i=1}^n \ln f(x_i; \theta)$. Le logarithme étant croissant, $L$ et $\ell$ ont le même maximum ; une somme se dérive plus facilement qu'un produit.
2. Résoudre $\ell'(\theta) = 0$ (équation de vraisemblance ; un système $\partial \ell / \partial \theta_j = 0$ s'il y a plusieurs paramètres).
3. Vérifier qu'il s'agit d'un maximum ($\ell''(\hat\theta) < 0$).

**Exemple 1, [[Loi exponentielle|loi exponentielle]]** : $f(x; \lambda) = \lambda e^{-\lambda x}$, donc $\ell(\lambda) = n\ln\lambda - \lambda\sum x_i$ et $\ell'(\lambda) = n/\lambda - \sum x_i$, nul pour
$$\hat\lambda = \frac{n}{\sum x_i} = \frac{1}{\bar{x}}.$$
$\ell''(\lambda) = -n/\lambda^2 < 0$ : c'est bien un maximum.

**Exemple 2, épreuves de Bernoulli** : $k$ succès sur $n$, $L(p) = p^k(1-p)^{n-k}$, $\ell'(p) = k/p - (n-k)/(1-p)$, nul pour $\hat p = k/n$, la proportion observée.

**Exemple 3, [[Loi normale|loi normale]] $N(\mu, \sigma)$** : $\ell(\mu, \sigma^2) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum (x_i - \mu)^2$. Les deux dérivées partielles s'annulent pour
$$\hat\mu = \bar{x}, \qquad \hat\sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2,$$
ce dernier étant **biaisé** (espérance $\frac{n-1}{n}\sigma^2$).

**Exemple 4, [[Loi uniforme|loi uniforme]] sur $[0, \theta]$** : $L(\theta) = \theta^{-n}$ si $\theta \ge \max x_i$, et $0$ sinon. $L$ décroît sur $[\max x_i, +\infty[$ : le maximum est atteint au bord, $\hat\theta = \max_i x_i$, sans passer par une dérivée nulle.

**Propriétés** :
- **Invariance** : l'EMV de $g(\theta)$ est $g(\hat\theta)$. Par exemple, l'EMV de $\sigma$ pour une loi normale est $\sqrt{\hat\sigma^2}$, et celui de la moyenne $1/\lambda$ d'une loi exponentielle est $\bar{x}$.
- **Pour $n$ grand**, sous des conditions de régularité (support ne dépendant pas de $\theta$, vraisemblance dérivable) : l'EMV est convergent, asymptotiquement normal, et asymptotiquement de variance minimale parmi les estimateurs convergents (efficacité asymptotique). Sa variance est alors approximativement $1/(n\,I(\theta))$, où $I(\theta) = -E\left[\frac{\partial^2}{\partial\theta^2}\ln f(X; \theta)\right]$ est l'information de Fisher.
- Pour $n$ petit, il peut être biaisé (exemples 3 et 4).

Il sert à ajuster de nombreux modèles : la [[Régression logistique|régression logistique]] estime ses coefficients par maximum de vraisemblance, et, pour un modèle linéaire à erreurs normales, les moindres carrés de la [[Régression linéaire|régression linéaire]] coïncident avec le maximum de vraisemblance.

## Dans le cours

Le cours ne le traite pas : le chapitre donne les estimateurs usuels sans méthode générale pour les obtenir. Il apparaît dans les compléments de [[4 - Inferential statistics 1]]. La page [[Vraisemblance]] présente la notion de vraisemblance vue en Data analysis ([[5 - Hypothesis Testing]]).

Notion parente : [[Vraisemblance]]. Voir aussi : [[Estimateur]], [[Méthode des moments]], [[Compromis biais-variance]].

Résumés : [[4 - Inferential statistics 1]]
