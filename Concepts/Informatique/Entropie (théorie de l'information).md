---
type: concept
tags: [year4]
aliases: [entropie, entropy, quantité d'information]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

**Quantité d'information** d'un sous-ensemble de cardinal $n$ tiré de $N$ événements : $Q = \log_2(N/n)$.

**Entropie** d'une partition, avec $p_i = n_i/N$ : $I = \sum_i p_i \log_2(1/p_i)$.

Un arbre de décision est vu comme une source qui émet $I(E) = \sum_{i=1}^{N_C} p_i \log_2(1/p_i)$, où $p_i$ est la fréquence de la classe $i$. À deux classes :

$$I(p, n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n}$$

L'entropie sert à calculer le [[Gain d'information]] dans ID3 ; CART utilise à la place l'[[Indice de Gini]].

Notion parente : [[Algorithme ID3]]. Voir aussi : [[Gain d'information]], [[Indice de Gini]].

## Erreurs du cours

- [[1 - intro to data mining|Chp1 - intro to data mining]] écrit, pour une partition $E_1, \ldots, E_k$, « $I(partition) = \sum_{i=1}^{m} \left(\frac{n_i}{N}\right) \log_2 \frac{N}{n_i}$ » ; il faut « $\sum_{i=1}^{k}$ » : la somme porte sur les $k$ sous-ensembles, comme dans la ligne suivante.

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
