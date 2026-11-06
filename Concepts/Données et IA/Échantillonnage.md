---
type: concept
tags: [year3]
aliases: [sampling, random sampling, échantillon aléatoire, simple random sample, stratified sampling, cluster sampling, systematic sampling, biais d'échantillonnage, sampling bias, iid, independent and identically distributed, variables iid, convenience sampling, échantillon de convenance, échantillonnage de convenance]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[Chp1 - Intro to statistics]]", "[[Chp3 - More on probability]]"]
maj: 2026-11-06
---

Un échantillon est une partie de la population, tirée pour estimer un paramètre par une statistique.

**Méthodes aléatoires** : simple (tous les échantillons de même taille équiprobables), stratifié (tirage proportionnel dans chaque strate), par grappes (grappes entières tirées), systématique (un élément sur $n$ après un départ aléatoire). L'échantillon de convenance est biaisé.

**Remise** : le vrai tirage aléatoire est avec remise ; sans remise, l'écart est négligeable si l'échantillon est petit devant la population.

**Erreurs** : erreur d'échantillonnage (liée au processus, par exemple une taille trop faible), erreur hors échantillonnage, biais d'échantillonnage (certains membres moins susceptibles d'être choisis).

**iid** : des variables $X_1, \dots, X_n$ indépendantes et de même loi forment un échantillon aléatoire simple. Avec tirage sans remise, on les traite comme iid si $n/N \le 0{,}05$.

**Data analysis** : la stratification réduit la variabilité, donc la largeur d'un intervalle ([[Intervalle de confiance]]).

Liens : [[Population et échantillon]], [[Erreur d'échantillonnage]], [[Tirage avec et sans remise]], [[Distribution d'échantillonnage]], [[Estimateur]]

Résumés : [[Chp1 - Intro to statistics (résumé)]], [[Chp3 - More on probability (résumé)]], [[Séance 4 - Estimation (résumé)]]
