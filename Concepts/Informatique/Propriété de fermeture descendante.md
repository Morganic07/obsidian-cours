---
type: concept
tags: [year4]
aliases: [downward closure, downward closure property, propriété Apriori, antimonotonie du support, anti-monotonie]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : si un itemset n'est pas fréquent, aucun de ses sur-ensembles ne l'est. De façon équivalente, si $X_k$ est un [[Itemset fréquent|itemset fréquent]], tous les itemsets inclus dans $X_k$ sont fréquents. Exemple : si $ABCD$ est fréquent, $ABC$, $ABD$, $ACD$, $BCD$, $AB$, $AC$, $AD$, $BC$, $BD$, $CD$, $A$, $B$, $C$, $D$ le sont aussi. [[Erreurs du cours#^e-propriete-de-fermeture-descendante|✎]]

C'est la propriété sur laquelle repose l'[[Algorithme Apriori]].

## Compléments (complément, hors du cours)

- **Preuve** : une transaction qui contient $X$ contient chacun de ses sous-ensembles ; donc $Y \subseteq X \Rightarrow \text{support}(Y) \geq \text{support}(X)$ (le [[Support (règle d'association)|support]] est anti-monotone), et si $X$ atteint `minSupp`, $Y$ aussi. La forme « un sur-ensemble d'un itemset non fréquent n'est pas fréquent » en est la [[Preuve par contraposition|contraposée]].
- **Usage** : l'étape de suppression d'apriori-gen retire tout candidat dont un sous-ensemble n'est pas fréquent, sans compter son support.
- Dans le [[Diagramme de Hasse|diagramme de Hasse]] des itemsets ordonnés par [[Inclusion (ensembles)|inclusion]], les itemsets fréquents forment une partie fermée vers le bas.

Notion parente : [[Itemset fréquent]]. Voir aussi : [[Règle d'association]].

Résumés : [[2 - association rules]]
