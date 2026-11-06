---
type: concept
tags: [year4]
aliases: [AdaBoost, AdaBoost.M1]
matieres: [data mining]
sources: [".raw/Year 4/data mining/cours data mining du prof.pdf"]
maj: 2026-11-06
---

Méthode d'ensemble présentée avec **AdaBoost.M1** : les exemples sont pondérés (poids initial $1/N$) et les modèles sont construits l'un après l'autre.

- L'erreur $e_t$ du modèle $t$ est la somme des poids des exemples mal classés sur la somme des poids.
- Arrêt si $e_t = 0$ ou $e_t > 0{,}5$.
- Sinon, les poids des exemples bien classés sont multipliés par $\frac{e_t}{1-e_t}$ puis normalisés : les exemples difficiles gagnent du poids.
- Classification : chaque modèle ajoute $-\log\frac{e_t}{1-e_t}$ au poids de la classe qu'il prédit.

Notion parente : [[Méthodes d'ensemble]]. Voir aussi : [[Bagging]].

## À vérifier

Le poids initial est $1/N$, mais la normalisation est faite « pour que la somme soit $N$ », alors qu'une autre diapositive dit « pour que la somme reste la même » : le cours ne tranche pas.

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
