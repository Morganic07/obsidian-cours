---
type: concept
tags: [year1, year2]
aliases: [ensemble des parties, famille d'ensembles, diagramme de Venn, lien entre logique et ensembles, lois de De Morgan pour une famille, power set]
matieres: [Outil Maths, Probability]
sources: ["[[Chapitre 2 ensembles]]", "[[raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre2-Ensemble (4)]]", "[[raw/Year 1/Outil Maths/Exos/TDEnsembles (1).pdf|TDEnsembles (1)]]", "[[raw/Year 1/Contrôles.pdf|Contrôles]]", "[[Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-06
---

Vocabulaire du chapitre sur les ensembles : appartenance ($\in$, pour un élément) et inclusion ($\subset$, pour une partie) ; ensemble des parties $\mathcal{P}(E)$ (power set), qui réunit tous les sous-ensembles de $E$ : $A \in \mathcal{P}(E) \iff A \subset E$, et $\{1, 2, 3\}$ a 8 parties, de $\emptyset$ à $E$ ; égalité par double inclusion. Une famille $(A_i)_{i \in I}$ est indexée par un ensemble d'indices $I$, et le diagramme de Venn schématise les relations entre ensembles.

**Opérations** : [[Intersection et union d'ensembles|intersection, union]], [[Différence d'ensembles|différence]] $A \setminus B = A \cap \overline{B}$, [[Complémentaire d'un ensemble|complémentaire]] $\overline{A}$. Pour une famille $(A_i)_{i \in I}$ : l'intersection contient les $x$ présents dans tous les $A_i$, l'union ceux présents dans au moins un. [[Lois de De Morgan|De Morgan]] : $\overline{A \cap B} = \overline{A} \cup \overline{B}$ et $\overline{A \cup B} = \overline{A} \cap \overline{B}$ (le cours imprime $\cup$ dans la seconde, à tort).

**[[Partition d'un ensemble|Partition]]** de $E$ : parties non vides, d'union $E$, deux à deux disjointes.

**Cardinal** : $|A \cup B| = |A| + |B| - |A \cap B|$. **[[Produit cartésien]]** $E_1 \times \ldots \times E_n$ : ensemble des $n$-uplets.

Correspondance avec la logique, donnée dans un tableau du cours : implication et inclusion, conjonction et intersection, disjonction et union, négation et complémentaire.

Le TD ajoute la [[Différence symétrique|différence symétrique]] $A \Delta B = (A \cup B) \setminus (A \cap B)$, commutative et associative, ainsi que $\mathcal{P}(E \cap F) = \mathcal{P}(E) \cap \mathcal{P}(F)$ et $|\mathcal{P}(E)| = 2^n$ si $E$ a $n$ éléments.

Le DS1 d'Outils math demande de montrer $A \cap C = A \cup B \iff B \subset A \subset C$ et $\mathcal{P}(E) \cup \mathcal{P}(F) \subset \mathcal{P}(E \cup F)$, et porte sur des produits cartésiens ([[Contrôles (résumé)]]).

**En Probability** : le chapitre 1 donne les diagrammes de Venn pour $\cap$, $\cup$, $A^c$ et des ensembles disjoints, puis les lois de De Morgan $(A \cup B)^c = A^c \cap B^c$, $(A \cap B)^c = A^c \cup B^c$ et leur version pour une famille $(A_i)$. Les événements sont des parties de l'espace d'échantillonnage ([[Événement (probabilités)]], [[Espace probabilisé]]).

Liens : [[Logique propositionnelle]], [[Relation d'équivalence]] (les classes forment une partition), [[Image et image réciproque]]

## À vérifier

- [[Chp 1 - Sample space,events, proba]] : les bornes des lois de De Morgan pour une famille ne sont pas visibles dans la transcription.

Résumés : [[Chapitre 2 ensembles (résumé)]], [[Chapitre2-Ensemble (4) (résumé)]], [[TDEnsembles (1) (résumé)]], [[Exo-Chapitre 2 (résumé)]], [[CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022 (résumé)]], [[Contrôles (résumé)]], [[Chp 1 - Sample space,events, proba (résumé)]]
