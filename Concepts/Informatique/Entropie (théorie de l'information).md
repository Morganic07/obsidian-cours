---
type: concept
tags: [year4]
aliases: [entropie, entropy, quantité d'information]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

**Quantité d'information** d'un sous-ensemble de cardinal $n$ tiré de $N$ événements : $Q = \log_2(N/n)$.

**Entropie** d'une partition $E_1, \ldots, E_k$, avec $p_i = n_i/N$ : $I = \sum_{i=1}^{k} p_i \log_2(1/p_i)$, la somme portant sur les $k$ sous-ensembles. [[Erreurs du cours#^e-entropie-theorie-de-l-information|✎]]

Un arbre de décision est vu comme une source qui émet $I(E) = \sum_{i=1}^{N_C} p_i \log_2(1/p_i)$, où $p_i$ est la fréquence de la classe $i$. À deux classes :

$$I(p, n) = \frac{p}{p+n}\log_2\frac{p+n}{p} + \frac{n}{p+n}\log_2\frac{p+n}{n}$$

Bornes (complément, hors du cours) : $I(E)$ vaut 0 quand tous les exemples sont de la même classe, et au plus $\log_2 N_C$, valeur atteinte quand les $N_C$ classes sont équiréparties (1 bit pour deux classes à 50 %) ; par convention, $0 \log_2 \frac{1}{0} = 0$.

L'entropie sert à calculer le [[Gain d'information]] dans ID3 ; CART utilise à la place l'[[Indice de Gini]].

Notion parente : [[Algorithme ID3]]. Voir aussi : [[Gain d'information]], [[Indice de Gini]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
