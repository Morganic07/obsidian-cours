---
type: concept
tags: [year4]
aliases: [lift, interest (association rules)]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : $\text{lift}(A \Rightarrow B) = \dfrac{\text{confidence}(A \Rightarrow B)}{P(B)} = \dfrac{P(A \cup B)}{P(A)\,P(B)}$. L'exercice 2 du cours demande de garder les règles qui « améliorent la prédiction par rapport à la mesure statistique induite par la base » et de donner un sens à la valeur du lift.

## Compléments (complément, hors du cours)

- **Lecture** : lift $= 1$, les deux ensembles d'items sont [[Indépendance d'événements|indépendants]] ($P(A \cap B) = P(A)P(B)$) et la règle n'apprend rien ; lift $> 1$, la présence de $A$ rend $B$ plus probable (corrélation positive) ; lift $< 1$, moins probable (corrélation négative).
- Il est symétrique : $\text{lift}(A \Rightarrow B) = \text{lift}(B \Rightarrow A)$.
- Exemple (exercice 3 du cours) : Coca → HotDogs a une confiance de $2/3$, qui passe le seuil `minConf` $= 2/3$, mais un lift de 1, car $P(\text{HotDogs}) = 2/3$ aussi : la règle est sans intérêt, ce que la [[Confiance (règle d'association)|confiance]] seule ne montrait pas.
- Comme une [[Covariance et corrélation|corrélation]], un lift élevé ne dit rien de la [[Corrélation et causalité|causalité]]. Il se calcule à partir du [[Tableau de contingence|tableau de contingence]] 2 × 2 de $A$ et $B$.

Voir aussi : [[Support (règle d'association)]], [[Règle d'association]].

Résumés : [[2 - association rules]]
