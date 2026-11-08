---
type: concept
tags: [year4]
aliases: [CART, Classification and Regression Tree]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-08
---

*Classification and Regression Tree* (Breiman, Friedman, Olshen, Stone, 1984) : algorithme d'[[Arbre de décision]] binaire (deux fils par nœud), qui accepte tous types de variables et choisit les séparations par l'[[Indice de Gini]].

**Construction** : tant que les conditions d'arrêt ne sont pas remplies (profondeur, nombre de feuilles, effectif d'un fils, performance suffisante ou plus d'amélioration), on cherche la meilleure séparation, celle qui maximise le gain de pureté $I_G(\text{avant}) - [W_1 I_G(\text{fils}_1) + W_2 I_G(\text{fils}_2)]$ (et non l'indice de Gini lui-même, petit pour un nœud pur), et on découpe. [[Erreurs du cours#^e-algorithme-cart|✎]] L'[[Élagage]] est facultatif.

Chaque feuille reçoit la classe majoritaire ; l'erreur globale est la somme pondérée des erreurs des feuilles.

Notion parente : [[Arbre de décision]]. Voir aussi : [[Indice de Gini]], [[Élagage]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
