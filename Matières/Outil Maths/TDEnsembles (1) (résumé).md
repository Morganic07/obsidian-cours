---
type: source
tags: [year1]
sources: ["[[raw/Year 1/Outil Maths/Exos/TDEnsembles (1).pdf|TD Ensembles (PDF)]]"]
maj: 2026-11-06
---

Résumé du corrigé [[raw/Year 1/Outil Maths/Exos/TDEnsembles (1).pdf|TD Ensembles (PDF)]] (36 pages, algèbre, premier semestre 2022), dans [[Outil Maths (matière)]]. 13 exercices avec solutions rédigées. L'énoncé seul est résumé dans [[Exo-Chapitre 2 (résumé)]]. Cours associé : [[Chapitre 2 ensembles (résumé)]], [[Opérations sur les ensembles]], [[Logique propositionnelle]].

## Thèmes et exercices

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
| 2.13 | Différence symétrique $\Delta$ : commutative, associative, distributivité de $\cap$ sur $\Delta$ ; $A \Delta \emptyset = A$, $A \Delta A = \emptyset$, $A \Delta B = B \setminus A$ si $A \subset B$ | Forme $(A \cup B) \setminus (A \cap B)$ ou $(A \setminus B) \cup (B \setminus A)$ |

## Méthodes à retenir

- Pour une inclusion, partir de « soit $x \in \ldots$ ». Pour une égalité, double inclusion ou chaîne d'équivalences.
- Ramener toute différence à une intersection avec un complémentaire, puis appliquer De Morgan.
- Un contre-exemple suffit à réfuter une inclusion réciproque : choisir des ensembles très simples (égaux, ou disjoints).

## Points à vérifier

- **Exercice 2.7** : l'énoncé annonce $(A \times C) \cap (B \times D) = (A \cap B) \times (C \cap D)$ ; la solution démontre la formule avec d'autres lettres, $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$. Le résultat est le même (complément).
- **Exercice 2.4, question 2, sens réciproque** : renvoyer à « l'implication réciproque » est maladroit, il s'agit en fait du sens direct appliqué aux complémentaires (complément).
