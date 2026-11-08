---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 1 : Sample space,events, proba.docx|Chp 1 - Sample space,events, proba]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 1 : Sample space,events, proba.docx|Chp 1 - Sample space,events, proba]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les images à formule ou à texte sont recopiées ci-dessous ; les deux figures (diagrammes de Venn, types d'ensembles) sont intégrées.

## Idée générale

Poser le cadre de toute la probabilité : un espace d'issues (*sample space*), des événements (*events*) qui en sont des sous-ensembles, et une fonction $P$ qui les mesure.

Ce cadre axiomatique est dû à Kolmogorov (*Fondements de la théorie des probabilités*, 1933). Le triplet $(S, \mathcal{A}, P)$ — issues, événements, probabilité — s'appelle un **[[Espace probabilisé|espace probabilisé]]** ; en français, on note souvent $\Omega$ l'univers et l'on dit **tribu** pour sigma-algèbre. Les axiomes ne disent pas ce qu'« est » une probabilité : l'interprétation **fréquentiste** y voit la limite de la fréquence d'un événement quand on répète l'expérience (ce que justifie la [[Loi des grands nombres|loi des grands nombres]]), l'interprétation **bayésienne** un degré de croyance. Les deux obéissent aux mêmes règles de calcul. [[Complément hors du cours|ⓘ]]

## Ensembles : cardinal et types

- **Cardinal** (*[[Cardinal d'un ensemble|cardinal of a set]]*) : nombre d'éléments d'un ensemble, noté $|S|$. Si $S = \emptyset$, alors $|S| = 0$.
- Un ensemble est fini ou infini : $S = \{1,2,3\}$ est fini, $S = \{1,2,3,\dots\} = \mathbb{N}$ est infini.
- Un ensemble n'a ni répétition ni ordre : $\{a,b,b,c,c\} = \{a,b,c\} = \{c,b,a\}$.

Tableau du cours (image, recopiée) :

| Propriété | *Finite / Infinite* | *[[Ensemble dénombrable\|Countable]] / Uncountable* | *Discrete / Continuous* |
|---|---|---|---|
| Définition | Nombre fini ou infini d'éléments | Peut-on associer chaque élément à $\mathbb{N}$ ? | Les éléments sont-ils séparés ou forment-ils un continuum ? |
| Exemples de cas finis | $\{1,2,3\}$ (3 éléments) | $\{a,b,c,d\}$ (4 éléments) | $\{1,2,3,4\}$ (espacés) [[Erreurs du cours#^e-1-sample-space-events-proba\|✎]] |
| Exemples de cas infinis | $\mathbb{N}, \mathbb{R}$ | $\mathbb{N}$ (dénombrable), $\mathbb{R}$ (indénombrable) | $\mathbb{R}$ (continu) |
| Exemples discrets | Tous les ensembles finis | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ | $\mathbb{N}$ (espacements fixes) |
| Exemples continus | Jamais | $\mathbb{R}$ est indénombrable | $[0,1]$, $\mathbb{R}$ |

## Définitions : expérience et espace d'échantillonnage

- **Expérience** (*experiment*) : action dont l'issue est incertaine, et qu'on peut répéter dans des conditions identiques ([[Expérience aléatoire]]).
- **Espace d'échantillonnage** (*[[Espace probabilisé|sample space]]*, $S$) : ensemble de toutes les issues possibles d'une expérience. Ses éléments peuvent être des nombres, des lettres, des vecteurs, des fonctions…
- Tout ensemble ne peut pas servir d'espace d'échantillonnage. Il doit être :
  - **exhaustif** (*exhaustive*) : il liste toutes les issues possibles ;
  - **exclusif** (*exclusive*) : il n'y a pas d'éléments répétés.

- Le choix de $S$ dépend de ce qu'on observe, et il conditionne les calculs. Pour deux lancers d'une pièce, $S = \{PP, PF, FP, FF\}$ a 4 issues équiprobables ; si l'on ne note que le nombre de « pile », $S = \{0, 1, 2\}$ convient aussi, mais ses issues ne sont plus équiprobables ($P(\{1\}) = 1/2$). De même, pour deux dés, l'espace des couples $\{1,\dots,6\}^2$ (36 issues équiprobables) est plus commode que celui des sommes $\{2,\dots,12\}$. [[Complément hors du cours|ⓘ]]

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

Chaque opération sur les ensembles traduit une phrase sur les événements : $A \cup B$ se lit « $A$ ou $B$ » (au moins l'un des deux se produit), $A \cap B$ « $A$ et $B$ », $A^c$ « non $A$ », $A \subset B$ « si $A$ se produit, $B$ aussi », $A \cap B = \emptyset$ « $A$ et $B$ ne peuvent pas se produire ensemble » ([[Événements incompatibles|événements incompatibles]]). $S$ est l'**événement certain**, $\emptyset$ l'**événement impossible**. [[Complément hors du cours|ⓘ]]

**[[Lois de De Morgan]]** (*De Morgan's Laws*) :
$$(A \cup B)^c = A^c \cap B^c \qquad (A \cap B)^c = A^c \cup B^c$$

Pour une famille $(A_i)_{i \ge 1}$ (la même chose vaut pour une famille finie, $i = 1, \dots, n$) : [[Erreurs du cours#^e-1-sample-space-events-proba|✎]]
$$(1)\ \Big(\bigcup_{i \ge 1} A_i\Big)^c = \bigcap_{i \ge 1} A_i^c \qquad (2)\ \Big(\bigcap_{i \ge 1} A_i\Big)^c = \bigcup_{i \ge 1} A_i^c$$

## L'espace des événements

- **Espace des événements** (*space of events*) : espace qui contient tous les événements possibles d'une expérience.
- Propriété : si $A$ et $B$ sont des événements de $S$, alors $A \cup B$, $A \cap B$ et $A^C$ sont aussi des événements de $S$.
- Un tel espace s'appelle une **sigma-algèbre** (*sigma algebra of sets*).

**Définition (sigma-algèbre).** Soit $\mathcal{A} \subset \mathcal{P}(\Omega)$. $\mathcal{A}$ est une sigma-algèbre si :
1. $\Omega \in \mathcal{A}$ ;
2. si $B \in \mathcal{A}$, alors $B^c \in \mathcal{A}$ (stabilité par complémentaire) ;
3. si $(B_i)_{i = 1,2,3,\dots}$ est une suite d'éléments de $\mathcal{A}$, alors $\bigcup_i B_i \in \mathcal{A}$ (stabilité par union dénombrable).

Les autres stabilités annoncées s'en déduisent : $\emptyset = \Omega^c \in \mathcal{A}$ ; une union finie $B_1 \cup \dots \cup B_n$ est l'union dénombrable $B_1 \cup \dots \cup B_n \cup \emptyset \cup \emptyset \cup \dots$ ; et l'intersection s'obtient par les lois de De Morgan, $\bigcap_i B_i = \big(\bigcup_i B_i^c\big)^c \in \mathcal{A}$. [[Complément hors du cours|ⓘ]]

Exemples : $\{\emptyset, \Omega\}$ est la plus petite sigma-algèbre (tribu grossière), $\mathcal{P}(\Omega)$ la plus grande ; pour un événement $A$, $\{\emptyset, A, A^c, \Omega\}$ est la plus petite sigma-algèbre qui contient $A$. [[Complément hors du cours|ⓘ]]

- Si $S$ est fini, l'espace des événements est simple : c'est l'ensemble de toutes les parties de $S$, l'**ensemble des parties** (*[[Opérations sur les ensembles|power set]]*), noté $\mathcal{P}(S)$, et $\emptyset \in \mathcal{P}(S)$.
- L'ensemble vide est élément de tout ensemble des parties.
- Si $|S| = n$, alors $|\mathcal{P}(S)| = 2^n$ : former une partie revient à décider, pour chacun des $n$ éléments, s'il y est ou non (voir [[3 - Combinatorics]]). Un dé à 6 faces a donc $2^6 = 64$ événements. [[Complément hors du cours|ⓘ]]
- Pourquoi ne pas toujours prendre $\mathcal{P}(S)$ ? Quand $S$ est indénombrable (comme $[0,1]$), on démontre (théorème de Vitali) qu'il n'existe aucune probabilité définie sur **toutes** les parties de $[0,1[$, respectant les axiomes, qui donne à chaque intervalle sa longueur et soit invariante par translation (modulo 1) ; on se restreint alors à une sigma-algèbre plus petite, la **tribu borélienne** (engendrée par les intervalles), qui contient tous les ensembles utiles en pratique. [[Complément hors du cours|ⓘ]]

## Espaces d'échantillonnage discrets

- $S$ est **discret** s'il contient un nombre fini de points, ou une infinité de points qu'on peut ranger en suite.
- Autrement dit, $S$ est **dénombrable** (*countable*, voir [[Ensemble dénombrable]]).
- Sinon, $S$ est un espace d'échantillonnage **continu** (*continuous sample space*).
- Exemple d'espace discret infini : lancer une pièce jusqu'au premier « pile » et compter les lancers, $S = \{1, 2, 3, \dots\}$. Exemple d'espace continu : la durée de vie d'une ampoule, $S = [0, +\infty[$. [[Complément hors du cours|ⓘ]]
- Pourquoi $\mathbb{R}$ (ou $[0,1]$) est indénombrable : c'est l'**argument diagonal de Cantor** (1891). Si l'on pouvait ranger tous les réels de $[0,1]$ en suite $x_1, x_2, \dots$, on construirait le réel dont la $n$-ième décimale diffère de celle de $x_n$, pour tout $n$ (en évitant les chiffres 0 et 9, à cause des doubles écritures comme $0{,}0999\ldots = 0{,}1$) : il ne serait égal à aucun $x_n$, contradiction. À l'inverse, $\mathbb{Q}$ est dénombrable : c'est le parcours du tableau des fractions $p/q$ de la figure ci-dessous. [[Complément hors du cours|ⓘ]]

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

C'est la **formule de Laplace** (« cas favorables sur cas possibles »). Elle ne vaut que si $S$ est fini et les issues équiprobables : chaque issue a alors la probabilité $1/|S|$, et l'additivité donne la formule. Elle n'a pas d'équivalent sur un ensemble dénombrable infini : il n'existe pas de probabilité uniforme sur $\mathbb{N}$, car des poids tous égaux à $p$ donneraient $\sum_i p = 0$ si $p = 0$, $+\infty$ si $p > 0$, jamais 1. Compter $|A|$ et $|S|$ est l'objet du [[Dénombrement|dénombrement]] ([[3 - Combinatorics]]). [[Complément hors du cours|ⓘ]]

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
8. **Croissance** (*monotonicity*) : si $A \subset B$, alors $P(A) \le P(B)$, et plus précisément $P(B \setminus A) = P(B) - P(A)$. [[Complément hors du cours|ⓘ]]

Ces propriétés se démontrent toutes à partir des axiomes, en découpant en morceaux disjoints : [[Complément hors du cours|ⓘ]]
- 1 : $A$ et $A^c$ sont disjoints et $A \cup A^c = S$, donc $P(A) + P(A^c) = P(S) = 1$ ;
- 2 : appliquer 1 à $A = S$, de complémentaire $\emptyset$ ; 3 : $P(A) = 1 - P(A^c)$ avec $P(A^c) \ge 0$ ;
- 8 : $B = A \cup (B \setminus A)$, union disjointe, donc $P(B) = P(A) + P(B \setminus A) \ge P(A)$ ;
- 4 : $A \cup B = A \cup (B \setminus A)$ et $B = (A \cap B) \cup (B \setminus A)$, deux unions disjointes ; donc $P(A \cup B) = P(A) + P(B \setminus A) = P(A) + P(B) - P(A \cap B)$ ;
- 5 découle de 4 car $P(A \cap B) \ge 0$ ; 6 et 7 s'obtiennent par [[Récurrence|récurrence]] sur $n$ à partir de (ii) et de 5.

La propriété 4 se généralise : c'est la **[[Formule du crible|formule du crible]]** (de Poincaré, ou d'inclusion-exclusion). Pour trois événements : [[Complément hors du cours|ⓘ]]
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$
et pour $n$ événements, on ajoute les probabilités des intersections d'un nombre impair d'événements et on retranche celles d'un nombre pair : [[Complément hors du cours|ⓘ]]
$$P\Big(\bigcup_{i=1}^{n} A_i\Big) = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \le i_1 < \dots < i_k \le n} P(A_{i_1} \cap \dots \cap A_{i_k})$$

Exemple : on tire une carte dans un jeu de 52 ; $A$ = « cœur », $B$ = « figure » (valet, dame, roi). $P(A \cup B) = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} = \frac{11}{26}$ : on retire les trois figures de cœur, comptées deux fois. [[Complément hors du cours|ⓘ]]

Enfin, l'additivité dénombrable (ii\*) donne la **continuité monotone** : si $A_1 \subset A_2 \subset \dots$, alors $P\big(\bigcup_n A_n\big) = \lim_{n \to \infty} P(A_n)$ ; si $A_1 \supset A_2 \supset \dots$, alors $P\big(\bigcap_n A_n\big) = \lim_{n \to \infty} P(A_n)$. C'est elle qui permet de passer à la limite dans les calculs de probabilités. [[Complément hors du cours|ⓘ]]

## Construire une mesure de probabilité

Méthode, pour un espace discret $S = \{\omega_1, \omega_2, \dots, \omega_n, \dots\}$ :

1. À chaque point $\omega_i$, associer un **poids** (*weight*) $p_i$ qui vérifie :
   - $\forall i = 1,2,\dots : p_i \ge 0$ ;
   - $\sum_i p_i = 1$.

   Les poids $p_i$ n'ont pas besoin d'être égaux.
2. Poser $\forall i : P(\omega_i) = p_i$.
3. Pour tout sous-ensemble $A \subset S$ :
$$P(A) = \sum_{\omega_i \in A} P(\omega_i) = \sum_{\omega_i \in A} p_i, \quad \text{qu'on écrit aussi } P(A) = \sum_{\omega \in A} P(\omega)$$

Exemples : [[Complément hors du cours|ⓘ]]
- **Dé truqué** : $S = \{1, \dots, 6\}$, le 6 sort deux fois plus souvent que chacune des autres faces. Poids $p_1 = \dots = p_5 = p$ et $p_6 = 2p$, avec $7p = 1$, donc $p = 1/7$. Alors $P(\text{pair}) = p_2 + p_4 + p_6 = 4/7$, alors que la formule $|A|/|S|$ donnerait à tort $1/2$.
- **Espace infini** : $S = \{1, 2, 3, \dots\}$ (rang du premier « pile » avec une pièce équilibrée), $p_i = 1/2^i$. Les poids conviennent, car $\sum_{i \ge 1} 1/2^i = 1$ (série géométrique). $P(\text{rang pair}) = \sum_{j \ge 1} 1/4^j = \frac{1/4}{1 - 1/4} = 1/3$.

Réciproquement, toute probabilité sur un espace discret est de cette forme : elle est entièrement déterminée par les poids $p_i = P(\{\omega_i\})$ des issues. Sur un espace continu, ce n'est plus possible (chaque issue peut avoir une probabilité nulle) : on passe par une densité, voir [[Variable aléatoire]]. [[Complément hors du cours|ⓘ]]

## Événements nuls et impossibles

- $A$ est **nul** (*null*) si $P(A) = 0$.
- $A$ est **impossible** si $A = \emptyset$. Un événement impossible est donc nul ; la réciproque n'est pas toujours vraie. [[Erreurs du cours#^e-1-sample-space-events-proba|✎]]
- Contre-exemple à la réciproque : on choisit un point « au hasard » dans $[0,1]$, avec $P([a,b]) = b - a$. L'événement « obtenir exactement $1/2$ » n'est pas vide, mais $P(\{1/2\}) = 0$ ; il en va de même pour tout ensemble dénombrable de points, comme $\mathbb{Q} \cap [0,1]$. Sur un espace discret où tous les poids $p_i$ sont strictement positifs, en revanche, seul $\emptyset$ est nul. [[Complément hors du cours|ⓘ]]
- Symétriquement, un événement de probabilité 1 est dit **presque sûr** (*almost sure*) : il peut ne pas se produire, mais avec une probabilité nulle. C'est le sens de « presque sûrement » dans les grands théorèmes, comme la loi forte des grands nombres. [[Complément hors du cours|ⓘ]]
