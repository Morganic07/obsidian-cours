---
type: concept
aliases: [bagging, boosting, random forest, forêt aléatoire, forêts aléatoires, AdaBoost, ensemble methods, bootstrap aggregating, combinaison de modèles]
matieres: [data mining]
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-05
---

Combiner plusieurs modèles pour obtenir une seule prédiction, par vote (pondéré ou non) en classification, ou par moyenne en numérique.

- **Bagging** (bootstrap aggregating) : $k$ échantillons de $N$ exemples tirés avec remise, un modèle (par exemple un [[Arbre de décision]]) par échantillon, vote majoritaire. Tous les modèles ont le même poids. Il neutralise l'instabilité des modèles face aux changements de données.
- **Boosting** (AdaBoost.M1) : les modèles sont construits l'un après l'autre, chacun influencé par les précédents, avec des exemples pondérés. Après chaque modèle d'erreur $e_t$ (arrêt si $e_t = 0$ ou $e_t > 0{,}5$), le poids des exemples bien classés est multiplié par $\dfrac{e_t}{1-e_t}$, puis les poids sont normalisés : les exemples difficiles gagnent du poids. Le vote est pondéré, chaque modèle apportant $-\log\dfrac{e_t}{1-e_t}$ à la classe qu'il prédit.
- **Forêt aléatoire** : bagging d'arbres où, à chaque nœud, on ne tire au hasard que $q$ variables parmi $p$ pour choisir la coupure. On fait voter ou on moyenne les $K$ arbres.

Résumés : [[Chp1 - intro to data mining (résumé)]], [[cours data mining du prof (résumé)]]
