---
type: matiere
tags: [year4]
sources: ["[[1 - intro to data mining (résumé)|Chp1 - intro to data mining]]"]
maj: 2026-11-06
---

Introduction à la fouille de données : classification, regroupement et combinaison de modèles. Une seule note, intégrée. La matière annonce des travaux pratiques (jeux Weather et IRIS, Weka, R, Python) dont le cours ne contient pas le contenu.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - intro to data mining (résumé)\|Chp1 - intro to data mining]] | Tâches, classification, validation, clustering, arbres, bagging et boosting | [[1 - intro to data mining (résumé)\|Résumé]] |

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| cours data mining du prof ([[Raw/Year 4/data mining/cours data mining du prof.pdf\|cours data mining du prof.pdf]]) | Cours complet de l'enseignante (73 diapositives) : classification, clustering, arbres ID3, C4.5 et CART, bagging, boosting, forêts, exercices | [[1 - pdf du prof (résumé)\|Résumé]] |

Ce PDF contient les diapositives d'exercices (k-means, arbres de formules booléennes, entropie et gain) que la note ne reprend pas.

## Concepts

- **Introduction** : [[Fouille de données]], [[Apprentissage automatique]], [[Apprentissage supervisé]], [[Variable cible et variable explicative]], [[Prétraitement des données]], [[Valeur manquante]], [[Règle d'association]], [[Série temporelle]]
- **Classification** : [[Classifieur]], [[K plus proches voisins]], [[Machine à vecteurs de support]], [[Réseau de neurones]]
- **Validation** : [[Validation d'un classifieur]], [[Ensemble d'entraînement et de test]], [[Erreur de type I et de type II]], [[F-mesure]]
- **Regroupement** : [[Clustering]], [[Distance]], [[Centroïde]], [[Inertie (clustering)]], [[K-moyennes]], [[Classification hiérarchique ascendante]], [[Méthode de Ward]]
- **Arbres de décision** : [[Arbre de décision]], [[Algorithme ID3]], [[Entropie (théorie de l'information)]], [[Gain d'information]], [[Algorithme C4.5]], [[Rapport de gain]], [[Algorithme CART]], [[Indice de Gini]], [[Élagage]]
- **Combinaison de modèles** : [[Méthodes d'ensemble]], [[Bagging]], [[Boosting]], [[Forêt aléatoire]]

## À revoir en priorité avant un examen

- [[1 - intro to data mining (résumé)]] : les poids du boosting (initiaux à $1/N$ puis normalisés pour une somme $N$) ne sont pas cohérents entre deux diapositives ; l'algorithme des k-means a des indices et un ordre d'instructions à vérifier.

## Liens avec les autres matières

- **[[Data analysis (index)]]** : l'[[Analyse en composantes principales]] et la [[Régression linéaire]] servent à explorer et prédire ; l'erreur de test et le test d'hypothèse y sont formalisés, avec l'[[Erreur de type I et de type II]]. Les distances du clustering (euclidienne) renvoient à la [[Norme]].
- **[[IA (index)]]** : les arbres, forêts et réseaux de neurones évoqués ici appartiennent à la branche connexionniste ou apprentissage automatique de la frise du cours d'IA ([[Approche symbolique et connexionniste]]). L'[[Apprentissage automatique]] et l'[[Apprentissage supervisé]] y sont aussi introduits.
- **[[Analyse dans Rn (index)]]** et **[[Bilinear Algebra (index)]]** : la [[Distance]] utilisée pour regrouper les exemples y est définie formellement.
