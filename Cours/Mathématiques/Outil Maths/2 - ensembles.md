---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]], dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]] (cours du 19/10/23). En cas d'écart, le cours et ses images font foi.

## Idée générale

Vocabulaire et opérations de la [[Ensemble (mathématiques)|théorie des ensembles]], relié aux connecteurs logiques de [[1 - logique]]. Voir [[Opérations sur les ensembles]].

La note s'ouvre sur « $N \in Z \in Q \in R$ », à lire $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ (voir « Erreurs du cours » et [[Ensembles de nombres]]).

## Définition par compréhension

[[Définition par compréhension|Un ensemble se définit par une propriété]] $P$ de ses éléments :

$$\{x \in E : P(x)\} \quad \text{ou} \quad \{x \in E \mid P(x)\}$$

Exemples :

- $2\mathbb{N} = \{n \in \mathbb{N} : n \text{ est divisible par } 2\}$, l'ensemble des entiers naturels pairs ;
- $2\mathbb{N}+1 = \{n \in \mathbb{N} : n \text{ n'est pas divisible par } 2\}$, l'ensemble des entiers naturels impairs ;
- $\mathbb{Q} = \{x \in \mathbb{R} : x = \frac{p}{q},\ p \in \mathbb{Z},\ q \in \mathbb{N}^*\}$ ;
- $[a, b[\ = \{x \in \mathbb{R} ;\ a \le x < b\}$ (voir [[Intervalle réel]]).

## Appartenance, inclusion, égalité

- Un **élément appartient** ($\in$) à un ensemble.
- Un **ensemble est inclus** ($\subset$) dans un ensemble. On dit que $\mathbb{N}$ est une **partie** de $\mathbb{Z}$, ou un **sous-ensemble** de $\mathbb{Z}$. Voir [[Inclusion (ensembles)]].
- Donc $0 \in \mathbb{N}$ et $\{0\} \subset \mathbb{N}$.

$$(A \subset B) \iff (x \in A \Rightarrow x \in B)$$

Deux ensembles sont égaux si :

$$(E = F) \iff (\forall x,\ x \in E \iff x \in F) \qquad (E = F) \iff (E \subset F \text{ et } F \subset E)$$

La seconde forme est la [[Double inclusion|double inclusion]].

## Ensemble des parties d'un ensemble

L'ensemble des parties de $E$ se note $\mathcal{P}(E)$ : c'est l'ensemble de tous les sous-ensembles de $E$.

Exemple : si $E = \{1, 2, 3\}$,

$$\mathcal{P}(E) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, E\}$$

- $x \in E \iff x = 1$ ou $x = 2$ ou $x = 3$ ;
- $A \in \mathcal{P}(E) \iff A \subset E \iff A = \emptyset$ ou $A = \{1\}$, …

(Le cours écrit $\Phi$ pour l'ensemble vide.)

## Opérations sur les ensembles

Voir [[Intersection et union d'ensembles]], [[Différence d'ensembles]] et [[Complémentaire d'un ensemble]].

### Intersection

$$(x \in A \cap B) \iff (x \in A \text{ et } x \in B)$$

![[Chapitre 2 ensembles - image11.png]]
*Figure : diagramme de Venn de $A$ et $B$, intersection $A \cap B$ en rose.*

### Union

$$(x \in A \cup B) \iff (x \in A \text{ ou } x \in B)$$

![[Chapitre 2 ensembles - image2.png]]
*Figure : diagramme de Venn, les deux disques entiers en rose : l'union $A \cup B$.*

### Différence

$$(x \in A \setminus B) \iff (x \in A \text{ et } x \notin B) \qquad A \setminus B = A \cap \overline{B}$$

![[Chapitre 2 ensembles - image25.png]]
*Figure : diagramme de Venn, la partie de $A$ hors de $B$ coloriée : $A \setminus B$.*

### Complémentaire

$$(x \in \overline{A}) \iff (x \notin A)$$

![[Chapitre 2 ensembles - image26.png]]
*Figure : $A$ inclus dans $E$ ; la zone de $E$ autour de $A$ est $\overline{A}$.*

Notations du complémentaire de $A$ dans $E$ : $\overline{A}$, $\mathrm{C}_E(A)$, $A^c$.

## Familles d'ensembles

Soit $I$ un ensemble d'indices et $(A_i)_{i \in I}$ une famille d'ensembles.

- **Intersection** : les éléments $x$ qui sont dans tous les $A_i$.
$$\bigcap_{i \in I} A_i = \{x \in E \mid \forall i \in I,\ x \in A_i\}$$
- **Union** : les éléments $x$ qui sont dans au moins un $A_i$.
$$\bigcup_{i \in I} A_i = \{x \in E \mid \exists i \in I,\ x \in A_i\}$$

### Distributivité de l'intersection et de l'union

1. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
2. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
3. $A \cap \left(\bigcup_{i \in I} B_i\right) = \bigcup_{i \in I} (A \cap B_i)$
4. $A \cup \left(\bigcap_{i \in I} B_i\right) = \bigcap_{i \in I} (A \cup B_i)$

## Propriétés du complémentaire

Soit $A, B \in \mathcal{P}(E)$.

1. $\overline{\overline{A}} = A$
2. $A \cap \overline{A} = \emptyset$
3. $A \cup \overline{A} = E$
4. $A \setminus B = A \cap \overline{B}$
5. $\overline{A \cap B} = \overline{A} \cup \overline{B}$
6. Le cours écrit $\overline{A \cup B} = \overline{A} \cup \overline{B}$ ; la formule juste est $\overline{A \cup B} = \overline{A} \cap \overline{B}$ (voir « Erreurs du cours »).
7. $\overline{\bigcap_{i \in I} A_i} = \bigcup_{i \in I} \overline{A_i}$
8. $\overline{\bigcup_{i \in I} A_i} = \bigcap_{i \in I} \overline{A_i}$

Les propriétés 5 à 8 sont les [[Lois de De Morgan|lois de De Morgan]]. Si $A \cap B = \emptyset$, on dit que $A$ et $B$ sont **[[Ensembles disjoints|disjoints]]**.

## Logique et ensembles

| Logique | Ensembles | Lien |
|---|---|---|
| [[Implication logique\|Implication]] | Inclusion | $(A \subset B) \iff (x \in A \Rightarrow x \in B)$ |
| Conjonction | Intersection | $x \in A \cap B \iff (x \in A \text{ ET } x \in B)$ |
| Disjonction | Union | $x \in A \cup B \iff (x \in A \text{ OU } x \in B)$ |
| Négation | Complémentaire | $x \in \overline{A} \iff x \notin A \iff \text{non}(x \in A)$ |

## Partitions

Soit $E$ un ensemble et $(A_i)_{i \in I}$ une famille de parties de $E$. C'est une [[Partition d'un ensemble|partition de $E$]] si :

1. $\forall i \in I,\ A_i \neq \emptyset$ ;
2. $\bigcup_{i \in I} A_i = E$ ;
3. $\forall (i,j) \in I^2,\ i \neq j \Rightarrow A_i \cap A_j = \emptyset$.

Annotation de l'étudiante : « en gros c pas possible que 2 ensembles aient le mm élément ».

## Ensembles d'ensembles

Un ensemble dont les éléments sont aussi des ensembles. Exemple : dans $\mathbb{N}$, la collection des sous-ensembles qui ne contiennent que des nombres pairs :

$$\mathcal{A} = \{A,\ A \subseteq \mathbb{N} ;\ \forall a \in A,\ a \text{ est pair}\}$$

Attention : $A \subseteq \mathbb{N}$ **mais** $A \in \mathcal{A}$, car $A$ est un sous-ensemble de $\mathbb{N}$ mais un élément de $\mathcal{A}$.

## Exemples de familles d'ensembles

### Union : $\bigcup_{n \in \mathbb{N}^*} \left[\frac{1}{n}, 1\right] = \,]0, 1]$

Soit $(A_n)_{n \in \mathbb{N}^*}$ avec $A_n = \left[\frac{1}{n}, 1\right]$.

- Pour tout $n$, $\left[\frac{1}{n}, 1\right] \subset \,]0, 1]$, donc $\bigcup_n A_n \subset \,]0, 1]$.
- Inversement, soit $x \in \,]0, 1]$. On cherche $n \in \mathbb{N}^*$ tel que $x \in \left[\frac{1}{n}, 1\right]$ : $x \in A_n \iff \frac{1}{n} \le x$ (car $x \le 1$) $\iff n \ge \frac{1}{x}$. Il suffit de prendre $n = \left\lfloor \frac{1}{x} \right\rfloor + 1$ (voir [[Partie entière]]). Alors $x \in A_n$, donc $x \in \bigcup_n A_n$.
- D'où l'égalité, par [[Double inclusion|double inclusion]].

### Intersection : $\bigcap_{n \in \mathbb{N}^*} \left[0, 1 + \frac{1}{n}\right[ = [0, 1]$

Soit $(B_n)_{n \in \mathbb{N}^*}$ avec $B_n = \left[0, 1 + \frac{1}{n}\right[$.

- Pour tout $n$, $[0, 1] \subset B_n$, donc $[0, 1] \subset \bigcap_n B_n$.
- Inversement, soit $x \in \bigcap_n B_n$ : pour tout $n$, $0 \le x < 1 + \frac{1}{n}$. Cette inégalité étant vraie pour tout $n$, on fait tendre $n$ vers $+\infty$ : $0 \le x \le 1$, donc $x \in [0, 1]$.
- D'où l'égalité.

## Cardinal d'un ensemble

- Un ensemble $E$ est **fini** s'il est vide ou s'il contient un nombre fini d'éléments.
- Le [[Cardinal d'un ensemble|cardinal]] de $E$ est son nombre d'éléments, noté $|E|$.

$$|A \cup B| = |A| + |B| - |A \cap B|$$

et si $A \cap B = \emptyset$, alors $|A \cup B| = |A| + |B|$.

## Produit cartésien

**Définition.** Soit $E_1, E_2, \dots, E_n$ des ensembles. On appelle [[Produit cartésien|produit cartésien]] des $E_i$, noté $E_1 \times E_2 \times \dots \times E_n$, l'ensemble des $n$-uplets $(x_1, x_2, \dots, x_n)$ où $x_i \in E_i$ pour $i = 1, \dots, n$. Si $E_1 = \dots = E_n = E$, il se note $E^n$.

Exemple : $(x ; y) \in \mathbb{N} \times \mathbb{R}_+$, avec $x$ entier naturel et $y$ réel positif.

## Erreurs du cours

- [[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]] écrit, propriété 6, « $\overline{A \cup B} = \overline{A} \cup \overline{B}$ » (vérifié sur l'image) ; il faut « $\overline{A \cup B} = \overline{A} \cap \overline{B}$ » (loi de De Morgan). La propriété 8, sur les familles, est juste.
- [[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]] écrit « N ∈ Z ∈ Q ∈ R » ; il faut « $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ » (inclusion, pas appartenance).
- [[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]] écrit « $(x \in A \text{ et } xB)$ » et « $(x \in \overline{A}) \Leftrightarrow (xA)$ » (vérifié sur les images : le symbole manque) ; il faut « $x \notin B$ » et « $x \notin A$ ».
