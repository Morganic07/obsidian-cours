---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Outil Maths/Cours/Chapitre 2 ensembles .docx|Chapitre 2 ensembles]], dans [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]] (cours du 19/10/23). Les passages ajoutés finissent par ⓘ.

## Idée générale

Vocabulaire et opérations de la [[Ensemble (mathématiques)|théorie des ensembles]], relié aux connecteurs logiques de [[1 - logique]]. Voir [[Opérations sur les ensembles]].

La note s'ouvre sur la chaîne d'inclusions $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ (voir [[Ensembles de nombres]]). [[Erreurs du cours#^e-2-ensembles|✎]]

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

Un ensemble est déterminé par ses seuls éléments : ni l'ordre ni les répétitions ne comptent, donc $\{1, 2\} = \{2, 1\} = \{1, 1, 2\}$. [[Complément hors du cours|ⓘ]]

L'**ensemble vide** $\emptyset$ est inclus dans tout ensemble $E$ : « $x \in \emptyset \Rightarrow x \in E$ » est vraie pour tout $x$, puisque $x \in \emptyset$ est toujours fausse (une implication à prémisse fausse est vraie, voir [[1 - logique]]). Il est aussi unique : deux ensembles vides sont inclus l'un dans l'autre, donc égaux. Ainsi $\emptyset \subset E$ et $E \subset E$ pour tout $E$. [[Complément hors du cours|ⓘ]]

## Ensemble des parties d'un ensemble

L'ensemble des parties de $E$ se note $\mathcal{P}(E)$ : c'est l'ensemble de tous les sous-ensembles de $E$.

Exemple : si $E = \{1, 2, 3\}$,

$$\mathcal{P}(E) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, E\}$$

- $x \in E \iff x = 1$ ou $x = 2$ ou $x = 3$ ;
- $A \in \mathcal{P}(E) \iff A \subset E \iff A = \emptyset$ ou $A = \{1\}$, …

(Le cours écrit $\Phi$ pour l'ensemble vide.)

**Nombre de parties** : si $E$ a $n$ éléments, $\mathcal{P}(E)$ en a $2^n$ (ici $2^3 = 8$). Former une partie revient à décider, pour chacun des $n$ éléments, s'il y entre ou non : deux choix, $n$ fois, d'où $2 \times 2 \times \cdots \times 2 = 2^n$. Si l'on compte les parties par taille, le nombre de parties à $k$ éléments est le coefficient binomial $\binom{n}{k}$ (ici 1, 3, 3, 1), d'où $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ (voir [[Formule du binôme de Newton]] et [[Combinaison (dénombrement)]]). [[Complément hors du cours|ⓘ]]

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

$$(x \in A \setminus B) \iff (x \in A \text{ et } x \notin B) \qquad A \setminus B = A \cap \overline{B}$$ [[Erreurs du cours#^e-2-ensembles|✎]]

![[Chapitre 2 ensembles - image25.png]]
*Figure : diagramme de Venn, la partie de $A$ hors de $B$ coloriée : $A \setminus B$.*

La différence n'est pas commutative : $A \setminus B \neq B \setminus A$ en général (avec $A = \{1, 2\}$ et $B = \{2, 3\}$ : $A \setminus B = \{1\}$, $B \setminus A = \{3\}$). Leur réunion est la [[Différence symétrique|différence symétrique]], les éléments qui sont dans un seul des deux ensembles : $A \,\Delta\, B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$, ici $\{1, 3\}$. C'est l'analogue ensembliste du [[Ou exclusif|ou exclusif]]. [[Complément hors du cours|ⓘ]]

### Complémentaire

$$(x \in \overline{A}) \iff (x \notin A)$$ [[Erreurs du cours#^e-2-ensembles|✎]]

![[Chapitre 2 ensembles - image26.png]]
*Figure : $A$ inclus dans $E$ ; la zone de $E$ autour de $A$ est $\overline{A}$.*

Notations du complémentaire de $A$ dans $E$ : $\overline{A}$, $\mathrm{C}_E(A)$, $A^c$.

Le complémentaire dépend de l'ensemble de référence $E$ : le complémentaire de $\mathbb{N}$ dans $\mathbb{Z}$ est l'ensemble des entiers strictement négatifs, alors que son complémentaire dans $\mathbb{R}$ contient aussi tous les non-entiers. La notation $\overline{A}$ n'a de sens que si $E$ est fixé sans ambiguïté. [[Complément hors du cours|ⓘ]]

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
6. $\overline{A \cup B} = \overline{A} \cap \overline{B}$ [[Erreurs du cours#^e-2-ensembles|✎]]
7. $\overline{\bigcap_{i \in I} A_i} = \bigcup_{i \in I} \overline{A_i}$
8. $\overline{\bigcup_{i \in I} A_i} = \bigcap_{i \in I} \overline{A_i}$

Les propriétés 5 à 8 sont les [[Lois de De Morgan|lois de De Morgan]]. Si $A \cap B = \emptyset$, on dit que $A$ et $B$ sont **[[Ensembles disjoints|disjoints]]**.

Ces propriétés se démontrent en traduisant chaque opération en connecteur (tableau suivant), puis en appliquant la loi de logique correspondante. Pour la propriété 6 : $x \in \overline{A \cup B} \iff \neg(x \in A \vee x \in B) \iff (x \notin A) \wedge (x \notin B) \iff x \in \overline{A} \cap \overline{B}$, par De Morgan sur les propositions. On retrouve ainsi la formule et l'on voit pourquoi l'union devient une intersection. [[Complément hors du cours|ⓘ]]

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

Autrement dit, chaque élément de $E$ appartient à **un et un seul** $A_i$. Exemples : les pairs $2\mathbb{N}$ et les impairs $2\mathbb{N}+1$ forment une partition de $\mathbb{N}$ ; $\mathbb{R}_-^*$, $\{0\}$, $\mathbb{R}_+^*$ forment une partition de $\mathbb{R}$ ; pour toute partie $A$ de $E$ différente de $\emptyset$ et de $E$, $\{A, \overline{A}\}$ est une partition de $E$. Les classes d'une [[Relation d'équivalence|relation d'équivalence]] (chapitre 3) forment toujours une partition. [[Complément hors du cours|ⓘ]]

## Ensembles d'ensembles

Un ensemble dont les éléments sont aussi des ensembles. Exemple : dans $\mathbb{N}$, la collection des sous-ensembles qui ne contiennent que des nombres pairs :

$$\mathcal{A} = \{A,\ A \subseteq \mathbb{N} ;\ \forall a \in A,\ a \text{ est pair}\}$$

Attention : $A \subseteq \mathbb{N}$ **mais** $A \in \mathcal{A}$, car $A$ est un sous-ensemble de $\mathbb{N}$ mais un élément de $\mathcal{A}$.

Le même piège sépare $\emptyset$ et $\{\emptyset\}$ : le premier n'a aucun élément, le second en a un (l'ensemble vide). Ainsi $\emptyset \in \mathcal{P}(E)$ et $\emptyset \subset \mathcal{P}(E)$ sont vrais tous les deux, et $\mathcal{P}(\emptyset) = \{\emptyset\}$ a un élément ($2^0 = 1$). [[Complément hors du cours|ⓘ]]

On ne peut pas pour autant former n'importe quel « ensemble d'ensembles ». Le [[Paradoxe de Russell|paradoxe de Russell]] (découvert par Bertrand Russell en 1901) considère $R = \{x \mid x \notin x\}$, l'ensemble des ensembles qui ne s'appartiennent pas à eux-mêmes : si $R \in R$, alors par définition $R \notin R$ ; si $R \notin R$, alors $R \in R$. Les deux cas sont contradictoires, donc $R$ n'est pas un ensemble. C'est pourquoi la définition par compréhension prend toujours ses éléments **dans un ensemble déjà connu** ($\{x \in E : P(x)\}$, comme dans ce cours), et pourquoi il n'existe pas d'« ensemble de tous les ensembles ». [[Complément hors du cours|ⓘ]]

## Exemples de familles d'ensembles

### Union : $\bigcup_{n \in \mathbb{N}^*} \left[\frac{1}{n}, 1\right] = \,]0, 1]$

Soit $(A_n)_{n \in \mathbb{N}^*}$ avec $A_n = \left[\frac{1}{n}, 1\right]$.

- Pour tout $n$, $\left[\frac{1}{n}, 1\right] \subset \,]0, 1]$, donc $\bigcup_n A_n \subset \,]0, 1]$.
- Inversement, soit $x \in \,]0, 1]$. On cherche $n \in \mathbb{N}^*$ tel que $x \in \left[\frac{1}{n}, 1\right]$ : $x \in A_n \iff \frac{1}{n} \le x$ (car $x \le 1$) $\iff n \ge \frac{1}{x}$. Il suffit de prendre $n = \left\lfloor \frac{1}{x} \right\rfloor + 1$ (voir [[Partie entière]]). Alors $x \in A_n$, donc $x \in \bigcup_n A_n$.
- D'où l'égalité, par [[Double inclusion|double inclusion]].

Pourquoi ce $n$ convient : la partie entière vérifie $\lfloor y \rfloor \le y < \lfloor y \rfloor + 1$, donc $n = \lfloor \frac{1}{x} \rfloor + 1 > \frac{1}{x}$, d'où $\frac{1}{n} < x$. Et $n \ge 1$ puisque $\frac{1}{x} \ge 1$, donc $n \in \mathbb{N}^*$. Le point $0$ n'est dans aucun $A_n$ (car $\frac{1}{n} > 0$) : l'union de fermés $[\frac{1}{n}, 1]$ donne un intervalle ouvert en $0$. Une union infinie d'intervalles fermés n'est donc pas forcément fermée. [[Complément hors du cours|ⓘ]]

### Intersection : $\bigcap_{n \in \mathbb{N}^*} \left[0, 1 + \frac{1}{n}\right[ = [0, 1]$

Soit $(B_n)_{n \in \mathbb{N}^*}$ avec $B_n = \left[0, 1 + \frac{1}{n}\right[$.

- Pour tout $n$, $[0, 1] \subset B_n$, donc $[0, 1] \subset \bigcap_n B_n$.
- Inversement, soit $x \in \bigcap_n B_n$ : pour tout $n$, $0 \le x < 1 + \frac{1}{n}$. Cette inégalité étant vraie pour tout $n$, on fait tendre $n$ vers $+\infty$ : $0 \le x \le 1$, donc $x \in [0, 1]$.
- D'où l'égalité.

Le passage à la limite transforme l'inégalité stricte $x < 1 + \frac{1}{n}$ en inégalité large $x \le 1$ : une limite ne conserve que les inégalités larges. Sans limite, par l'absurde : si $x > 1$, on choisit $n > \frac{1}{x - 1}$ ; alors $\frac{1}{n} < x - 1$, soit $x > 1 + \frac{1}{n}$, donc $x \notin B_n$. Ici, l'intersection d'intervalles semi-ouverts $[0, 1 + \frac{1}{n}[$ donne un intervalle fermé. [[Complément hors du cours|ⓘ]]

## Cardinal d'un ensemble

- Un ensemble $E$ est **fini** s'il est vide ou s'il contient un nombre fini d'éléments.
- Le [[Cardinal d'un ensemble|cardinal]] de $E$ est son nombre d'éléments, noté $|E|$.

$$|A \cup B| = |A| + |B| - |A \cap B|$$

et si $A \cap B = \emptyset$, alors $|A \cup B| = |A| + |B|$.

Pourquoi on retranche $|A \cap B|$ : dans $|A| + |B|$, les éléments communs sont comptés deux fois, une fois dans $A$ et une fois dans $B$. Pour trois ensembles, la même idée (la **formule du crible**, ou d'inclusion-exclusion) donne $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$ : on ajoute les ensembles, on retire les intersections deux à deux, on rajoute l'intersection triple. Exemple : dans une promotion, 20 étudiants font du sport, 15 de la musique, 5 les deux ; $20 + 15 - 5 = 30$ font au moins l'un des deux. [[Complément hors du cours|ⓘ]]

Autres formules utiles pour $E$, $A$, $B$ finis : $|\overline{A}| = |E| - |A|$ pour $A \subset E$ ; si $A \subset B$, alors $|A| \le |B|$ ; $|A \times B| = |A| \times |B|$ ; $|\mathcal{P}(E)| = 2^{|E|}$. Voir [[Cardinal d'un ensemble]]. [[Complément hors du cours|ⓘ]]

Pour les ensembles infinis, on compare les tailles par des [[Bijection|bijections]] : un ensemble en bijection avec $\mathbb{N}$ est dit [[Ensemble dénombrable|dénombrable]]. $\mathbb{Z}$ et $\mathbb{Q}$ sont dénombrables, $\mathbb{R}$ ne l'est pas (résultats de Georg Cantor, fin du XIXᵉ siècle) : il y a des infinis de tailles différentes. [[Complément hors du cours|ⓘ]]

## Produit cartésien

**Définition.** Soit $E_1, E_2, \dots, E_n$ des ensembles. On appelle [[Produit cartésien|produit cartésien]] des $E_i$, noté $E_1 \times E_2 \times \dots \times E_n$, l'ensemble des $n$-uplets $(x_1, x_2, \dots, x_n)$ où $x_i \in E_i$ pour $i = 1, \dots, n$. Si $E_1 = \dots = E_n = E$, il se note $E^n$.

Exemple : $(x ; y) \in \mathbb{N} \times \mathbb{R}_+$, avec $x$ entier naturel et $y$ réel positif.

Dans un $n$-uplet, contrairement à un ensemble, l'ordre et les répétitions comptent : $(1, 2) \neq (2, 1)$ alors que $\{1, 2\} = \{2, 1\}$, et $(1, 1)$ est un couple valide. Deux couples sont égaux si et seulement si leurs composantes le sont une à une : $(a, b) = (c, d) \iff a = c$ et $b = d$. Par conséquent $A \times B \neq B \times A$ en général. Exemple : $\{1, 2\} \times \{a, b, c\} = \{(1,a), (1,b), (1,c), (2,a), (2,b), (2,c)\}$, qui a $2 \times 3 = 6$ éléments. [[Complément hors du cours|ⓘ]]
