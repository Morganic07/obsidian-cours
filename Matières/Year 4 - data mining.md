---
type: matiere
sources: ["[[Chp1 - intro to data mining]]"]
maj: 2026-11-05
---

Introduction à la fouille de données : classification, regroupement et combinaison de modèles. Une seule note, intégrée. La matière annonce des travaux pratiques (jeux Weather et IRIS, Weka, R, Python) dont le cours ne contient pas le contenu.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Chp1 - intro to data mining]] | Tâches, classification, validation, clustering, arbres, bagging et boosting | [[Chp1 - intro to data mining (résumé)\|Résumé]] |

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| [[raw/Year 4/data mining/cours data mining du prof.pdf\|cours data mining du prof]] | Cours complet de l'enseignante (73 diapositives) : classification, clustering, arbres ID3, C4.5 et CART, bagging, boosting, forêts, exercices | [[cours data mining du prof (résumé)\|Résumé]] |

Ce PDF contient les diapositives d'exercices (k-means, arbres de formules booléennes, entropie et gain) que la note ne reprend pas.

## Concepts

- **Classification** : [[Arbre de décision]], [[Validation d'un classifieur]]
- **Regroupement** : [[K-moyennes]]
- **Combinaison de modèles** : [[Méthodes d'ensemble]]

## À revoir en priorité avant un examen

- [[Chp1 - intro to data mining (résumé)]] : les poids du boosting (initiaux à $1/N$ puis normalisés pour une somme $N$) ne sont pas cohérents entre deux diapositives ; l'algorithme des k-means a des indices et un ordre d'instructions à vérifier.

## Liens avec les autres matières

- **[[Year 3 - Data analysis (Thanos)]]** : l'[[Analyse en composantes principales]] et la [[Régression linéaire]] servent à explorer et prédire ; l'erreur de test et le test d'hypothèse y sont formalisés. Les distances du clustering (euclidienne) renvoient à la [[Norme]].
- **[[Year 3 - IA]]** : les arbres, forêts et réseaux de neurones évoqués ici appartiennent à la branche connexionniste ou apprentissage automatique de la frise du cours d'IA ([[Approche symbolique et connexionniste]]).
