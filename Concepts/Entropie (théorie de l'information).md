---
type: concept
aliases: [entropie, entropy, quantité d'information]
matieres: [data mining]
sources: ["[[raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof]]"]
maj: 2026-11-06
---

**Quantité d'information** d'un sous-ensemble de cardinal $n$ tiré de $N$ événements : $Q = \log_2(N/n)$.

**Entropie** d'une partition, avec $p_i = n_i/N$ : $I = \sum_i p_i \log_2(1/p_i)$.

Un arbre de décision est vu comme une source qui émet $I(E) = \sum_{i=1}^{N_C} p_i \log_2(1/p_i)$, où $p_i$ est la fréquence de la classe $i$. À deux classes :

$$I(p, n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n}$$

L'entropie sert à calculer le [[Gain d'information]] dans ID3 ; CART utilise à la place l'[[Indice de Gini]].

Notion parente : [[Algorithme ID3]]. Voir aussi : [[Gain d'information]], [[Indice de Gini]].

## À vérifier

- L'indice de la somme passe de $m$ à $k$ pour le nombre de sous-ensembles (coquille relevée par le résumé).

Résumés : [[Chp1 - intro to data mining (résumé)]], [[cours data mining du prof (résumé)]]
