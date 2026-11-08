---
type: concept
tags: [year4]
aliases: [k-means, K-means, kmeans, k-moyennes, k-means++, méthode du coude, elbow method]
matieres: [data mining]
sources: ["[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Algorithme de partitionnement non hiérarchique : trouver $K$ groupes d'exemples sans étiquette, chacun représenté par son centroïde.

**[[Inertie (clustering)|Inertie]]** d'un ensemble de $N$ exemples de centroïde $g$ : $I = \frac{1}{N}\sum d^2(x_i, g)$, où $d$ est une distance (euclidienne, de Manhattan, de Hamming). Avec $K$ groupes : $I = I_W + I_B$, l'inertie intra-classes $I_W$ et l'inertie inter-classes $I_B = \sum w_id^2(g_i, g)$, $w_i = |g_i|/N$. On veut des groupes denses et bien séparés, donc minimiser $I_W$.

**Algorithme** : choisir $K$ centroïdes au hasard parmi les exemples ; répéter (affecter chaque exemple au centroïde le plus proche, recalculer les centroïdes) jusqu'à ce que $I_W$ change de moins de $\epsilon$. À chaque tour, le cours garde l'ancienne valeur ($I \leftarrow I_W$) avant de recalculer $I_W$, puis teste $|I - I_W| < \epsilon$ ; au départ, $I \leftarrow \infty$.

**Exercice du cours** : points 1, 2, 9, 12, 20 avec $k = 2$ (centres 1 et 20, puis 2 et 9) et $k = 3$ (1, 9, 12).

**Résultats de l'exercice (complément, hors du cours)**, avec $I_W$ = somme des carrés des écarts au centroïde de son groupe, divisée par $N = 5$ :

| Départ | Partition finale | Centroïdes | $I_W$ |
|---|---|---|---|
| $k=2$, centres 1 et 20 | {1, 2, 9}, {12, 20} | 4 ; 16 | $70/5 = 14$ |
| $k=2$, centres 2 et 9 | {1, 2}, {9, 12, 20} | 1,5 ; 13,67 | $\approx 13{,}03$ |
| $k=3$, centres 1, 9, 12 | {1, 2}, {9, 12}, {20} | 1,5 ; 10,5 ; 20 | $5/5 = 1$ |

Les deux départs à $k=2$ aboutissent à deux partitions différentes : l'illustration d'un minimum local.

## Compléments (hors du cours)

**Convergence** : avec la distance euclidienne, chaque étape fait baisser ou laisse égale $I_W$ — la réaffectation au centroïde le plus proche ne peut que réduire les distances, et la moyenne d'un groupe est le point qui minimise la somme des carrés des écarts. Le nombre de partitions étant fini, l'algorithme s'arrête en un nombre fini d'itérations, mais sur un **minimum local** qui dépend de l'initialisation. On le relance donc plusieurs fois avec des centres différents et on garde la partition de plus petite $I_W$ ; **k-means++** choisit des centres initiaux éloignés les uns des autres (chaque nouveau centre tiré avec une probabilité proportionnelle au carré de sa distance au centre déjà choisi le plus proche).

**Choix de $K$** : $I_W$ décroît toujours quand $K$ augmente (elle vaut 0 pour $K = N$, chaque exemple étant son propre groupe), donc on ne peut pas choisir $K$ en minimisant $I_W$. **Méthode du coude** : tracer $I_W$ en fonction de $K$ et retenir le point où la baisse ralentit nettement. Autre critère courant : le **score de silhouette**, qui compare pour chaque exemple la distance moyenne à son groupe et au groupe voisin le plus proche.

**Limites** : sensible aux valeurs aberrantes (elles déplacent la moyenne) ; trouve surtout des groupes compacts, à peu près sphériques et de tailles comparables ; $K$ doit être fixé à l'avance ; les attributs doivent être à la même échelle.

**Autre approche, hiérarchique** : on fusionne les exemples du bas vers le haut en un arbre (dendrogramme), qu'une coupe horizontale transforme en $K$ groupes. Critères de fusion : saut minimal, maximal, moyen, ou méthode de Ward (perte minimale de $I_W$).

Notion parente : [[Clustering]]. Voir aussi : [[Centroïde]], [[Inertie (clustering)]], [[Classification hiérarchique ascendante]], [[Méthode de Ward]], [[Centrage et réduction]], [[Distance]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
