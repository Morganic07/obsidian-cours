---
type: concept
tags: [year2, year3]
aliases: [boule ouverte, boules ouvertes, boule fermée, boules fermées, voisinage, voisinages, sphère de centre a, boule unité, intersection de voisinages]
matieres: [Analyse dans Rn, Analyse Maths, Analyse, Séries]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[0 - Revision chapter|Chp0 - Revision chapter]]"]
maj: 2026-11-07
---

Dans un EVN :

- **Boule ouverte** : $B(a, r) = \{x \mid \|x - a\| < r\}$.
- **Boule fermée** : $\overline{B}(a, r) = \{x \mid \|x - a\| \le r\}$.
- **Sphère** : $S(a, r) = \{x \mid \|x - a\| = r\}$, et $\overline{B}(a, r) = B(a, r) \cup S(a, r)$.

La forme dépend de la norme. Dans $\mathbb{R}^2$, la boule fermée de rayon 1 est un losange pour $\|\cdot\|_1$, un disque pour $\|\cdot\|_2$ et un carré pour $\|\cdot\|_\infty$. Dans $\mathbb{R}$, c'est un intervalle centré en $a$.

**Voisinage** : $V$ est un voisinage de $a$ si $\exists r > 0$ tel que $B(a, r) \subset V$. Alors $a \in V$. Toute réunion, et toute intersection **finie**, de voisinages de $a$ est un voisinage de $a$. Une intersection infinie peut ne pas en être un : $\bigcap_n \,]-\frac{1}{n}, \frac{1}{n}[\, = \{0\}$. En dimension finie, être un voisinage ne dépend pas de la norme. Tout EVN est séparé : deux points distincts ont des voisinages disjoints (voir [[Espace séparé]]).

**En Séries** : le chapitre de révision nomme le voisinage $\nu(a)$ d'un point $a \in \overline{\mathbb{R}}$, sans le redéfinir, pour définir $o$, $O$ et les équivalents près de $a$ ([[Comparaison asymptotique]]).

Notion parente : [[Norme]]. Voir aussi : [[Ouvert et fermé]], [[Espace séparé]], [[Intérieur et adhérence]], [[Limite et continuité]], [[Comparaison asymptotique]]

## Erreurs du cours

- [[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]], propriété 7, écrit « $r < r' \iff B(a,r) \subset B(a,r')$ » (et de même pour les boules fermées) ; il faut « $r \le r'$ » : pour $r = r'$, l'inclusion est vraie alors que $r < r'$ est faux.
- Le même chapitre, sur la figure de la boule fermée pour $\|\cdot\|_1$, étiquette le côté du quadrant $x < 0, y > 0$ « $y = x - 1$ » ; il faut « $y = 1 + x$ », comme le donne le texte juste au-dessus.

Résumés : [[2 - éléments de topologie dans Rn]], [[0 - Revision chapter]]
