---
type: concept
tags: [year4]
aliases: [forêts aléatoires, random forest, random forests]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 4/data mining/Chp1 - intro to data mining.docx|Chp1 - intro to data mining]]"]
maj: 2026-11-08
---

[[Bagging]] d'arbres de décision : on construit $K$ arbres sur des échantillons tirés avec remise et, à chaque nœud, on tire $q$ variables parmi les $p$ disponibles. La prédiction se fait par vote ou par moyenne. Le tirage des variables vise à rendre les arbres plus indépendants entre eux, ce qui rend le vote des « experts » plus efficace. La méthode est efficace en grande dimension (diapositives 68 à 70 de [[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]], la 69 étant un schéma : sous-ensembles aléatoires de données, un arbre par sous-ensemble, et à chaque nœud un petit sous-ensemble de variables tiré au hasard).

## Compléments (complément, hors du cours)

- Méthode formalisée par L. Breiman (2001), coauteur de [[Algorithme CART|CART]].
- **Pourquoi tirer les variables** : sans ce tirage, une variable très prédictive serait à la racine de presque tous les arbres, qui seraient fortement corrélés ; le vote d'arbres corrélés réduit peu la variance.
- **Valeurs usuelles de $q$** : $q \approx \sqrt{p}$ en classification, $q \approx p/3$ en régression. Plus $q$ est petit, moins les arbres sont corrélés, mais chacun est moins bon.
- Les arbres sont poussés au bout, sans [[Élagage]] : leur variance est compensée par le vote.
- Une forêt fournit gratuitement l'erreur out-of-bag (voir [[Bagging]]) et une **importance des variables** : baisse moyenne d'impureté due à la variable, ou perte de performance quand on permute ses valeurs.

Notion parente : [[Bagging]]. Voir aussi : [[Arbre de décision]], [[Méthodes d'ensemble]], [[Surapprentissage]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
