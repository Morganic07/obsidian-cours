---
type: concept
tags: [year1]
aliases: [classe d'équivalence, classes d'équivalence, ensemble quotient, représentant d'une classe]
matieres: [Outil Maths]
sources: ["[[3 - Relation binaire (résumé)|Chapitre 3 - Relation binaire]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]", "[[Raw/Year 1/Outil Maths/Exos/TDRelations.pdf|TDRelations.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-06
---

Une [[Relation binaire]] $\mathcal{R}$ sur $E$ est une propriété reliant deux éléments, ou une partie de $E \times E$. Elle peut être réflexive, symétrique, antisymétrique, transitive.

**Relation d'équivalence** (notée $\sim$) : [[Relation réflexive|réflexive]], [[Relation symétrique|symétrique]], [[Relation transitive|transitive]]. La **classe** d'un élément est $[a] = \{x \in E \mid a \mathcal{R} x\}$, aussi notée $\mathrm{Cl}(a)$ ; tout élément de la classe en est un **représentant**. Une classe se dit « avoir le même (propriété) ».

L'**ensemble quotient** $E/R = \{[a] \mid a \in E\}$ regroupe les classes, et $x \mapsto \mathrm{Cl}(x)$ est surjective de $E$ dans $E/R$.

Deux classes sont égales ou disjointes : $[x] = [y] \iff [x] \cap [y] \neq \emptyset$. Les classes forment une [[Partition d'un ensemble|partition]] de $E$ : [[3 - Relation binaire (résumé)|Chapitre 3 - Relation binaire]] ne le disait pas, le PDF du cours ([[3 - pdf (résumé)]]) l'énonce.

Exemples : la [[Congruence modulo n]], dont l'ensemble quotient est $\mathbb{Z}/n\mathbb{Z}$ (TD) ; sur $\mathbb{R}$, la relation $x^2 - y^2 = x - y$, de classes $\{x, 1 - x\}$. Le DS2 d'Outils math I (janvier 2023) demande d'étudier les relations définies par $x^2 - y^2 = x - y$, $xy \ge 0$ et $|z| = |z'|$, et leurs classes ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

Notion parente : [[Relation binaire]]. Voir aussi : [[Relation d'ordre]], [[Partition d'un ensemble]], [[Congruence modulo n]], [[Relation réflexive]], [[Relation symétrique]], [[Relation transitive]], [[Opérations sur les ensembles]]

## À vérifier

- [[5 - Analyse Maths (résumé)|chp5 (Analyse)]] dit aussi que $\sim$ (l'équivalence de suites ou de fonctions) est une « relation d'équivalence » (réflexive, symétrique, transitive) : voir [[Équivalent (comparaison asymptotique)]].

Résumés : [[3 - Relation binaire (résumé)]], [[3 - pdf (résumé)]]
