---
type: concept
tags: [year2]
aliases: [points intérieurs, adhérence, adhérent, adhérents, frontière, intérieur d'un ensemble, Fr(A), dense, partie dense]
matieres: [Analyse dans Rn]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-08
---

Pour une partie $A$ d'un EVN :

- **Intérieur** : $x \in \mathring{A} \iff \exists r > 0, B(x, r) \subset A$. C'est le plus grand ouvert contenu dans $A$, et $A$ est ouvert si et seulement si $\mathring{A} = A$.
- **Adhérence** (le cours dit « adhérent ») : $x \in \overline{A} \iff \forall r > 0, B(x, r) \cap A \neq \emptyset$. C'est le plus petit fermé contenant $A$, et $A$ est fermé si et seulement si $\overline{A} = A$.
- **Frontière** : $\partial A$, notée aussi $\mathrm{Fr}(A)$, vaut $\overline{A} \setminus \mathring{A}$. Alors $\overline{A} = A \cup \partial A$ et $\mathring{A} = A \setminus \partial A$.

On a $\mathring{A} \subset A \subset \overline{A}$. Les deux opérations sont idempotentes et conservent l'inclusion. Dans $\mathbb{R}$, l'intérieur de tout intervalle d'extrémités $a$ et $b$ est $]a, b[$.

**Méthode** : deviner un candidat $B$, puis vérifier en 3 étapes. Pour $\overline{A}$ : $B$ est fermé, $A \subset B$, et $\forall x \in B \setminus A, \forall r > 0, B(x, r) \cap A \neq \emptyset$. Pour $\mathring{A}$ : $B$ est ouvert, $B \subset A$, et $\forall x \in A \setminus B, \forall r > 0, B(x, r) \not\subset A$.

## Compléments (hors du cours)

- **Caractérisation séquentielle** : $x \in \overline{A}$ si et seulement s'il existe une suite d'éléments de $A$ qui converge vers $x$ (voir [[Caractérisation séquentielle de la limite]]).
- **Dualité** : en notant $A^c$ le complémentaire, $\left(\overline{A}\right)^c = \operatorname{int}\left(A^c\right)$ et $\left(\mathring{A}\right)^c = \overline{A^c}$, où $\operatorname{int}$ désigne l'intérieur : le complémentaire de l'adhérence est l'intérieur du complémentaire, et inversement.
- **Frontière** : $\partial A$ est fermée, et $x \in \partial A$ si et seulement si toute boule centrée en $x$ rencontre à la fois $A$ et $A^c$.
- **Partie dense** : $A$ est dense dans $E$ si $\overline{A} = E$. Par exemple, $\overline{\mathbb{Q}} = \mathbb{R}$, l'intérieur de $\mathbb{Q}$ est vide et $\partial \mathbb{Q} = \mathbb{R}$ (voir [[Densité de ℚ dans ℝ]]).
- **Exemples** : l'adhérence de la boule ouverte $B(a, r)$ est la boule fermée $\overline{B}(a, r)$ (avec $r > 0$) ; $\partial B(a, r) = S(a, r)$, la sphère de centre $a$ et de rayon $r$ ; $\partial [a, b[ = \{a, b\}$.

Notion parente : [[Ouvert et fermé]]. Liens : [[Boule et voisinage]], [[Caractérisation séquentielle de la limite]], [[Densité de ℚ dans ℝ]]

Résumé : [[2 - éléments de topologie dans Rn]]
