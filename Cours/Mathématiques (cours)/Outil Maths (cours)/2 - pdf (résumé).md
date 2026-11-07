---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre2-Ensemble (4).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du support du professeur Chapitre 2 - Ensembles (PDF) ([[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre2-Ensemble (4).pdf|Chapitre2-Ensemble (4).pdf]]) (26 diapositives, octobre 2023, Outils mathématiques, semestre 1), dans [[Outil Maths (index)]]. C'est la version du professeur du cours déjà résumé dans [[2 - ensembles (résumé)]] ; notions : [[Opérations sur les ensembles]], [[Logique propositionnelle]].

Plan du support : 1. Introduction à la théorie des ensembles ; 2. Ensemble des parties d'un ensemble ; 3. Diagramme de Venn ; 4. Produits cartésiens.

## 1. Introduction à la théorie des ensembles

### Ensemble, appartenance

**Définition.** Un [[Ensemble (mathématiques)|ensemble]] $E$ est une collection ou un groupement d'objets distincts ; ces objets $x$ sont les *éléments* de $E$.
- Si $x$ est un élément de $E$, on dit que $x$ *appartient* à $E$ (ou est dans $E$) : $x \in E$.
- Sinon, $x$ n'appartient pas à $E$ : $x \notin E$.

**Exemples** ([[Ensembles de nombres]]) :
- $\mathbb{N} = \{0, 1, 2, 3, 4, 5, \dots\}$, nombres naturels ;
- $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$, nombres entiers ;
- $\mathbb{Q}$, nombres rationnels (tous ceux qui s'écrivent sous forme de fraction) ;
- $\mathbb{R}$, nombres réels (rationnels et irrationnels) ;
- l'**ensemble vide**, noté $\Phi$ (ou $\emptyset$), qui ne contient aucun élément.

### Définition par compréhension

On définit un ensemble [[Définition par compréhension|par compréhension]] en donnant une propriété $P$ que ses éléments vérifient et sont seuls à vérifier :
$$\{x \in E : P(x)\} \quad \text{ou} \quad \{x \in E \mid P(x)\}.$$

**Exemples.**
- $2\mathbb{N} = \{n \in \mathbb{N} : n \text{ divisible par } 2\}$, les entiers naturels pairs ;
- $2\mathbb{N} + 1 = \{n \in \mathbb{N} : n \text{ non divisible par } 2\}$, les impairs ;
- $\mathbb{Q} = \{x \in \mathbb{R} : x = \frac{p}{q},\ p \in \mathbb{Z},\ q \in \mathbb{N}^*\}$ ;
- $[a, b[\ = \{x \in \mathbb{R} ;\ a \le x < b\}$.

### Inclusion

**Définition.** $E$ est *inclus* dans $F$ (ou $F$ contient $E$, ou $E$ est une *partie* de $F$), noté $E \subset F$, si tout élément de $E$ est élément de $F$ ([[Inclusion (ensembles)]]) :
$$E \subset F \iff \forall x,\ (x \in E \Rightarrow x \in F).$$

**Exemples.** $\{1\} \subset \{1, 4\} \subset \{1, 4, 9\}$ ; $2\mathbb{N} \subset \mathbb{N}$ ; $[a, b[\ \subset \mathbb{R}$.

**Attention : appartenance et inclusion.**
- $0 \in \mathbb{N}$ mais $0 \not\subset \mathbb{N}$ ; en revanche $\{0\} \subset \mathbb{N}$.
- $\{-1, 0, 1\} \subset \mathbb{Z}$ mais $\{-1, 0, 1\} \notin \mathbb{Z}$.
- $\mathbb{N} \subset \mathbb{Z}$ mais $\mathbb{N} \notin \mathbb{Z}$.

Un élément peut appartenir à un ensemble mais pas y être inclus ; un ensemble peut être inclus dans un ensemble mais pas lui appartenir (sauf s'il s'agit d'un ensemble d'ensembles).

**Remarque.** Si $E \subset F$, on dit que $E$ est une *partie* ou un *sous-ensemble* de $F$.

### Méthode : montrer une inclusion

Pour montrer $E \subset F$, on écrit « sans réfléchir » : *Soit $x \in E$. Montrons que $x \in F$.*

**Exemple.** Montrer que $\{x \in \mathbb{R} : \exists y \in \mathbb{R}_+,\ x \ge y\} \subset \mathbb{R}_+$.
*Preuve :* soit $x \in \mathbb{R}$ ; on suppose qu'il existe $y \in \mathbb{R}_+$ avec $x \ge y$. Montrons que $x \in \mathbb{R}_+$. Or $y \ge 0$ par hypothèse et $x \ge y$, donc $x \ge 0$.

### Partie, égalité, double inclusion

**Définition.** Une *partie* de $E$ est tout ensemble $F$ inclus dans $E$. L'ensemble des parties de $E$ se note $\mathcal{P}(E)$.

**Définition (égalité).** $E = F$ si tout élément de $E$ est élément de $F$ et réciproquement :
$$(E = F) \iff (\forall x,\ x \in E \iff x \in F).$$

**Proposition ([[Double inclusion]]).** $E = F$ si et seulement si $E \subset F$ et $F \subset E$ :
$$(E = F) \iff (E \subset F \text{ et } F \subset E).$$

**Méthode.**
- *Inclusion* $E \subset F$ : « Soit $x \in E$. Montrons que $x \in F$. »
- *Égalité* $E = F$ : soit raisonner par équivalence ($x \in E \iff x \in F$), soit par double inclusion, en deux étapes : « Soit $x \in E$. Montrons que $x \in F$. », puis « Soit $x \in F$. Montrons que $x \in E$. »

**Exemple.** Si $E = \{1, 2, 3\}$ :
$$\mathcal{P}(E) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, E\}$$
(8 parties). $x \in E \iff x = 1$ ou $x = 2$ ou $x = 3$ ; $A \in \mathcal{P}(E) \iff A \subset E \iff A = \emptyset$ ou $A = \{1\}$ ou…

### Opérations sur les ensembles

**Intersection.** Pour deux ensembles $A$ et $B$, $A \cap B$ est l'ensemble des éléments qui sont à la fois dans $A$ et dans $B$ ([[Intersection et union d'ensembles]]) :
$$(x \in A \cap B) \iff (x \in A \text{ et } x \in B).$$

![[Chapitre2-Ensemble - p12.jpg]]
*Figure : diagramme de Venn de $A \cap B$, la zone commune aux deux disques.*

**Union.** $A \cup B$ est l'ensemble des éléments qui sont dans $A$ ou dans $B$ :
$$(x \in A \cup B) \iff (x \in A \text{ ou } x \in B).$$

![[Chapitre2-Ensemble - p13.jpg]]
*Figure : diagramme de Venn de $A \cup B$, les deux disques entiers.*

**Famille d'ensembles.** Soit $I$ un ensemble d'indices et $(A_i)_{i \in I}$ une famille d'ensembles.
- Intersection : $\left(x \in \bigcap_{i \in I} A_i\right) \iff (\forall i \in I,\ x \in A_i)$ (éléments qui sont dans **tous** les $A_i$) ;
- Union : $\left(x \in \bigcup_{i \in I} A_i\right) \iff (\exists i \in I,\ x \in A_i)$ (éléments qui sont dans **au moins un** $A_i$).

**Distributivité** (« Définition I » dans le support). Pour trois ensembles $A$, $B$, $C$ :
1. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ ;
2. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ ;
3. $A \cap \left(\bigcup_{i \in I} B_i\right) = \bigcup_{i \in I} (A \cap B_i)$ ;
4. $A \cup \left(\bigcap_{i \in I} B_i\right) = \bigcap_{i \in I} (A \cup B_i)$.

**Différence.** Pour $A$, $B$ deux parties de $E$, la [[Différence d'ensembles|différence]] $A \setminus B$ est l'ensemble des éléments de $A$ qui ne sont pas dans $B$ :
$$(x \in A \setminus B) \iff (x \in A \text{ et } x \notin B).$$

![[Chapitre2-Ensemble - p16.jpg]]
*Figure : $A \setminus B$, la partie de $A$ hors de $B$.*

**Complémentaire.** Pour $A$ partie de $E$, le [[Complémentaire d'un ensemble|complémentaire]] de $A$ dans $E$ est $E \setminus A$, noté $\overline{A}$, $\complement_E(A)$ ou $A^c$ : l'ensemble des éléments de $E$ qui ne sont pas dans $A$.
$$(x \in \overline{A}) \iff (x \notin A).$$

![[Chapitre2-Ensemble - p17.jpg]]
*Figure : $\overline{A}$, la partie de $E$ hors du disque $A$.*

### Propriétés du complémentaire

Soit $A, B \in \mathcal{P}(E)$.
1. $\overline{\overline{A}} = A$ ;
2. $A \cap \overline{A} = \emptyset$ ;
3. $A \cup \overline{A} = E$ ;
4. $A \setminus B = A \cap \overline{B}$ ;
5. $\overline{A \cap B} = \overline{A} \cup \overline{B}$ ;
6. $\overline{A \cup B} = \overline{A} \cap \overline{B}$ (le support écrit $\overline{A} \cup \overline{B}$ : erreur, voir les points à vérifier) ;
7. $\overline{\bigcap_{i \in I} A_i} = \bigcup_{i \in I} \overline{A_i}$ ;
8. $\overline{\bigcup_{i \in I} A_i} = \bigcap_{i \in I} \overline{A_i}$.

Les propriétés 5 à 8 sont les [[Lois de De Morgan]]. Si $A \cap B = \emptyset$, on dit que $A$ et $B$ sont **[[Ensembles disjoints|disjoints]]**.

### Lien entre logique et ensembles

| Logique | Ensembles | Lien |
|---|---|---|
| [[Implication logique\|Implication]] | Inclusion | $(A \subset B) \iff (x \in A \Rightarrow x \in B)$ |
| Conjonction | Intersection | $x \in A \cap B \iff (x \in A \text{ ET } x \in B)$ |
| Disjonction | Union | $x \in A \cup B \iff (x \in A \text{ OU } x \in B)$ |
| Négation | Complémentaire | $x \in \overline{A} \iff x \notin A \iff \text{non}(x \in A)$ |

### Partition

Soit $E$ un ensemble et $(A_i)_{i \in I}$ une famille de parties de $E$. C'est une **[[Partition d'un ensemble|partition]]** de $E$ si :
1. $\forall i \in I$, $A_i \neq \emptyset$ ;
2. $\bigcup_{i \in I} A_i = E$ ;
3. $\forall (i, j) \in I^2$, $i \neq j \Rightarrow A_i \cap A_j = \emptyset$.

## 2. Ensemble des parties d'un ensemble

On peut considérer une collection de sous-ensembles d'un ensemble. Exemple : pour $S = \mathbb{N}$, la collection des sous-ensembles de $\mathbb{N}$ ne contenant que des nombres pairs est bien définie ; c'est un ensemble dont les éléments sont des ensembles :
$$\mathcal{A} = \{A,\ A \subseteq \mathbb{N} ;\ \forall a \in A,\ a \text{ est pair}\}.$$

**Définition.** L'ensemble de tous les sous-ensembles de $E$ est l'**ensemble des parties** de $E$, noté $\mathcal{P}(E)$.

**Attention aux notations.** Si $A$ est un sous-ensemble de $\mathbb{N}$ ne contenant que des pairs, on écrit $A \subseteq \mathbb{N}$ mais $A \in \mathcal{A}$ : $A$ est un sous-ensemble de $\mathbb{N}$, mais un élément de $\mathcal{A}$.

### Ensembles finis, cardinal

**Définition.** $E$ est *fini* s'il est vide ou contient exactement $m$ éléments ($m \in \mathbb{N}$) ; sinon il est *infini*. Le nombre d'éléments d'un ensemble fini est son [[Cardinal d'un ensemble|cardinal]], noté $|E|$.
- Si $A \cap B = \emptyset$ : $|A \cup B| = |A| + |B|$.
- Sinon : $|A \cup B| = |A| + |B| - |A \cap B|$.

## 3. Diagramme de Venn

**Définition.** Un diagramme de Venn est un schéma qui représente des relations logiques entre des ensembles et leurs éléments. On l'utilise en théorie des ensembles, logique, probabilités, informatique et statistiques.

**Exemple.** $E = \{a, b, c, d, e, f, g, h, i, j, k, m, n\}$, $A = \{d, e, f, g, h, i, j\}$, $B = \{f, g, h, i, j, k, m, n\}$, $C = \{a, b, c, d, e, j, k, m, n\}$. Le support n'en donne pas le diagramme (la diapositive s'arrête à l'énoncé des ensembles).

## 4. Produits cartésiens

**Définition.** Soient $E_1, \dots, E_n$ des ensembles. Le [[Produit cartésien|produit cartésien]] $E_1 \times E_2 \times \dots \times E_n$ est l'ensemble des $n$-uplets $(x_1, \dots, x_n)$ où $x_i \in E_i$ pour $i = 1, \dots, n$. Si $E_1 = \dots = E_n = E$, on le note $E^n$.

**$n$-uplet.** Tout élément d'un produit cartésien de $n$ ensembles. Un 2-uplet est un *couple*, un 3-uplet un *triplet*, etc.

**Paires ordonnées.** Pour représenter des points du plan, on utilise deux coordonnées ; $(2, 3)$ et $(3, 2)$ ne sont pas le même point. Pour deux ensembles $A$ et $B$ :
$$A \times B = \{(a, b) \mid a \in A \text{ et } b \in B\}.$$
La définition s'étend à un nombre fini d'ensembles. Exemple : $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$.

## Points à vérifier

1. **De Morgan, propriété 6** (diapositive 18, image ouverte) : le support écrit $\overline{A \cup B} = \overline{A} \cup \overline{B}$. La bonne formule est $\overline{A} \cap \overline{B}$ (complément). Même erreur que dans [[2 - ensembles (résumé)]]. La propriété 8, sur les familles, est correcte.
2. **Proposition d'égalité** (diapositive 9) : « $E \subset F$ et $F \subset F$ » est une coquille, il faut $F \subset E$ (complément).
3. **Exemple d'inclusion** (diapositive 7) : la preuve écrit « On suppose que $\exists y \in \mathbb{R}_+$ » sans écrire la condition $x \ge y$, qu'elle utilise ensuite.
4. **Diagramme de Venn** (diapositive 24) : l'ensemble $B$ est écrit « $\{, f, g, \dots\}$ », avec une virgule en tête (élément manquant ou coquille) ; et l'exemple n'est pas suivi de son diagramme.
5. La distributivité est présentée comme « Définition I » alors qu'il s'agit de propriétés.
6. L'ensemble vide est noté $\Phi$ dans le support, $\emptyset$ dans les propriétés.
