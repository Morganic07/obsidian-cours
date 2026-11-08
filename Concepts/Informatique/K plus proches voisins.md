---
type: concept
tags: [year4]
aliases: [k-NN, kNN, k-nearest neighbours, k-nearest neighbors, apprentissage paresseux, lazy learning]
matieres: [data mining]
sources: ["[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Classifieur par estimation directe : on classe un point selon les classes de ses $k$ voisins. Sur la figure du cours (deux attributs numériques), $k = 3$ donne 1 jaune et 2 violets, $k = 6$ donne 4 jaunes et 2 violets : le résultat dépend de $k$. La méthode est prévue en TP.

## Compléments (hors du cours)

**Principe** : pour classer un point, calculer sa [[Distance]] à tous les exemples étiquetés, garder les $k$ plus proches et prendre leur classe majoritaire (la moyenne de leurs valeurs en régression).

**Apprentissage paresseux** (lazy learning) : aucun modèle n'est construit, il n'y a pas de phase d'apprentissage ; tout le calcul se fait au moment de classer, et le coût de chaque prédiction est proportionnel à la taille de la base, ce qui devient lourd sur de grandes bases.

**Choix de $k$** : un petit $k$ suit le bruit ($k = 1$ recopie la classe du plus proche voisin, même aberrant) ; un grand $k$ lisse la frontière vers la classe majoritaire ($k = N$ donne toujours la classe majoritaire). On prend $k$ impair à deux classes pour éviter les égalités, et on le choisit par [[Validation d'un classifieur|validation croisée]].

**Mise à l'échelle** : normaliser les attributs ([[Centrage et réduction|centrage-réduction]], ou min-max pour les ramener entre 0 et 1), sinon l'attribut aux grandes valeurs domine la distance.

Notion parente : [[Classifieur]]. Voir aussi : [[Distance]], [[Validation d'un classifieur]], [[Surapprentissage]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
