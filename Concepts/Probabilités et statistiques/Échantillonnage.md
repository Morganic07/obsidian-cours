---
type: concept
tags: [year3]
aliases: [sampling, random sampling, échantillon aléatoire, simple random sample, stratified sampling, cluster sampling, systematic sampling, biais d'échantillonnage, sampling bias, iid, independent and identically distributed, variables iid, convenience sampling, échantillon de convenance, échantillonnage de convenance, base de sondage, sampling frame, méthode des quotas, quota sampling]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[1 - Intro to statistics|Chp1 - Intro to statistics]]", "[[3 - More on probability|Chp3 - More on probability]]"]
maj: 2026-11-08
---

Un échantillon est une partie de la population, tirée pour estimer un paramètre par une statistique.

**Méthodes aléatoires** : simple (tous les échantillons de même taille équiprobables), stratifié (tirage proportionnel dans chaque strate), par grappes (grappes entières tirées), systématique (un élément sur $n$ après un départ aléatoire). L'échantillon de convenance est biaisé.

**Remise** : le vrai tirage aléatoire est avec remise ; sans remise, l'écart est négligeable si l'échantillon est petit devant la population.

**Erreurs** : erreur d'échantillonnage (liée au processus, par exemple une taille trop faible), erreur hors échantillonnage, biais d'échantillonnage (certains membres moins susceptibles d'être choisis).

**iid** : des variables $X_1, \dots, X_n$ indépendantes et de même loi forment un échantillon aléatoire simple. Avec tirage sans remise, on les traite comme iid si $n/N \le 0{,}05$.

**Compléments (hors du cours)** :
- **Strates et grappes** : les strates sont choisies homogènes à l'intérieur, ce qui rend l'estimation plus précise qu'avec un tirage simple de même taille ; les grappes sont hétérogènes à l'intérieur (chacune ressemble à la population) et choisies pour réduire le coût, au prix de la précision.
- **Base de sondage** (*sampling frame*) : liste complète des unités de la population, nécessaire au tirage simple et au tirage systématique. Le tirage systématique est biaisé si la liste présente une périodicité égale au pas.
- **Méthode des quotas** : non aléatoire, l'échantillon reproduit la structure de la population sur quelques critères (sexe, âge, profession). La marge d'erreur probabiliste ne s'y applique pas en toute rigueur.
- **Taille et biais** : l'erreur d'échantillonnage diminue en $\sigma/\sqrt{n}$, mais un biais ne diminue pas quand $n$ augmente. Exemple : le *Literary Digest* en 1936, environ 2,4 millions de réponses et une prédiction fausse de l'élection présidentielle américaine ([[1 - Intro to statistics]]).

**Data analysis** : la stratification réduit la variabilité, donc la largeur d'un intervalle ([[Intervalle de confiance]]).

Liens : [[Population et échantillon]], [[Erreur d'échantillonnage]], [[Tirage avec et sans remise]], [[Distribution d'échantillonnage]], [[Estimateur]]

Résumés : [[1 - Intro to statistics]], [[3 - More on probability]], [[4 - Estimation]]
