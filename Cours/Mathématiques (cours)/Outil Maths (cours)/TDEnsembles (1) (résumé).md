---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Exos/TDEnsembles (1).pdf|TDEnsembles (1).pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du corrigé TD Ensembles (PDF) ([[Raw/Year 1/Outil Maths/Exos/TDEnsembles (1).pdf|TDEnsembles (1).pdf]]) (36 diapositives, « TD Algèbre — Ensemble », CY Tech, premier semestre 2022), dans [[Outil Maths (index)]]. 13 exercices avec solutions rédigées, recopiées ici dans l'ordre. L'énoncé seul est résumé dans [[Exo-Chapitre 2 (résumé)]]. Cours associé : [[chp 2 - ensembles (résumé)]], [[Opérations sur les ensembles]], [[Logique propositionnelle]].

Le document ne contient aucune figure : uniquement du texte et des formules.

## Vue d'ensemble

| Exercice | Thème | Méthode |
|---|---|---|
| 2.1 | Caractérisations de $A \subset B$ : $A \cup B = B$, $A^c \cup B = E$, puis $A \cap B = A$ et $A \cap B^c = \emptyset$ | Double implication, double inclusion ; les deux dernières se déduisent par De Morgan et contraposition |
| 2.2 | Distributivité ; $A \cup B = A \cap C \iff B \subset A \subset C$ ; identité symétrique à trois ensembles | Raisonnement par équivalences sur les éléments, puis distributivités successives |
| 2.3 | $A \cup B \subset A \cup C$ et $A \cap B \subset A \cap C \Rightarrow B \subset C$ ; si $\cap$ et $\cup$ coïncident, alors $B = C$ | Disjonction de cas ($x \in A$ ou $x \in C$) |
| 2.4 | $A \cap B = A \cup B \iff A = B$ ; $A \cap B = A \cap C \iff A \cap B^c = A \cap C^c$ ; $(A \cup B) \setminus (A \cup C) \subset A \cup (B \setminus C)$ | Absurde pour la seconde ; contre-exemple $A = B = C$ non vide pour l'inclusion réciproque |
| 2.5 | Produit cartésien $A \times B$ (20 couples) et nombre de parties : $2^{20}$ | $\lvert\mathcal{P}(E)\rvert = 2^n$ |
| 2.6 | Comparer $\mathcal{P}(E \cup F)$ et $\mathcal{P}(E) \cup \mathcal{P}(F)$ ; $\mathcal{P}(E \cap F)$ et $\mathcal{P}(E) \cap \mathcal{P}(F)$ ; $\mathcal{P}(E \times F)$ et $\mathcal{P}(E) \times \mathcal{P}(F)$ | Inclusion $\mathcal{P}(E) \cup \mathcal{P}(F) \subset \mathcal{P}(E \cup F)$, stricte en général (contre-exemple $E = \{a,b\}$, $F = \{c,d\}$) ; égalité pour l'intersection ; aucune inclusion pour le produit (objets de nature différente) |
| 2.7 | $(A \times C) \cup (B \times C) = (A \cup B) \times C$ ; intersection de deux produits | Équivalences sur les couples $(x, y)$ |
| 2.8 | Toute partie de $E \times F$ est-elle de la forme $A \times B$ ? Non | Contre-exemple : le cercle unité, par l'absurde avec $(0,1)$, $(1,0)$, donc $(0,0)$ |
| 2.9 | Si $E = A_i \cup B_i$ pour tout $i$, alors $E = (\bigcup A_i) \cup (\bigcap B_i)$ | Double inclusion ; si $x \notin \bigcap B_i$, il existe $i$ avec $x \notin B_i$, donc $x \in A_i$ |
| 2.10 | Simplifier 4 expressions (résultats : $A \cap B$, $A \cup B$, $A \cap B \cap C$, $A \cup B \cup C$) | Distributivité, $A \cap A^c = \emptyset$, $A \cup A^c = E$ |
| 2.11 | $(A \setminus B) \setminus C = A \setminus (B \cup C)$ ; $(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D)$ | Passer par $A \setminus B = A \cap B^c$ puis De Morgan |
| 2.12 | $A \setminus (B \cap C)$ et $A \setminus (B \cup C)$ | Idem |
| 2.13 | [[Différence symétrique]] $\Delta$ : commutative, associative, distributivité de $\cap$ sur $\Delta$ ; $A \Delta \emptyset = A$, $A \Delta A = \emptyset$, $A \Delta B = B \setminus A$ si $A \subset B$ | Forme $(A \cup B) \setminus (A \cap B)$ ou $(A \setminus B) \cup (B \setminus A)$ |

## Exercice 2.1 — Caractérisations de l'inclusion

**Énoncé.** Soient $A$ et $B$ deux parties d'un ensemble $E$. Montrer
$$A \subset B \iff A \cup B = B \qquad\text{et}\qquad A \subset B \iff A^c \cup B = E.$$
En déduire
$$A \subset B \iff A \cap B = A \qquad\text{et}\qquad A \subset B \iff A \cap B^c = \emptyset.$$

**Correction.**

1. $A \subset B \iff A \cup B = B$, par double implication.
   - $\Rightarrow$ : on suppose $A \subset B$ et on raisonne par [[Double inclusion|double inclusion]]. Clairement $B \subset A \cup B$. Réciproquement, $x \in A \cup B \iff x \in A \subset B$ ou $x \in B$, donc $x \in B$ : $A \cup B \subset B$.
   - $\Leftarrow$ : si $A \cup B = B$, alors $A \subset A \cup B = B$.
2. $A \subset B \iff A^c \cup B = E$.
   - $\Rightarrow$ : clairement $A^c \cup B \subset E$. Comme $A \subset B$ : $E = A \cup A^c \subset B \cup A^c = A^c \cup B$.
   - $\Leftarrow$ : on a $A \subset E = A^c \cup B$, donc pour $x \in A$ : $x \in A^c$ ou $x \in B$. Comme $x \in A$, $x \notin A^c$, donc $x \in B$.
3. Déduction de $A \subset B \iff A \cap B = A$ :
$$A = A \cap B \underset{\text{De Morgan}}{\iff} A^c = A^c \cup B^c \underset{\text{question 1}}{\iff} B^c \subset A^c \underset{\text{contraposition}}{\iff} A \subset B.$$
4. Déduction de $A \subset B \iff A \cap B^c = \emptyset$ :
$$A \cap B^c = \emptyset \underset{\text{De Morgan}}{\iff} A^c \cup B = \emptyset^c = E \underset{\text{question 2}}{\iff} A \subset B.$$

Voir [[Lois de De Morgan]], [[Preuve par contraposition]], [[Inclusion (ensembles)]].

## Exercice 2.2 — Distributivité et identités à trois ensembles

**Énoncé.** Soient $A, B, C$ trois ensembles. Montrer que
1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ ;
2. $A \cup B = A \cap C \iff B \subset A \subset C$ ;
3. $(A \cup B) \cap (B \cup C) \cap (C \cup A) = (A \cap B) \cup (B \cap C) \cup (C \cap A)$.

**Correction.**

1. Chaîne d'équivalences :
$$\begin{aligned}
x \in A \cup (B \cap C) &\iff x \in A \text{ ou } (x \in B \text{ et } x \in C)\\
&\iff (x \in A \text{ ou } x \in B) \text{ et } (x \in A \text{ ou } x \in C) \quad\text{(distributivité de « ou » sur « et »)}\\
&\iff x \in A \cup B \text{ et } x \in A \cup C \iff x \in (A \cup B) \cap (A \cup C).
\end{aligned}$$
2. Double implication.
   - $\Rightarrow$ : si $A \cup B = A \cap C$ : $x \in B \Rightarrow x \in A \cup B = A \cap C \Rightarrow x \in A$, donc $B \subset A$ ; $x \in A \Rightarrow x \in A \cup B = A \cap C \Rightarrow x \in C$, donc $A \subset C$.
   - $\Leftarrow$ : $B \subset A \Rightarrow A \cup B = A$ et $A \subset C \Rightarrow A \cap C = A$, d'où $A \cup B = A = A \cap C$.
3. Par distributivités successives :
$$\begin{aligned}
(A \cup B) \cap (B \cup C) \cap (C \cup A) &= (B \cup A) \cap (B \cup C) \cap (C \cup A)\\
&= [B \cup (A \cap C)] \cap (C \cup A) \quad (\cup \text{ sur } \cap)\\
&= [B \cap (C \cup A)] \cup [(A \cap C) \cap (C \cup A)] \quad (\cap \text{ sur } \cup)\\
&= [(B \cap C) \cup (B \cap A)] \cup [(A \cap C) \cap (C \cup A)].
\end{aligned}$$
Or $A \cap C \subset C \cup A$, donc $(A \cap C) \cap (C \cup A) = A \cap C$, et on obtient $(A \cap B) \cup (B \cap C) \cup (C \cap A)$.

## Exercice 2.3 — Simplification par $A$

**Énoncé.** Soient $A, B, C$ trois ensembles.
1. Montrer que $\begin{cases} A \cup B \subset A \cup C \\ A \cap B \subset A \cap C \end{cases} \Longrightarrow B \subset C$.
2. On suppose $A \cap B = A \cap C$ et $A \cup B = A \cup C$. Que peut-on dire de $B$ et $C$ ?

**Correction.**

1. Soit $x \in B$. Alors $x \in A \cup B \subset A \cup C$, donc $x \in A$ ou $x \in C$ ([[Raisonnement par disjonction des cas|disjonction de cas]]) :
   - si $x \in C$, rien à prouver ;
   - si $x \in A$, alors $x \in A \cap B \subset A \cap C$, donc $x \in C$.

   Ainsi $B \subset C$.
2. **$B = C$**, par double inclusion. Soit $x \in B$, donc $x \in A \cup B$.
   - Si $x \in A$ : $x \in A \cap B = A \cap C \subset C$.
   - Si $x \notin A$ : comme $x \in A \cup B = A \cup C$, nécessairement $x \in C$.

   Donc $B \subset C$ ; en échangeant les rôles de $B$ et $C$, $C \subset B$.

## Exercice 2.4

**Énoncé.** Soient $A, B, C$ trois parties d'un ensemble $E$.
1. Montrer que $A \cap B = A \cup B \iff A = B$.
2. Montrer que $A \cap B = A \cap C \iff A \cap B^c = A \cap C^c$.
3. Montrer que $(A \cup B) \setminus (A \cup C) \subset A \cup (B \setminus C)$. Donner un contre-exemple pour l'inclusion contraire.

**Correction.**

1. Double implication.
   - $\Rightarrow$ : $x \in A \Rightarrow x \in A \cup B = A \cap B \Rightarrow x \in B$, donc $A \subset B$ ; de même $B \subset A$.
   - $\Leftarrow$ : si $A = B$, $A \cap B = A \cap A = A = A \cup A = A \cup B$.
2. Double implication.
   - $\Rightarrow$ : montrons $A \cap B^c \subset A \cap C^c$. Soit $x \in A \cap B^c$ ; comme $x \in A$, il suffit de montrer $x \in C^c$. [[Raisonnement par l'absurde|Par l'absurde]] : si $x \in C$, alors $x \in A \cap C = A \cap B$, donc $x \in B$, absurde. En échangeant $B$ et $C$, $A \cap C^c \subset A \cap B^c$.
   - $\Leftarrow$ : on applique le sens direct aux complémentaires : $A \cap B^c = A \cap C^c \Rightarrow A \cap (B^c)^c = A \cap (C^c)^c \iff A \cap B = A \cap C$.
3. Soit $x \in (A \cup B) \setminus (A \cup C)$ : $x \in A \cup B$ et $x \notin A \cup C$. En particulier $x \notin A$, donc $x \in B$ ; et $x \notin C$, donc $x \in B \setminus C \subset A \cup (B \setminus C)$.

   **Contre-exemple** pour l'inclusion contraire : $A = B = C$ non vide. Alors $(A \cup B) \setminus (A \cup C) = A \setminus A = \emptyset$ et $A \cup (B \setminus C) = A \cup \emptyset = A$, et $A \not\subset \emptyset$. Voir [[Preuve par contre-exemple]].

## Exercice 2.5 — Produit cartésien et nombre de parties

**Énoncé.** Soient $A = \{a_1, a_2, a_3, a_4\}$ et $B = \{b_1, b_2, b_3, b_4, b_5\}$.
1. Écrire le [[Produit cartésien|produit cartésien]] $A \times B$.
2. Quel est le nombre de parties de $A \times B$ ?

**Correction.**

1. $A \times B = \{(a_i, b_j) : 1 \le i \le 4,\ 1 \le j \le 5\}$, soit les 20 couples :

| | $b_1$ | $b_2$ | $b_3$ | $b_4$ | $b_5$ |
|---|---|---|---|---|---|
| $a_1$ | $(a_1, b_1)$ | $(a_1, b_2)$ | $(a_1, b_3)$ | $(a_1, b_4)$ | $(a_1, b_5)$ |
| $a_2$ | $(a_2, b_1)$ | $(a_2, b_2)$ | $(a_2, b_3)$ | $(a_2, b_4)$ | $(a_2, b_5)$ |
| $a_3$ | $(a_3, b_1)$ | $(a_3, b_2)$ | $(a_3, b_3)$ | $(a_3, b_4)$ | $(a_3, b_5)$ |
| $a_4$ | $(a_4, b_1)$ | $(a_4, b_2)$ | $(a_4, b_3)$ | $(a_4, b_4)$ | $(a_4, b_5)$ |

2. **Proposition** : soit $E$ un ensemble à $n$ éléments ; l'ensemble $\mathcal{P}(E)$ des parties de $E$ est fini et a $2^n$ éléments. $A \times B$ a 20 éléments, il y a donc $2^{20}$ parties. Voir [[Cardinal d'un ensemble]].

## Exercice 2.6 — Ensembles des parties

**Énoncé.** Soient $E$ et $F$ deux ensembles. Quelle relation y a-t-il entre :
1. $\mathcal{P}(E \cup F)$ et $\mathcal{P}(E) \cup \mathcal{P}(F)$ ?
2. $\mathcal{P}(E \cap F)$ et $\mathcal{P}(E) \cap \mathcal{P}(F)$ ?
3. $\mathcal{P}(E \times F)$ et $\mathcal{P}(E) \times \mathcal{P}(F)$ ?

**Correction.**

1. $\mathcal{P}(E) \cup \mathcal{P}(F) \subset \mathcal{P}(E \cup F)$ :
$$A \in \mathcal{P}(E) \cup \mathcal{P}(F) \Rightarrow A \subset E \text{ ou } A \subset F \Rightarrow A \subset E \cup F \Rightarrow A \in \mathcal{P}(E \cup F).$$
Selon le corrigé, ce n'est une égalité que si $E \subset F$ ou $F \subset E$. Exemple : $E = \{a, b\}$, $F = \{c, d\}$ ; alors $E \cup F = \{a, b, c, d\} \notin \mathcal{P}(E) \cup \mathcal{P}(F)$.
2. **Égalité** $\mathcal{P}(E \cap F) = \mathcal{P}(E) \cap \mathcal{P}(F)$ :
$$A \in \mathcal{P}(E) \cap \mathcal{P}(F) \iff A \subset E \text{ et } A \subset F \iff A \subset E \cap F \iff A \in \mathcal{P}(E \cap F).$$
3. **Aucune inclusion** : un élément de $\mathcal{P}(E) \times \mathcal{P}(F)$ est un couple $(A, B)$ avec $A \subset E$ et $B \subset F$, alors qu'un élément de $\mathcal{P}(E \times F)$ est un sous-ensemble $C \subset E \times F$, c'est-à-dire un ensemble de couples $(x, y)$ avec $x \in E$, $y \in F$. Les deux ensembles ne contiennent pas les mêmes objets, ils ne sont pas comparables.

## Exercice 2.7 — Produits cartésiens et opérations

**Énoncé.** Soient $A, B, C, D$ quatre ensembles.
1. Montrer que $(A \times C) \cup (B \times C) = (A \cup B) \times C$.
2. Montrer que $(A \times C) \cap (B \times D) = (A \cap B) \times (C \cap D)$.

**Correction.**

1.
$$\begin{aligned}
(x, y) \in (A \times C) \cup (B \times C) &\iff (x \in A \text{ et } y \in C) \text{ ou } (x \in B \text{ et } y \in C)\\
&\iff (x \in A \text{ ou } x \in B) \text{ et } y \in C \iff (x, y) \in (A \cup B) \times C.
\end{aligned}$$
2. Le corrigé démontre la formule écrite avec d'autres lettres, $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$ :
$$\begin{aligned}
(x, y) \in (A \times B) \cap (C \times D) &\iff (x \in A \text{ et } y \in B) \text{ et } (x \in C \text{ et } y \in D)\\
&\iff (x \in A \cap C) \text{ et } (y \in B \cap D) \iff (x, y) \in (A \cap C) \times (B \cap D).
\end{aligned}$$

## Exercice 2.8 — Parties de $E \times F$

**Énoncé.** Soient $E$ et $F$ deux ensembles. Tous les sous-ensembles de $E \times F$ sont-ils de la forme $A \times B$ avec $A \subset E$ et $B \subset F$ ?

**Correction.** **Non.** Soit $E = F = \mathbb{R}$ et le cercle unité $C = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$. Par l'absurde, supposons $C = A \times B$. Alors $0 \in A$ car $(0, 1) \in C$, et $0 \in B$ car $(1, 0) \in C$, donc $(0, 0) \in A \times B = C$. Or $(0, 0) \notin C$ : contradiction.

## Exercice 2.9 — Familles de parties

**Énoncé.** Soient $(A_i)_{i \in I}$ et $(B_i)_{i \in I}$ deux familles de parties de $E$, avec $E = A_i \cup B_i$ pour tout $i \in I$. Montrer que
$$E = \Big(\bigcup_{i \in I} A_i\Big) \cup \Big(\bigcap_{i \in I} B_i\Big).$$

**Correction.** Notons $F$ le membre de droite ; double inclusion.
- $F \subset E$ : immédiat, ce sont des parties de $E$.
- $E \subset F$ : soit $x \in E = \big(\bigcap B_i\big) \cup \big(\bigcap B_i\big)^c$. Si $x \in \bigcap B_i$, alors $x \in F$. Sinon, il existe $i \in I$ tel que $x \notin B_i$ ; or $E = A_i \cup B_i$, donc $x \in A_i \subset \bigcup A_i$, et $x \in F$.

## Exercice 2.10 — Simplifications

**Énoncé.** Simplifier, pour $A, B, C$ parties de $E$ : $A \cap (A^c \cup B)$ ; $A \cup (A^c \cap B)$ ; $A \cap (A^c \cup B) \cap (A^c \cup B^c \cup C)$ ; $A \cup (A^c \cap B) \cup (A^c \cap B^c \cap C)$.

**Correction.**
- $A \cap (A^c \cup B) = (A \cap A^c) \cup (A \cap B) = \emptyset \cup (A \cap B) = A \cap B$.
- $A \cup (A^c \cap B) = (A \cup A^c) \cap (A \cup B) = E \cap (A \cup B) = A \cup B$.
- $A \cap (A^c \cup B) \cap (A^c \cup B^c \cup C) = (A \cap B) \cap (A^c \cup B^c \cup C) = (A \cap B \cap A^c) \cup (A \cap B \cap B^c) \cup (A \cap B \cap C) = A \cap B \cap C$.
- $A \cup (A^c \cap B) \cup (A^c \cap B^c \cap C) = (A \cup B) \cup (A^c \cap B^c \cap C) = (A \cup B \cup A^c) \cap (A \cup B \cup B^c) \cap (A \cup B \cup C) = E \cap E \cap (A \cup B \cup C) = A \cup B \cup C$.

## Exercice 2.11 — Différences

**Énoncé.** Soient $A, B, C, D$ des parties de $E$. Montrer que
1. $(A \setminus B) \setminus C = A \setminus (B \cup C)$ ;
2. $(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D)$.

Rappel : $A \setminus B = \{x \in E : x \in A \text{ et } x \notin B\} = A \cap B^c$ (voir [[Différence d'ensembles]]).

**Correction.**
1. $(A \setminus B) \setminus C = (A \cap B^c) \cap C^c = A \cap (B^c \cap C^c) \underset{\text{De Morgan}}{=} A \cap (B \cup C)^c = A \setminus (B \cup C)$.
2. $(A \setminus B) \cap (C \setminus D) = (A \cap B^c) \cap (C \cap D^c) = (A \cap C) \cap (B^c \cap D^c) \underset{\text{De Morgan}}{=} (A \cap C) \cap (B \cup D)^c = (A \cap C) \setminus (B \cup D)$.

## Exercice 2.12

**Énoncé.** Soient $A, B, C$ trois parties de $E$. Montrer que
1. $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$ ;
2. $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.

**Correction.**
1. $A \setminus (B \cap C) = A \cap (B \cap C)^c \underset{\text{De Morgan}}{=} A \cap (B^c \cup C^c) = (A \cap B^c) \cup (A \cap C^c) = (A \setminus B) \cup (A \setminus C)$.
2. $A \setminus (B \cup C) = A \cap (B \cup C)^c \underset{\text{De Morgan}}{=} A \cap (B^c \cap C^c) = (A \cap A) \cap (B^c \cap C^c) = (A \cap B^c) \cap (A \cap C^c) = (A \setminus B) \cap (A \setminus C)$.

## Exercice 2.13 — Différence symétrique

**Énoncé.** Soit $\Delta$ la différence symétrique dans $\mathcal{P}(E)$.
1. Montrer que $A \Delta B = B \Delta A$, puis que $(A \Delta B) \Delta C = A \Delta (B \Delta C)$.
2. Montrer que $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$.
3. Que valent $A \Delta \emptyset$, $A \Delta A$, et $A \Delta B$ quand $A \subset B$ ?

**Définition rappelée :**
$$A \Delta B = (A \cup B) \setminus (A \cap B) = (A \cup B) \cap (A^c \cup B^c) = (A \setminus B) \cup (B \setminus A).$$

**Correction.**

1. *Commutativité* : $A \Delta B = (A \setminus B) \cup (B \setminus A) = (B \setminus A) \cup (A \setminus B) = B \Delta A$.

   *Associativité* : on développe
$$\begin{aligned}
(A \Delta B) \Delta C &= [(A \Delta B) \cup C] \cap [(A \Delta B)^c \cup C^c]\\
&= \big[[(A \cup B) \cap (A^c \cup B^c)] \cup C\big] \cap \big[[(A^c \cup B) \cap (A \cup B^c)] \cup C^c\big]\\
&= (A \cup B \cup C) \cap (A^c \cup B^c \cup C) \cap (A^c \cup B \cup C^c) \cap (A \cup B^c \cup C^c).
\end{aligned}$$
   Cette expression est symétrique : on la réordonne en
$$(B \cup C \cup A) \cap (B^c \cup C^c \cup A) \cap (B \cup C^c \cup A^c) \cap (B^c \cup C \cup A^c) = [(B \Delta C) \cup A] \cap [(B \Delta C)^c \cup A^c] = (B \Delta C) \Delta A = A \Delta (B \Delta C).$$
2. D'un côté :
$$A \cap (B \Delta C) = A \cap [(B \cap C^c) \cup (C \cap B^c)] = (A \cap B \cap C^c) \cup (A \cap B^c \cap C).$$
   De l'autre :
$$\begin{aligned}
(A \cap B) \Delta (A \cap C) &= [(A \cap B) \cap (A \cap C)^c] \cup [(A \cap C) \cap (A \cap B)^c]\\
&= [(A \cap B) \cap (A^c \cup C^c)] \cup [(A \cap C) \cap (A^c \cup B^c)]\\
&= \emptyset \cup (A \cap B \cap C^c) \cup \emptyset \cup (A \cap B^c \cap C).
\end{aligned}$$
   Les deux sont égaux.
3. $A \Delta \emptyset = (A \cup \emptyset) \setminus (A \cap \emptyset) = A \setminus \emptyset = A$ ; $A \Delta A = A \setminus A = \emptyset$ ; si $A \subset B$, $A \Delta B = (A \cup B) \setminus (A \cap B) = B \setminus A$.

## Méthodes à retenir

- Pour une inclusion, partir de « soit $x \in \ldots$ ». Pour une égalité, double inclusion ou chaîne d'équivalences.
- Ramener toute différence à une intersection avec un complémentaire, puis appliquer De Morgan.
- Un contre-exemple suffit à réfuter une inclusion réciproque : choisir des ensembles très simples (égaux, ou disjoints).

## Points à vérifier

- **Exercice 2.7** : l'énoncé annonce $(A \times C) \cap (B \times D) = (A \cap B) \times (C \cap D)$ ; la solution démontre la formule avec d'autres lettres, $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$. Le résultat est le même (complément).
- **Exercice 2.4, question 2, sens réciproque** : renvoyer à « l'implication réciproque » est maladroit, il s'agit en fait du sens direct appliqué aux complémentaires (complément).
- **Exercice 2.4, question 1** : le corrigé écrit « $x \in A \cup B =\in A \cap B$ », coquille pour « $x \in A \cup B = A \cap B$ ».
- **Exercice 2.6, question 1** : le corrigé affirme que l'égalité n'a lieu « que si $E \subset F$ ou $F \subset E$ » sans démontrer ce sens (seul un exemple est donné). L'affirmation est vraie ($E \cup F$ doit appartenir à $\mathcal{P}(E)$ ou à $\mathcal{P}(F)$), mais la justification est à compléter (complément).
