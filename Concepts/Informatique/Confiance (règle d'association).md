---
type: concept
tags: [year4]
aliases: [minConf, confiance minimale, minimum confidence]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : $\text{confidence}(A \Rightarrow B) = P(B \mid A) = \dfrac{P(A \cup B)}{P(A)}$, soit $\text{support}(A \cup B)/\text{support}(A)$. Une règle est retenue quand sa confiance atteint le seuil `minConf`.

Exemple du cours : si $ABCD$ est fréquent, la règle $AB \Rightarrow CD$ a pour confiance $\text{support}(ABCD)/\text{support}(AB)$. Sur les transactions {1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}, la règle $2 \to 35$ a une confiance de $2/3$.

## Compléments (complément, hors du cours)

- C'est une [[Probabilité conditionnelle|probabilité conditionnelle]] estimée sur la base : la proportion des transactions contenant $A$ qui contiennent aussi $B$.
- Elle n'est pas symétrique : $\text{confidence}(A \Rightarrow B) \neq \text{confidence}(B \Rightarrow A)$ en général.
- Son défaut : une règle vers un item très fréquent a une forte confiance même sans lien entre les items. Le [[Lift (règle d'association)|lift]] compare la confiance à la probabilité du conséquent pour corriger ce biais.
- Ajouter des items à gauche ne fait pas baisser la confiance à itemset constant ($AB \Rightarrow C$ a une confiance au moins égale à $A \Rightarrow BC$) : c'est le fondement de la [[Redondance des règles d'association]].

Voir aussi : [[Support (règle d'association)]], [[Règle d'association]].

Résumés : [[2 - association rules]]
