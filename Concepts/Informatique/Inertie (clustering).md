---
type: concept
tags: [year4]
aliases: [inertie intra-classe, inertie inter-classe, inertie intra-classes, inertie inter-classes, intra-cluster inertia, théorème de Huygens, théorème de König-Huygens, within-cluster sum of squares]
sources: ["[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Inertie d'un ensemble de $N$ exemples de [[Centroïde|centroïde]] $g$ : $I = \frac{1}{N}\sum_{i=1}^N d^2(x_i, g)$.

Avec plusieurs groupes : inertie **intra-classe** $I_W = \sum_k I_k$, inertie **inter-classe** $I_B = \sum_i w_i\, d^2(g_i, g)$ avec $w_i = |g_i|/N$, et $I = I_W + I_B$. On veut des groupes denses et bien séparés, donc minimiser $I_W$ : c'est le critère d'arrêt des [[K-moyennes]] et le critère de fusion de la [[Méthode de Ward]].

## Compléments (hors du cours)

**Théorème de Huygens** (ou de König-Huygens) : la décomposition $I = I_W + I_B$ est exacte avec la distance euclidienne et
$$I_k = \frac{1}{N}\sum_{x \in G_k} d^2(x, g_k), \qquad I_W = \sum_k I_k .$$
Si l'on définit plutôt $I_k$ comme une moyenne sur les $|G_k|$ exemples du groupe, il faut pondérer : $I_W = \sum_k w_k I_k$ avec $w_k = |G_k|/N$.

**Conséquences** :

- l'inertie totale $I$ ne dépend pas de la partition, donc minimiser $I_W$ revient exactement à maximiser $I_B$ : groupes denses et groupes bien séparés sont un seul et même objectif ;
- le rapport $I_B / I \in [0, 1]$ mesure la part d'inertie expliquée par la partition (1 si chaque groupe est réduit à un point, 0 si tous les centroïdes coïncident) ;
- le critère de Ward $S = \dfrac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j)$ est exactement l'augmentation de $I_W$ (et la baisse de $I_B$) causée par la fusion des groupes $i$ et $j$.

Notion parente : [[Clustering]]. Voir aussi : [[Centroïde]], [[K-moyennes]], [[Méthode de Ward]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
