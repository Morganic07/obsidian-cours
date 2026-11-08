---
type: concept
tags: [year4]
aliases: [AdaBoost, AdaBoost.M1, Adaptive Boosting]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

Méthode d'ensemble présentée avec **AdaBoost.M1** : les exemples sont pondérés (poids initial $1/N$) et les modèles sont construits l'un après l'autre.

- L'erreur $e_t$ du modèle $t$ est la somme des poids des exemples mal classés sur la somme des poids.
- Arrêt si $e_t = 0$ ou $e_t > 0{,}5$.
- Sinon, les poids des exemples bien classés sont multipliés par $\frac{e_t}{1-e_t}$ puis normalisés pour que leur somme reste égale à 1 : les exemples difficiles gagnent du poids. [[Erreurs du cours#^e-boosting|✎]]
- Classification : chaque modèle ajoute $-\log\frac{e_t}{1-e_t}$ au poids de la classe qu'il prédit.

## Compléments (complément, hors du cours)

- **Poids du modèle** : $W_t = \log\frac{1-e_t}{e_t}$ (la valeur $-\log\frac{e_t}{1-e_t}$ du cours) est positif tant que $e_t < 0{,}5$ et nul en $0{,}5$. D'où l'arrêt si $e_t > 0{,}5$ (à deux classes, le modèle fait pire que le hasard) ou si $e_t = 0$ (poids infini).
- **Effet de la mise à jour** : après multiplication des poids des exemples bien classés par $\frac{e_t}{1-e_t}$, leur somme passe de $1 - e_t$ à $e_t$, égale à celle des mal classés. L'erreur pondérée du modèle $t$ vaut alors exactement 50 % : le modèle suivant est forcé d'apprendre autre chose.
- Chaque modèle n'a besoin que d'être un **apprenant faible**, à peine meilleur que le hasard, souvent un *decision stump* (arbre à une seule coupe).
- Le boosting réduit surtout le biais. Il est séquentiel (pas de construction en parallèle, contrairement au [[Bagging]]) et sensible au bruit : les exemples mal étiquetés voient leur poids grimper.
- AdaBoost (*Adaptive Boosting*) est dû à Y. Freund et R. Schapire (1995-1997). Sa forme moderne est le *gradient boosting* (XGBoost, LightGBM).

Notion parente : [[Méthodes d'ensemble]]. Voir aussi : [[Bagging]], [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
