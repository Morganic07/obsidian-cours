---
type: concept
tags: [year4]
aliases: [classifier validation, matrice de confusion, confusion matrix, validation croisée, cross validation, cross-validation, précision et rappel, precision and recall, exactitude, accuracy, sensibilité et spécificité, leave-one-out, validation croisée stratifiée]
matieres: [data mining]
sources: ["[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]", "[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

Estimer la qualité d'un classifieur sur des données qu'il n'a pas vues : on sépare les données en entraînement (construction du modèle) et test (mesure de l'erreur). L'erreur $Er$ est la probabilité de mal prédire la classe, le taux de réussite est $1 - Er$. L'erreur d'entraînement, mesurée sur les données d'entraînement, ne suffit pas.

**Matrice de confusion** : lignes = classe réelle, colonnes = classe prédite. VP et VN (vrais positifs et négatifs) sur la diagonale, FN (positifs manqués) et FP (fausses alertes) hors diagonale.

- Précision positive $\dfrac{TP}{TP+FP}$ : parmi ce qui est classé positif, quelle part l'est vraiment.
- Rappel positif $\dfrac{TP}{TP+FN}$ : parmi les vrais positifs, quelle part est trouvée.
- Versions négatives : $\dfrac{TN}{TN+FN}$ et $\dfrac{TN}{TN+FP}$.

Exemple du cours (filtre anti-spam, 100 e-mails) : 15 VP, 5 FN, 2 FP, 78 VN, soit précision 88,2 % et rappel 75 %.

**Validation croisée** : on coupe les données en $n$ parties disjointes de même taille (chaque valeur de la cible présente dans chacune), puis on entraîne sur $n-1$ parties et on teste sur la dernière, à tour de rôle. L'erreur globale est la moyenne des erreurs des $n$ tests (exemple : 5 %, 9 %, 7 %, soit 7 %).

## Compléments (hors du cours)

**Exactitude** (accuracy) : $\dfrac{TP+TN}{TP+TN+FP+FN} = 1 - Er$, soit $93/100 = 93\,\%$ sur l'exemple du filtre anti-spam. Le rappel positif s'appelle aussi **sensibilité**, le rappel négatif $\frac{TN}{TN+FP}$ **spécificité**.

**Classes déséquilibrées** : l'exactitude trompe. Sur l'exemple spam (20 spams, 80 e-mails normaux), un filtre qui ne classe jamais rien en spam obtient 80 % de réussite avec un rappel positif nul ; avec 99 % de négatifs, répondre toujours « négatif » donne 99 %. On regarde alors précision, rappel et [[F-mesure]].

**Erreur d'entraînement optimiste** : un modèle peut apprendre par cœur ses données d'entraînement ([[Surapprentissage]]), d'où une erreur d'entraînement faible et trompeuse. Seul un ensemble de **test**, jamais utilisé pour construire ni régler le modèle, estime l'erreur de généralisation. Le choix d'un modèle ou d'un hyperparamètre (le $k$ des [[K plus proches voisins]], la profondeur d'un arbre) se fait sur un ensemble de **validation** distinct, ou par validation croisée sur les données d'entraînement ; le test est réservé à l'évaluation finale.

**Validation croisée en pratique** : $n = 5$ ou $10$ plis le plus souvent ; $n = N$ donne le **leave-one-out** (chaque exemple sert de test une fois). Quand chaque classe garde ses proportions dans chaque pli (ce que demande le cours), la validation croisée est dite **stratifiée**. Elle sert à estimer l'erreur ou à choisir un réglage ; le modèle final est ensuite réappris sur toutes les données.

Notion parente : [[Classifieur]]. Liens : [[Ensemble d'entraînement et de test]], [[F-mesure]], [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
