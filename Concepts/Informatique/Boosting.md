---
type: concept
tags: [year4]
aliases: [AdaBoost, AdaBoost.M1]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

Méthode d'ensemble présentée avec **AdaBoost.M1** : les exemples sont pondérés (poids initial $1/N$) et les modèles sont construits l'un après l'autre.

- L'erreur $e_t$ du modèle $t$ est la somme des poids des exemples mal classés sur la somme des poids.
- Arrêt si $e_t = 0$ ou $e_t > 0{,}5$.
- Sinon, les poids des exemples bien classés sont multipliés par $\frac{e_t}{1-e_t}$ puis normalisés : les exemples difficiles gagnent du poids.
- Classification : chaque modèle ajoute $-\log\frac{e_t}{1-e_t}$ au poids de la classe qu'il prédit.

Notion parente : [[Méthodes d'ensemble]]. Voir aussi : [[Bagging]].

## Erreurs du cours

- [[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]] (diapositive 64) écrit « Normaliser les poids de tous les exemples (pour que la sommes soit N) » ; il faut « pour que la somme reste égale à 1 » : le poids initial est $1/N$ (somme 1), et la diapositive 66 dit « pour que la somme reste la même pour toutes les itérations ».

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
