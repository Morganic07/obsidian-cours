---
type: concept
tags: [year4]
aliases: [bootstrap aggregating]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

Méthode d'ensemble : pour chacune des $k$ itérations, tirer $N$ exemples avec remise dans la base d'apprentissage, apprendre un modèle et le stocker. Pour classer, on renvoie la classe majoritaire parmi les modèles (la moyenne pour une sortie numérique). Les ensembles tirés ne sont pas disjoints.

Le bagging sert à neutraliser l'instabilité des méthodes sensibles aux changements de données.

## Compléments (complément, hors du cours)

- **Échantillon bootstrap** : le tirage de $N$ exemples avec remise parmi $N$. Un exemple donné en est absent avec la probabilité $\left(1 - \frac{1}{N}\right)^N \xrightarrow[N\to\infty]{} e^{-1} \approx 0{,}368$ : chaque échantillon contient donc environ 63,2 % des exemples distincts.
- **Erreur out-of-bag** : les exemples non tirés pour un modèle lui servent d'ensemble de test ; en les classant par les seuls modèles qui ne les ont pas vus, on estime l'erreur sans ensemble de test séparé.
- **Biais et variance** : le vote réduit la variance, sans augmenter le biais. Il est donc utile pour les méthodes instables (arbres profonds) et apporte peu à une méthode stable.

Notion parente : [[Méthodes d'ensemble]]. Voir aussi : [[Forêt aléatoire]], [[Boosting]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
