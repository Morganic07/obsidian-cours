---
type: concept
aliases: [classifier validation, matrice de confusion, confusion matrix, validation croisée, cross validation, cross-validation, précision et rappel, precision and recall]
matieres: [data mining]
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-05
---

Estimer la qualité d'un classifieur sur des données qu'il n'a pas vues : on sépare les données en entraînement (construction du modèle) et test (mesure de l'erreur). L'erreur $Er$ est la probabilité de mal prédire la classe, le taux de réussite est $1 - Er$. L'erreur d'entraînement, mesurée sur les données d'entraînement, ne suffit pas.

**Matrice de confusion** : lignes = classe réelle, colonnes = classe prédite. VP et VN (vrais positifs et négatifs) sur la diagonale, FN (positifs manqués) et FP (fausses alertes) hors diagonale.

- Précision positive $\dfrac{TP}{TP+FP}$ : parmi ce qui est classé positif, quelle part l'est vraiment.
- Rappel positif $\dfrac{TP}{TP+FN}$ : parmi les vrais positifs, quelle part est trouvée.
- Versions négatives : $\dfrac{TN}{TN+FN}$ et $\dfrac{TN}{TN+FP}$.

Exemple du cours (filtre anti-spam, 100 e-mails) : 15 VP, 5 FN, 2 FP, 78 VN, soit précision 88,2 % et rappel 75 %.

**Validation croisée** : on coupe les données en $n$ parties disjointes de même taille (chaque valeur de la cible présente dans chacune), puis on entraîne sur $n-1$ parties et on teste sur la dernière, à tour de rôle. L'erreur globale est la moyenne des erreurs des $n$ tests (exemple : 5 %, 9 %, 7 %, soit 7 %).

Liens : [[Arbre de décision]]. Résumés : [[Chp1 - intro to data mining (résumé)]], [[cours data mining du prof (résumé)]]
