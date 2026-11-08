---
type: concept
tags: [year1]
aliases: [coefficients binomiaux, "p parmi n", binomial coefficient]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td0slides.pdf|td0slides.pdf]]"]
maj: 2026-11-08
---

Le chapitre 0 définit $\binom{n}{p}$ et donne sa symétrie ; c'est un entier, ce que l'on prouve par récurrence avec la relation de Pascal. En TD : $k\binom{n}{k} = n\binom{n-1}{k-1}$.

## Compléments (complément, hors du cours)

**Définition** : pour des entiers $0 \le p \le n$,
$$\binom{n}{p} = \frac{n!}{p!\,(n-p)!},$$
et $\binom{n}{p} = 0$ si $p > n$ (ou $p < 0$). Se lit « $p$ parmi $n$ ».

**Sens en dénombrement** : $\binom{n}{p}$ est le nombre de parties à $p$ éléments d'un ensemble à $n$ éléments, c'est-à-dire le nombre de façons de choisir $p$ objets parmi $n$ sans ordre ni répétition (combinaisons). Exemple : le nombre de mains de 5 cartes dans un jeu de 32 est $\binom{32}{5}$.

**Calcul pratique** : après simplification par $(n-p)!$,
$$\binom{n}{p} = \frac{n(n-1)\cdots(n-p+1)}{p!},$$
avec $p$ facteurs au numérateur. Exemple : $\binom52 = \frac{5 \times 4}{2} = 10$.

**Valeurs à connaître** : $\binom n0 = \binom nn = 1$, $\binom n1 = \binom n{n-1} = n$, $\binom n2 = \frac{n(n-1)}{2}$.

**Symétrie** $\binom{n}{p} = \binom{n}{n-p}$ : choisir les $p$ éléments retenus revient à choisir les $n-p$ éléments écartés, d'où autant de parties à $p$ éléments que de parties à $n-p$ éléments.

**Preuve de $p\binom np = n\binom{n-1}{p-1}$** (pour $1 \le p \le n$) par les factorielles :
$$p\binom np = \frac{p\,n!}{p!\,(n-p)!} = \frac{n!}{(p-1)!\,(n-p)!} = n\cdot\frac{(n-1)!}{(p-1)!\,\big((n-1)-(p-1)\big)!} = n\binom{n-1}{p-1}.$$
Lecture combinatoire : choisir un comité de $p$ personnes parmi $n$ puis son président ($p\binom np$), ou choisir d'abord le président puis les $p-1$ autres membres parmi les $n-1$ restants ($n\binom{n-1}{p-1}$).

Notion parente : [[Dénombrement]]. Voir aussi : [[Formule de Pascal]], [[Formule du binôme de Newton]], [[Factorielle]], [[Récurrence]].

Résumés : [[0 - Rappels-etc]]
