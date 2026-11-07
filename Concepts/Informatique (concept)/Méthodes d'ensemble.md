---
type: concept
tags: [year4]
aliases: [ensemble methods, combinaison de modèles]
matieres: [data mining]
sources: ["[[chp 1 - intro to data mining (résumé)|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-06
---

Combiner plusieurs modèles pour obtenir une seule prédiction, par vote (pondéré ou non) en classification, ou par moyenne en numérique. En bagging, les modèles ont tous le même poids ; en boosting, leur poids dépend de leur succès.

- **[[Bagging]]** (bootstrap aggregating) : $k$ échantillons de $N$ exemples tirés avec remise, un modèle (par exemple un [[Arbre de décision]]) par échantillon, vote majoritaire. Tous les modèles ont le même poids. Il neutralise l'instabilité des modèles face aux changements de données.
- **[[Boosting]]** (AdaBoost.M1) : les modèles sont construits l'un après l'autre, chacun influencé par les précédents, avec des exemples pondérés. Après chaque modèle d'erreur $e_t$ (arrêt si $e_t = 0$ ou $e_t > 0{,}5$), le poids des exemples bien classés est multiplié par $\dfrac{e_t}{1-e_t}$, puis les poids sont normalisés : les exemples difficiles gagnent du poids. Le vote est pondéré, chaque modèle apportant $-\log\dfrac{e_t}{1-e_t}$ à la classe qu'il prédit.
- **[[Forêt aléatoire]]** : bagging d'arbres où, à chaque nœud, on ne tire au hasard que $q$ variables parmi $p$ pour choisir la coupure. On fait voter ou on moyenne les $K$ arbres.

Résumés : [[chp 1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
