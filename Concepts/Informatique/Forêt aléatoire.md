---
type: concept
tags: [year4]
aliases: [forêts aléatoires, random forest]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

[[Bagging]] d'arbres de décision : on construit $K$ arbres sur des échantillons tirés avec remise et, à chaque nœud, on tire $q$ variables parmi les $p$ disponibles. La prédiction se fait par vote ou par moyenne. Le tirage des variables vise à rendre les arbres plus indépendants entre eux, ce qui rend le vote des « experts » plus efficace. La méthode est efficace en grande dimension (diapositives 68 à 70 de [[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]], la 69 étant un schéma : sous-ensembles aléatoires de données, un arbre par sous-ensemble, et à chaque nœud un petit sous-ensemble de variables tiré au hasard).

Notion parente : [[Bagging]]. Voir aussi : [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
