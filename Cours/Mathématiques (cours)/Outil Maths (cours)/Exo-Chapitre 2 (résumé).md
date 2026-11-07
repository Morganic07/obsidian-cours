---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Outil Maths/Exos/Exo-Chapitre 2.pdf|Exo-Chapitre 2.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de la feuille d'exercices Exo Chapitre 2 (PDF) ([[Raw/Year 1/Outil Maths/Exos/Exo-Chapitre 2.pdf|Exo-Chapitre 2.pdf]]) (2 pages, Outils Mathématiques, semestre 1, 2023/2024), dans [[Outil Maths (index)]]. Énoncés seuls, sans corrigé : les solutions de la plupart sont dans [[TDEnsembles (1) (résumé)]]. Cours : [[Chapitre2-Ensemble (4) (résumé)]], [[chp 2 - ensembles (résumé)]], [[Opérations sur les ensembles]].

La feuille ne contient aucune figure. Les numéros de corrigé renvoient au TD [[TDEnsembles (1) (résumé)|TDEnsembles]].

## Exercice 1 : construire des ensembles

Soit $E = \{2 ; 4 ; 6 ; 8\}$, $F = \{4 ; 5 ; 6\}$, $G = \{a ; b\}$.

1. Construire les ensembles suivants :
$$E \cap F,\quad E \cap G,\quad E \cup F,\quad F \cup G,\quad E,\quad E \times G,\quad \mathcal{P}(E),\quad \mathcal{P}(E) \cap \mathcal{P}(F)$$
2. Expliquer pourquoi les écritures suivantes sont fausses, et les corriger :
$$2 \subset E,\quad 4 \in \mathcal{P}(F),\quad 8 \in E \times G,\quad \varphi \subset \mathcal{P}(E)$$

Travail sur l'appartenance et l'[[Inclusion (ensembles)|inclusion]], le [[Produit cartésien|produit cartésien]] et l'ensemble des parties. Pas de corrigé sur la feuille.

## Exercice 2 : caractérisations de l'inclusion

Soit $A$ et $B$ deux parties d'un ensemble $E$. Montrer :

1. $A \subset B \iff A \cup B = B$
2. $A \subset B \iff A^c \cup B = E$

En déduire :

3. $A \subset B \iff A \cap B = A$
4. $A \subset B \iff A \cap B^c = \emptyset$

Corrigé : TD, ex. 2.1.

## Exercice 3 : distributivité et égalités

Soient $A, B, C$ trois ensembles. Montrer que :

1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.
2. $A \cup B = A \cap C \;\;[\iff]\;\; B \subset A \subset C$ (le symbole d'équivalence manque dans le PDF).
3. $(A \cup B) \cap (B \cup C) \cap (C \cup A) = (A \cap B) \cup (B \cap C) \cup (C \cap A)$.

Corrigé : TD, ex. 2.2.

## Exercice 4 : produit cartésien

Soit $A = \{a_1, a_2, a_3, a_4\}$ et $B = \{b_1, b_2, b_3, b_4, b_5\}$.

1. Écrire le produit cartésien $A \times B$.
2. Quel est le nombre de parties de $A \times B$ ?

Corrigé : TD, ex. 2.5.

## Exercice 5 : ensembles des parties

Soit $E$ et $F$ deux ensembles. Quelle relation y a-t-il entre :

1. $\mathcal{P}(E \cup F)$ et $\mathcal{P}(E) \cup \mathcal{P}(F)$ ?
2. $\mathcal{P}(E \cap F)$ et $\mathcal{P}(E) \cap \mathcal{P}(F)$ ?
3. $\mathcal{P}(E \times F)$ et $\mathcal{P}(E) \times \mathcal{P}(F)$ ?

La feuille répète ensuite la question 1. Corrigé : TD, ex. 2.6.

## Exercice 6 : parties d'un produit

Soit $E$ et $F$ deux ensembles. Tous les sous-ensembles de $E \times F$ sont-ils de la forme $A \times B$ avec $A \subset E$ et $B \subset F$ ?

Corrigé : TD, ex. 2.8.

## Exercice 7 : simplifications

Simplifier, où $A$, $B$, $C$ sont des parties d'un ensemble $E$ :

1. $A \cap (A^c \cup B)$
2. $A \cup (A^c \cap B)$
3. $A \cap (A^c \cup B) \cap (A^c \cup B^c \cup C)$
4. $A \cup (A^c \cap B) \cup (A^c \cap B^c \cap C)$

Corrigé : TD, ex. 2.10.

## Exercice 8 : différence symétrique

Soit $\Delta$ la [[Différence symétrique|différence symétrique]] dans $\mathcal{P}(E)$.

1. Montrer que $A \Delta B = B \Delta A$, puis que $(A \Delta B) \Delta C = A \Delta (B \Delta C)$.
2. Montrer que $A \cap (B \Delta C) = (A \cap B) \Delta (A \cap C)$.
3. Que valent $A \Delta \emptyset$, $A \Delta A$, et $A \Delta B$ quand $A \subset B$ ?

Corrigé : TD, ex. 2.13.

## Exercice 9 : différences itérées

Soit $A, B, C, D$ des parties d'un ensemble $E$. Montrer que :

1. $(A \setminus B) \setminus C = A \setminus (B \cup C)$.
2. $(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D)$.

Rappel donné par la feuille : $A \setminus B = \{x \in E : x \in A \text{ et } x \notin B\} = A \cap B^c$ (voir [[Différence d'ensembles]]).

Corrigé : TD, ex. 2.11.

## Exercice 10 : différence et De Morgan

Soit $A, B, C$ trois parties d'un ensemble $E$. Montrer que :

1. $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$.
2. $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$.

Voir [[Lois de De Morgan]]. Corrigé : TD, ex. 2.12.

## Exercice 11 : produits cartésiens

Soient $A, B, C, D$ quatre ensembles.

1. Montrer que $(A \times C) \cup (B \times C) = (A \cup B) \times C$.
2. Comparer $(A \times C) \cap (B \times D)$ et $(A \cap B) \times (C \cap D)$.

L'énoncé dit « comparer » (le corrigé du TD demande de montrer l'égalité).

## Points à vérifier

- **Exercice 11.2** : la comparaison porte sur $(A \times C) \cap (B \times D)$ et $(A \cap B) \times (C \cap D)$. Les deux sont égaux, mais l'énoncé n'invite pas à le démontrer (complément).
- **Exercice 5** : la dernière ligne répète la question 1, c'est une coquille de mise en page.
- **Exercice 3.2** : vérifié sur la page rendue, le symbole $\iff$ entre $A \cup B = A \cap C$ et $B \subset A \subset C$ manque dans le PDF lui-même.
- **Exercice 1.1** : la liste contient « $E$ » seul, sans barre de complémentaire visible sur la page rendue. Il s'agit peut-être d'un complémentaire ($\overline{E}$ dans un ensemble de référence non précisé) perdu à la composition ; tel quel, construire $E$ n'a pas d'intérêt.
- **Exercice 1.2** : la feuille écrit $\varphi$ (phi) pour l'ensemble vide $\emptyset$.
