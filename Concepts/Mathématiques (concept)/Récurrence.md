---
type: concept
tags:
  - year1
  - year2
aliases:
  - preuve par récurrence
  - raisonnement par récurrence
  - démonstration par récurrence
  - hérédité
matieres:
  - Outil Maths
  - Algo Maths
  - Analyse Maths
  - Algo
sources:
  - "[[1 - logique (résumé)|Chapitre 1 logique]]"
  - "[[0 - Algo Maths (résumé)|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]"
  - "[[Raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf]]"
  - "[[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique.pdf]]"
  - "[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]"
  - "[[0 - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
maj: 2026-11-06
---

Preuve qu'une propriété $P(n)$ est vraie pour tout entier $n$ à partir d'un rang : **initialisation** ($P$ vraie au premier rang), **hérédité** (si $P(n)$ est vraie, $P(n+1)$ l'est), **conclusion**.

Exemples du cours : $1 + 2 + \ldots + n = \frac{n(n+1)}{2}$ (chapitre de logique) et $f(n) = 2^n - 1$ pour $f(0) = 0$, $f(n+1) = 2f(n) + 1$ (nombre de coups des [[Tours de Hanoï]]).

**Piège** : le [[Problème des crayons]] « tous de la même couleur » est une fausse récurrence, dont l'hérédité échoue au passage de 1 à 2 crayons. La feuille d'exercices de logique ([[Raw/Year 1/Outil Maths/Exos/Exo_Chapitre1_Logique.pdf|Exo_Chapitre1_Logique]]) montre aussi que l'hérédité seule ne suffit pas : « $10^n + 1$ divisible par 9 » est héréditaire mais fausse pour tout $n$.

**En Outil Maths**, le DS1 ([[Raw/Year 1/Outil Maths/controles/CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022.pdf|CorrigéDS1-algèbre-ensav-GEM-supmeca-octobre2022]]) prouve « 3 divise $4^n + 2$ » et « tout $n \geq 8$ s'écrit $3a + 5b$ » ; pour la seconde, l'hérédité se fait par [[Raisonnement par disjonction des cas|disjonction des cas]] (au moins un 5 dans l'écriture, ou aucun).

**En analyse**, elle sert à montrer que $\binom{n}{p}$ est entier, la [[Formule du binôme de Newton|formule du binôme]] ([[0 - Rappels-etc (résumé)]]), l'inégalité de Bernoulli $(1+a)^n \ge 1+na$ ([[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels]]), $\varphi(n) \ge n$, et des propriétés des parties de $\mathbb{N}$ ([[1 - Ensemble des Reels (résumé)]]) ; $2^n > n^2$ pour $n \ge 5$ ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

**En algorithmique**, le cours relie récursivité et récurrence : un algorithme récursif correspond à une récurrence ([[0 - diapo prof (résumé)]]), et une fonction récursive se prouve souvent par récurrence (voir [[Récursivité]]). Les fractales sont des motifs définis par récurrence. Une suite définie par récurrence sert aussi à compter la complexité d'un algorithme récursif : voir [[Complexité algorithmique]]. En 2e année, [[4 - Arbres binaires (résumé)|le chapitre 4 d'Algo]] prouve en détail que tout [[Arbre binaire]] non vide a une feuille, par récurrence sur la taille avec $n = 1 + n(l) + n(r)$.

**En Bilinear Algebra**, $A^n\mathbf{x} = \lambda^n\mathbf{x}$ se montre par récurrence ([[0 - Eigenvalues and eigenvectors (résumé)]]).

Notion parente : [[Logique propositionnelle]]. Voir aussi : [[Récursivité]], [[Tours de Hanoï]], [[Problème des crayons]], [[Formule du binôme de Newton]], [[Raisonnement par disjonction des cas]], [[Arbre binaire]]

## À vérifier

- [[0 - Algo Maths (résumé)|Cours 1 (Algo Maths)]] : la conclusion dit « vraie pour tout entier ≥ 1 » alors que l'initialisation est en 0, et $2^{k+1}$ est écrit « 2^k+1 ».

Résumés : [[1 - logique (résumé)]], [[0 - Algo Maths (résumé)|Cours 1 (résumé, Algo Maths)]], [[0 - diapo prof (résumé)]], [[0 - Rappels-etc (résumé)]], [[1 - Ensemble des Reels (résumé)]], [[4 - Arbres binaires (résumé)]], [[0 - Eigenvalues and eigenvectors (résumé)]]
