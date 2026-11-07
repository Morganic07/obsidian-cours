---
type: concept
tags: [year1]
aliases: [densité de Q dans R, ℚ est dense dans ℝ, Q dense dans R]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]"]
maj: 2026-11-07
---

Entre deux réels distincts, il y a une infinité de rationnels et d'irrationnels.

**Preuve du chapitre 1** : pour $x < y$, choisir $n$ tel que $10^{-n} < y - x$, puis poser $r = d_n + 10^{-n}$, où $d_n$ est l'[[Approximation décimale]] par défaut de $x$ ; alors $x < r < y$.

Le TD des suites la redémontre par la limite $\dfrac{E(x) + E(2x) + \dots + E(nx)}{n^2} \to \dfrac{x}{2}$.

Notion parente : [[Ensembles de nombres]]. Voir aussi : [[Approximation décimale]], [[Nombre rationnel]].

## Erreurs du cours

- [[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]] conclut « $x < r < y$ et $y \in \mathbb{Q}$ » ; il faut « $r \in \mathbb{Q}$ ».

Résumés : [[1 - Ensemble des Reels]]
