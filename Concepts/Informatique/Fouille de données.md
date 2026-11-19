---
type: concept
tags: [year4]
aliases: [data mining, knowledge discovery, découverte de connaissances, KDD, extraction de connaissances à partir des données]
sources: ["[[Raw/Year 4/data mining/chp 1 - cours data mining du prof.pdf|chp 1 - cours data mining du prof.pdf]]", "[[1 - intro to data mining|Chp 1 - intro to data mining]]", "[[Raw/Year 4/data mining/Chp 1 - intro to data mining.docx|Chp 1 - intro to data mining]]", "[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-08
---

Découverte de connaissances dans les données (« comment faire parler les données ? ») : utiliser les données passées pour analyser l'issue d'un problème [Fayyad et al., 1995]. La note [[1 - intro to data mining|Chp1 - intro to data mining]] y ajoute l'extraction de structures cachées, de corrélations non évidentes et de tendances, en combinant algorithmes, statistiques et IA.

**Processus** : analyse du problème, sélection et exploration des données, [[Prétraitement des données|prétraitement]], algorithme, évaluation et interprétation.

**Résultat** : un modèle (vue globale) ou des motifs (description locale, comme des règles).

## Compléments (complément, hors du cours)

- Au sens strict, la fouille n'est qu'une étape du processus d'**extraction de connaissances à partir des données** (ECD, en anglais KDD, *Knowledge Discovery in Databases*) : sélection des données, prétraitement (nettoyage, valeurs manquantes), transformation (discrétisation, normalisation, [[Réduction de dimension|réduction de dimension]]), fouille, puis interprétation et évaluation.
- **Tâches prédictives** ([[Apprentissage supervisé]]) : prédire une cible ; c'est une **classification** si la valeur est discrète, une **régression** si elle est continue. **Tâches descriptives** ([[Apprentissage non supervisé]]) : décrire la structure des données (groupes, règles d'association).

## Tâches (d'après [[2 - association rules]])

Le chapitre 2 range les tâches en deux familles. **Supervisées** (prédictives) : chaque instance a $p$ variables prédictives et une variable cible ; [[Classifieur|classification]] si la cible est discrète (diagnostic d'une maladie), [[Régression (apprentissage automatique)|régression]] si elle est continue (estimation d'un prix) ; le schéma y ajoute l'analyse de [[Série temporelle|séries temporelles]] et la prédiction. **Non supervisées** (descriptives) : [[Clustering]] (détection de profils d'utilisateurs), [[Règle d'association|règles d'association]] (analyse des logs d'un serveur web), [[Résumé de données|résumé]] et [[Extraction de motifs séquentiels|découverte de séquences]].

Voir aussi : [[Apprentissage automatique]], [[Prétraitement des données]], [[Apprentissage supervisé]], [[Clustering]], [[Algorithme Apriori]].

Résumés : [[1 - pdf du prof]], [[1 - intro to data mining]], [[2 - association rules]]
