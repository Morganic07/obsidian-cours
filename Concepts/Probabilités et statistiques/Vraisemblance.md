---
type: concept
tags: [year3]
aliases: [likelihood, fonction de vraisemblance, likelihood function, maximum de vraisemblance, maximum likelihood, MLE, estimateur du maximum de vraisemblance]
matieres: [Data analysis (Thanos)]
sources: ["[[5 - Hypothesis Testing|Cours 5 - Hypothesis Testing]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 5 : Hypothesis Testing .docx|Cours 5 - Hypothesis Testing]]"]
maj: 2026-11-08
---

La **probabilité** va des paramètres vers les données : le paramètre est fixé. La **vraisemblance** va des données vers les paramètres : les données sont fixées et l'on évalue la crédibilité d'un paramètre.

Dans un test, la [[P-value]] sert à juger la vraisemblance de $H_0$.

**Définition formelle (complément, hors du cours)** : pour des observations $x$ et un modèle de densité (ou de probabilité) $f(x \mid \theta)$, la vraisemblance est

$$L(\theta \mid x) = f(x \mid \theta),$$

la même expression que la densité, mais lue comme une fonction de $\theta$, les données $x$ étant fixées. Pour un échantillon de $n$ observations indépendantes, $L(\theta \mid x_1, \dots, x_n) = \prod_{i=1}^n f(x_i \mid \theta)$, et l'on travaille souvent avec la log-vraisemblance $\ell(\theta) = \sum_{i=1}^n \ln f(x_i \mid \theta)$, plus simple à dériver.

- La vraisemblance **n'est pas une probabilité sur $\theta$** : intégrée ou sommée sur $\theta$, elle ne vaut pas 1 en général. Elle sert à comparer des valeurs de $\theta$ entre elles.
- La valeur $\hat\theta$ qui maximise $L$ (ou $\ell$) est l'**estimateur du maximum de vraisemblance** (*maximum likelihood estimator*, MLE). Exemple : pour $n$ épreuves de Bernoulli avec $k$ succès, $L(p) = p^k (1-p)^{n-k}$ est maximale en $\hat p = k/n$, la proportion observée.

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[P-value]], [[Estimateur]], [[Régression logistique]].

Résumés : [[5 - Hypothesis Testing]]
