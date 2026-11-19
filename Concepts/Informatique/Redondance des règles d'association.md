---
type: concept
tags: [year4]
aliases: [redondance simple, redondance stricte, règle redondante, simple redundancy, strict redundancy]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : approches descendantes (*top-down*) de génération des [[Règle d'association|règles d'association]] à partir des [[Itemset fréquent|itemsets fréquents]].

- **Redondance simple** : pour un itemset fréquent donné, on teste d'abord les règles qui ont le moins de conditions à gauche. Pour $R_1 : A \Rightarrow B, C$ et $R_2 : A, B \Rightarrow C$, $\text{confidence}(R_1) = \text{support}(ABC)/\text{support}(A)$ et $\text{confidence}(R_2) = \text{support}(ABC)/\text{support}(AB)$, donc $\text{confidence}(R_2) \geq \text{confidence}(R_1)$. [[Erreurs du cours#^e-redondance-des-regles-d-association|✎]]
- **Redondance stricte** : on commence par les itemsets les plus longs. Pour $R_1 : A \Rightarrow B, C, D$ et $R_2 : A \Rightarrow B, C$, $\text{confidence}(R_1) = \text{support}(ABCD)/\text{support}(A)$ et $\text{confidence}(R_2) = \text{support}(ABC)/\text{support}(A)$, donc $\text{confidence}(R_2) \geq \text{confidence}(R_1)$. [[Erreurs du cours#^e-redondance-des-regles-d-association|✎]]

## Compléments (complément, hors du cours)

- Les deux inégalités viennent de l'anti-monotonie du [[Support (règle d'association)|support]] ([[Propriété de fermeture descendante]]) ; l'égalité est possible quand les supports comparés sont égaux.
- **Usage optimiste** : si la règle la plus générale passe le seuil `minConf` ($A \Rightarrow BC$, ou $A \Rightarrow BCD$), les règles plus spécifiques passent aussi et n'ont pas à être testées ; elles sont dites redondantes. Rentable quand `minConf` est bas.
- **Usage pessimiste** : par [[Preuve par contraposition|contraposition]], si la règle la plus spécifique échoue ($AB \Rightarrow C$, ou $A \Rightarrow BC$), les plus générales échouent aussi. Rentable quand `minConf` est haut.
- Dans l'exercice 1 du cours (14 règles possibles), la stratégie optimiste fait 8 tests (stricte) ou 11 (simple) à `minConf` $= 0{,}5$, et n'en économise aucun à `minConf` $= 1$.

Voir aussi : [[Confiance (règle d'association)]], [[Algorithme Apriori]].

Résumés : [[2 - association rules]]
