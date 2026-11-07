---
type: concept
tags: [year4]
aliases: [Ward method, critère de Ward]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

Critère de fusion de la classification hiérarchique : on fusionne les deux groupes qui font perdre le moins d'inertie intra-classe $I_W$, avec

$$S_{G_i,G_j} = \frac{w_i w_j}{w_i + w_j}\, d^2(g_i, g_j), \qquad w_i = \frac{|G_i|}{N},$$

où $g_i$ est le centroïde du groupe $G_i$.

Notion parente : [[Classification hiérarchique ascendante]]. Voir aussi : [[Inertie (clustering)]], [[K-moyennes]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
