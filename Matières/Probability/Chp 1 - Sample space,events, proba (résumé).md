---
type: source
tags: [year2]
sources: ["[[Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp 1 - Sample space,events, proba]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les images à formule ou à texte sont recopiées ci-dessous ; les deux figures (diagrammes de Venn, types d'ensembles) sont intégrées.

## Idée générale

Poser le cadre de toute la probabilité : un espace d'issues (*sample space*), des événements (*events*) qui en sont des sous-ensembles, et une fonction $P$ qui les mesure.

## Ensembles : cardinal et types

- **Cardinal** (*[[Cardinal d'un ensemble|cardinal of a set]]*) : nombre d'éléments d'un ensemble, noté $|S|$. Si $S = \emptyset$, alors $|S| = 0$.
- Un ensemble est fini ou infini : $S = \{1,2,3\}$ est fini, $S = \{1,2,3,\dots\} = \mathbb{N}$ est infini.
- Un ensemble n'a ni répétition ni ordre : $\{a,b,b,c,c\} = \{a,b,c\} = \{c,b,a\}$.

Tableau du cours (image, recopiée) :

| Propriété | *Finite / Infinite* | *[[Ensemble dénombrable\|Countable]] / Uncountable* | *Discrete / Continuous* |
|---|---|---|---|
| Définition | Nombre fini ou infini d'éléments | Peut-on associer chaque élément à $\mathbb{N}$ ? | Les éléments sont-ils séparés ou forment-ils un continuum ? |
| Exemples de cas finis | $\{1,2,3\}$ (« 5 éléments », sic) | $\{a,b,c,d\}$ (4 éléments) | $\{1,2,3,4\}$ (espacés) |
| Exemples de cas infinis | $\mathbb{N}, \mathbb{R}$ | $\mathbb{N}$ (dénombrable), $\mathbb{R}$ (indénombrable) | $\mathbb{R}$ (continu) |
| Exemples discrets | Tous les ensembles finis | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ | $\mathbb{N}$ (espacements fixes) |
| Exemples continus | Jamais | $\mathbb{R}$ est indénombrable | $[0,1]$, $\mathbb{R}$ |

## Définitions : expérience et espace d'échantillonnage

- **Expérience** (*experiment*) : action dont l'issue est incertaine, et qu'on peut répéter dans des conditions identiques ([[Expérience aléatoire]]).
- **Espace d'échantillonnage** (*[[Espace probabilisé|sample space]]*, $S$) : ensemble de toutes les issues possibles d'une expérience. Ses éléments peuvent être des nombres, des lettres, des vecteurs, des fonctions…
- Tout ensemble ne peut pas servir d'espace d'échantillonnage. Il doit être :
  - **exhaustif** (*exhaustive*) : il liste toutes les issues possibles ;
  - **exclusif** (*exclusive*) : il n'y a pas d'éléments répétés.

## Événements et théorie des ensembles

- **Événement** (*[[Événement (probabilités)|event]]*) : sous-ensemble de l'espace d'échantillonnage.
- Exemple : lancer un dé, $S = \{1,2,3,4,5,6\}$.
  - « faire 6 » : $A = \{6\}$, **événement simple** (*simple event*) ;
  - « faire un nombre pair » : $A = \{2,4,6\}$, **événement composé** (*compound event*).
- Écriture par propriété : $A = \{x \in S \mid x \text{ satisfait } p_A\}$, où $p_A$ est la proposition qui définit l'événement (ex. « faire un nombre pair »). Si aucun élément de $S$ ne satisfait $p_A$, alors $A = \emptyset$.
- **Complémentaire** (*complementary*) : $A^C$ est formé de tous les points qui ne sont pas dans $A$ ([[Complémentaire d'un ensemble]]) :
$$A^C = \{x \in S \mid x \notin A\} = S \setminus A$$

### Rappels de théorie des ensembles

![[Chp 1 - Sample space,events, proba - image7.png]]
*Figure : diagrammes de Venn dans le rectangle $S$ — $A \cap B$ (intersection grisée), $A \cup B$ (deux cercles grisés), $A^c$ (tout sauf $A$), $A \cap B = \emptyset$ (cercles disjoints).*

Voir [[Intersection et union d'ensembles]] et [[Ensembles disjoints]].

**[[Lois de De Morgan]]** (*De Morgan's Laws*) :
$$(A \cup B)^c = A^c \cap B^c \qquad (A \cap B)^c = A^c \cup B^c$$

Pour une famille $(A_i)$ :
$$(1)\ \Big(\bigcup_{i=1} A_i\Big)^c = \bigcap_{i=1} A_i^c \qquad (2)\ \Big(\bigcap_{i=1} A_i\Big)^c = \bigcup_{i=1} A_i^c$$
(bornes supérieures absentes dans le cours, voir Points à vérifier).

## L'espace des événements

- **Espace des événements** (*space of events*) : espace qui contient tous les événements possibles d'une expérience.
- Propriété : si $A$ et $B$ sont des événements de $S$, alors $A \cup B$, $A \cap B$ et $A^C$ sont aussi des événements de $S$.
- Un tel espace s'appelle une **sigma-algèbre** (*sigma algebra of sets*).

**Définition (sigma-algèbre).** Soit $\mathcal{A} \subset \mathcal{P}(\Omega)$. $\mathcal{A}$ est une sigma-algèbre si :
1. $\Omega \in \mathcal{A}$ ;
2. si $B \in \mathcal{A}$, alors $B^c \in \mathcal{A}$ (stabilité par complémentaire) ;
3. si $(B_i)_{i = 1,2,3,\dots}$ est une suite d'éléments de $\mathcal{A}$, alors $\bigcup_i B_i \in \mathcal{A}$ (stabilité par union dénombrable).

- Si $S$ est fini, l'espace des événements est simple : c'est l'ensemble de toutes les parties de $S$, l'**ensemble des parties** (*[[Opérations sur les ensembles|power set]]*), noté $\mathcal{P}(S)$, et $\emptyset \in \mathcal{P}(S)$.
- L'ensemble vide est élément de tout ensemble des parties.

## Espaces d'échantillonnage discrets

- $S$ est **discret** s'il contient un nombre fini de points, ou une infinité de points qu'on peut ranger en suite.
- Autrement dit, $S$ est **dénombrable** (*countable*, voir [[Ensemble dénombrable]]).
- Sinon, $S$ est un espace d'échantillonnage **continu** (*continuous sample space*).

![[Chp 1 - Sample space,events, proba - image2.png]]
*Figure : trois types d'ensembles — fini (pommes en pyramide), infini dénombrable (les entiers $1, 2, 3, \dots, n, \dots$ et le tableau des fractions $p/q$ qu'on peut parcourir), indénombrable (segment $[0,1]$, demi-droite $[0,\infty[$, carré unité rempli de points).*

## 4) Probabilité d'un événement

- **Cardinal** (*cardinality*) : $|A|$ est le nombre d'éléments de $A$.
- La probabilité est une fonction :
$$P : \text{espace des événements} \to \mathbb{R}, \qquad A \mapsto P(A)$$
- Rappel : si $|S| < \infty$ ($S$ fini), l'espace des événements est l'ensemble des parties de $S$.

### Équiprobabilité

Si l'expérience est [[Équiprobabilité|équiprobable]], toutes les issues ont la même probabilité, et :
$$P(A) = \frac{|A|}{|S|} = \frac{\text{nombre d'issues dans } A}{\text{nombre de toutes les issues possibles}}$$

### Définition d'une probabilité $P$ (axiomes)

1. **(i)** Pour tout $A \subset S$, $P(A) \ge 0$.
2. **(ii) Additivité** : si $A$ et $B$ sont [[Événements incompatibles|disjoints]] (*disjoint events*), $P(A \cup B) = P(A) + P(B)$.
3. **(ii\*) Additivité dénombrable** (*countable additivity*) : pour toute suite infinie d'ensembles disjoints $A_1, A_2, \dots, A_n, \dots$,
$$P\Big(\bigcup_{i=1}^{\infty} A_i\Big) = \sum_{i=1}^{\infty} P(A_i)$$
4. **(iii)** $P(S) = 1$.

### Propriétés d'une probabilité $P$

1. Pour tout événement $A \subset S$ : $P(A) = 1 - P(A^c)$.
2. $P(\emptyset) = 0$.
3. Pour tout $A \subset S$ : $P(A) \le 1$.
4. Pour $A, B \subset S$ : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
5. Pour $A, B \subset S$ : $P(A \cup B) \le P(A) + P(B)$.
6. **Additivité finie** (*finite additivity*) : pour toute famille finie d'ensembles disjoints $A_1, \dots, A_n$,
$$P\Big(\bigcup_{i=1}^{n} A_i\Big) = \sum_{i=1}^{n} P(A_i)$$
7. **Sous-additivité finie** (*finite sub-additivity*) : pour toute famille finie $A_1, \dots, A_n$,
$$P\Big(\bigcup_{i=1}^{n} A_i\Big) \le \sum_{i=1}^{n} P(A_i)$$

## Construire une mesure de probabilité

Méthode, pour un espace discret $S = \{\omega_1, \omega_2, \dots, \omega_n, \dots\}$ :

1. À chaque point $\omega_i$, associer un **poids** (*weight*) $p_i$ qui vérifie :
   - $\forall i = 1,2,\dots : p_i \ge 0$ ;
   - $\sum_i p_i = 1$.

   Les poids $p_i$ n'ont pas besoin d'être égaux.
2. Poser $\forall i : P(\omega_i) = p_i$.
3. Pour tout sous-ensemble $A \subset S$ :
$$P(A) = \sum_{\omega_i \in A} P(\omega_i) = \sum_{\omega_i \in A} p_i, \quad \text{qu'on écrit aussi } P(A) = \sum_{\omega \in A} P(\omega)$$

## Événements nuls et impossibles

- $A$ est **nul** (*null*) si $P(A) = 0$.
- $A$ est **impossible** si $A = \emptyset$ (la note écrit « $P(A) = \emptyset$ », voir Points à vérifier). Un événement impossible est donc nul ; la réciproque n'est pas toujours vraie.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Impossible** : la note écrit « A is impossible if P(A) = ø », ce qui mélange $P(A) = 0$ et $A = \emptyset$. La phrase suivante (« un événement impossible est nul, inverse pas toujours vrai ») n'a de sens que si impossible veut dire $A = \emptyset$ (complément).
2. **Tableau fini / dénombrable** : la transcription note « 5 éléments » pour $\{1,2,3\}$, qui en a 3. Vérifié sur l'image le 2026-11-06 : l'image écrit bien « (5 éléments) ». La coquille est dans le cours et ne touche pas le fond.
3. **Lois de De Morgan en famille** : les bornes des unions et intersections ne sont pas visibles dans la transcription. Vérifié sur l'image le 2026-11-06 : l'image n'écrit que $i=1$, sans borne haute ; il faut comprendre $i = 1, \dots, n$ ou $i \ge 1$ (complément).
4. **Définition de $P$** : le cours donne (ii) et (ii\*) comme deux axiomes. L'additivité finie (ii) découle de (ii\*) avec $P(\emptyset) = 0$ (complément).
5. **Tableau des ensembles** : la colonne *Discrete / Continuous* range $\mathbb{N}$ parmi les exemples « infinis » sans le citer, et la ligne « Exemples continus » de la colonne *Countable* répond « $\mathbb{R}$ est indénombrable » : le tableau mêle les trois notions. À lire avec la définition du cours (discret = dénombrable).
