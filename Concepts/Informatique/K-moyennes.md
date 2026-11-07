---
type: concept
tags: [year4]
aliases: [k-means, K-means, kmeans, k-moyennes]
matieres: [data mining]
sources: ["[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

Algorithme de partitionnement non hiérarchique : trouver $K$ groupes d'exemples sans étiquette, chacun représenté par son centroïde.

**[[Inertie (clustering)|Inertie]]** d'un ensemble de $N$ exemples de centroïde $g$ : $I = \frac{1}{N}\sum d^2(x_i, g)$, où $d$ est une distance (euclidienne, de Manhattan, de Hamming). Avec $K$ groupes : $I = I_W + I_B$, l'inertie intra-classes $I_W$ et l'inertie inter-classes $I_B = \sum w_id^2(g_i, g)$, $w_i = |g_i|/N$. On veut des groupes denses et bien séparés, donc minimiser $I_W$.

**Algorithme** : choisir $K$ centroïdes au hasard parmi les exemples ; répéter (affecter chaque exemple au centroïde le plus proche, recalculer les centroïdes) jusqu'à ce que $I_W$ change de moins de $\epsilon$. À chaque tour, le cours garde l'ancienne valeur ($I \leftarrow I_W$) avant de recalculer $I_W$, puis teste $|I - I_W| < \epsilon$ ; au départ, $I \leftarrow \infty$.

**Exercice du cours** : points 1, 2, 9, 12, 20 avec $k = 2$ (centres 1 et 20, puis 2 et 9) et $k = 3$ (1, 9, 12).

**Autre approche, hiérarchique** : on fusionne les exemples du bas vers le haut en un arbre (dendrogramme), qu'une coupe horizontale transforme en $K$ groupes. Critères de fusion : saut minimal, maximal, moyen, ou méthode de Ward (perte minimale de $I_W$).

Notion parente : [[Clustering]]. Voir aussi : [[Centroïde]], [[Inertie (clustering)]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
