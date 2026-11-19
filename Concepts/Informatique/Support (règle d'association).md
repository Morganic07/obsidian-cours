---
type: concept
tags: [year4]
aliases: [minSupp, support minimal, minimum support]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : $\text{support}(A \Rightarrow B) = P(A \cup B)$, où $P(X)$ est le pourcentage (la probabilité) des [[Transaction (fouille de données)|transactions]] qui contiennent l'ensemble d'items $X$. Un [[Itemset fréquent|itemset]] est fréquent quand son support atteint le seuil `minSupp`.

Exemple du cours : sur 4 transactions dont 2 contiennent {2, 3, 5}, $\text{support}(235) = 2/4$.

## Compléments (complément, hors du cours)

- $A \cup B$ est la [[Intersection et union d'ensembles|réunion]] des **items** : le support compte les transactions qui contiennent à la fois tous les items de $A$ et tous ceux de $B$. En termes d'[[Événement (probabilités)|événements]], c'est la probabilité de l'intersection « contient $A$ » et « contient $B$ ». C'est une [[Fréquence relative|fréquence relative]].
- Le support est anti-monotone : $Y \subseteq X \Rightarrow \text{support}(Y) \geq \text{support}(X)$ ([[Propriété de fermeture descendante]]).
- Il mesure l'importance d'une règle (combien de transactions elle concerne), pas sa fiabilité, qui est mesurée par la [[Confiance (règle d'association)|confiance]]. Un seuil trop haut ne garde que des évidences, un seuil trop bas fait exploser le nombre d'itemsets.

Voir aussi : [[Confiance (règle d'association)]], [[Lift (règle d'association)]], [[Règle d'association]].

Résumés : [[2 - association rules]]
