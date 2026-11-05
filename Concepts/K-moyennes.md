---
type: concept
aliases: [k-means, K-means, kmeans, k-moyennes, inertie intra-classe, inertie inter-classe]
matieres: [data mining]
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-05
---

Algorithme de partitionnement non hiérarchique : trouver $K$ groupes d'exemples sans étiquette, chacun représenté par son centroïde.

**Inertie** d'un ensemble de $N$ exemples de centroïde $g$ : $I = \frac{1}{N}\sum d^2(x_i, g)$, où $d$ est une distance (euclidienne, de Manhattan, de Hamming). Avec $K$ groupes : $I = I_W + I_B$, l'inertie intra-classes $I_W$ et l'inertie inter-classes $I_B = \sum w_id^2(g_i, g)$, $w_i = |g_i|/N$. On veut des groupes denses et bien séparés, donc minimiser $I_W$.

**Algorithme** : choisir $K$ centroïdes au hasard parmi les exemples ; répéter (affecter chaque exemple au centroïde le plus proche, recalculer les centroïdes) jusqu'à ce que $I_W$ change de moins de $\epsilon$.

**Autre approche, hiérarchique** : on fusionne les exemples du bas vers le haut en un arbre (dendrogramme), qu'une coupe horizontale transforme en $K$ groupes. Critères de fusion : saut minimal, maximal, moyen, ou méthode de Ward (perte minimale de $I_W$).

Résumé : [[Chp1 - intro to data mining (résumé)]]
