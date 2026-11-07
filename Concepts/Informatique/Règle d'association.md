---
type: concept
tags: [year4]
aliases: [règles d'association, association rules]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : une règle d'association est une implication de la forme $X \Rightarrow Y$ entre deux ensembles d'items disjoints, extraite d'une base de transactions : « les transactions qui contiennent $X$ contiennent souvent aussi $Y$ » (par exemple, dans des tickets de caisse, lait $\Rightarrow$ couches). On l'évalue par son support, la proportion de transactions qui contiennent à la fois $X$ et $Y$, et par sa confiance, la proportion de transactions contenant $X$ qui contiennent aussi $Y$. L'algorithme Apriori est la méthode classique pour extraire les règles dont le support et la confiance dépassent des seuils fixés.

## Dans le cours

Nommée dans le cours de data mining sans définition : les règles d'association y sont citées comme tâche non supervisée (descriptive), avec pour exemple l'analyse des logs d'un serveur web.

Notion parente : [[Apprentissage non supervisé]]. Voir aussi : [[Apprentissage supervisé]].

Résumés : [[Chp1 - intro to data mining (résumé)]], [[séance data mining du prof (résumé)]]
