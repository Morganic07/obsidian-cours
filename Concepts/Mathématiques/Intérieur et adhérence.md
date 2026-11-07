---
type: concept
tags: [year2]
aliases: [points intérieurs, adhérence, adhérent, adhérents, frontière, intérieur d'un ensemble, Fr(A)]
matieres: [Analyse dans Rn]
sources: ["[[Chp 2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-06
---

Pour une partie $A$ d'un EVN :

- **Intérieur** : $x \in \mathring{A} \iff \exists r > 0, B(x, r) \subset A$. C'est le plus grand ouvert contenu dans $A$, et $A$ est ouvert si et seulement si $\mathring{A} = A$.
- **Adhérence** (le cours dit « adhérent ») : $x \in \overline{A} \iff \forall r > 0, B(x, r) \cap A \neq \emptyset$. C'est le plus petit fermé contenant $A$, et $A$ est fermé si et seulement si $\overline{A} = A$.
- **Frontière** : $\partial A$, notée aussi $\mathrm{Fr}(A)$, vaut $\overline{A} \setminus \mathring{A}$. Alors $\overline{A} = A \cup \partial A$ et $\mathring{A} = A \setminus \partial A$.

On a $\mathring{A} \subset A \subset \overline{A}$. Les deux opérations sont idempotentes et conservent l'inclusion. Dans $\mathbb{R}$, l'intérieur de tout intervalle d'extrémités $a$ et $b$ est $]a, b[$.

**Méthode** : deviner un candidat $B$, puis vérifier en 3 étapes. Pour $\overline{A}$ : $B$ est fermé, $A \subset B$, et $\forall x \in B \setminus A, \forall r > 0, B(x, r) \cap A \neq \emptyset$. Pour $\mathring{A}$ : $B$ est ouvert, $B \subset A$, et $\forall x \in A \setminus B, \forall r > 0, B(x, r) \not\subset A$.

Notion parente : [[Ouvert et fermé]]. Liens : [[Boule et voisinage]]

## À vérifier

- [[Chp 2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]], définition 11 : coquille « Fr(a) » pour $\mathrm{Fr}(A)$.

Résumé : [[Chp 2 - éléments de topologie dans Rn (résumé)]]
