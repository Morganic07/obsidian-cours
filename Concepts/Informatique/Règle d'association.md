---
type: concept
tags: [year4]
aliases: [règles d'association, association rules, association rule]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]", "[[Raw/Year 4/data mining/chp 1 - cours data mining du prof.pdf|chp 1 - cours data mining du prof.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : la fouille de règles d'association cherche des relations entre items dans de grandes bases de [[Transaction (fouille de données)|transactions]]. Une règle s'écrit $A \Rightarrow B$, où $A$ et $B$ sont des ensembles d'items (vin $\Rightarrow$ fromage ; vin, fromage $\Rightarrow$ jambon). C'est une tâche non supervisée, dont l'exemple type est l'analyse des journaux d'un serveur web ou le « panier de la ménagère » ([[Analyse du panier de la ménagère]]).

**Mesures** :
- [[Support (règle d'association)|support]] : $P(A \cup B)$, proportion des transactions qui contiennent tous les items de $A$ et de $B$ ;
- [[Confiance (règle d'association)|confiance]] : $P(B \mid A) = P(A \cup B)/P(A)$ ;
- [[Lift (règle d'association)|lift]] : $P(A \cup B)/(P(A)P(B))$.

**Méthode** : avec deux seuils `minSupp` et `minConf`, trouver les [[Itemset fréquent|itemsets fréquents]] (support $\geq$ `minSupp`), par exemple avec l'[[Algorithme Apriori]], puis en tirer les règles de confiance $\geq$ `minConf`. La génération des règles s'accélère par la [[Redondance des règles d'association|redondance simple ou stricte]].

## Compléments (complément, hors du cours)

- Le problème a été posé par Agrawal, Imieliński et Swami (SIGMOD, 1993), sur des données de ventes en supermarché.
- Une règle d'association n'est pas une [[Implication logique|implication logique]] : elle vaut pour une proportion des transactions (sa confiance), et elle ne dit rien de la [[Corrélation et causalité|causalité]].
- Applications : disposition des rayons et promotions croisées en [[Marketing|marketing]], [[Système de recommandation|systèmes de recommandation]], analyse de parcours sur un site web.

## Dans le cours

- Dans l'introduction ([[1 - intro to data mining]], [[1 - pdf du prof]]), les règles d'association sont seulement nommées comme tâche non supervisée (descriptive), avec pour exemple l'analyse des logs d'un serveur web.
- Le chapitre 2 ([[2 - association rules]]) leur est consacré : terminologie, support, confiance, lift, Apriori, génération des règles et trois exercices.

Notion parente : [[Apprentissage non supervisé]]. Voir aussi : [[Apprentissage supervisé]], [[Fouille de données]], [[Algorithme FP-Growth]].

Résumés : [[2 - association rules]], [[1 - intro to data mining]], [[1 - pdf du prof]]
