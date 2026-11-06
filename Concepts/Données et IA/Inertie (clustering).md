---
type: concept
tags: [year4]
aliases: [inertie intra-classe, inertie inter-classe, inertie intra-classes, inertie inter-classes, intra-cluster inertia]
sources: [".raw/Year 4/data mining/cours data mining du prof.pdf"]
maj: 2026-11-06
---

Inertie d'un ensemble de $N$ exemples de [[Centroïde|centroïde]] $g$ : $I = \frac{1}{N}\sum_{i=1}^N d^2(x_i, g)$.

Avec plusieurs groupes : inertie **intra-classe** $I_W = \sum_k I_k$, inertie **inter-classe** $I_B = \sum_i w_i\, d^2(g_i, g)$ avec $w_i = |g_i|/N$, et $I = I_W + I_B$. On veut des groupes denses et bien séparés, donc minimiser $I_W$ : c'est le critère d'arrêt des [[K-moyennes]] et le critère de fusion de la [[Méthode de Ward]].

Notion parente : [[Clustering]]. Voir aussi : [[Centroïde]], [[K-moyennes]], [[Méthode de Ward]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
