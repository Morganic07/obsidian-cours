---
type: matiere
tags: [year4]
sources: ["[[1 - intro to data mining|Chp1 - intro to data mining]]", "[[2 - association rules|chp 2 - association rules]]"]
maj: 2026-11-18
---

Fouille de données : classification, regroupement et combinaison de modèles (chapitre 1), règles d'association et algorithme Apriori (chapitre 2). La matière annonce des travaux pratiques (jeux Weather et IRIS, Weka, R, Python) dont le cours ne contient pas le contenu.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - intro to data mining\|Chp 1 - intro to data mining]] | Tâches, classification, validation, clustering, arbres, bagging et boosting | [[1 - intro to data mining\|Résumé]] |

## Documents PDF

| Document | Contenu | Résumé |
|---|---|---|
| chp 1 - cours data mining du prof ([[Raw/Year 4/data mining/chp 1 - cours data mining du prof.pdf\|chp 1 - cours data mining du prof.pdf]]) | Cours complet de l'enseignante (73 diapositives) : classification, clustering, arbres ID3, C4.5 et CART, bagging, boosting, forêts, exercices | [[1 - pdf du prof\|Résumé]] |
| chp 2 - association rules ([[Raw/Year 4/data mining/chp 2 - association rules.pdf\|chp 2 - association rules.pdf]]) | Diaporama de l'enseignante (18 diapositives) : tâches du data mining, support, confiance, lift, algorithme Apriori, génération des règles par redondance simple et stricte, trois exercices (corrigés en complément) | [[2 - association rules\|Résumé]] |

Le PDF du chapitre 1 contient les diapositives d'exercices (k-means, arbres de formules booléennes, entropie et gain) que la note ne reprend pas. Le chapitre 2 n'existe qu'en PDF.

## Concepts

- **Introduction** : [[Fouille de données]], [[Apprentissage automatique]], [[Apprentissage supervisé]], [[Apprentissage non supervisé]], [[Variable cible et variable explicative]], [[Prétraitement des données]], [[Valeur manquante]], [[Série temporelle]], [[Régression (apprentissage automatique)]], [[Résumé de données]], [[Extraction de motifs séquentiels]]
- **Classification** : [[Classifieur]], [[K plus proches voisins]], [[Machine à vecteurs de support]], [[Réseau de neurones]]
- **Validation** : [[Validation d'un classifieur]], [[Ensemble d'entraînement et de test]], [[Erreur de type I et de type II]], [[F-mesure]]
- **Regroupement** : [[Clustering]], [[Distance]], [[Centroïde]], [[Inertie (clustering)]], [[K-moyennes]], [[Classification hiérarchique ascendante]], [[Méthode de Ward]]
- **Arbres de décision** : [[Arbre de décision]], [[Algorithme ID3]], [[Entropie (théorie de l'information)]], [[Gain d'information]], [[Algorithme C4.5]], [[Rapport de gain]], [[Algorithme CART]], [[Indice de Gini]], [[Élagage]]
- **Combinaison de modèles** : [[Méthodes d'ensemble]], [[Bagging]], [[Boosting]], [[Forêt aléatoire]]
- **Règles d'association** : [[Règle d'association]], [[Transaction (fouille de données)]], [[Itemset fréquent]], [[Support (règle d'association)]], [[Confiance (règle d'association)]], [[Lift (règle d'association)]], [[Algorithme Apriori]], [[Propriété de fermeture descendante]], [[Redondance des règles d'association]], [[Analyse du panier de la ménagère]], [[Explosion combinatoire]] ; compléments : [[Algorithme FP-Growth]], [[Système de recommandation]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[1 - intro to data mining]] : les poids du boosting (initiaux à $1/N$, renormalisés pour que leur somme reste 1), les indices de l'algorithme des k-means et la formule de l'inertie intra-classes $I_W = \sum w_i I_i$.
- [[2 - association rules]] : dérouler Apriori à la main (jointure puis suppression dans apriori-gen), calculer confiance et lift, et savoir lire un lift par rapport à 1. Les inégalités de la redondance sont larges ($\geq$), pas strictes.

## Liens avec les autres matières

- **[[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]]** : l'[[Analyse en composantes principales]] et la [[Régression linéaire]] servent à explorer et prédire ; l'erreur de test et le test d'hypothèse y sont formalisés, avec l'[[Erreur de type I et de type II]]. Les distances du clustering (euclidienne) renvoient à la [[Norme]].
- **[[Cours/Probabilités et statistiques/Probability/_index|Probability]]** : la confiance d'une règle d'association est une [[Probabilité conditionnelle]], et le lift compare la fréquence observée à celle de l'[[Indépendance d'événements|indépendance]].
- **[[Cours/Informatique/IA/_index|IA]]** : les arbres, forêts et réseaux de neurones évoqués ici appartiennent à la branche connexionniste ou apprentissage automatique de la frise du cours d'IA ([[Approche symbolique et connexionniste]]). L'[[Apprentissage automatique]] et l'[[Apprentissage supervisé]] y sont aussi introduits.
- **[[Cours/Informatique/Data base/_index|Data base]]** : l'étape de jointure d'apriori-gen s'écrit comme une requête [[Langage SQL|SQL]], une jointure de l'[[Algèbre relationnelle]].
- **[[Cours/Informatique/Graph theory/_index|Graph theory]]** : Apriori parcourt l'espace des itemsets niveau par niveau, comme un [[Parcours en largeur]].
- **[[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]]** et **[[Cours/Mathématiques/Bilinear Algebra/_index|Bilinear Algebra]]** : la [[Distance]] utilisée pour regrouper les exemples y est définie formellement.
